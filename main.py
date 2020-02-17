from game.engine import GameEngine
from game.entity.entity import Entity
from game.area.area import Area
import tdl


def main():
    #set up the console
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    font_path = 'arial12x12.png'
    tdl.set_font(font_path, greyscale=True, altLayout=True)
    title = "Rogue School"
    fullscreen = False
    console = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)
    main_window = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title=title, fullscreen=fullscreen)

    player = Entity(int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2), '@', (255,0,0))

    start_area = Area(0, 0, 0, 'empty')

    start_area.entity_dict[(player.x, player.y)] = player
    player.area = start_area

    game = GameEngine(console, main_window, SCREEN_WIDTH, SCREEN_HEIGHT)
    game.current_area = start_area
    game.game_loop()
    

if __name__ == '__main__':
    main()



