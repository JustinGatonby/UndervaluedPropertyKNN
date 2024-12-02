# UndervaluedPropertyKNN
An R and Python project using K-Nearest Neighbors regression to identify undervalued properties in the Western Cape, South Africa.

## Data Collection 
* Data collection is implemented in Python. 
* The source code of Propery24’s website is converted into a string.
* Then using built-in string functions, data on 1583 properties under the value of R1.5 million, from Cape Town is collected; this includes price (target variable), a link to the property, location, type, number of bedrooms, number of bathrooms, parkings spaces, floor size and erf size.
* These attributes are stored in the csv file, property data.

## Feature Engineering 
* coords.py adds the coordinates of each location to the data set, producing property_data(1).csv.
* type.py cleans the type variable, producing property_data(2).csv.

## Data Cleaning 
* The property_data(2).csv file is loaded to RStudio, where it is simply labeled "data".
* Using functions from the *dplyr* package, the missing values are dealt with.
* There are only missing values under "Erf Size" and "Floor Size", however, each observation must contain a value for at least one of the aforementioned variables. 
* Observations meeting certain conditions are removed, as a result, the data set is reduced to 1322 observations.
* The cleaned data is stored as data.csv.

## Data Visualisation and Analysis 
* Visualisation is primarily conducted using functions from the *ggplot2* package.
* Important attributes are plotted to find which are most informative.
* Concluded that a kNN model would be most effective at predicting property prices.

## Modelling and Evaluation
* Variables selected during the process of data visualization and analysis are used in a knn model.
* The code for the initial model and the tests conducted on it can be found under Evaluation.Rmd.
* Each variable is weighted according to its importance, determined by a random forest model. The output of which can be found under weights_of_attributes.png.
* Then various values of k are tested and their performance measured using mean absolute error.The output of which can be found under evaluating_k.png
* The most effective model took the average price of the five most similar properties.


  
