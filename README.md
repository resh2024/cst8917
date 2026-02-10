## Running the Project Locally

### Prerequisites

- Python 3.12+
- Azure Functions Core Tools
- An Azure Cosmos DB account

### Setup Steps

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set the following environment variables:

   ```bash
    COSMOS_CONNECTION_STRING

    COSMOS_DATABASE_NAME

    COSMOS_CONTAINER_NAME
   ```

3. Start the Azure Functions runtime:

   ```bash
   func start
   ```

4. Test the API endpoints locally:

   ```bash
   http://localhost:7071/api/TextAnalyzer

    http://localhost:7071/api/GetAnalysisHistory
   ```
