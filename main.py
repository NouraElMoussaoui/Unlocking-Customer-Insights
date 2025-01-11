from scripts.data_loader import load_data
from scripts.data_cleaner import clean_data
from scripts.data_transform import transform_features
from scripts.eda import perform_eda

def main():

    file_path = "data/bank.csv"
    df = load_data(file_path)
    cleaned_df = clean_data(df)
    output_path = "results/preprocessed_dataset.csv"
    cleaned_df.to_csv(output_path, index=False)

    print(f"Data cleansing completed. Cleaned dataset saved to {output_path}.")

    transformed_df = transform_features(df)
    print("Features have been successfully transformed.")

    # print("Starting EDA...")
    perform_eda(transformed_df)
    print("Main pipeline completed.")

if __name__ == "__main__":
    main()