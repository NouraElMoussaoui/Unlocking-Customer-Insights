import pandas as pd 

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully!")
    print("Shape of Dataset:", df.shape)
    print("First Five Rows:\n", df.head())
    return df
