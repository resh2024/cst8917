# CST8917 Assignment 2- Serverless Service Alternatives Report

## Objective

In this course, we used different Microsoft Azure serverless services to build and deploy applications. The purpose of this assignment is to build on that knowledge by exploring similar services offered by AWS and Google Cloud Platform (GCP).

For each Azure service covered in class, I looked into the closest equivalents in AWS and GCP and compared them based on features, integrations, monitoring, and pricing. This gives a better overall understanding of how serverless architectures are implemented across different cloud providers.

## Azure Functions (Triggers & Bindings)

Overview

- Azure Functions: Runs event-driven code using triggers and bindings.
- AWS Lambda: Executes code in response to events with automatic scaling.
- Google Cloud Functions: Lightweight event-driven compute service.

### Comparison table

| Feature         | Azure Functions                | AWS Lambda                   | GCP Cloud Functions    |
| --------------- | ------------------------------ | ---------------------------- | ---------------------- |
| Triggers        | HTTP, Timer, Queue, Event Grid | API Gateway, S3, EventBridge | HTTP, Pub/Sub, Storage |
| Bindings        | Strong built-in support        | No native bindings           | Limited                |
| Scaling         | Automatic                      | Automatic                    | Automatic              |
| Execution Model | Event-driven                   | Event-driven                 | Event-driven           |
| Ease of Use     | Very high                      | Moderate                     | High                   |

### Analysis

Azure Functions stands out mainly because of its bindings, which make it easier to connect to other services with less code. AWS Lambda is more flexible, but it usually requires more setup. GCP Cloud Functions is simple and easy to use, but it doesn’t offer as many features as the other two.

## Durable Functions (Orchestration)

- Azure Durable Functions: Extends Azure Functions to support workflows and orchestration.

- AWS Step Functions: Manages workflows using state machines.

- Google Cloud Workflows: Orchestrates services and APIs.

### Comparison Table

| Feature       | Durable Functions        | AWS Step Functions    | GCP Workflows        |
| ------------- | ------------------------ | --------------------- | -------------------- |
| Orchestration | Code-based               | Visual + JSON         | YAML/JSON            |
| Patterns      | Fan-out/Fan-in, chaining | State machines        | Sequential workflows |
| Complexity    | Moderate                 | High                  | Moderate             |
| Use Case      | App workflows            | Complex orchestration | Service coordination |

### Analysis

Durable Functions is more developer-friendly since workflows are written directly in code. AWS Step Functions is very powerful, especially for complex workflows, but it can be harder to set up. GCP Workflows is easier to understand, but it doesn’t support as many advanced patterns.

---

## Azure Logic Apps

- Azure Logic Apps: No-code/low-code workflow automation tool.

- AWS Step Functions + EventBridge: Used together for workflows.

- Google Cloud Workflows: Automates workflows.

### Comparison Table

| Feature      | Azure Logic Apps           | AWS (Step Functions/EventBridge) | GCP Workflows        |
| ------------ | -------------------------- | -------------------------------- | -------------------- |
| Interface    | Visual designer            | Limited UI                       | Some UI              |
| Ease of Use  | Very high                  | Moderate                         | Moderate             |
| Integration  | Large number of connectors | Strong AWS ecosystem             | Strong GCP ecosystem |
| Target Users | Developers + non-devs      | Developers                       | Developers           |

### Analysis

Logic Apps is the easiest to use, especially for people who don’t want to write much code. AWS and GCP offer similar functionality, but they require more configuration and are generally more developer-focused.

---

## Azure Service Bus (Queues & Topics)

- Azure Service Bus: Enterprise messaging with queues and topics.

- Amazon SQS / Amazon SNS: Queue and pub/sub messaging.

- Google Cloud Pub/Sub: Messaging and event ingestion.

### Comparison Table

| Feature        | Azure Service Bus    | AWS SQS/SNS         | GCP Pub/Sub       |
| -------------- | -------------------- | ------------------- | ----------------- |
| Messaging Type | Queue + Topics       | Queue + Pub/Sub     | Pub/Sub           |
| Ordering       | Supported            | Limited             | Supported         |
| Reliability    | High                 | High                | High              |
| Use Case       | Enterprise messaging | Distributed systems | Event-driven apps |

### Analysis

Azure Service Bus is more feature-rich and better suited for enterprise-level applications. AWS splits messaging into two services (SQS and SNS), which can make things a bit more complex. GCP Pub/Sub is simple, scalable, and works well for most event-driven use cases.

---

## Azure Event Grid

- Azure Event Grid: Event routing system for reactive programming.

- Amazon EventBridge: Event-driven architecture service.

- Google Eventarc: Event routing across services.

### Comparison Table

| Feature       | Azure Event Grid   | AWS EventBridge  | GCP Eventarc |
| ------------- | ------------------ | ---------------- | ------------ |
| Event Routing | Yes                | Yes              | Yes          |
| Filtering     | Advanced           | Advanced         | Moderate     |
| Integration   | Azure services     | AWS services     | GCP services |
| Event Sources | Wide Azure support | Wide AWS support | GCP services |

### Analysis

All three services are quite similar in terms of functionality. EventBridge is slightly more mature, while Event Grid integrates very well within the Azure ecosystem. Eventarc is effective but not as feature-rich as the other two.

---

## Azure Event Hubs

- Azure Event Hubs: Big data streaming service.

- Amazon Kinesis: Real-time data streaming.

- Google Cloud Pub/Sub: Used for streaming ingestion.

### Comparison Table

| Feature        | Azure Event Hubs   | AWS Kinesis         | GCP Pub/Sub           |
| -------------- | ------------------ | ------------------- | --------------------- |
| Streaming      | Yes                | Yes                 | Yes                   |
| Throughput     | High               | High                | High                  |
| Use Case       | Big data streaming | Real-time analytics | Messaging + streaming |
| Data Retention | Configurable       | Configurable        | Configurable          |

### Analysis

Event Hubs and Kinesis are very similar and are both designed for high-throughput data streaming. GCP Pub/Sub overlaps with these services but is more general-purpose, which makes it slightly less specialized for large-scale streaming.

---
