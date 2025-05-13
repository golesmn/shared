
# Access Management System

This project follows **Domain-Driven Design (DDD)**, **Clean Architecture**, and **Event-Driven Design (EDD)** principles to structure an access management microservice. It is designed to be modular, testable, and highly scalable.

---

## 📚 Table of Contents

- [Project Structure](#project-structure)
- [Architecture Overview](#architecture-overview)
  - [Domain-Driven Design (DDD)](#domain-driven-design-ddd)
  - [Clean Architecture](#clean-architecture)
  - [Event-Driven Design](#event-driven-design)
- [Core Concepts](#core-concepts)
- [Getting Started](#getting-started)
- [Learning Resources](#learning-resources)

---

## 📁 Project Structure

```bash
.
├── access_management/            # Core service for access control
│   ├── application/              # Use cases and application services
│   ├── domain/                   # Domain logic (entities, aggregates, events, value objects)
│   ├── handlers/                 # Command handlers
│   ├── infrastructure/          # ORM models, repository implementations
│   ├── interfaces/              # Future APIs or CLI interfaces
│   └── main.py                  # Entry point (can be renamed for clarity)
├── shared/                      # Reusable libraries and abstractions
│   ├── abstractions/            # Commands, events, primitives
│   ├── infrastructure/          # DB connections, messaging (Kafka)
│   ├── utils/                   # Helper scripts
│   └── docs/                    # Developer documentation
├── specs/                       # Fission/Kubernetes specs
└── README.md
````

---

## 🧠 Architecture Overview

### Domain-Driven Design (DDD)

DDD is about structuring code around **business domains** and **domain logic**.

* **Entities** have identity and lifecycle.
* **Value Objects** are immutable and compared by value.
* **Aggregates** enforce consistency rules and business logic.
* **Domain Events** notify the system of important occurrences in the domain.

Example:

* `domain/aggregates/user.py` contains the User aggregate.
* `domain/value_objects/email.py` ensures valid email structure.
* `domain/events/user_created.py` represents a domain-level event.

---

### Clean Architecture

Clean Architecture enforces **layered separation of concerns**:

1. **Entities** → Core domain logic (`domain/`)
2. **Use Cases** → Application logic (`application/`)
3. **Interface Adapters** → Input/output ports (`handlers/`, `repositories/`)
4. **Frameworks & Drivers** → External concerns (`infrastructure/`)

> Core rule: **Dependencies always point inward**.

---

### Event-Driven Design

The system communicates through **events** to promote decoupling.

* `domain/events/` contains domain events.
* `shared/abstractions/events/` contains:

  * Event dispatcher
  * Handler base classes
  * Registry
* `shared/infrastructure/messaging/kafka_producer.py` handles publishing to Kafka.

Use this pattern to:

* Decouple services
* Enable async processing
* Achieve eventual consistency

---

## ⚙️ Core Concepts

| Concept        | Location                                            | Description                                          |
| -------------- | --------------------------------------------------- | ---------------------------------------------------- |
| Aggregate Root | `domain/aggregates/user.py`                         | Enforces consistency and encapsulates business logic |
| Command        | `application/commands/create_user.py`               | Represents intent (e.g., create user)                |
| Handler        | `handlers/user_creation.py`                         | Executes command, triggers events                    |
| Event          | `domain/events/user_created.py`                     | Notification of domain change                        |
| Repository     | `infrastructure/repositories/user_repository.py`    | Accesses data source for aggregates                  |
| Kafka Producer | `shared/infrastructure/messaging/kafka_producer.py` | Sends events to message broker                       |

---

## 🚀 Getting Started

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run service**:

   ```bash
   python access_management/main.py
   ```

3. **Run tests** *(if available)*:

   ```bash
   pytest
   ```

---

## 📘 Learning Resources

### 📗 Domain-Driven Design

* [Domain-Driven Design Reference (Vaughn Vernon)](https://www.amazon.com/Domain-Driven-Design-Reference-Vaughn-Vernon/dp/0321834577)
* [DDD Quickly (free ebook)](https://www.infoq.com/minibooks/domain-driven-design-quickly/)
* [What is Domain-Driven Design? (Martin Fowler)](https://martinfowler.com/bliki/DomainDrivenDesign.html)

### 📙 Clean Architecture

* [Clean Architecture by Uncle Bob](https://www.amazon.com/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164)
* [Clean Architecture explained](https://medium.com/swlh/clean-architecture-9f3bf34fdfdb)

### 📘 Event-Driven Architecture

* [Event-Driven Architecture — Martin Fowler](https://martinfowler.com/articles/201701-event-driven.html)
* [Introduction to Event-Driven Architecture](https://docs.microsoft.com/en-us/azure/architecture/guide/architecture-styles/event-driven)

---

## ✨ Contributing

See `shared/docs/adding_new_resources.md` for information on how to add new features, aggregates, or services to the project.

---