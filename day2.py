class Solution:
    def __init__(self):
        self.choice_points = {"A": 1, "B": 2, "C": 3}
        self.game_points = {"AB": 6, "AC": 0, "BA": 0, "BC": 6, "CA": 6, "CB": 0}
        self.code = {"X": "A", "Y": "B", "Z": "C"}
        self.choice = {"AX": "C", "AZ": "B", "BX": "A", "BZ": "C", "CX": "B", "CZ": "A"}

    def calc_result1(self, input_data):
        total_score = 0
        for line in input_data:
            line = line.rstrip("\n")

            a, b = line.split(" ")
            b = self.code[b]

            if a == b:
                game_score = 3
            else:
                game_score = self.game_points[f"{a}{b}"]

            choice_score = self.choice_points[b]
            total_score += game_score + choice_score

        return total_score

    def calc_result2(self, input_data):
        total_score = 0
        for line in input_data:
            line = line.rstrip("\n")

            a, b = line.split(" ")

            if b == "Y":
                game_score = 3
                choice = a
            elif b == "X":
                game_score = 0
                choice = self.choice[f"{a}{b}"]
            else:
                game_score = 6
                choice = self.choice[f"{a}{b}"]

            choice_score = self.choice_points[choice]
            total_score += game_score + choice_score

        return total_score


if __name__ == "__main__":
    solution = Solution()
    test_data = """A Y\nB X\nC Z"""
    test_data = test_data.split("\n")
    print("Test data result 1 puzzle:", solution.calc_result1(test_data))
    print("Test data result 2 puzzle:", solution.calc_result2(test_data))

    with open("data/day2_input.txt", 'r') as file:
        print("Puzzle 1 answer:", solution.calc_result1(file))
        file.seek(0)
        print("Puzzle 2 answer:", solution.calc_result2(file))


