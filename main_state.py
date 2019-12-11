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
from Backgorund_objacts import Castle

from UI_s import Goblin_knight_UI
from UI_s import Goblin_spear_UI
from UI_s import Goblin_babarian_UI
from UI_s import Mouse_UI

from Minions import Goblin_Knight
from Minions import Goblin_Spear
from Minions import Goblin_Babarian
from Minions import Dwarf_worrior
from Minions import Dwarf_babarian

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
castle = None

fly_path = []

# ====================================================

scr_w = 800
scr_h = 600

sling_p = None

mouse_distance = 0
rope_lenght = 90
angle = 0
money = 0

# color
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


mouse_pressed = False
running = True
Flying = False

def vector(p0, p1):
    a = p1[0] - p0[0]
    b = p1[1] - p0[1]
    return (a, b)


def unit_vector(v):
    h = ((v[0] ** 2) + (v[1] ** 2)) ** 0.5
    if h == 0:
        h = 0.000000000000001
    ua = v[0] / h
    ub = v[1] / h
    return (ua, ub)


def distance(xo, yo, x, y):
    dx = x - xo
    dy = y - yo
    d = ((dx ** 2) + (dy ** 2)) ** 0.5
    return d


def sling_action():
    """Set up sling behavior"""
    global mouse_distance
    global rope_lenght
    global angle
    global sling_p
    sling_p = (scr_w//2 + catulpult.w/2 - 10, catulpult.h - 10)

    # Fixing bird to the sling rope

    v = vector((sling_p.x + 50, sling_p.y + 40), (mouse.x, mouse.y))
    uv = unit_vector(v)
    uv1 = uv[0]
    uv2 = uv[1]
    mouse_distance = distance(sling_p.x + 50, sling_p.y + 40, mouse.x, mouse.y)
    pu = (uv1 * rope_lenght + sling_p.x + 50, uv2 * rope_lenght + sling_p.y + 40)
    bigger_rope = 120
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
        pu2 = (uv1 * bigger_rope + sling_p.x + 60, uv2 * bigger_rope + sling_p.y + 40)

        #pygame.draw.line(win, (0, 0, 0), (catulpult.x + 70, catulpult.y + 20), pu2, 5)
        #pygame.draw.rect(win, (0, 0, 255), (pux, puy, 30, 30))
        #draw_line
        draw_rectangle((pux, puy, pux + 30, puy + 30))

        # pygame.draw.circle(win, BLUE, (pux, puy), 12, 2)
        #pygame.draw.line(win, (0, 0, 0), (catulpult.x + 70, catulpult.y + 20), pu2, 5)
        #draw_line
    else:
        mouse_distance += 10
        pu3 = (uv1 * mouse_distance + sling_p.x + 50, uv2 * mouse_distance + sling_p.y + 40)
        #pygame.draw.line(win, (0, 0, 0), (catulpult.x + 70, catulpult.y + 20), pu3, 5)
        # draw_line
        # screen.blit(redbird, (x_redbird, y_redbird))
        #pygame.draw.rect(win, (0, 0, 255), (x_diver, y_diver, 30, 30))
        # draw_line
        # pygame.draw.circle(win, BLUE, (x_diver, y_diver), 12, 2)
        #pygame.draw.line(win, (0, 0, 0), (catulpult.x + 80, catulpult.y + 20), pu3, 5)
        # draw_line

    # Angle of impulse
    dy = mouse.y - sling_p.y - 40
    dx = mouse.x - sling_p.x - 50
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

    global castle
    castle = Castle()
    game_world.add_object(castle, 2)
    castle.set_center_object(catulpult)

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
        if random.randint(0, 100) <= 50:
            enemys.append(Dwarf_worrior())
            game_world.add_object(enemys[E_spawn_count], 1)
        else:
            enemys.append(Dwarf_babarian())
            game_world.add_object(enemys[E_spawn_count], 1)
        enemys[E_spawn_count].set_center_object(catulpult)
        E_spawn_count += 1

    for game_object in game_world.all_objects():
        game_object.update()

    for goblin in goblins:
        for enemy in enemys:
            if collide(goblin, enemy):
                enemy.attack()
                goblin.attack()
                if 15< enemy.frame <=15.5:
                    goblin.Health_point -= clamp(1,enemy.AP - goblin.DF,enemy.AP)
                if 15< goblin.frame <= 15.5:
                    enemy.Health_point -= clamp(1,goblin.AP - enemy.DF,goblin.AP)
                if enemy.Health_point <= 0:
                    for goblin_q in goblins:
                        enemy.dead()
                        goblin_q.kill()
                        game_world.remove_object(enemy)
                if goblin.Health_point <= 0:
                    for enemy_q in enemys:
                        goblin.dead()
                        enemy_q.kill()
                        game_world.remove_object(goblin)
    for enemy in enemys:
        if collide(catulpult, enemy):
            print("Crash")
            #game_framework.change_state(title_state)

    delay(0.01)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    mouse.draw()

    update_canvas()
