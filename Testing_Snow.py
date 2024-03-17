import snowflake.connector
import boto3
import pandas as pd

# Initialize the S3 client
client = boto3.client(
    's3',
    region_name='us-east-1',
    aws_access_key_id='AKIAUMMQEMX5XKO4QJ6O',
    aws_secret_access_key='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'
)

# Fetch Raw File
bucket_name1 = 'data-storage-repo-dev'
key1 = 'ETL_DEMO/raw/OrderHistory/Order_History_Sales.csv'

obj1 = client.get_object(Bucket=bucket_name1, Key=key1)

raw_file = pd.read_csv(obj1['Body'],delimiter='|')

#Fetch processed file
bucket_name2 = 'data-storage-repo-dev'
key2 = 'ETL_DEMO/processed/orderHistory/part-00000-9140b2f3-84ef-47fd-872c-2bdc579d3fb7-c000.csv'

obj2 = client.get_object(Bucket=bucket_name2, Key=key2)

processed_file = pd.read_csv(obj2['Body'])

# Snowflake connection parameters
account = 'wqwibah-wk13429'
user = 'rajapandi'
password = 'Optisol@2023'
warehouse = 'COMPUTE_WH'
database = 'OPTISOL_SALES_DW'
schema = 'ANALYTICS'

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)

cur = conn.cursor()

cur.execute("SELECT * FROM ORDER_HISTORY")

results = cur.fetchall()

columns = [desc[0] for desc in cur.description]

snowflake_df = pd.DataFrame(results, columns=columns)

# Close the cursor and connection
cur.close()
conn.close()

# Count rows in dataframes
count_snowflake = snowflake_df.count()
count_s3_1 = raw_file.count()
count_s3_2 = processed_file.count()

# Print the counts
print("Count of rows in Snowflake dataframe:", count_snowflake)
print("Count of rows in S3 dataframe 1:", count_s3_1)
print("Count of rows in S3 dataframe 2:", count_s3_2)