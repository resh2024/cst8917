# DATABASE CHOICE

## Your Choice: Which database did you select?

Ans - I selected Azure Cosmos DB (Core / NoSQL API) as the database for this project.

---

## Justification: Why is this the best choice for this use case? (3-5 sentences)

Ans - Azure Cosmos DB works well for this project because the text analysis results are stored as JSON and don’t need a fixed structure. This makes it easy to add or change fields later without updating a database schema. It also integrates directly with Azure Functions, which keeps the backend simple and secure. Since the application is API-based, fast read and write performance is another reason Cosmos DB is a good fit.

---

## Alternatives Considered: What other options did you evaluate and why did you reject them?

Ans - Azure SQL Database was considered, but it was not ideal because it requires a predefined schema, which is less flexible for storing analysis data. File-based storage and in-memory solutions were also considered, but they were rejected because they do not persist data reliably or scale in a cloud environment. Other external NoSQL databases were not chosen because Cosmos DB provides better integration with Azure services used in this project.

## Cost Considerations: How does pricing work for your chosen database?

Ans - Cosmos DB pricing is based on Request Units, which reflect how much work each database operation uses. This allows costs to stay low when usage is minimal. For this project, the number of reads and writes is small, so costs remain very manageable. Azure’s free tier also makes it suitable for development and academic use.

---
