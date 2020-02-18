import tdl
from game.world import World
from game.entities.drawable_entity import DrawableEntity
from game.areas.area import Area

class Game:
    def __init__(self, sw, sh, font_path):
        self.SCREEN_HEIGHT = sh
        self.SCREEN_WIDTH = sw
        self.FONT_PATH = font_path
        self.CENTERX = self.SCREEN_WIDTH//2
        self.CENTERY = self.SCREEN_HEIGHT//2
        self.main_window = None
        self.console = None
        self.action_queue = []
        self.world = None

    def push(self, action):
        self.action_queue.append(action)

    def pop(self):
        if len(self.action_queue > 0):
            if self.action_queue[0].time_left <= 0:
                self.action_queue[0].resolve()
                self.action_queue = self.action_queue[1:]
                return
            for action in self.action_queue:
                action.time_left -= 1

    def render_game(self):
        pass

    def initialize(self):
        tdl.set_font(self.FONT_PATH, greyscale=True, altLayout=True)
        self.console = tdl.Console(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.main_window = tdl.init(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, title="Rogue School", fullscreen=False)
        self.world = World()
        initial_area = Area(0,0, 100, 100, 'empty', '0,0 empty', (30,30,30))
        self.world.areas[(0,0)] = initial_area
    
    def main_loop(self):
        while not tdl.event.is_window_closed():
            self.render_game()
            for event in tdl.event.get():
                pass


class Main:
    def run(self):
        game = Game(80, 40, "arial12x12.png")
        game.initialize()
        game.main_loop()

if __name__ == "__main__":
    Main().run()

