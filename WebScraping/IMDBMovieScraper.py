# Import necessary libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
import pandas as pd  # For handling data in a DataFrame

# Define the function to scrape top movies from IMDb
def scrape_imdb_top_movies():
    # Set user-agent and language headers to simulate a web browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    # Make a GET request to IMDb's top movies page with the defined headers
    response = requests.get('https://www.imdb.com/chart/top/', headers=headers)

    # Check the status code of the response (200 means success)
    print(response.url)  # Print the URL of the response 
    print(response.status_code)  # Print the HTTP status code of the response

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all containers that hold the movie information on the page
    movie_containers = soup.find_all('div', class_='sc-be6f1408-0 gVGktK cli-children')

    # Initialize lists to store movie data
    titles = []
    release_years = []
    runtimes = []
    rateds = []

    # Loop through each movie container to extract information
    for container in movie_containers:
        # Extract title and remove numbering
        title_element = container.find('a', href=lambda href: href and '/title/' in href)
        title = title_element.text.strip().split('. ', 1)[-1] if title_element else "N/A"

        # Extract release year, runtime, and rated
        metadata_items = container.find_all('span', class_='sc-be6f1408-8 fcCUPU cli-title-metadata-item')
        
        release_year = metadata_items[0].text.strip() if len(metadata_items) > 0 else "N/A"
        runtime = metadata_items[1].text.strip() if len(metadata_items) > 1 else "N/A"
        rated = metadata_items[2].text.strip() if len(metadata_items) > 2 else "N/A"

        # Print or append the data to lists as needed
        print(f"Title: {title}, Year: {release_year}, Runtime: {runtime}, Rated: {rated}")

        titles.append(title)
        release_years.append(release_year)
        runtimes.append(runtime)
        rateds.append(rated)

    # Create a DataFrame using the scraped data
    df = pd.DataFrame({
        'Title': titles,
        'Year': release_years,
        'Runtime': runtimes,
        'Rated': rateds
    })

    # Return the DataFrame
    return df

# Call the function if the script is run as the main module
if __name__ == "__main__":
    scrape_imdb_top_movies()
