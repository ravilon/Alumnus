# Class main
# Here we will teste the QueryExecutor class

# Import the class QueryExecutor
from DataBaseInterface.QueryExecutor import QueryExecutor

# Create a instance of the class QueryExecutor
query_executor = QueryExecutor()

# Create a query to get all the Users
query = "SELECT * FROM ConectUser"

# Fetch the results from the cursor
results = query_executor.execute_query(query, None)

# Print the results
for row in results:
    print(row)

# Close the connection
query_executor.close()


