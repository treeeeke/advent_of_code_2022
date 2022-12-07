from collections import Counter


class Solution:
    def calc_result1(self, input_data, n):

        counter = Counter()

        for number, symbol in enumerate(input_data):
            counter[symbol] += 1

            if number < (n-1):
                continue

            check = True
            for value in counter.values():
                if value != 1:
                    check = False

            if check:
                return number + 1

            symbol_to_minus = input_data[number - (n - 1)]
            counter[symbol_to_minus] -= 1
            if counter[symbol_to_minus] == 0:
                del counter[symbol_to_minus]


if __name__ == "__main__":
    solution = Solution()
    test_data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
    print("Test data result 1 puzzle:", solution.calc_result1(test_data, 4))
    print("Test data result 2 puzzle:", solution.calc_result1(test_data, 14))

    with open("data/day6_input.txt", 'r') as file:
        print("Puzzle 1 answer:", solution.calc_result1(file.read(), 4))
        file.seek(0)
        print("Puzzle 2 answer:", solution.calc_result1(file.read(), 14))

