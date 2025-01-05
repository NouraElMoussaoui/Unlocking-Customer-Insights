#Perform data cleansing
import pandas  as pd
import numpy as np

# Handling Missing Values

def clean_data(df):
    # Replace Missing values in numerical columns with the column mean
    numerical_cols  = df.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        df[col].fillna(df[col].median())

    # Replace missing values in categorical columns with the most frequent value (mode)

    categorical_cols = df.select_dtypes(include=["object"]).columns
    for col in categorical_cols:
        df[col].fillna(df[col].mode()[0])
        # df[col].replace('unknown', df[col].mode()[0])
        # if df[col].nunique() == 1 and df[col].iloc[0] == 'unknown':
        #     df.drop(columns=[col])

    #Remove duplicate rows
    df = df.drop_duplicates()

    #Handling Outliers

    for col in numerical_cols:
        mean = df[col].mean()
        std_dev = df[col].std()
        lower_bound = mean - 3 * std_dev
        upper_bound = mean + 3 * std_dev
        df[col] = np.clip(df[col], lower_bound, upper_bound)
        # #Outliers are values more than 3 standard deviations away from the mean
        # df[col] = df[col].apply(lambda x: mean if (x > mean + 3 * std_dev) or (x < mean - 3 * std_dev) else x)

    # #Drop columns that are not useful for analysis 
    # default : Credit default may not add much value if most values are the same
    # contact : Type of communication may not be central to segmentation.
    # Day: day of last contact is unlikely to affect segmentation
    # duration: Highly predictive of target (deposit), but not intrinsic to segmentation.
    # pdays: If most values are -1, it adds little value.
    # deposit: This is the target variable (binary classification).
    irrelevant_columns = ['default', 'contact','day', 'duration', 'pdays', 'deposit', 'poutcome']
    try:
        dropped_cols = df.drop(columns=irrelevant_columns, errors='ignore', inplace=False)
        print(f"Dropped columns: {dropped_cols.columns.tolist()}")
        df = df.drop(columns=irrelevant_columns, errors='ignore')
    except Exception as e:
        print(f"Error dropping columns: {e}")
    return df

