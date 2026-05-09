---
tags:
  - lab
  - ubuntu
  - structured-programming
  - cli
  - software-engineering
date: 05/09/2026
instructor: Zerina Begum
---



# Comprehensive Software Engineering Fundamentals

## 1. Core Concepts & Definitions

- **Software:** Computer programs and their associated documentation. Software products can be developed for a specific custom client or for a general market.
    
- **Software Engineering (SE):** An engineering discipline concerned with all aspects of software production, from early system specification through to post-deployment maintenance.
    
    - _Engineering Discipline:_ Engineers focus on making things work. They apply theories, methods, and tools selectively, but will also discover solutions when applicable theories are absent. They must always operate within organizational and financial constraints.
        
    - _All Aspects:_ SE is not limited to technical programming; it includes project management, tool development, and theory creation.
        
- **SE vs. Computer Science:** Computer science focuses on the underlying theories and fundamentals of computers and software. Software engineering focuses on the practicalities and problems of producing and delivering useful software. Computer science knowledge is essential for a software engineer, much like physics is essential for an electrical engineer.
    
- **SE vs. System Engineering:** System engineering covers all aspects of complex computer-based systems development, including hardware, software, process design, policy, and deployment. System engineers define the overall architecture and integrate the parts; they are less concerned with engineering the individual components. SE is just one part of this broader process.
    

## 2. The Software Process & Models

- **Software Process:** A set of activities and associated results whose goal is the development or evolution of a software product. Different types of systems (e.g., real-time aircraft software vs. e-commerce) require different processes, but using an inappropriate process can increase costs or reduce quality.
    
- **Four Fundamental Process Activities:**
    
    1. **Software Specification:** Customers and engineers define what the software will do and operational constraints.
        
    2. **Software Development:** The software is designed and programmed.
        
    3. **Software Validation:** The software is checked to ensure it meets customer requirements.
        
    4. **Software Evolution:** The software is modified to adapt to changing customer or market needs.
        
- **Software Process Model:** A simplified representation or description of a software process, viewed from a specific perspective. Models include activities, products, and roles.
    
    - **Workflow Model:** Shows the sequence of activities, inputs, outputs, and dependencies, representing human actions.
        
    - **Dataflow / Activity Model:** Represents the process as activities that carry out data transformations (e.g., transforming a specification into a design), carried out by humans or computers.
        
    - **Role/Action Model:** Represents the roles of people and the activities they are responsible for.
        
- **General Paradigms of Software Development:**
    
    1. **The Waterfall Approach:** Represents activities as separate, sequential phases (requirements, design, implementation, testing). A stage must be defined and 'signed-off' before the next begins.
        
    2. **Iterative Development:** Interleaves specification, development, and validation. An initial abstract system is rapidly developed, refined with customer input, and then either delivered or reimplemented structurally.
        
    3. **Component-Based Software Engineering (CBSE):** Assumes parts of the system already exist and focuses on assembling them.
        

## 3. Costs and Challenges

- **Costs:** Generally, 60% of costs go to development and 40% to testing. For custom software, evolution (maintenance) costs usually exceed development costs. Cost distribution varies heavily based on the software type; for example, real-time software requires much more extensive testing than web-based systems.
    
- **Key Challenges for the 21st Century:**
    
    1. **The Heterogeneity Challenge:** Building dependable, flexible software that can operate as distributed systems across networks, on different computers, and integrate with older legacy systems in varying languages.
        
    2. **The Delivery Challenge:** Shortening delivery times for large, complex systems to meet rapidly changing business needs without compromising quality.
        
    3. **The Trust Challenge:** Developing techniques to demonstrate that software intertwined with our lives (especially remote/web services) is trustworthy and secure.
        

## 4. Attributes of Good Software

Good software isn't just about services; it involves non-functional attributes that reflect execution behavior, code structure, and documentation quality (e.g., response times, code understandability). Different applications prioritize different attributes (e.g., banks need security, games need responsiveness).

- **Maintainability:** Must be written so it can evolve to meet changing customer needs, which is critical due to inevitably changing business environments.
    
- **Dependability:** Encompasses reliability, security, and safety. It should not cause physical or economic damage if the system fails.
    
- **Efficiency:** Must not waste system resources (memory, processor cycles). Includes responsiveness and processing time.
    
- **Usability:** Must be usable without undue effort by its target audience, requiring an appropriate UI and adequate documentation.
    

## 5. Software Engineering Methods & CASE

- **Methods:** Structured approaches to facilitate the production of cost-effective, high-quality software.
    
    - _History:_ 1970s saw function-oriented methods like Structured Analysis (DeMarco) and JSD (Jackson). 1980s/90s introduced Object-Oriented (OO) methods by Booch and Rumbaugh. These are now integrated into the Unified Modeling Language (UML). There is no "ideal" method; OO is great for interactive systems but not for strict real-time systems.
        
    - _Components of a Method:_
        
        - **System model descriptions:** Defines the models to be developed and their notation (e.g., Object models, state machine models).
            
        - **Rules:** Constraints that always apply (e.g., "Every entity must have a unique name").
            
        - **Recommendations:** Good design practice heuristics (e.g., "No object should have more than 7 sub-objects").
            
        - **Process guidance:** Activities to follow to develop the models.
            
- **CASE (Computer-Aided Software Engineering):** Automated software systems used to support process activities (analysis, modeling, debugging, testing). Often provides method support via editors, analysis modules to check rules, and report generators for documentation.
    

## 6. A Generic View of Software Engineering

Engineering focuses on answering what the problem is, how it will be solved/constructed, how errors will be uncovered, and how it will be supported. This applies across three generic phases:

- **The Definition Phase (What):** Identifies information to be processed, desired performance, interfaces, design constraints, and validation criteria. Tasks include system/information engineering, project planning, and requirements analysis.
    
- **The Development Phase (How):** Defines data structures, software architecture, procedural details, and testing parameters. Tasks include software design, code generation, and testing.
    
- **The Support Phase (Change):** Deals with changes over time, reapplying definition and development steps to existing software. Users also receive continuing support via technical assistants or help desks. The four types of change are:
    
    1. **Correction:** Corrective maintenance to fix defects uncovered by the customer.
        
    2. **Adaptation:** Adaptive maintenance to modify the software for changes in its external environment (e.g., new CPU or OS).
        
    3. **Enhancement:** Perfective maintenance that extends the software beyond original requirements to add beneficial functions.
        
    4. **Prevention:** Software reengineering (preventive maintenance) to alter programs so they don't deteriorate and can be more easily corrected or adapted in the future.
        

### Umbrella Activities

A process framework requires a small set of foundational activities overlayed by "umbrella activities" that happen throughout the entire process, regardless of project size. Examples include:

- Software project tracking and control
    
- Formal technical reviews
    
- Software quality assurance
    
- Software configuration management
    
- Document preparation and production
    
- Reusability management
    
- Measurement
    
- Risk management
    

## 7. SEI Process Maturity Levels (CMM)

The Software Engineering Institute (SEI) Capability Maturity Model (CMM) measures the global effectiveness of an organization's software practices via an assessment questionnaire distilled into a single grade.

- **Level 1: Initial:** Processes are ad hoc, occasionally chaotic. Success depends on individual effort, not defined processes.
    
- **Level 2: Repeatable:** Basic project management processes (cost, schedule, functionality) are in place to repeat earlier successes.
    
- **Level 3: Defined:** Both management and engineering processes are documented, standardized, and integrated organization-wide.
    
- **Level 4: Managed:** Process and product quality are quantitatively understood and controlled via detailed measures.
    
- **Level 5: Optimizing:** Continuous process improvement is driven by quantitative feedback and testing innovative technologies.
    

### Key Process Areas (KPAs)

KPAs are the software engineering functions required to satisfy good practice at each maturity level. Each KPA is described by its:

- **Goals:** Objectives to achieve.
    
- **Commitments:** Organizational requirements to achieve goals.
    
- **Abilities:** Technical/organizational structures needed to meet commitments.
    
- **Activities:** Specific tasks required.
    
- **Monitoring/Verifying Methods:** How implementation is tracked and verified.
    

**KPA Breakdown by Level:**

- **Level 2 KPAs:** Config management, subcontract management, tracking & oversight, planning, requirements management.
    
- **Level 3 KPAs:** Peer reviews, intergroup coordination, product engineering, integrated management, training, process definition, process focus.
    
- **Level 4 KPAs:** Quality management, quantitative process management.
    
- **Level 5 KPAs:** Process change management, technology change management, defect prevention.