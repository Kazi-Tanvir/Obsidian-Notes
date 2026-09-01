---
tags:
- devops
- terraform
- aws
- ecs-fargate
- vpc
- cloud-infrastructure
- security
- backend
date: 2026-09-01
---

# Day 32 - Cloud Infrastructure as Code: Terraform, AWS ECS Fargate, VPC Networking & IAM Security

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Infrastructure as Code (IaC) & Immutable Cloud Architecture

Managing cloud infrastructure through manual web consoles leads to configuration drift, untracked changes, and catastrophic deployment outages.

**Terraform (HashiCorp HCL)** is a declarative Infrastructure as Code tool that provisions and manages multi-cloud resources.

- **Declarative vs. Imperative**: You define the desired end state (resource "aws_ecs_service"), and Terraform calculates the delta dependency graph required to reach that state.

- **State File Management (terraform.tfstate)**: Acts as the single source of truth mapping declared configuration to actual cloud resource IDs. In production, the state file **must** be stored remotely in **AWS S3 with server-side encryption and DynamoDB state locking** to prevent race condition corruptions during team executions.

┌────────────────────────────────────── Production AWS VPC Topology ──────────────────────────────────────┐

│ │

│ AWS Region (e.g. us-east-1) │

│ ┌────────────────────────────────────────────── VPC (10.0.0.0/16) ──────────────────────────────────┐ │

│ │ │ │

│ │ ┌───────────────────────── Availability Zone A ────────────┐ ┌─── Availability Zone B ────────┐ │ │

│ │ │ │ │ │ │ │

│ │ │ Public Subnet A (10.0.1.0/24) │ │ Public Subnet B (10.0.2.0/24) │ │ │

│ │ │ • Internet Gateway (IGW) │ │ • Application Load Balancer │ │ │

│ │ │ • NAT Gateway A (Outbound Internet for Private Subnets) │ │ • NAT Gateway B │ │ │

│ │ └──────────────────────────────┬───────────────────────────┘ └────────────────────────────────┘ │ │

│ │ │ Route Table: 0.0.0.0/0 -> NAT GW │ │

│ │ ┌──────────────────────────────▼───────────────────────────┐ ┌────────────────────────────────┐ │ │

│ │ │ Private App Subnet A (10.0.11.0/24) │ │ Private App Subnet B │ │ │

│ │ │ • AWS ECS Fargate Container Tasks (Node.js/Next.js APIs)│ │ • AWS ECS Fargate Tasks │ │ │

│ │ │ • No Direct Public IP / Protected from Internet │ │ │ │ │

│ │ └──────────────────────────────┬───────────────────────────┘ └────────────────────────────────┘ │ │

│ │ │ Security Group: Allow port 5432 from App Subnets ONLY │ │

│ │ ┌──────────────────────────────▼───────────────────────────┐ ┌────────────────────────────────┐ │ │

│ │ │ Isolated DB Subnet A (10.0.21.0/24) │ │ Isolated DB Subnet B │ │ │

│ │ │ • Amazon RDS Aurora PostgreSQL (Primary Writer) │ │ • Aurora Read Replica │ │ │

│ │ └──────────────────────────────────────────────────────────┘ └────────────────────────────────┘ │ │

│ └───────────────────────────────────────────────────────────────────────────────────────────────────┘ │

└────────────────────────────────────────────────────────────────────────────────────────────────────────┘

### 2. Serverless Container Orchestration on AWS ECS Fargate

**AWS ECS Fargate** provides serverless container compute, eliminating the overhead of provisioning, patching, and managing underlying EC2 virtual machine instances.

#### IAM Roles: Task Execution Role vs. Task Role

A critical security distinction in ECS:

1.  **ECS Task Execution Role (execution_role_arn)**: Used by the AWS ECS Agent to pull private Docker images from AWS ECR, configure CloudWatch logs, and decrypt environment secrets from **AWS Secrets Manager** / SSM Parameter Store.

2.  **ECS Task Role (task_role_arn)**: Used by your running application container code at runtime (e.g. Node.js code accessing AWS S3 buckets or DynamoDB tables via AWS SDK).

# ECS Task Definition with Secrets Manager Integration

resource "aws_ecs_task_definition" "api" {

family = "production-api"

network_mode = "awsvpc"

requires_compatibilities = ["FARGATE"]

cpu = "1024" # 1 vCPU

memory = "2048" # 2 GB RAM

execution_role_arn = aws_iam_role.ecs_execution_role.arn

task_role_arn = aws_iam_role.ecs_task_role.arn

container_definitions = jsonencode([

```javascript
{
```

name = "api-service"

image = "${aws_ecr_repository.api.repository_url}:latest"

essential = true

portMappings = [

```javascript
{
```

containerPort = 8080

hostPort = 8080

protocol = "tcp"

```javascript
}
]
```

secrets = [

```javascript
{
```

name = "DATABASE_URL"

valueFrom = "${aws_secretsmanager_secret.db_secret.arn}:DATABASE_URL::"

},

```javascript
{
```

name = "JWT_SECRET"

valueFrom = "${aws_secretsmanager_secret.jwt_secret.arn}:JWT_SECRET::"

```javascript
}
]
```

logConfiguration = {

logDriver = "awslogs"

options = {

"awslogs-group" = "/ecs/production-api"

"awslogs-region" = "us-east-1"

"awslogs-stream-prefix" = "ecs"

```javascript
}
}
}
])
}
```

### 3. Application Load Balancer & Auto-Scaling Policies

Configuring target tracking auto-scaling based on CPU utilization and incoming HTTP request counts per target:

# ECS Service with Fargate Launch Type

resource "aws_ecs_service" "api" {

name = "api-service"

cluster = aws_ecs_cluster.main.id

task_definition = aws_ecs_task_definition.api.arn

desired_count = 3

launch_type = "FARGATE"

network_configuration {

subnets = aws_subnet.private_app[*].id

security_groups = [aws_security_group.ecs_tasks.id]

assign_public_ip = false

```javascript
}
```

load_balancer {

target_group_arn = aws_lb_target_group.api.arn

container_name = "api-service"

container_port = 8080

```javascript
}
}
```

# Auto-Scaling Target Tracking Policy (Maintains ~70% CPU)

resource "aws_appautoscaling_policy" "ecs_cpu" {

name = "ecs-cpu-target-tracking"

policy_type = "TargetTrackingScaling"

resource_id = aws_appautoscaling_target.ecs_target.resource_id

scalable_dimension = aws_appautoscaling_target.ecs_target.scalable_dimension

service_namespace = aws_appautoscaling_target.ecs_target.service_namespace

target_tracking_scaling_policy_configuration {

predefined_metric_specification {

predefined_metric_type = "ECSServiceAverageCPUUtilization"

```javascript
}
```

target_value = 70.0

scale_in_cooldown = 300

scale_out_cooldown = 60

```javascript
}
}
```

## SECTION 2: DOCUMENTATION CHEAT SHEET

### Terraform CLI Commands Reference:

| **Command** | **Action** |
| --- | --- |
| terraform init -backend-config=... | nitializes provider plugins and remote S3 backend |
| terraform plan -out=tfplan | Generates speculative execution plan delta |
| terraform apply "tfplan"            A | plies exact pre-calculated infrastructure changes |
| terraform destroy | Tears down all resources managed by state file |
| terraform state rm <resource>       U | tracks resource from state without deleting cloud resource |

### Security Group Ingress / Egress Rule Matrix:

┌────────────────────────────────────── Security Group Chain ──────────────────────────────────────┐

│ │

│ 1. ALB Security Group: Ingress: 0.0.0.0/0 (Ports 80/443) ──► Egress: Port 8080 to ECS SG Only │

│ │

│ 2. ECS Security Group: Ingress: Port 8080 from ALB SG Only ──► Egress: Port 5432 to DB SG Only │

│ │

│ 3. RDS Security Group: Ingress: Port 5432 from ECS SG Only ──► Egress: None │

│ │

└──────────────────────────────────────────────────────────────────────────────────────────────────┘

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: Multi-AZ Enterprise Cloud Infrastructure Design on AWS

Design a high-availability, zero-single-point-of-failure cloud infrastructure using Terraform on AWS for an enterprise SaaS platform serving 200M monthly API requests:

**Requirements**:

1.  **Network & Compute Topology**:

    - 3-tier VPC architecture across 3 Availability Zones (us-east-1a, us-east-1b, us-east-1c).

    - ECS Fargate cluster with dynamic capacity providers (Fargate On-Demand + Fargate Spot for 60% cost savings).

    - Application Load Balancer with AWS WAF integration (SQL injection, XSS, rate-based bot throttling rules).

2.  **Database & Cache Topology**:

    - Multi-AZ Amazon Aurora PostgreSQL with auto-scaling read replicas.

    - Redis Cluster on Amazon ElastiCache with multi-AZ replication in isolated database subnets.

3.  **Disaster Recovery**:

    - Automated cross-region S3 state replication and Terraform workspace variables for instant deployment in us-west-2.

### Problem 2: Complete Production Terraform Module Suite in HCL

Write a modular, production-ready **Terraform Module for an ECS Fargate Service**:

**Requirements**:

1.  **VPC Module (modules/vpc)**:

    - Creates VPC with configurable CIDR, public/private/database subnets, Internet Gateway, and redundant NAT Gateways across 2 AZs.

2.  **ECS Service Module (modules/ecs-service)**:

    - Provisions ECS Cluster, CloudWatch Log Group with 30-day retention, Fargate Task Definition with AWS Secrets Manager injection, ECS Service, ALB Target Group with HTTP /healthz healthcheck probes, and CPU/Memory target tracking auto-scaling.

3.  **Security Module (modules/security-groups)**:

    - Strict least-privilege security group rules (ALB -> ECS Tasks -> RDS Database) with zero open public database ports.
