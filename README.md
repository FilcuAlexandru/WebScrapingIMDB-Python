# WebScrapingIMDB-Python
 A Python scraper that scrapes the best movies and TV series from IMDB and then saves them to excel files and feeds them into an Oracle 21c database using SQLAlchemy.

Prerequisites for WebScrapingIMDB Project
 - Before you begin working with the WebScrapingIMDB project, ensure you have the following prerequisites:

1. Python 3.8 or Later: The project is developed using Python. Download and install Python from the official Python website.

2. Docker: Docker is used for containerization. Install Docker from the official Docker website.

3. Git: Git is required for version control and cloning the project repository. Install Git from Git's official website.

4. Code Editor: Choose a code editor or integrated development environment (IDE) of your preference. Popular choices include Visual Studio Code, PyCharm, or Atom.

5. Oracle Database: The project is designed to work with an Oracle Database. Ensure you have access to an Oracle Database instance, and note the connection details (username, password, host, port, service name).

6. Oracle Instant Client (Optional): If you are connecting to an Oracle Database remotely, you might need the Oracle Instant Client. Follow the instructions in the Oracle documentation to install it.


WebScrapingIMDB Project Documentation

Project Structure
 - The WebScrapingIMDB project is organized into several folders, each serving a specific purpose:

1. The "Database" Folder:
 -> CreateTableMovies.py: Defines the SQLAlchemy model for movies and creates the corresponding table in the Oracle database.
 -> CreateTableTVSeries.py: Defines the SQLAlchemy model for TV series and creates the corresponding table in the Oracle database.
 -> DatabaseConnection.py: Manages the connection to the Oracle database using cx_Oracle and SQLAlchemy.
 -> InsertIMDBMoviesToDB.py: Inserts data from the "imdb_top_movies.xlsx" file into the movies table in the Oracle database.
 -> InsertIMDBTVSeriesToDB.py: Inserts data from the "imdb_top_tv_series.xlsx" file into the TV series table in the Oracle database.
 -> PopulateTableMovies.py: Uses SQLAlchemy to update existing records or insert new movies into the movies table.

2. The "SaveToExcel" Folder:
 -> SaveScrapedMoviesToExcel.py: Saves scraped data from IMDb's top movies to an Excel file.
 -> SaveScrapedTVSeriesToExcel.py: Saves scraped data from IMDb's top TV series to an Excel file.

3. The "WebScraping" Folder:
 -> IMDBMovieScraper.py: Scrapes IMDb's top movies data using requests and BeautifulSoup.
 -> IMDBTVSeriesScraper.py: Scrapes IMDb's top TV series data using requests and BeautifulSoup.

4. The "Docker Setup" Files:
 -> Dockerfile: Defines a Docker image for the project. Uses the official Python 3.8-slim image, sets up the working directory, copies project files, installs dependencies from requirements.txt, and specifies the default script to execute.
 -> requirements.txt: Lists the project dependencies, including pandas, sqlalchemy, and requests.

5. The "Scraped Excel" Files:
 -> imdb_top_movies.xlsx: Excel file to store scraped top movie data. This excel is visible only after running the SaveScrapedMoviesToExcel.py script.
 -> imdb_top_tv_series.xlsx: Excel file to store scraped top TV series data. This excel is visible only after running the SaveScrapedTVSeriesToExcel.py script.

Docker Setup for WebScrapingIMDB Project:

 a.) Build the Docker Image, open a terminal in the project root directory and run the following command to build the Docker image: docker build -t webscrapingimdb-app .
 b.) Run the Docker Container, once the image is built, you can run a Docker container: docker run -it --rm webscrapingimdb-app
 c.) Explore the Container, you will now be inside the Docker container. Explore the contents and run scripts as needed.


 🎬🍿🚀 Enjoy exploring the world of movies and TV series with WebScrapingIMDB! 🎬🍿 🚀

I hope you find this project insightful and have a great time discovering the top movies and TV series from IMDb. If you have any questions, feedback, or suggestions, feel free to reach out. 
Happy coding and movie-watching! 🌟✨

Enjoy the journey,
Alexandru Filcu!




