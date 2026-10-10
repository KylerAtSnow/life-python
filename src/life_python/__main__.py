

from life_python.world import World


def life(i: int = 100) -> World:
    world = World()
    world.add_glider(1,1)
    return world.iterations(i)

def main():
    world = life()
    print(world.living_cells())

main()
