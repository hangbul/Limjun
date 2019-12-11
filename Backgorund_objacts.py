from pico2d import *


class Ground:
    def __init__(self):
        self.image = load_image("resources/images/ground.jpg")
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.y = 30

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)

    def set_center_object(self, catulpult):
        self.center_object = catulpult

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.y, self.canvas_width, self.y + 30, 0,0)

        #self.image.draw(self.window_left, self.y)
        #self.image.draw(self.window_left + 800, self.y)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 1600 - 1, 50

class Background:
    def __init__(self):
        self.image = load_image('resources/images/background_under.jpg')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.y = 300

    def set_center_object(self, catulpult):
        self.center_object = catulpult


    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, self.h - self.canvas_height)


    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)

class Frontground:
    def __init__(self):
        self.image = load_image('resources/images/background_under_front2.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.y = 300

    def set_center_object(self, catulpult):
        self.center_object = catulpult


    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y) - self.canvas_height // 2, self.h - self.canvas_height)


    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.canvas_width, self.canvas_height, 0, 0)

class Castle:
    def __init__(self):
        self.Health_Point = 5000
        self.image = load_image('resources/images/Dwarf_Castle.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h
        self.x = 1600
        self.y = 240

    def get_bb(self):
        return -self.w//2 - self.window_left + self.x, -self.h//2 + self.y, self.w//2 - self.window_left + self.x, self.h//2 + self.y


    def update(self):
        self.window_left = clamp(0, int(self.center_object.x) - self.canvas_width // 2, 1839 - self.canvas_width)

    def set_center_object(self, catulpult):
        self.center_object = catulpult

    def draw(self):
        self.image.draw(self.x-self.window_left, self.y)
        draw_rectangle(*self.get_bb())