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
In this part I used Matplotlib to explore the data. I used histograms, boxplots, correlation tables, heatmaps, bar charts and pivot tables:

![alt text](https://github.com/Rami97rgb/Real-Estate-Price-Prediction/blob/master/images/describe.png "describe")
![alt text](https://github.com/Rami97rgb/Real-Estate-Price-Prediction/blob/master/images/barchart.png "barchart")
![alt text](https://github.com/Rami97rgb/Real-Estate-Price-Prediction/blob/master/images/boxplot.png "boxplot")
![alt text](https://github.com/Rami97rgb/Real-Estate-Price-Prediction/blob/master/images/heatmap.png "heatmap")

## Model Building
Using scikit-learn I split data into train and test and then trained three different models: Linear Regeression, Random Forest, and SVR.
   * Linear Regeression achieved a mae of ~600
   * SVR achieved a mae of ~400
   * Random Forest a mae of ~200
   
linear regression is performing badly because we have a very sparse matrix and multicolinearity.

random forest is performing best because we have a sparse matrix when replacing city variable with one-hot vectors.

## Productionisation
A Flask API has been used to interact with the client where a simple website frontend was built that interfaces with our model in the backend:

![alt text](https://github.com/Rami97rgb/Real-Estate-Price-Prediction/blob/master/images/website.png "website")

## Resources
A huge help and inspiration for this project: https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

Learning BeautifulSoup scraping: https://www.youtube.com/watch?v=dRcvJRmqFHQ

Productionizing the model: https://towardsdatascience.com/productionizing-your-machine-learning-model-221468b0726d
