import pandas as pd 

def get_data():
    df = pd.read_csv("final_dataset.csv") 
    pd.options.display.float_format = '{:.0f}'.format
    df["Predicted"] = df["Predicted"].round(0)
    return df

def add_difference(df):
    df["Difference"] = 0 
    df["Difference"] = df["Predicted"] - df["Price"] 
    df = df.sort_values(by='Difference', ascending=False)
    return df 

def main():
    df = get_data() 
    df = add_difference(df) 
    df.to_csv('final_report.csv', index=False)
if __name__ == "__main__": main() 
