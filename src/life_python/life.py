
from typing import Iterable

from life_python.cell import Cell
from life_python.world import World

def simulate(iterations: int, starting_cells: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    world = World()
    for cell in starting_cells:
        world.add(Cell(*cell))
    return [i.as_tuple() for i in world.iterations(iterations).living()]

def life(i: int = 100_000) -> World:
    world = World()
    world.add_glider(1,1)
    return world.iterations(i)

def main():
    world = life()
    print(world.living_cells())
