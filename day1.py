import heapq


class Solution:
    def get_max_food(self, input_file):
        max_food = 0
        current_food = 0
        for line in input_file:
            line = line.rstrip("\n")
            if line == "":
                max_food = max(max_food, current_food)
                current_food = 0
            else:
                current_food += int(line)

        return max_food

    def get_max_food_by_top_n_elfes(self, input_file, n):
        heap = []
        current_food = 0
        for line in input_file:
            line = line.rstrip("\n")

            if line == "":
                if len(heap) < n:
                    heapq.heappush(heap, current_food)
                elif current_food > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, current_food)
                current_food = 0
            else:
                current_food += int(line)

        return sum(heap)


if __name__ == "__main__":
    solution = Solution()

    with open("day1_input.txt", 'r') as file:
        print("Puzzle 1 answer:", solution.get_max_food(file))
        file.seek(0)
        print("Puzzle 2 answer:", solution.get_max_food_by_top_n_elfes(file, 3))


