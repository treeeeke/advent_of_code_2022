from typing import Any


class Node:
    def __init__(self, name: str, prev: Any):
        self.name = name
        self.prev = prev
        self.files = []
        self.children = []


class Solution:
    @staticmethod
    def collect_nodes(input_data):
        dummy = Node('dummy', None)
        cur_folder = dummy
        for line in input_data:
            line = line.rstrip("\n")
            if line.startswith("$ cd"):

                if line == "$ cd ..":
                    cur_folder = cur_folder.prev
                else:
                    temp = Node(line.lstrip("$ cd "), cur_folder)
                    cur_folder.children.append(temp)
                    cur_folder = temp

            elif line[0].isdigit():
                size = int(line.split(" ")[0])
                filename = line.split(" ")[1]
                cur_folder.files.append((filename, size))

        return dummy.children[0]

    def calc_result1(self, input_data):
        root = self.collect_nodes(input_data)

        total_counter = [0]
        def calc_size(root):
            node_counter = 0
            for _, size in root.files:
                 node_counter += size

            for child_node in root.children:
                node_counter += calc_size(child_node)

            if node_counter <= 100000:
                total_counter[0] += node_counter

            return node_counter

        calc_size(root)
        return total_counter

    def calc_result2(self, input_data, total_disc_space=70000000, space_for_update=30000000):
        root = self.collect_nodes(input_data)

        folders_size = []
        def calc_size(root):
            node_counter = 0
            for _, size in root.files:
                node_counter += size
            for child_node in root.children:
                node_counter += calc_size(child_node)
            folders_size.append(node_counter)
            return node_counter

        total_used_space = calc_size(root)
        total_unused_space = total_disc_space - total_used_space

        for size in sorted(folders_size):
            if total_unused_space + size > space_for_update:
                return size


if __name__ == "__main__":
    solution = Solution()
    test_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
    print("Test data result 1 puzzle:", solution.calc_result1(test_data.split("\n")))
    print("Test data result 2 puzzle:", solution.calc_result2(test_data.split("\n")))
    #
    with open("data/day7_input.txt", 'r') as file:
        print("Puzzle 1 answer:", solution.calc_result1(file))
        file.seek(0)
        print("Puzzle 2 answer:", solution.calc_result2(file))


