# Real-Estate-Price-Prediction
* Built an app that can predict value of California properties.
* Scraped 800 California property entries from Zillow using BeautifaulSoup.
* Cleaned the scraped data.
* Done some exploratory data analysis.
* Compared different machine learning models.
* Productionized the model using a website and a Flask API to interface with the client.

## Data Scraping
Used BeautifulSoup web scraper to get 800 data points located in California from Zillow. Selected these attributes:
* Property price
* Number of bedrooms
* Number of bathrooms
* Floorsize
* Address

## Data Cleaning
* Cleaned the by deleting invalid entries.
* converted price, bedrooms, bathrooms, and floorsize strings into actual values.
* Exracted city and zipcode from address string.
* Final DataFrame shape:

   Quantitive variables: price, bedrooms, bathrooms, floorsize, and zipcode.

   Categorical variables: city.

## EDA
In this I used Matplotlib to explore the data. I used histograms, boxplots, correlation tables, heatmaps, bar charts and pivot tables:
