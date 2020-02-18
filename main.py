import tdl

class Main:
    def run(self):
        tdl.init(80, 50)

        while not tdl.event.is_window_closed():
            user_input = tdl.event.key_wait()
            key_pressed = user_input.keychar
            if key_pressed == "ESCAPE" or key_pressed == 'q':
                break
            else:
                print("You pressed {}".format(key_pressed))

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
    
    def main_loop(self):
        while not tdl.event.is_window_closed():
            self.render_game()
            for event in tdl.event.get():
                pass


if __name__ == "__main__":
    Main().run()

