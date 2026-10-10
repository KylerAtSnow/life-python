
from __future__ import annotations

from life_python.cell import Cell


class World:

    __world: set[Cell]
    __born: tuple[int, ...]
    __survive: tuple[int, ...]

    def __init__(
        self,
        born: tuple[int, ...] = (3,),
        survive: tuple[int, ...] = (2,3,),
        /, world: set[Cell] | None = None,
    ) -> None:
        self.__born = born
        self.__survive = survive
        self.__world = world or set()

    def __repr__(self) -> str:
        return f"World({self.rule_string}, {len(self.__world)})"

    def __contains__(self, item: Cell): return item in self.__world

    def living_cells(self) -> str:
        return '\n'.join(str(i) for i in self.__world)

    def living(self) -> set[Cell]: return self.__world.copy()

    @property
    def born(self) -> tuple[int, ...]: return self.__born
    @property
    def survive(self) -> tuple[int, ...]: return self.__survive

    @property
    def rule_string(self) -> str:
        return f"B{''.join(str(i) for i in self.__born)}/S{''.join(str(i) for i in self.__survive)}"

    def add(self, cell: Cell): self.__world.add(cell)

    def add_glider(self, x: int, y: int, /, dir: int = 0):
        # 010
        # 001
        # 111
        if dir == 0:
            self.add(Cell(x+0,y+1))
            self.add(Cell(x+1,y+0))
            self.add(Cell(x-1,y-1))
            self.add(Cell(x+0,y-1))
            self.add(Cell(x+1,y-1))
        # 011
        # 101
        # 001
        if dir == 1:
            self.add(Cell(x+1,y+0))
            self.add(Cell(x+1,y+1))
            self.add(Cell(x-1,y+0))
            self.add(Cell(x+1,y+0))
            self.add(Cell(x+1,y-1))
        # 111
        # 100
        # 010
        if dir == 2:
            self.add(Cell(x-1,y+1))
            self.add(Cell(x+0,y+1))
            self.add(Cell(x+1,y+1))
            self.add(Cell(x-1,y+0))
            self.add(Cell(x+0,y-1))
        # 100
        # 101
        # 110
        if dir == 3:
            self.add(Cell(x-1,y+1))
            self.add(Cell(x-1,y+0))
            self.add(Cell(x+1,y+0))
            self.add(Cell(x-1,y-1))
            self.add(Cell(x+0,y-1))

    def world_and_neighbors(self) -> set[Cell]:
        return self.__world.union(*(c.neighbors() for c in self.__world))

    def next_generation(self) -> World:
        return World(self.born, self.survive, world={c for c in self.world_and_neighbors() if c.will_live(self)})

    def iterations(self, i: int, /) -> World:
        world = self
        for _ in range(i):
            world = world.next_generation()
        return world
