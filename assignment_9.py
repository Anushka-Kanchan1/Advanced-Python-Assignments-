import csv
import json
from pathlib import Path

# File names
input_file = Path("input.csv")
output_file = Path("output.json")

try:
    # Read CSV file
    with open(input_file, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Convert data into JSON and store it
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("CSV file converted to JSON successfully!")
    print("Output file:", output_file)

except FileNotFoundError:
    print("Error: CSV file not found!")

except Exception as e:
    print("Error:", e)

