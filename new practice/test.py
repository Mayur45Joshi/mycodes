import oracledb

# Create a connection
connection = oracledb.connect(
    user="your_username",
    password="your_password",
    dsn="localhost:1521/orcl"   # host:port/service_name
)

# Create a cursor
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SELECT * FROM DEPT")

# Fetch all rows
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.close()



