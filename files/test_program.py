import os
import subprocess

def create_csv_file(file_name, rows, fieldnames):
    import csv
    with open(file_name, mode="w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def run_analyzer(csv_file):
    result = subprocess.run(
        ["python3", "program.py", csv_file],
        capture_output=True, text=True
    )
    return result.stdout

def main():
    print("========== Automaton Analyzer Test Suite ==========\n")
    fieldnames = ["Start", "State", "Input", "Next State", "Accept"]

    test1_file = "test1.csv"
    rows_test1 = [
        {"Start": "Yes", "State": "S0", "Input": "0", "Next State": "S0", "Accept": "Yes"},
        {"Start": "No",  "State": "S0", "Input": "1", "Next State": "S0", "Accept": "Yes"},
    ]
    create_csv_file(test1_file, rows_test1, fieldnames)

    output_test1 = run_analyzer(test1_file)
    criteria_test1 = {
        "Decidable: Yes": "Decidable = Yes",
        "Recognizable: Yes": "Recognizable = Yes",
        "Co-Turing Recognizable: Yes": "Co-Turing = Yes",
        "Time Complexity: O(n)": "Time Complexity: O(n)"
    }
    passed_test1 = all(k in output_test1 for k in criteria_test1.keys())

    print("Test 1 (Single-state fully connected) :", "PASSED" if passed_test1 else "FAILED")

    test2_file = "test2.csv"
    rows_test2 = [
        {"Start": "Yes", "State": "S0", "Input": "0", "Next State": "S0", "Accept": "No"},
        {"Start": "No",  "State": "S0", "Input": "1", "Next State": "S1", "Accept": "No"},
        {"Start": "No",  "State": "S1", "Input": "0", "Next State": "S1", "Accept": "Yes"},
        {"Start": "No",  "State": "S1", "Input": "1", "Next State": "S1", "Accept": "Yes"},
    ]
    create_csv_file(test2_file, rows_test2, fieldnames)

    output_test2 = run_analyzer(test2_file)
    criteria_test2 = {
        "Decidable: Yes": "Decidable = Yes",
        "Recognizable: Yes": "Recognizable = Yes",
        "Co-Turing Recognizable: Yes": "Co-Turing = Yes",
        "Time Complexity: O(n)": "Time Complexity: O(n)"
    }
    passed_test2 = all(k in output_test2 for k in criteria_test2.keys())

    print("Test 2 (Two-state complete)         :", "PASSED" if passed_test2 else "FAILED")

    test3_file = "test3.csv"
    rows_test3 = [
        {"Start": "Yes", "State": "S0", "Input": "0", "Next State": "S1", "Accept": "No"},
        {"Start": "No",  "State": "S1", "Input": "0", "Next State": "S1", "Accept": "Yes"},
        {"Start": "No",  "State": "S1", "Input": "1", "Next State": "S1", "Accept": "Yes"},
    ]
    create_csv_file(test3_file, rows_test3, fieldnames)

    output_test3 = run_analyzer(test3_file)
    expected_strings_test3 = ["Decidable: No", "Recognizable: Yes", "Co-Turing Recognizable: Yes"]
    passed_test3 = all(s in output_test3 for s in expected_strings_test3)
    print("Test 3 (Missing a transition)       :", "PASSED" if passed_test3 else "FAILED")

    test4_file = "test4.csv"
    rows_test4 = [
        {"Start": "Yes", "State": "S0", "Input": "0", "Next State": "S1", "Accept": "No"},
        {"Start": "No",  "State": "S0", "Input": "1", "Next State": "S1", "Accept": "No"},
        {"Start": "No",  "State": "S1", "Input": "0", "Next State": "S2", "Accept": "No"},
        {"Start": "No",  "State": "S1", "Input": "1", "Next State": "S2", "Accept": "No"},
        {"Start": "No",  "State": "S2", "Input": "0", "Next State": "S3", "Accept": "Yes"},
        {"Start": "No",  "State": "S2", "Input": "1", "Next State": "S3", "Accept": "Yes"},
        {"Start": "No",  "State": "S3", "Input": "0", "Next State": "S3", "Accept": "Yes"},
        {"Start": "No",  "State": "S3", "Input": "1", "Next State": "S3", "Accept": "Yes"},
        {"Start": "No",  "State": "S1", "Input": "0", "Next State": "S3", "Accept": "No"}
    ]
    create_csv_file(test4_file, rows_test4, fieldnames)

    output_test4 = run_analyzer(test4_file)
    expected_strings_test4 = ["Decidable: Yes", "Recognizable: Yes", "Time Complexity: O(n**2)"]
    passed_test4 = all(s in output_test4 for s in expected_strings_test4)
    print("Test 4 (Triggers O(n^2))            :", "PASSED" if passed_test4 else "FAILED")

    test5_file = "test5.csv"
    rows_test5 = [
        {"Start": "Yes", "State": "S0", "Input": "0", "Next State": "S1", "Accept": "No"},
        {"Start": "No",  "State": "S0", "Input": "1", "Next State": "S2", "Accept": "No"},

        {"Start": "No",  "State": "S1", "Input": "0", "Next State": "S0", "Accept": "No"},
        {"Start": "No",  "State": "S1", "Input": "1", "Next State": "S2", "Accept": "Yes"},

        {"Start": "No",  "State": "S2", "Input": "0", "Next State": "S1", "Accept": "No"},
        {"Start": "No",  "State": "S2", "Input": "1", "Next State": "S0", "Accept": "No"},

        {"Start": "No",  "State": "S2", "Input": "0", "Next State": "S2", "Accept": "No"},
        {"Start": "No",  "State": "S1", "Input": "1", "Next State": "S1", "Accept": "Yes"},
        {"Start": "No",  "State": "S0", "Input": "0", "Next State": "S2", "Accept": "No"},
        {"Start": "No",  "State": "S0", "Input": "1", "Next State": "S1", "Accept": "No"},
    ]
    create_csv_file(test5_file, rows_test5, fieldnames)

    output_test5 = run_analyzer(test5_file)
    expected_strings_test5 = ["Decidable: Yes", "Recognizable: Yes", "Time Complexity: O(2**n)"]
    passed_test5 = all(s in output_test5 for s in expected_strings_test5)
    print("Test 5 (Triggers O(2^n))            :", "PASSED" if passed_test5 else "FAILED")

    print("\nAll tests completed.\n")

if __name__ == "__main__":
    main()
