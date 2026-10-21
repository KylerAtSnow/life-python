
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from life_python.world import World


@dataclass(frozen=True)
class Cell:
    x: int
    y: int

    def as_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)

    def neighbors(self) -> set[Cell]:
        return {
            Cell(self.x-1, self.y-1),
            Cell(self.x+0, self.y-1),
            Cell(self.x+1, self.y-1),
            Cell(self.x-1, self.y+0),
            Cell(self.x+1, self.y+0),
            Cell(self.x-1, self.y+1),
            Cell(self.x+0, self.y+1),
            Cell(self.x+1, self.y+1),
        }

    def count_neighbors(self, world: World) -> int:
        return sum(c in world for c in self.neighbors())

    def will_live(self, world: World) -> bool:
        count = self.count_neighbors(world)
        return (
            (self in world and count in world.survive) or
            (self not in world and count in world.born)
        )
