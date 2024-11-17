import pandas as pd 
import re 

def clean_type(data):
    # Apply the function to the Type column
    data['Type'] = data['Type'].apply(simplify_type)
    # Save the updated data
    data.to_csv('property_data(2).csv', index=False)

def simplify_type(property_type):
    # Use regex to find the last word in the property type, which is likely the main type
    match = re.search(r"\b\w+$", property_type)
    if match:
        return match.group(0).lower()  # Return the matched type in lowercase for consistency
    else:
        return property_type.lower()   # Return original if no match

def main():
    # Read in updated data 
    data = pd.read_csv('property_data(1).csv')
    clean_type(data)

if __name__ == "__main__": main() 
