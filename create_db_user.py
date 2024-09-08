import psycopg

# Connect to the PostgreSQL service (use the service name as the host)
connection = psycopg.connect(
    host="localhost",  # Change this to match the service name in your GitHub Action
    user="postgres",  # Superuser
    password="testpwd",  # Password set in the GitHub Action
    port="5432",
    dbname="postgres"  # Default database
)

# Set autocommit to True because CREATE USER and CREATE DATABASE statements 
# cannot run inside a transaction
connection.autocommit = True

# Create a user and a database, assign ownership to the new user
connection.execute("CREATE USER myuser WITH PASSWORD 'mypassword'")
connection.execute("CREATE DATABASE mydatabase WITH OWNER myuser")

# Close the connection
connection.close()
