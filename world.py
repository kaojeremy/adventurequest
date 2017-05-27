import tiles, items

def tile_at(x,y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

world_map = [ [None, None, tiles.VictoryRoom(2,0), None, None], 
              [tiles.OpenChestRoom(0,1,items.Sword), tiles.EmptyCavePath(1,1), tiles.DoorRoom(2,1), tiles.EmptyCavePath(3,1), tiles.SkeletonRoom(4,1)],
              [None, None, tiles.StartingRoom(2,2), None, None] ]