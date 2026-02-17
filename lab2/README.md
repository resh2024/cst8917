# Lab 2: Smart Image Analyzer with Durable Functions

## CST8917 – Serverless Applications | Winter 2026

## Youtube Link Demo Video

https://www.youtube.com/watch?v=9d9XLfyqRp4

---

## Overview

This project implements a Smart Image Analyzer using Azure Durable Functions and the **Fan-Out/Fan-In** pattern.

When an image is uploaded to Azure Blob Storage, a Durable Function orchestration is triggered automatically. Four image analysis activities run in parallel, their results are combined, and the final report is stored in Azure Table Storage. Results can be retrieved through an HTTP endpoint.

---

## Technologies Used

- Azure Functions (Python)
- Durable Functions
- Azure Blob Storage (Trigger)
- Azure Table Storage
- Azurite (Local Storage Emulator)
- Pillow (Image processing)

---

## Prerequisites

- Python 3.11 or 3.12
- Azure Functions Core Tools
- VS Code with Azure Functions Extension
- Azure Storage Explorer
- Azurite

---

## Running Locally

### 1. Start Azurite

azurite

---

### 2. Activate Virtual Environment

**Mac/Linux**
source .venv/bin/activate

**Windows**
.venv\Scripts\activate

---

### 3. Install Dependencies

python -m pip install -r requirements.txt

---

### 4. Start the Function App

func start

---

### 5. Test the Workflow

1. Upload an image to the configured Blob container.
2. The Blob trigger starts the orchestration.
3. Four activities execute in parallel.
4. Results are stored in Azure Table Storage.
5. Retrieve results using the HTTP endpoint shown in the terminal.

---

## Pattern Used

**Fan-Out/Fan-In**  
Independent image analyses run in parallel, reducing total execution time compared to sequential execution.
