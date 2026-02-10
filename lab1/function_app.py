# =============================================================================
# IMPORTS
# =============================================================================
import azure.functions as func
import logging
import json
import re
from datetime import datetime
import os
import uuid

from azure.cosmos import CosmosClient

# =============================================================================
# CREATE THE FUNCTION APP
# =============================================================================
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# =============================================================================
# COSMOS CLIENT FACTORY (Safe)
# =============================================================================
def get_cosmos_client():
    """
    Returns a CosmosClient instance using environment variables.
    Client is created inside the function call to avoid startup crashes.
    """
    conn_str = os.getenv("COSMOS_CONNECTION_STRING")
    if not conn_str:
        raise RuntimeError("COSMOS_CONNECTION_STRING is missing")

    db_name = os.getenv("COSMOS_DATABASE_NAME", "TextAnalyzerDB")
    container_name = os.getenv("COSMOS_CONTAINER_NAME", "AnalysisResults")

    client = CosmosClient.from_connection_string(conn_str)
    database = client.get_database_client(db_name)
    container = database.get_container_client(container_name)
    return container

# =============================================================================
# DEFINE THE TEXT ANALYZER FUNCTION
# =============================================================================
@app.route(route="TextAnalyzer")
def TextAnalyzer(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Text Analyzer API was called!')

    # -----------------------------
    # STEP 1: GET THE TEXT INPUT
    # -----------------------------
    text = req.params.get('text')
    if not text:
        try:
            req_body = req.get_json()
            text = req_body.get('text')
        except ValueError:
            pass

    if not text:
        # -----------------------------
        # STEP 2: HANDLE MISSING TEXT
        # -----------------------------
        instructions = {
            "error": "No text provided",
            "howToUse": {
                "option1": "Add ?text=YourText to the URL",
                "option2": "Send a POST request with JSON body: {\"text\": \"Your text here\"}",
                "example": "https://your-function-url/api/TextAnalyzer?text=Hello world"
            }
        }
        return func.HttpResponse(
            json.dumps(instructions, indent=2),
            mimetype="application/json",
            status_code=400
        )

    # -----------------------------
    # STEP 3: ANALYZE THE TEXT
    # -----------------------------
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    char_count_no_spaces = len(text.replace(" ", ""))
    sentence_count = len(re.findall(r'[.!?]+', text)) or 1
    paragraph_count = len([p for p in text.split('\n\n') if p.strip()])
    reading_time_minutes = round(word_count / 200, 1)
    avg_word_length = round(char_count_no_spaces / word_count, 1) if word_count > 0 else 0
    longest_word = max(words, key=len) if words else ""
    analysis_id = str(uuid.uuid4())

    response_data = {
        "id": analysis_id,
        "analysis": {
            "wordCount": word_count,
            "characterCount": char_count,
            "characterCountNoSpaces": char_count_no_spaces,
            "sentenceCount": sentence_count,
            "paragraphCount": paragraph_count,
            "averageWordLength": avg_word_length,
            "longestWord": longest_word,
            "readingTimeMinutes": reading_time_minutes
        },
        "metadata": {
            "analyzedAt": datetime.utcnow().isoformat(),
            "textPreview": text[:100] + "..." if len(text) > 100 else text
        }
    }

    # -----------------------------
    # STEP 4: STORE DOCUMENT IN COSMOS DB
    # -----------------------------
    try:
        container = get_cosmos_client()
        document = {
            "id": analysis_id,
            "analysis": response_data["analysis"],
            "metadata": response_data["metadata"],
            "originalText": text
        }
        container.create_item(body=document)
    except Exception as e:
        logging.exception("Cosmos DB write failed")
        return func.HttpResponse(
            json.dumps({"error": "Failed to store data in Cosmos DB"}),
            mimetype="application/json",
            status_code=500
        )

    # -----------------------------
    # STEP 5: RETURN RESPONSE
    # -----------------------------
    return func.HttpResponse(
        json.dumps(response_data, indent=2),
        mimetype="application/json",
        status_code=200
    )

# =============================================================================
# DEFINE THE ANALYSIS HISTORY FUNCTION
# =============================================================================
@app.route(route="GetAnalysisHistory", methods=["GET"])
def GetAnalysisHistory(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("GetAnalysisHistory API was called!")

    # -----------------------------
    # STEP 1: READ LIMIT PARAMETER
    # -----------------------------
    limit_param = req.params.get("limit")

    try:
        limit = int(limit_param) if limit_param else 10
    except ValueError:
        limit = 10

    # Optional safety cap
    if limit > 50:
        limit = 50

    # -----------------------------
    # STEP 2: QUERY COSMOS DB
    # -----------------------------
    try:
        container = get_cosmos_client()

        query = """
            SELECT c.id, c.analysis, c.metadata
            FROM c
            ORDER BY c.metadata.analyzedAt DESC
        """

        items = list(
            container.query_items(
                query=query,
                enable_cross_partition_query=True
            )
        )

        results = items[:limit]

    except Exception as e:
        logging.exception("Cosmos DB read failed")
        return func.HttpResponse(
            json.dumps({"error": "Failed to retrieve analysis history"}),
            mimetype="application/json",
            status_code=500
        )

    # -----------------------------
    # STEP 3: RETURN RESPONSE
    # -----------------------------
    response = {
        "count": len(results),
        "results": results
    }

    return func.HttpResponse(
        json.dumps(response, indent=2),
        mimetype="application/json",
        status_code=200
    )

