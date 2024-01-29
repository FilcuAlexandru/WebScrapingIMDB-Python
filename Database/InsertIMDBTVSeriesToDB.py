import pandas as pd
from sqlalchemy import create_engine
from DatabaseConnection import engine

# Load data from the Excel file
excel_file_path = r'C:\Users\alexandru.filcu\OneDrive - virtual7 GmbH\Desktop\WebScrapingIMDB\imdb_top_tv_series.xlsx'
df = pd.read_excel(excel_file_path)

# Table name in your database
table_name = 'tvseries_data'

# Insert DataFrame into Oracle database
try:
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f'Data inserted into the table "{table_name}" successfully.')
except Exception as ex:
    print(f'An error occurred while inserting data: {ex}')