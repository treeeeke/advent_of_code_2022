class Solution:
    def calc_result1(self, input_data):
        fully_counter = 0

        for line in input_data:
            line = line.rstrip("\n")
            first_period, second_period = line.split(",")
            fp_start, fp_finish = [int(x) for x in first_period.split("-")]
            sp_start, sp_finish = [int(x) for x in second_period.split("-")]
            if fp_start >= sp_start and fp_finish <= sp_finish or fp_start <= sp_start and fp_finish >= sp_finish:
                fully_counter += 1

        return fully_counter

    def calc_result2(self, input_data):
        overlap_counter = 0

        for line in input_data:
            line = line.rstrip("\n")
            first_period, second_period = line.split(",")
            fp_start, fp_finish = [int(x) for x in first_period.split("-")]
            sp_start, sp_finish = [int(x) for x in second_period.split("-")]
            if (fp_start <= sp_start <= fp_finish) or \
               (fp_start <= sp_finish <= fp_finish) or \
               (sp_start <= fp_start and fp_finish <= sp_finish):
                overlap_counter += 1

        return overlap_counter


if __name__ == "__main__":
    solution = Solution()
    test_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
    print("Test data result 1 puzzle:", solution.calc_result1(test_data.split("\n")))
    print("Test data result 2 puzzle:", solution.calc_result2(test_data.split("\n")))
    #
    with open("data/day4_input.txt", 'r') as file:
        print("Puzzle 1 answer:", solution.calc_result1(file))
        file.seek(0)
        print("Puzzle 2 answer:", solution.calc_result2(file))


