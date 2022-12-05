import re

class Solution:
    def parse_input(self, input_data):
        crates_raw_collection = []
        moves = []

        crates_flag = True
        for line in input_data:
            line = line.rstrip("\n")
            if crates_flag:
                if line == "":
                    crates_flag = False
                else:
                    crates_raw_collection.append(line)
            else:
                move = tuple([int(x) for x in re.findall("[0-9]+", line)])
                moves.append(move)

        coords = {}
        for line_no, line in enumerate(reversed(crates_raw_collection)):
            if line_no == 0:
                for symb_no, symb in enumerate(line):
                    if symb.isdigit():
                        coords[int(symb)] = symb_no

                crates_collections = [[] for x in range(max(coords.keys()))]
                continue

            for symb, coord in coords.items():
                    temp = line[coord]
                    if temp != " ":
                        crates_collections[symb - 1].append(temp)

        return crates_collections, moves

    def make_moves(self, moves, crates_collections):
        for number, from_crates, to_crates in moves:
            for _ in range(number):
                temp = crates_collections[from_crates - 1].pop()
                crates_collections[to_crates - 1].append(temp)

        return crates_collections

    def make_moves2(self, moves, crates_collections):
        for number, from_crates, to_crates in moves:
            temp_collection = []
            for _ in range(number):
                temp_collection.append(crates_collections[from_crates - 1].pop())

            for _ in range(len(temp_collection)):
                temp = temp_collection.pop()
                crates_collections[to_crates - 1].append(temp)

        return crates_collections

    def calc_result1(self, input_data):
        crates_collections, moves = self.parse_input(input_data)
        crates_collections = self.make_moves(moves, crates_collections)

        result = []
        for crate in crates_collections:
            result.append(crate[-1])
        return "".join(result)

    def calc_result2(self, input_data):
        crates_collections, moves = self.parse_input(input_data)
        crates_collections = self.make_moves2(moves, crates_collections)

        result = []
        for crate in crates_collections:
            result.append(crate[-1])
        return "".join(result)


if __name__ == "__main__":
    solution = Solution()
    test_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
    print("Test data result 1 puzzle:", solution.calc_result1(test_data.split("\n")))
    print("Test data result 2 puzzle:", solution.calc_result2(test_data.split("\n")))

    with open("data/day5_input.txt", 'r') as file:
        print("Puzzle 1 answer:", solution.calc_result1(file))
        file.seek(0)
        print("Puzzle 2 answer:", solution.calc_result2(file))


