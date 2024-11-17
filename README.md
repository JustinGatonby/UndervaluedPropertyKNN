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

  
