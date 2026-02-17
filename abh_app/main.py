import pandas as pd
from abh_app.agents.diff_agent import detect_bug_line
from abh_app.agents.explanation_agent import generate_explanation
from abh_app.utils.csv_writer import write_results


DATASET_PATH = "samples.csv"


def main():

    print("Starting Agentic Bug Hunter...")

    df = pd.read_csv(DATASET_PATH)
    df.columns = df.columns.str.strip()

    results = []

    for _, row in df.iterrows():

        code_id = row["ID"]
        incorrect_code = row["Code"]
        correct_code = row["Correct Code"]

        print(f"Processing ID: {code_id}")

        bug_line = detect_bug_line(incorrect_code, correct_code)
        explanation = generate_explanation(incorrect_code, correct_code, bug_line)
        print("Generated Explanation:")
        print(explanation)
        print("--------------------------------------------------")


        results.append([code_id, bug_line, explanation])

    write_results(results)

    print("Finished. Output saved to output.csv")


if __name__ == "__main__":
    main()
