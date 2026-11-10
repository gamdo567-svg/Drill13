from pico2d import *
import game_framework

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def pause():
    pass


def resume():
    pass


def update():
    pass


def render():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()   # play_mode로 돌아감
