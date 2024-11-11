# Basic script to split the dataset

import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset():
    dataset_filepath = '../dataset/quotes_classification_data.csv'
    df = pd.read_csv(dataset_filepath)

    # Split into train (70%) and val and test each (15%)
    train_df, temp_df = train_test_split(df, test_size=0.3, random_state=42)
    val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

    # Save the splits
    train_df.to_csv('../dataset_splits/train_dataset.csv', index=False)
    val_df.to_csv('../dataset_splits/val_dataset.csv', index=False)
    test_df.to_csv('../dataset_splits/test_dataset.csv', index=False)

    print("Datasets saved: train_dataset.csv, val_dataset.csv, test_dataset.csv")

if __name__ == "__main__":
    split_dataset()