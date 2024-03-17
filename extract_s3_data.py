import boto3
import pandas as pd

# Initialize the S3 client
client = boto3.client(
    's3',
    region_name='us-east-1',
    aws_access_key_id='AKIAUMMQEMX5XKO4QJ6O',
    aws_secret_access_key='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'
)

#To create access and secret id, Create a user in IAM with S3Full access and generate these
#ID's from there. Then only we can able to access the contents

# Specify the bucket and key
bucket_name = 'data-storage-repo-dev'
key = 'ETL_DEMO/raw/OrderHistory/Order_History_Sales.csv'

# Get the object
obj = client.get_object(Bucket=bucket_name, Key=key)

# Read the CSV file
df = pd.read_csv(obj['Body'],delimiter='|')

# Now df contains the data from the CSV file
print(df.head())
