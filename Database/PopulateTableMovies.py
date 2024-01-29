# Import necessary modules and classes
import pandas as pd
from sqlalchemy.orm import sessionmaker
from DatabaseConnection import engine
from CreateTableMovies import Movie

# Load data from the Excel file
excel_file_path = r'C:\Users\alexandru.filcu\OneDrive - virtual7 GmbH\Desktop\WebScrapingIMDB\imdb_top_movies.xlsx'
df = pd.read_excel(excel_file_path)

# SQLAlchemy session
Session = sessionmaker(bind=engine)
session = Session()

# Table name in your database
table_name = 'movies'

# Update existing records or insert new ones
try:
    for index, row in df.iterrows():
        # Use the __init__ method that excludes the 'id' column
        movie = Movie(
            title=row['Title'],
            year=row['Year'],
            runtime=row['Runtime'],
            rated=row['Rated']
        )
        # Use add method to insert records without specifying id
        session.add(movie)

    # Commit the changes
    session.commit()

    print(f'Data updated in the table "{table_name}" successfully.')
except Exception as ex:
    print(f'An error occurred while updating data: {ex}')
finally:
    # Close the session
    session.close()
