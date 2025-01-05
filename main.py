from scripts.data_loader import load_data
from scripts.data_cleaner import clean_data


def main():
    #load Dataset
    file_path = "data/bank.csv"
    df = load_data(file_path)
    cleaned_df = clean_data(df)
    output_path = "results/preprocessed_dataset.csv"
    cleaned_df.to_csv(output_path, index=False)

    print(f"Data cleansing completed. Cleaned dataset saved to {output_path}.")

if __name__ == "__main__":
    main()