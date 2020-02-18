from game.actions.action import MoveAction

class Move:
    def __init__(self, area):
        self.area = area

    def check_move(self, x, y):
        return not self.area.entityList[(x,y)].has('blocks_movement')

    def make_move(self, entity, dx, dy):
        return MoveAction(1, entity, dx, dy)