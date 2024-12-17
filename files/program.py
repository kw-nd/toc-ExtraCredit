import csv
import sys
from sympy import symbols, O

class AutomatonAnalyzer:
    def __init__(self, file_name):
        self.file_name = file_name
        self.states = []
        self.transitions = {}
        self.start_state = None
        self.accept_states = []
        self.time_complexity = None
        self.load_csv()

    def load_csv(self):
        try:
            with open(self.file_name, mode="r") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["State"] not in self.states:
                        self.states.append(row["State"])
                    if row["Start"] == "Yes":
                        self.start_state = row["State"]
                    if row["Accept"] == "Yes":
                        self.accept_states.append(row["State"])
                    key = (row["State"], row["Input"])
                    self.transitions[key] = row["Next State"]

        except FileNotFoundError:
            print(f"File {self.file_name} not found.")
            sys.exit(1)
        except KeyError:
            print("Invalid CSV structure. Ensure columns: Start, State, Input, Next State, Accept.")
            sys.exit(1)

    def is_decidable(self):
        visited = set()
        to_visit = [self.start_state]

        while to_visit:
            state = to_visit.pop()
            if state in visited:
                continue
            visited.add(state)
            for symbol in ["0", "1"]:
                if (state, symbol) in self.transitions:
                    next_state = self.transitions[(state, symbol)]
                    if next_state not in visited:
                        to_visit.append(next_state)

        for state in visited:
            for symbol in ["0", "1"]:
                if (state, symbol) not in self.transitions:
                    return False

        return True

    def is_recognizable(self):
        visited = set()
        to_visit = [self.start_state]

        while to_visit:
            state = to_visit.pop()
            if state in visited:
                continue
            visited.add(state)
            if state in self.accept_states:
                return True
            for symbol in ["0", "1"]:
                if (state, symbol) in self.transitions:
                    next_state = self.transitions[(state, symbol)]
                    if next_state not in visited:
                        to_visit.append(next_state)

        return False

    def is_co_turing_recognizable(self):
        return True

    def calculate_complexity(self):
        num_states = len(self.states)
        num_transitions = len(self.transitions)

        if num_transitions == num_states * 2:
            self.time_complexity = O(symbols("n"))
        elif num_transitions < num_states * num_states:
            self.time_complexity = O(symbols("n**2"))
        else:
            self.time_complexity = O(2 ** symbols("n"))

    def analyze(self):
        print("Analyzing automaton...")
        decidable = self.is_decidable()
        recognizable = self.is_recognizable()
        co_turing_recognizable = self.is_co_turing_recognizable()

        self.calculate_complexity()

        print("\nAnalysis Results:")
        print(f"- Decidable: {'Yes' if decidable else 'No'}")
        print(f"- Recognizable: {'Yes' if recognizable else 'No'}")
        print(f"- Co-Turing Recognizable: {'Yes' if co_turing_recognizable else 'No'}")
        print(f"- Time Complexity: {self.time_complexity}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 program.py <csv_file>")
        sys.exit(1)

    file_name = sys.argv[1]
    analyzer = AutomatonAnalyzer(file_name)
    analyzer.analyze()
