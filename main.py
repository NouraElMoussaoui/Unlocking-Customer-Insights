from scripts.data_loader import load_data

def main():
    #load Dataset
    file_path = "data/bank.csv"
    df = load_data(file_path)

if __name__ == "__main__":
    main()