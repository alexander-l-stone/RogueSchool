from game.entity import Entity
import tdl

class DrawableEntity(Entity):
    def __init__(self, x, y, char, color, bgcolor, *components):
        Entity.__init__(self, *components)
        self.char = char
        self.color = color
        self.bgcolor = bgcolor
        self.x = x
        self.y = y
    
    def draw(self, console, topx, topy, sw, sh):
        if (self.x-topx > 0) and (self.y-topy > 0) and (self.x-topx < sw) and (self.y-topy < sh):
            console.draw_char(self.x-topx, self.y-topy, self.char, self.color, bg=self.bgcolor)

    def clear(self, console, topx, topy, sw, sh, clearbg=None):
        if (self.x-topx > 0) and (self.y-topy > 0) and (self.x-topx < sw) and (self.y-topy < sh):
            console.draw_char(self.x-topx, self.y-topy, ' ', bg=clearbg)
