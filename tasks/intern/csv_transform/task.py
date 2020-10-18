import csv
from typing import List


def main() -> None:

    with open(file="sample.text", mode="r") as f:
        file_data: List[str] = [line for line in f]

    partitoned_rows: List[List[str]] = [(lambda row: row.replace("\n", "").split("  "))(row) for row in file_data]
    # print(partitoned_rows)

    with open(file="output.csv", mode="w") as o:
        writer = csv.writer(o)
        writer.writerow(["x_position", "y_position", "weight", "type"])  # header
        writer.writerows(partitoned_rows)


if __name__ == "__main__":
    main()
