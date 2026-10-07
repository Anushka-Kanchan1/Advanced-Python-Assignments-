from pathlib import Path
from datetime import datetime

# File paths
input_file = Path("input.txt")
output_file = Path("extracted_data.txt")

try:
    # Read all lines from input file
    lines = input_file.read_text(encoding="utf-8").splitlines()

    # Count total lines
    line_count = len(lines)

    # Extract first two lines
    first_two_lines = lines[:2]

    # Prepare output data
    output_data = (
        f"File Processing Report\n"
        f"Generated: {datetime.now()}\n"
        f"Total Lines: {line_count}\n"
        f"\nFirst Two Lines:\n"
        f"{chr(10).join(first_two_lines)}\n"
    )

    # Write extracted data into new file
    output_file.write_text(output_data, encoding="utf-8")

    print("File processed successfully!")
    print(f"Total lines: {line_count}")
    print(f"First two lines: {first_two_lines}")
    print(f"Output saved in: {output_file}")

except FileNotFoundError:
    print("Error: Input file not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print(f"Unexpected error: {e}")
