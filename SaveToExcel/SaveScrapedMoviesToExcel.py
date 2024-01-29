import os
import sys
from pathlib import Path

# Add the parent directory to sys.path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

# Import the scrape_imdb_top_movies function
from WebScraping.IMDBMovieScraper import scrape_imdb_top_movies

if __name__ == "__main__":
    # Call the scraping function directly from IMDBMovieScraperToExcel.py
    scraped_data = scrape_imdb_top_movies()

    # Save the DataFrame to an Excel file
    scraped_data.to_excel('imdb_top_movies.xlsx', index=False)
    print("Data saved to imdb_top_movies.xlsx")
