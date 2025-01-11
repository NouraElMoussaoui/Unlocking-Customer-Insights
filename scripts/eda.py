import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def perform_eda(df):
    # Descriptive statistics
    print("Descriptive Statistics (Numerical):")
    print(df.describe())
    
    print("\nDescriptive Statistics (Categorical):")
    categorical_cols = df.select_dtypes(include=["object"]).columns
    for col in categorical_cols:
        print(f"\nValue Counts for {col}:\n{df[col].value_counts()}")
    
    # Visualizations
    # Distribution of numerical features
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    for col in numerical_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f"Distribution of {col}")
        plt.show()
    
    # Correlation heatmap for numerical features
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
    
    # Pairplot for selected features (if the dataset isn't too large)
    sns.pairplot(df.select_dtypes(include=[np.number]))
    plt.show()

    # Categorical features bar plot
    for col in categorical_cols:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=df, x=col, order=df[col].value_counts().index)
        plt.title(f"Bar Plot of {col}")
        plt.xticks(rotation=45)
        plt.show()
