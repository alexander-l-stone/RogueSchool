#This is an interface. Never actually use this class please.

class Action:
    def __init__(self, time_left):
        self.time_left = time_left
    
    def resolve(self):
        return

class MoveAction(Action):
    def __init__(self, time_left, source, dx, dy):
        Action.__init__(self, time_left)
        self.source = source
        self.dx = dx
        self.dy = dy
    
    def resolve(self):
        self.source.x += self.dx
        self.source.y += self.dy