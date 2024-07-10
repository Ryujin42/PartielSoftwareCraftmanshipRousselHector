from random import randint


class Zombie:
    def __init__(self, position: tuple[int, int]):
        self.position = position

    def move(self):
        direction = randint(0, 3)
        if direction == 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == 1:
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == 2:
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == 3:
            self.position = (self.position[0] - 1, self.position[1])
