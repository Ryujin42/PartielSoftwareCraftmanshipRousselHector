from random import randint

from resource import Resource
from survivor import Survivor
from zombie import Zombie

orientations = ["north", "east", "south", "west"]


class Map:
    def __init__(self, survivor: Survivor):
        self.survivor = survivor
        self.resources = []
        self.zombies = []

    def explore(self, command: str):
        match command:
            case "forward":
                match self.survivor.orientation:
                    case "north":
                        self.survivor.position = (self.survivor.position[0], self.survivor.position[1] - 1)
                    case "east":
                        self.survivor.position = (self.survivor.position[0] + 1, self.survivor.position[1])
                    case "south":
                        self.survivor.position = (self.survivor.position[0], self.survivor.position[1] + 1)
                    case "west":
                        self.survivor.position = (self.survivor.position[0] - 1, self.survivor.position[1])

            case "turn left":
                self.survivor.orientation = orientations[(orientations.index(self.survivor.orientation) - 1) % 4]

            case "turn right":
                self.survivor.orientation = orientations[(orientations.index(self.survivor.orientation) + 1) % 4]

        if self.survivor.position[0] < 0 or self.survivor.position[0] > 9 or self.survivor.position[1] < 0 or self.survivor.position[1] > 9:
            self.survivor.health = 0

    def encounter(self):
        for zombie in self.zombies:
            if self.survivor.position == zombie.position:
                self.survivor.health -= 1

    def pickup(self):
        for resource in self.resources:
            if self.survivor.position == resource.position:
                self.survivor.inventory.append(resource)
                self.resources.remove(resource)
