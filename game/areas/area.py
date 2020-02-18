#This area holds the basic terrain and location of stuff for a displayed zone


class Area:
    def __init__(self, x, y, h, w, areaType, name, floorColor, entityList={}, animalList=[]):
        self.x = x
        self.y = y
        self.height = h
        self.width = w
        self.areaType = areaType
        self.name = name
        self.centerx = self.width//2
        self.centery = self.height//2
        self.floorColor = floorColor
        self.entityList = entityList

    def draw(self, console, topx, topy, sw, sh):
        for drawx in range(0, sw):
            for drawy in range(0, sh):
                if ((topx-drawx > self.x-self.width//2) and (topx-drawx < self.x+self.width//2)) and ((drawy-topy > self.y-self.height//2) and (drawy-topy < self.y+self.height//2)):
                    console.draw_char(drawx-topx, drawy-topy,' ', bg=self.floorColor)
        for key, val in self.entityList.items():
            val.draw(console, topx, topy, sw, sh)
            
    def clear(self, console, topx, topy, sw, sh, clearbg=None):
        for drawx in range(0, sw):
            for drawy in range(0, sh):
                console.draw_char(drawx-topx, drawy-topy, ' ', bg=clearbg)
        for key, val in self.entityList.items():
            val.clear(console, topx, topy, sw, sh, clearbg)
