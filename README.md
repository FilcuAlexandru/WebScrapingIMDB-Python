# WebScrapingIMDB-Python
A Python scraper that extracts the best movies and TV series from IMDB, saving them to Excel files, and feeding them into an Oracle 21c database using SQLAlchemy.

## Prerequisites for WebScrapingIMDB Project

Before you begin working with the WebScrapingIMDB project, ensure you have the following prerequisites:

1. **Python 3.8 or Later:** The project is developed using Python. [Download and install Python](https://www.python.org/downloads/).

2. **Docker:** Docker is used for containerization. [Install Docker](https://www.docker.com/get-started).

3. **Git:** Git is required for version control and cloning the project repository. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

4. **Code Editor:** Choose a code editor or integrated development environment (IDE) of your preference. Popular choices include Visual Studio Code, PyCharm, or Atom.

5. **Oracle Database:** The project is designed to work with an Oracle Database. Ensure you have access to an Oracle Database instance, and note the connection details (username, password, host, port, service name).

6. **Oracle Instant Client (Optional):** If you are connecting to an Oracle Database remotely, you might need the Oracle Instant Client. [Follow the instructions](https://www.oracle.com/database/technologies/instant-client.html).

## WebScrapingIMDB Project Documentation

### Project Structure

#### The "Database" Folder:

- `CreateTableMovies.py:` Defines the SQLAlchemy model for movies and creates the corresponding table in the Oracle database.
- `CreateTableTVSeries.py:` Defines the SQLAlchemy model for TV series and creates the corresponding table in the Oracle database.
- `DatabaseConnection.py:` Manages the connection to the Oracle database using cx_Oracle and SQLAlchemy.
- `InsertIMDBMoviesToDB.py:` Inserts data from the "imdb_top_movies.xlsx" file into the movies table in the Oracle database.
- `InsertIMDBTVSeriesToDB.py:` Inserts data from the "imdb_top_tv_series.xlsx" file into the TV series table in the Oracle database.
- `PopulateTableMovies.py:` Uses SQLAlchemy to update existing records or insert new movies into the movies table.

#### The "SaveToExcel" Folder:

- `SaveScrapedMoviesToExcel.py:` Saves scraped data from IMDb's top movies to an Excel file.
- `SaveScrapedTVSeriesToExcel.py:` Saves scraped data from IMDb's top TV series to an Excel file.

#### The "WebScraping" Folder:

- `IMDBMovieScraper.py:` Scrapes IMDb's top movies data using requests and BeautifulSoup.
- `IMDBTVSeriesScraper.py:` Scrapes IMDb's top TV series data using requests and BeautifulSoup.

#### The "Docker Setup" Files:

- `Dockerfile:` Defines a Docker image for the project. Uses the official Python 3.8-slim image, sets up the working directory, copies project files, installs dependencies from requirements.txt, and specifies the default script to execute.
- `requirements.txt:` Lists the project dependencies, including pandas, sqlalchemy, and requests.

#### The "Scraped Excel" Files:

- `imdb_top_movies.xlsx:` Excel file to store scraped top movie data. This excel is visible only after running the SaveScrapedMoviesToExcel.py script.
- `imdb_top_tv_series.xlsx:` Excel file to store scraped top TV series data. This excel is visible only after running the SaveScrapedTVSeriesToExcel.py script.

### Docker Setup for WebScrapingIMDB Project:

1. **Build the Docker Image:**
    ```bash
    docker build -t webscrapingimdb-app .
    ```

2. **Run the Docker Container:**
    ```bash
    docker run -it --rm webscrapingimdb-app
    ```

3. **Explore the Container:**
    You will now be inside the Docker container. Explore the contents and run scripts as needed.

🎬🍿🚀 **Enjoy exploring the world of movies and TV series with WebScrapingIMDB!** 🎬🍿 🚀

I hope you find this project insightful and have a great time discovering the top movies and TV series from IMDb. If you have any questions, feedback, or suggestions, feel free to reach out. 

Happy coding and movie-watching! 🌟✨

Enjoy the journey,
Alexandru Filcu!
