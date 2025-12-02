class Solution:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def read_input(self):
        with open(self.input_file, 'r') as file:
            return file.read().strip().splitlines()

    def solve(self, start_with: int):
        current = start_with
        total_zero_hits = 0
        rotations = self.read_input()

        for line in rotations:
            direction = line[0]
            steps = int(line[1:])

            if direction == "R":
                # move clockwise: +i
                for i in range(1, steps + 1):
                    pos = (current + i) % 100
                    if pos == 0:
                        total_zero_hits += 1

                current = (current + steps) % 100

            else:  # direction == "L"
                # move anticlockwise: -i
                for i in range(1, steps + 1):
                    pos = (current - i) % 100
                    if pos == 0:
                        total_zero_hits += 1

                current = (current - steps) % 100

        return total_zero_hits


if __name__ == "__main__":
    solution = Solution("./input.txt")
    print(solution.solve(50))
