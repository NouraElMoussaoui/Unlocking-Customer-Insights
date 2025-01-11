from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd
import numpy as np

def transform_features(df):
    # Encoding categorical variables
    categorical_cols = df.select_dtypes(include=["object"]).columns
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded_data = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_cols))
    
    # Drop original categorical columns and merge with the encoded dataframe
    df = df.drop(columns=categorical_cols).reset_index(drop=True)
    df = pd.concat([df, encoded_df], axis=1)
    
    # Scaling numerical features
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[numerical_cols])
    scaled_df = pd.DataFrame(scaled_data, columns=numerical_cols)
    
    # Replace the original numerical columns with scaled values
    df[numerical_cols] = scaled_df
    
    return df
