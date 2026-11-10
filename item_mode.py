from pico2d import *
import game_framework
import game_world
import play_mode

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
    # pause_mode와 달리 아이템 창이 떠 있는 동안에도 게임은 계속 진행된다
    game_world.update()


def render():
    clear_canvas()
    game_world.render()      # 뒤의 게임 화면을 그대로 그리고
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)  # 그 위에 아이템 창
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.pop_mode()   # play_mode로 돌아감
        elif event.type == SDL_KEYDOWN and event.key == SDLK_0:
            play_mode.boy.item = None           # 아이템 해제
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            play_mode.boy.item = 'SmallBall'    # 작은 공
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            play_mode.boy.item = 'BigBall'      # 큰 공
            game_framework.pop_mode()
        else:
            # 게임이 멈추지 않으므로 소년 조작 키는 계속 전달한다
            play_mode.boy.handle_event(event)
