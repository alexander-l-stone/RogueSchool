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

if __name__ == "__main__":
    Main().run()

