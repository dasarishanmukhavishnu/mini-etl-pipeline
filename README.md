# 🚀 Order Processing ETL Pipeline

A modular and object-oriented ETL (Extract, Transform, Load) pipeline built with Python. This project demonstrates how to design a maintainable, scalable, and configurable data pipeline by applying software engineering principles such as OOP, Separation of Concerns, Dependency Injection, and Configuration-Driven Development.

---

## 📌 Project Overview

This ETL pipeline processes raw order data from a CSV file and performs the following operations:

- Read raw order data
- Validate business rules
- Transform and standardize records
- Separate valid and invalid records
- Export cleaned and invalid datasets
- Generate detailed execution logs

The project is designed to simulate how production ETL systems are structured rather than simply processing CSV files.

---

## 🏗️ Project Architecture

```
                main.py
                   │
                   ▼
          Load Configuration
                   │
                   ▼
            Initialize Logger
                   │
                   ▼
         Create Pipeline Components
                   │
                   ▼
             ETLPipeline.run()
                   │
      ┌────────────┼────────────┐
      ▼            ▼            ▼
   Reader      Validator   Transformer
      │            │            │
      └──────┬─────┴─────┬──────┘
             ▼
       Valid / Invalid Split
             │
      ┌──────┴──────┐
      ▼             ▼
 Valid Writer   Invalid Writer
```

---

# 📂 Project Structure

```
OrderProcessingETL/
│
├── config/
│   └── config.yaml
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── invalid/
│
├── exceptions/
│
├── logs/
│
├── models/
│   └── order.py
│
├── pipeline/
│   └── pipeline.py
│
├── readers/
│   ├── base_reader.py
│   └── csv_reader.py
│
├── transformer/
│   └── transformer.py
│
├── utils/
│   ├── config.py
│   └── logger.py
│
├── validators/
│   └── validator.py
│
├── writers/
│   └── csv_writer.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Features

- Modular ETL Architecture
- Object-Oriented Design
- Configurable Pipeline using YAML
- Centralized Logging
- Custom Exception Handling
- Business Rule Validation
- Data Transformation
- Valid & Invalid Record Separation
- Clean Folder Structure
- Type Hinting
- Dependency Injection
- Extensible Reader/Writer Design

---

# 🧩 ETL Workflow

### 1️⃣ Extract

- Reads raw CSV data
- Converts each row into an `Order` object
- Handles file-related exceptions
- Logs extraction progress

---

### 2️⃣ Validate

Business validation rules include:

- Required field validation
- Positive order amount
- Valid age range
- Valid payment method
- Date format validation
- Missing value detection

Invalid records are separated without stopping the pipeline.

---

### 3️⃣ Transform

Transforms clean records by:

- Removing unnecessary whitespace
- Standardizing text fields
- Formatting dates
- Cleaning optional fields
- Standardizing values before loading

---

### 4️⃣ Load

Writes

- Clean records → Cleaned CSV
- Invalid records → Invalid CSV

Generates execution logs throughout the process.

---

# 🛠️ Technologies Used

- Python 3
- CSV Module
- YAML
- Logging
- Dataclasses
- Abstract Base Classes (ABC)
- Type Hinting

---

# 📚 Software Engineering Concepts Applied

## Object-Oriented Programming

- Classes
- Dataclasses
- Abstraction
- Encapsulation

---

## SOLID Principles

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Dependency Injection
- Separation of Concerns

---

## Configuration Management

Pipeline configuration is stored inside:

```
config/config.yaml
```

This avoids hardcoded values and allows configuration changes without modifying application code.

---

## Logging

The pipeline logs:

- Pipeline start/end
- File reading
- Validation summary
- Writing status
- Errors
- Warnings

Console logging and file logging are both supported.

---

## Exception Handling

Custom exceptions are used for:

- File Read Errors
- File Write Errors
- Validation Errors
- Unexpected Runtime Errors

---

# 📊 Validation Rules

Examples include:

- Age must be within the allowed range
- Order amount must be greater than zero
- Required fields cannot be empty
- Payment method must be valid
- Date format must match the expected format

---

# 🔄 Pipeline Execution Flow

```
main.py
    │
    ▼
Load Config
    │
    ▼
Initialize Logger
    │
    ▼
Create ETL Pipeline
    │
    ▼
Read CSV
    │
    ▼
Validate Records
    │
    ├───────────────┐
    ▼               ▼
Valid           Invalid
    │               │
Transform          │
    │               │
    └──────┬────────┘
           ▼
      Write Output Files
           ▼
        Pipeline Ends
```

---

# 🚀 How to Run

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd OrderProcessingETL
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the pipeline

```bash
python main.py
```

---

# 📈 Future Improvements

- JSON Reader
- Excel Reader
- REST API Reader
- Database Writer
- PostgreSQL Integration
- Factory Pattern
- Strategy Pattern
- Unit Testing with pytest
- Streaming large datasets using generators
- Airflow orchestration
- Docker support
- CI/CD pipeline
- Data Quality Reports
- Performance Metrics

---

# 🎯 Learning Outcomes

This project helped me gain practical experience with:

- ETL Pipeline Design
- Object-Oriented Programming
- Python Project Structure
- Configuration Management
- Logging
- Exception Handling
- Data Validation
- Data Transformation
- Clean Code Principles
- Software Engineering Best Practices

---

# 📄 License

This project is created for educational and portfolio purposes.
