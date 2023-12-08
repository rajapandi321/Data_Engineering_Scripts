import snowflake.connector

# Establishing connection parameters
conn = snowflake.connector.connect(
    user='JEEVAN',
    password='Optisol@2023',
    account='oozelmy-lxb06506',
    warehouse='COMPUTE_WH',
    database='SNOWFLAKE_PYTHON',
    schema='PUBLIC',
    role='ACCOUNTADMIN'
)

# Creating a cursor object using the connection
cur = conn.cursor()

# Set the schema and database context
cur.execute("USE DATABASE SNOWFLAKE_PYTHON")
cur.execute("USE SCHEMA PUBLIC")

# Execute your query
cur.execute('create table if not exists student(id int,name varchar(20),mark int)')
cur.execute("insert into student values(1,'Raja',56)")
cur.execute('select * from student')
rows = cur.fetchall()

for row in rows:
    print(row)

# Closing the cursor and connection
cur.close()
conn.close()
