import pandas as pd

df = pd.read_excel(r"D:\\Versand\\8541_Errors.xlsx")
df1 = df[['client_id', 'api_error_message']]
pattern = r"Verkäufer: '(?P<seller>.*?)' \/ Amazon: '(?P<amazon>.*?)'"

# Use str.extract to create new columns in the original DataFrame (df1)
extracted_data = df1['api_error_message'].str.extract(pattern)
 
# Check if any rows were matched and update the DataFrame accordingly
if extracted_data is not None:
    df1[['verkaufer', 'amazon']] = extracted_data # Selecting columns 1 and 2 from the extracted data
else:
    df1[['verkaufer', 'amazon']] = 'Not Available'
 
# Display the original DataFrame with the new columns and 'client_id'
dataframe = df1[['client_id', 'verkaufer', 'amazon']]
dataframe.rename(columns={'verkaufer': 'Seller'}, inplace=True)
dataframe.rename(columns={'amazon': 'Amazon_Catalog'}, inplace=True)
 
dataframe.to_csv("D:\\excel.csv",index=False, header=True)