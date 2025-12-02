class Solution:
    def __init__(self, input_file: str):
        self.input_file = input_file

    def read_input(self):
        with open(self.input_file, 'r') as file:
            return file.read()

    def solve(self, start_with: int):
        current_number = start_with
        data = self.read_input()
        data = data.split("\n")
        ans = 0
        for line in data:
            action = line[0]
            value = int(line[1:])
            if action == "R":
                current_number = (value + current_number) % 100
            elif action == "L":
                current_number = (current_number - value) % 100
            if current_number == 0:
                ans += 1
        return ans

if __name__ == "__main__":
    solution = Solution("./input.txt")
    print(solution.solve(50))