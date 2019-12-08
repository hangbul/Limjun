import random
import json
import os
import math

from pico2d import *
import game_framework
import game_world

import title_state


from Backgorund_objacts import Ground
from Backgorund_objacts import Background
from Backgorund_objacts import Frontground

from UI_s import Goblin_knight_UI
from UI_s import Goblin_spear_UI
from UI_s import Goblin_babarian_UI

from UI_s import Mouse_UI

from Minions import Goblin_Knight
from Minions import Goblin_Spear
from Minions import Goblin_Babarian

from Minions import Dwarf_worrior

from Catulpult_main_char import Goblin_Doom_catulpult

current_path = os.getcwd()

name = "MainState"

#background
frontground = None
background = None
ground = None

#UI
UIs = []
mouse = None

game_run_time = 0

# army
spawn_count = 0
goblins = []
divers = []
catulpult = None

# enemy
E_spawn_count = 0
enemys = []
#castle = Enemy_castle()

fly_path = []

# ====================================================



mouse_distance = 0
rope_lenght = 90
angle = 0
money = 0

# color
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# vecter - gravtity
# space = pm.Space()
# space.gravity = (0.0, -700.0)


mouse_pressed = False
running = True
Flying = False


def to_pygame(p):
    """Convert pymunk to pygame coordinates"""
    return int(p.x), int(-p.y + 600)


def vector(p0, p1):
    """Return the vector of the points
    p0 = (xo,yo), p1 = (x1,y1)"""
    a = p1[0] - p0[0]
    b = p1[1] - p0[1]
    return (a, b)


def unit_vector(v):
    """Return the unit vector of the points
    v = (a,b)"""
    h = ((v[0] ** 2) + (v[1] ** 2)) ** 0.5
    if h == 0:
        h = 0.000000000000001
    ua = v[0] / h
    ub = v[1] / h
    return (ua, ub)


def distance(xo, yo, x, y):
    """distance between points"""
    dx = x - xo
    dy = y - yo
    d = ((dx ** 2) + (dy ** 2)) ** 0.5
    return d


def sling_action():
    """Set up sling behavior"""
    global mouse_distance
    global rope_lenght
    global angle

    # Fixing bird to the sling rope

    v = vector((catulpult.x + 50, catulpult.y + 40), (mouse.x, mouse.y))
    uv = unit_vector(v)
    uv1 = uv[0]
    uv2 = uv[1]
    mouse_distance = distance(catulpult.x + 50, catulpult.y + 40, mouse.x, mouse.y)
    pu = (uv1 * rope_lenght + catulpult.x + 50, uv2 * rope_lenght + catulpult.y + 40)
    bigger_rope = 102
    x_diver = mouse.y - 20
    y_diver = mouse.y - 20
    if mouse_distance > rope_lenght:
        pux, puy = pu
        pux -= 20
        puy -= 20
        pul = pux, puy
        # loaded shell
        #pygame.draw.rect(win, (0, 0, 255), (pux, puy, 30, 30))
        draw_rectangle((pux, puy, 30, 30))
        #
        pu2 = (uv1 * bigger_rope + catulpult.x + 60, uv2 * bigger_rope + catulpult.y + 40)

        #pygame.draw.line(win, (0, 0, 0), (catulpult.x + 70, catulpult.y + 20), pu2, 5)
        #pygame.draw.rect(win, (0, 0, 255), (pux, puy, 30, 30))
        #draw_line
        draw_rectangle((pux, puy, 30, 30))
        # pygame.draw.circle(win, BLUE, (pux, puy), 12, 2)
        #pygame.draw.line(win, (0, 0, 0), (catulpult.x + 70, catulpult.y + 20), pu2, 5)
        #draw_line
    else:
        mouse_distance += 10
        pu3 = (uv1 * mouse_distance + catulpult.x + 50, uv2 * mouse_distance + catulpult.y + 40)
        #pygame.draw.line(win, (0, 0, 0), (catulpult.x + 70, catulpult.y + 20), pu3, 5)
        # draw_line
        # screen.blit(redbird, (x_redbird, y_redbird))
        #pygame.draw.rect(win, (0, 0, 255), (x_diver, y_diver, 30, 30))
        # draw_line
        # pygame.draw.circle(win, BLUE, (x_diver, y_diver), 12, 2)
        #pygame.draw.line(win, (0, 0, 0), (catulpult.x + 80, catulpult.y + 20), pu3, 5)
        # draw_line

    # Angle of impulse
    dy = mouse.y - catulpult.y - 40
    dx = mouse.x - catulpult.x - 50
    if dx == 0:
        dx = 0.00000000000001
    angle = math.atan((float(dy)) / dx)


# ====================================================

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global background
    background = Background()
    game_world.add_object(background, 0)

    global ground
    ground = Ground()
    game_world.add_object(ground, 0)

    global catulpult
    catulpult = Goblin_Doom_catulpult()
    game_world.add_object(catulpult, 1)

    ground.set_center_object(catulpult)
    background.set_center_object(catulpult)
    ground.set_center_object(catulpult)
    catulpult.set_background(background)

    global frontground
    frontground = Frontground()
    game_world.add_object(frontground, 2)
    frontground.set_center_object(catulpult)

    global UIs
    UIs = [Goblin_knight_UI(), Goblin_spear_UI(), Goblin_babarian_UI()]
    for UI in UIs:
        game_world.add_object(UI, 2)



    global mouse
    mouse = Mouse_UI()

def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():

    events = get_events()
    global mouse_pressed
    global mouse_distance
    global spawn_count

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYUP and event.key == SDLK_1:
            goblins.append(Goblin_Knight())
            game_world.add_object(goblins[spawn_count], 1)
            goblins[spawn_count].set_center_object(catulpult)
            spawn_count += 1
        elif event.type == SDL_KEYUP and event.key == SDLK_2:
            goblins.append(Goblin_Spear())
            game_world.add_object(goblins[spawn_count], 1)
            goblins[spawn_count].set_center_object(catulpult)
            spawn_count += 1
        elif event.type == SDL_KEYUP and event.key == SDLK_3:
            goblins.append(Goblin_Babarian())
            game_world.add_object(goblins[spawn_count], 1)
            goblins[spawn_count].set_center_object(catulpult)
            spawn_count += 1

        elif event.type == SDL_MOUSEBUTTONDOWN and event.key == SDLK_LEFT:
            mouse_pressed = True
        elif event.type == SDL_MOUSEBUTTONUP and mouse_pressed:
            mouse_pressed = False

            # cat_x = 50
            # cat_y = 480

            xo = catulpult.x + 105
            yo = 100
            if mouse_distance > rope_lenght:
                mouse_distance = rope_lenght

            if mouse.x < catulpult.x + 5:
                #diver = Doom_diver(mouse_distance, angle, xo, yo, space)
                #divers.append(diver)
                pass
            else:
                #diver = Doom_diver(-mouse_distance, angle, xo, yo, space)
                #divers.append(diver)
                pass
        elif event.type == SDL_MOUSEMOTION:
            mouse.x = event.x
            mouse.y = 600 - event.y +1
        else:
            catulpult.handle_event(event)


def update():
    global game_run_time, E_spawn_count
    game_run_time += 1

    if game_run_time % 500 == 0:
        enemys.append(Dwarf_worrior())
        game_world.add_object(enemys[E_spawn_count], 1)
        enemys[E_spawn_count].set_center_object(catulpult)
        E_spawn_count += 1

    for game_object in game_world.all_objects():
        game_object.update()

    for goblin in goblins:
        for enemy in enemys:
            if collide(goblin, enemy):
                goblin.attack()
                enemy.attack()
            else:
                goblin.walk()
                enemy.walk()

    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    mouse.draw()

    update_canvas()
