import csv

def process_file(input_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8', errors='replace') as file:
            lines = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
        return []
    except Exception as e:
        print(f"Error reading {input_file_path}: {e}")
        return []

    quotes = []
    
    for i in range(0, len(lines), 4):
        memorable_quote = lines[i+1]
        non_memorable_quote = ' '.join(lines[i+3].split()[1:])  # The join is needed to get rid of the leading number in the ".txt" file
        quotes.append((memorable_quote, 1))
        quotes.append((non_memorable_quote, 0))

    return quotes

def write_to_csv(quotes, csv_file_path):
    try:
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quote', 'Memorable'])
            for quote, quote_type in quotes:
                writer.writerow([quote, quote_type])
    except Exception as e:
        print(f"Error writing to {csv_file_path}: {e}")

if __name__ == "__main__":
    input_file_path = '../dataset/moviequotes.memorable_nonmemorable_pairs.txt'
    csv_file_path = '../dataset/quotes_classification_data1.csv'

    quotes = process_file(input_file_path)
    if quotes:
        write_to_csv(quotes, csv_file_path)