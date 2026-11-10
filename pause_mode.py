from pico2d import *
import game_framework
import game_world
import play_mode

image = None


def init():
    global image
    image = load_image('pause.png')


def finish():
    global image
    del image


def update():
    # 일시정지 중에는 게임 월드를 업데이트하지 않는다
    pass


def render():
    clear_canvas()
    game_world.render()      # 멈춘 게임 화면을 그대로 보여주고
    image.draw(400, 300)     # 그 위에 일시정지 이미지를 겹쳐 그린다
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()   # play_mode로 돌아감
        elif event.type == SDL_KEYUP:
            # 방향키를 누른 채 멈췄다가 떼는 경우, 재개 후 계속 달리지 않도록 전달
            play_mode.boy.handle_event(event)
