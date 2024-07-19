# QuotesScraperAnalysis
# Quotes Scraping and Analysis

This repository contains a project that scrapes quotes from the website [Quotes to Scrape](https://quotes.toscrape.com/), performs data analysis on the collected quotes, visualizes the results, and saves the data to a SQLite database.

## Project Structure

- **quote_scraper.py**: The main script that scrapes quotes, performs analysis, visualizes the results, and saves the data to the database.
- **requirements.txt**: A list of Python dependencies required to run the project.

## Features

- Scrapes quotes and authors from the [Quotes to Scrape](https://quotes.toscrape.com/) website.
- Analyzes the most frequent authors.
- Generates a word cloud of the most common words in the quotes.
- Saves the scraped data to a SQLite database.
- Visualizes the analysis results using bar plots and word clouds.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/QuotesScrapingAndAnalysis.git
    cd QuotesScrapingAndAnalysis
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `quote_scraper.py` script:
    ```bash
    streamlit run quote_scraper.py
    ```

2. Follow the instructions on the Streamlit app to scrape the quotes, analyze the data, and visualize the results.

## Dependencies

The project requires the following Python libraries:

- requests
- beautifulsoup4
- pandas
- matplotlib
- seaborn
- streamlit
- sqlalchemy
- wordcloud
- nltk

You can install all dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt

Example

The project includes an example script that demonstrates how to use the quote_scraper.py script. The example shows how to scrape the quotes, analyze the data, visualize the results, and save the data to the database.

Results

After running the project, the results include:

	•	A bar plot showing the top authors by the number of quotes.
	•	A word cloud visualizing the most common words in the quotes.
	•	The scraped data saved in a SQLite database (quotes.db).

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Süheyl Özdemir
Data Scientist & AI Volunteer

### Explanation

- **Title and Description**: Provides a clear title and description of the project.
- **Project Structure**: Lists the main files in the repository.
- **Features**: Describes the main features of the project.
- **Installation**: Instructions on how to clone the repository and install dependencies.
- **Usage**: Instructions on how to run the script.
- **Dependencies**: Lists the required Python libraries and how to install them.
- **Example**: Describes the example script included in the project.
- **Results**: Describes the results produced by the project.
- **License**: Specifies the project's license.
- **Author**: Includes the author's name and title.

This README file should provide a clear and comprehensive overview of your project. Adjust any sections as necessary to fit your specific project details.
