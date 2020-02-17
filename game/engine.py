import tdl

class GameEngine:
    def __init__(self, console, main_window, screen_width, screen_height):
        self.action_queue = [] #These are all Action Objects
        self.areas = {}
        self.current_area = None
        self.console = console
        self.main_window = main_window
        self.SCREEN_HEIGHT = screen_height
        self.SCREEN_WIDTH = screen_width
    
    def game_loop(self):
        while not tdl.event.is_window_closed():
            self.pop()
            self.draw()

            for event in tdl.event.get():
                if event.type == 'KEYDOWN' and event.keychar != 'TEXT':
                    key_x, key_y = self.MOVEMENT_KEYS.get(
                        event.keychar, (0, 0))
                    action = self.ACTION_KEYS.get(event.keychar, (0, 0))
                    self.player.move(self.currentArea, key_x, key_y)

    def pop(self):
        if len(self.action_queue) < 1:
            return
        if self.action_queue[0].time_left <= 0:
            self.action_queue[0].resolve()
            self.action_queue.pop(0)
        else:
            for action in self.action_queue:
                action.time_left -= 1
    
    def push(self, action):
        self.action_queue.append(action)
    
    def draw(self):
        self.current_area.draw(self.console)
        self.main_window.blit(self.console, 0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 0, 0)
        tdl.flush()

#This is an interface. NEVER EVER USE
# TODO: See if this needs additional stuff
class Action:
    def __init__(self, time_left):
        self.time_left = time_left
    
    #This needs to be overwritten
    def resolve(self):
        return
