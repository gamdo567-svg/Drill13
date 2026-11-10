from pico2d import *
import game_framework
import game_world
import title_mode
import pause_mode
from boy import Boy
from grass import Grass

boy = None


def init():
    global boy
    grass = Grass()
    game_world.add_oject(grass, 0)

    boy = Boy()
    game_world.add_oject(boy, 1)


def finish():
    # 다시 들어올 때 오브젝트가 중복되지 않도록 월드를 비운다
    game_world.clear()


def pause():
    # pause_mode가 위에 올라올 때 호출됨
    pass


def resume():
    # pause_mode가 빠지고 다시 돌아올 때 호출됨
    pass


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        else:
            boy.handle_event(event)
