
import pytest

from life_python.cell import Cell
from life_python.world import World

@pytest.fixture
def sample_world():
    world = World()
    world.add_glider(0,0)
    return world

@pytest.mark.parametrize("cell, neighbors", [
    (Cell(0,0), {Cell(-1,-1), Cell(0,-1), Cell(1,-1), Cell(-1,0), Cell(1,0), Cell(-1,1), Cell(0,1), Cell(1,1), }),
    (Cell(1,0), {Cell(0,-1), Cell(1,-1), Cell(2,-1), Cell(0,0), Cell(2,0), Cell(0,1), Cell(1,1), Cell(2,1), }),
])
def test_cell_neighbors(cell: Cell, neighbors: set[Cell]):
    assert cell.neighbors() == neighbors

def test_add_glider(sample_world: World):
    assert sample_world.living() == {Cell(0,1), Cell(1,0), Cell(-1,-1), Cell(0,-1), Cell(1,-1), }

@pytest.mark.parametrize("cell, count", [
    (Cell(0,0), 5),
    (Cell(1,0), 3),
    (Cell(5,5), 0),
])
def test_cell_count_neighbors(sample_world: World, cell: Cell, count: int):
    assert cell.count_neighbors(sample_world) == count

@pytest.mark.parametrize("cell, will_live", [
    (Cell(0,0), False),
    (Cell(0,1), False),
    (Cell(1,0), True),
    (Cell(0,-2), True),
    (Cell(5,5), False),
])
def test_cell_will_live(sample_world: World, cell: Cell, will_live: bool):
    assert cell.will_live(sample_world) == will_live
