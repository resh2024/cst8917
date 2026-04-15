# CST8917 Lab 4 PhotoPipe

## YouTube Demo Link

https://www.youtube.com/watch?v=e45e_LwAHBc

PhotoPipe is a simple event-driven app using Azure. When you upload an image, it automatically processes it, pulls some basic info (like size and type), and logs the event.

---

## What it uses

- Azure Blob Storage
- Azure Functions (Python)
- Event Grid
- Table Storage
- Basic HTML client

---

## Setup

### 1. Azure setup

- Create a resource group
- Create a storage account
- Add 2 containers:
  - `image-uploads` (public)
  - `image-results` (private)

- Enable CORS (`*`) and blob anonymous access

### 2. Functions

- Create a Python Azure Functions project
- Add the provided files (`function_app.py`, etc.)
- Install deps:

```bash
pip install -r requirements.txt
```

- Add your connection string in `local.settings.json`
- Run locally:

```bash
func start
```

### 3. Deploy

- Deploy the function app to Azure
- Add `STORAGE_CONNECTION_STRING` in app settings
- Test `/api/health`

### 4. Event Grid

- Create a system topic for your storage account
- Add:
  - **process-image** → only `.jpg` / `.png`
  - **audit-log** → all uploads

### 5. Client

- Open `client.html`
- Enter:
  - storage account name
  - SAS token
  - function app URL

---

## Testing

- Upload `.jpg` / `.png` → shows results + logs
- Upload other files → only logs
