import random


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.start_pos = None
        self.end_pos = None
        self.obstacles = set()
        self.generate_board()

    def generate_board(self):
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.obstacles.add((x, y))  
        self.start_pos = self.generate_random_position()
        self.end_pos = self.generate_random_position()
        while self.end_pos == self.start_pos:
            self.end_pos = self.generate_random_position()
        for x in range(self.width):
            for y in range(self.height):
                if (x, y) not in self.obstacles and (x, y) != self.start_pos and (x, y) != self.end_pos:
                    if random.random() < 0.2:  
                        self.obstacles.add((x, y))

    def generate_random_position(self):
        x = random.randint(1, self.width - 2)
        y = random.randint(1, self.height - 2)
        return x, y

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacles

    def is_border(self, x, y):
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def is_valid_position(self, x, y):
        return not self.is_obstacle(x, y) and not self.is_border(x, y)

    def display(self):
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) == self.start_pos:
                    print('A', end=' ')
                elif (x, y) == self.end_pos:
                    print('B', end=' ')
                elif (x, y) in self.obstacles:
                    print('X', end=' ')
                else:
                    print('.', end=' ')
            print()


board = Board(10, 10)
board.display()
