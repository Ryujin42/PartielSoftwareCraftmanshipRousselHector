orientations = ["north", "east", "south", "west"]


class Survivor:
    def __init__(self, position: tuple[int, int], orientation: str, health: int):
        self.position = position
        self.orientation = orientation
        self.health = health
        self.inventory = []

    def encounter_zombie(self):
        self.health -= 1

    def pickup_resource(self, resource):
        self.inventory.append(resource)

    def is_alive(self):
        return self.health > 0
