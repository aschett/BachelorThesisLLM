import pandas as pd
import os

def prepare_dataset():
    current_directory = os.getcwd()
    file_path = current_directory + "/dataset_word_memorability/word_memorability.csv"

    word_dataset = pd.read_csv(file_path)

    #Delete all missing recall values
    word_dataset = word_dataset.dropna(subset=["pRecall"])

    #Convert Recall into binary label
    threshold = word_dataset["pRecall"].median()
    word_dataset["Memorable"] = (word_dataset["pRecall"] >= threshold).astype(int)

    columns_to_keep = ["word", "pRecall", "Memorable", "Concreteness", "Arousal", "Valence", "Animacy"]
    processed_dataset = word_dataset[columns_to_keep]

    processed_dataset.to_csv(current_directory + "/dataset_word_memorability/processed_words_dataset.csv", index=False)

if __name__ == "__main__":
    prepare_dataset()