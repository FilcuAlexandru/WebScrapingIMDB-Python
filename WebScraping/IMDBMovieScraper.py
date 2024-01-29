# scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_imdb_top_movies():
    # Set user-agent and language headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5'
    }

    # Make the GET request with headers
    response = requests.get('https://www.imdb.com/chart/top/', headers=headers)

    # Check the status code for response received
    # Success code - 200 means the request was successful
    print(response.url)  # Print the URL of the response 
    print(response.status_code)  # Print the HTTP status code of the response

    # Parse the HTML content
    # Create a BeautifulSoup object to parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the container that holds the movie titles and release years
    # Locate the HTML element with the specified class that contains movie information
    movie_container = soup.find('ul', class_='ipc-metadata-list')

    # Check if movie_container is not None before attempting to find titles and release years
    if movie_container:
        # Find all h3 tags (h3 tags = movie title) within the movie_container
        # Extract a list of all 'h3' tags containing movie information
        movie_elements = movie_container.find_all('h3')

        # Initialize lists to store data
        titles = []
        release_years = []
        runtimes = []
        rateds = []

        # Iterate over each movie element to extract and print title, release year, runtime, and rated
        for movie_element in movie_elements:
            # Extract and print the movie title
            title = movie_element.text.strip()

            # Extract and print the release year
            # Locate the next 'span' tag with a specific class relative to the current 'h3' tag
            release_year_span = movie_element.find_next('span', class_='sc-1e00898e-8 hsHAHC cli-title-metadata-item')
            release_year = release_year_span.text.strip() if release_year_span else "N/A"

            # Extract and print the runtime
            # Locate the next 'span' tag with a specific class relative to the current 'span' tag
            runtime_span = release_year_span.find_next('span', class_='sc-1e00898e-8 hsHAHC cli-title-metadata-item')
            runtime = runtime_span.text.strip() if runtime_span else "N/A"

            # Extract and print the rated
            # Locate the next 'span' tag with a specific class relative to the current 'span' tag
            rated_span = runtime_span.find_next('span', class_='sc-1e00898e-8 hsHAHC cli-title-metadata-item')
            rated = rated_span.text.strip() if rated_span else "N/A"

            # Print all information in the same line
            print(f"Title: {title}, Year: {release_year}, Runtime: {runtime}, Rated: {rated}")

            # Append the data to lists
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

    else:
        # Print an error message if movie_container is not found
        print("Could not find the movie container. Check the HTML structure.")

# Call the function
if __name__ == "__main__":
    scrape_imdb_top_movies()
