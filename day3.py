class Solution:
    @staticmethod
    def _get_item_priority(letter):
        if letter.isupper():
            return ord(letter) - ord("A") + 27
        else:
            return ord(letter) - ord("a") + 1

    def calc_result1(self, input_data):
        total_item_prioriry = 0
        for line in input_data:
            line = line.rstrip("\n")

            size = len(line)
            half_size = size // 2
            second_part_set = set(line[half_size:])

            for index in range(half_size):
                letter = line[index]
                if letter in second_part_set:
                    total_item_prioriry += self._get_item_priority(letter)
                    break
        return total_item_prioriry

    def calc_result2(self, input_data):
        total_item_prioriry = 0
        temp_collection = []
        for line_no, line in enumerate(input_data):
            line = line.rstrip("\n")
            temp_collection.append(line)

            if (line_no + 1) % 3 == 0:
                set1 = set(temp_collection[0])
                set2 = set(temp_collection[1])
                for symbol in temp_collection[2]:
                    if symbol in set1 and symbol in set2:
                        total_item_prioriry += self._get_item_priority(symbol)
                        break
                temp_collection = []

        return total_item_prioriry


if __name__ == "__main__":
    solution = Solution()
    test_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    test_data2 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
    print("Test data result 1 puzzle:", solution.calc_result1(test_data.split("\n")))
    print("Test data result 2 puzzle:", solution.calc_result2(test_data2.split("\n")))

    with open("data/day3_input.txt", 'r') as file:
        print("Puzzle 1 answer:", solution.calc_result1(file))
        file.seek(0)
        print("Puzzle 2 answer:", solution.calc_result2(file))


