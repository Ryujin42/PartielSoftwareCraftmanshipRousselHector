import pytest

from map import Map
from resource import Resource
from survivor import Survivor
from zombie import Zombie


@pytest.fixture
def map():
    map = Map(Survivor((5, 5), 'north', 10))
    map.resources.append(Resource((5, 4), 'water'))
    map.zombies.append(Zombie((4, 5)))
    return map


def test_forward(map):
    map.explore("forward")
    assert (map.survivor.position[0], map.survivor.position[1]) == (5, 4)


def test_turn_left(map):
    map.explore("turn left")
    assert map.survivor.orientation == 'west'


def test_turn_right(map):
    map.explore("turn right")
    assert map.survivor.orientation == 'east'


def test_encounter_zombie(map):
    map.explore("turn left")
    map.explore("forward")
    map.encounter()
    assert map.survivor.health == 9


def test_encounter_ressource(map):
    map.explore("forward")
    map.pickup()
    assert map.survivor.inventory[0].resource_name == 'water'


def test_survivor_out_of_bounds(map):
    map.survivor.position = (-1, 5)
    map.explore("forward")
    assert not map.survivor.is_alive()


if __name__ == '__main__':
    pytest.main()
