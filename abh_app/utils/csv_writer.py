import csv
import os

def write_results(results, output_file="output.csv"):
    full_path = os.path.abspath(output_file)
    print("Writing CSV to:", full_path)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Bug Line", "Explanation"])

        for row in results:
            writer.writerow(row)
