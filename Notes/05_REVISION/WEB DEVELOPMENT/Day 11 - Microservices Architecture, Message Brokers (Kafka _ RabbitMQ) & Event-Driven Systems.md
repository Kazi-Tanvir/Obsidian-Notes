tags:

- microservices

- kafka

- rabbitmq

- event-driven

- backend

- system-design date: 2026-08-11

# Day 11 - Microservices Architecture, Message Brokers (Kafka / RabbitMQ) & Event-Driven Systems

## SECTION 1: IN-DEPTH THEORY & ARCHITECTURE

### 1. Monolith vs Microservices & Event-Driven Architecture (EDA)

Moving from a monolithic application to a microservices architecture decomposes a single deployment unit into autonomous, loosely coupled services bounded by business domain contexts.

- **Synchronous REST / gRPC**: Tight coupling, cascading failures, latency amplification.

- **Asynchronous Event-Driven Architecture**: Decoupled producers and consumers communicating via immutable event logs or message queues.

### 2. Message Brokers: Kafka vs RabbitMQ

Understanding when to select Kafka vs RabbitMQ depends on architectural requirements:

  ---------------------------------------------------------------------------------------------------------------------------
  **Architecture Metric**   **Apache Kafka**                                   **RabbitMQ**
  ------------------------- -------------------------------------------------- ----------------------------------------------
  **Core Abstraction**      Distributed Immutable Commit Log                   AMQP Message Queue & Exchange

  **Consumption Model**     Pull-based by Consumer Groups                      Push-based to Consumers

  **Message Replay**        Native support (Replay past offsets)               Messages deleted upon ack

  **Routing Flexibility**   Topic-based partitions                             Complex routing keys (Topic, Fanout, Direct)

  **Throughput Target**     Millions of msgs/sec (High-throughput streaming)   Complex routing & per-message workflows
  ---------------------------------------------------------------------------------------------------------------------------

### 3. Kafka Core Primitives & Consumer Groups

- **Topics & Partitions**: Topics are divided into partitions distributed across cluster broker nodes. Order is strictly guaranteed **within a partition**, not across partitions.

- **Partition Keying**: Events with identical keys (e.g. orderId) hash to the same partition, guaranteeing ordered sequential processing.

- **Consumer Groups**: Scalable consumer instances sharing topic consumption. Each partition is assigned to exactly one consumer within a group.

// producer.ts - KafkaJS Production Setup

import { Kafka, Partitioners } from \'kafkajs\';

const kafka = new Kafka({

clientId: \'order-service\',

brokers: \[\'kafka-broker-1:9092\', \'kafka-broker-2:9092\'\],

});

const producer = kafka.producer({

createPartitioner: Partitioners.DefaultPartitioner,

});

export async function publishOrderCreatedEvent(order: { id: string; userId: string; total: number }) {

await producer.connect();

await producer.send({

topic: \'order-events\',

messages: \[

{

key: order.id, // Ensures order messages hash to same partition!

value: JSON.stringify({ type: \'ORDER_CREATED\', payload: order }),

headers: { correlationId: \'req-123-abc\' },

},

\],

});

}

// consumer.ts - KafkaJS Idempotent Consumer

import { Kafka } from \'kafkajs\';

const kafka = new Kafka({ clientId: \'payment-service\', brokers: \[\'kafka:9092\'\] });

const consumer = kafka.consumer({ groupId: \'payment-processor-group\' });

export async function startConsumer() {

await consumer.connect();

await consumer.subscribe({ topic: \'order-events\', fromBeginning: false });

await consumer.run({

eachMessage: async ({ topic, partition, message }) =\> {

const event = JSON.parse(message.value?.toString() \|\| \'{}\');

// Idempotency check using DB deduplication table

const isProcessed = await db.processedEvent.findUnique({

where: { eventId: message.key?.toString() }

});

if (isProcessed) return;

if (event.type === \'ORDER_CREATED\') {

await processPayment(event.payload);

// Mark event as processed in DB transaction

await db.processedEvent.create({ data: { eventId: message.key?.toString() } });

}

},

});

}

### 4. Transactional Outbox Pattern

To avoid **Dual-Write Vulnerabilities** (updating database succeeds but message broker publish fails or vice versa), the **Transactional Outbox Pattern** saves events directly inside the database transaction alongside business entity updates. A separate CDC (Change Data Capture) or background polling process publishes outbox events to Kafka.

## SECTION 2: DOCUMENTATION CHEAT SHEET

  ----------------------------------------------------------------------------------------------------------------------------------------------------------
  **Tool / Pattern**          **CLI Command / Configuration**                                           **Purpose**
  --------------------------- ------------------------------------------------------------------------- ----------------------------------------------------
  **Kafka Topic Creation**    kafka-topics.sh \--create \--topic order-events \--partitions 3           Creates partitioned topic

  **Consumer Group Offset**   kafka-consumer-groups.sh \--bootstrap-server localhost:9092 \--describe   Checks consumer lag across partitions

  **Partition Keying**        { key: \'userId\', value: \'\...\' }                                      Guarantees ordered execution per key

  **KafkaJS Ack Levels**      acks: -1 (or all)                                                         Highest durability; waits for all in-sync replicas

  **Transactional Outbox**    DB Table Outbox { id, aggregateId, type, payload, processed }             Prevents database/broker dual-write failures
  ----------------------------------------------------------------------------------------------------------------------------------------------------------

## SECTION 3: WEEKLY SYSTEM DESIGN & CODING PROBLEMS

### Problem 1: System Design (Event-Driven Order & Inventory System)

Design an asynchronous, fault-tolerant Event-Driven E-Commerce System handling Order Placement, Payment Processing, Inventory Deduction, and Email Notifications.

**Requirements**:

1.  Diagram Kafka topic and partition layouts (order-events, payment-events, inventory-events).

2.  Explain how to handle out-of-order event delivery using event timestamps and sequence numbers.

3.  Design a Dead-Letter Queue (DLQ) retry architecture for failed consumer messages.

### Problem 2: End-to-End Code Implementation Challenge

Build a resilient **Kafka Order Processing Consumer Service** in Node.js/TypeScript using kafkajs.

**Requirements**:

1.  Subscribe to order-events under consumer group inventory-service.

2.  Implement idempotent message processing using a local database transaction (checking if message.offset or orderId was previously processed).

3.  Handle transient consumer errors with exponential backoff retries.

4.  Route unprocessable messages to a order-events-dlq topic after 3 failed retries.
