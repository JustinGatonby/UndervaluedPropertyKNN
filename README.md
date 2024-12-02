# UndervaluedPropertyKNN
An R and Python project using K-Nearest Neighbors regression to identify undervalued properties in the Western Cape, South Africa.

## Overview 
* Scrapes data from the Property24 website.
* Cleans data set and adds features.
* Visualizes and analyzes data.
* Implements and evaluates a kNN model.
* Produces an informative data set. 

## Data Collection 
* Data collection is implemented in Python. 
* The source code of Propery24’s website is converted into a string.
* Then using built-in string functions, data on 1583 properties under the value of R1.5 million, from Cape Town is collected; this includes price (target variable), a link to the property, location, type, number of bedrooms, number of bathrooms, parkings spaces, floor size and erf size.
* These attributes are stored in the data set, property_data.csv.

## Feature Engineering 
* coords.py adds the coordinates of each location to the data set, producing property_data(1).csv.
* type.py cleans the type variable, producing property_data(2).csv.

## Data Cleaning 
* The property_data(2).csv file is loaded to RStudio, where it is labeled "data".
* Using functions from the *dplyr* package, the missing values are dealt with.
* Only missing values under "Erf Size" and "Floor Size" remain, on the condition that each observation must contain a value for at least one of the aforementioned variables. 
* Observations meeting certain conditions are removed and, as a result, the data set is reduced to 1322 observations.
* The cleaned data is stored as clean_data.csv, which will be used for visualization and analysis. 

## Data Visualisation and Analysis 
* Visualisation is primarily conducted using functions from the *ggplot2* package.
* Important attributes are plotted to find those which are most informative.
* The findings concluded that a kNN model would be most effective at predicting property prices.

## Modelling and Evaluation
* Variables selected during the process of data visualization and analysis are used in a kNN model.
* The code for the initial model and the tests conducted on it can be found under Evaluation.Rmd.
* Each variable is weighted according to its importance, determined by a random forest model. The output of which can be found under weights_of_attributes.png.
* Then various values of k are tested and their performance measured using mean absolute error. The output of which can be found under evaluating_k.png
* The most effective model used the average price of the five most similar properties, as its prediction.

## Final Report
* The file labelled final_report.csv contains all relevant attributes collected.
* Properties classified as vacant land are removed due to unrealistic 
* Observations are ranked from most undervalued to most overpriced.
* 


  
