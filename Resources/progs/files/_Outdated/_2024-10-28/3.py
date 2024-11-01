import random

class Environment:
    def __init__(self, rows, cols):
        self.grid = [[random.choice(['Clean', 'Dirty']) for _ in range(cols)] for _ in range(rows)]
        self.agent_position = [0, 0]  # Agent starts at top-left corner

    def is_dirty(self, row, col):
        return self.grid[row][col] == 'Dirty'

    def clean(self, row, col):
        self.grid[row][col] = 'Clean'

    def display(self):
        for row in self.grid:
            print(row)
        print()

class VacuumAgent:
    def __init__(self, env):
        self.env = env

    def sense_and_act(self):
        row, col = self.env.agent_position
        if self.env.is_dirty(row, col):
            print(f"Cleaning position: {row}, {col}")
            self.env.clean(row, col)
        else:
            print(f"Position: {row}, {col} is already clean")
        self.move()

    def move(self):
        row, col = self.env.agent_position
        if col < len(self.env.grid[0]) - 1:  # Move right if possible
            self.env.agent_position = [row, col + 1]
        elif row < len(self.env.grid) - 1:  # Move down if possible
            self.env.agent_position = [row + 1, 0]

if __name__ == "__main__":
    rows, cols = 2, 3  # 2x3 grid environment
    env = Environment(rows, cols)
    agent = VacuumAgent(env)

    print("Initial Environment:")
    env.display()

    for _ in range(rows * cols):  # Perform actions for all grid cells
        agent.sense_and_act()

    print("Final Environment:")
    env.display()
