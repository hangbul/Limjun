from pico2d import *


class Mouse_UI:
    def __init__(self):
        #self.image = load_image("resources/images/UI/GK_botton.png")
        self.x = -20
        self.y = -20


    def draw(self):
        #self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10 , self.x + 10 - 1, self.y + 10 -1

class Goblin_knight_UI:
    def __init__(self):
        self.image = load_image("resources/images/UI/GK_botton.png")
        self.x = 40
        self.y = 560

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40 - 1, self.y + 40 -1

class Goblin_spear_UI:
    def __init__(self):
        self.image = load_image("resources/images/UI/GS_botton.png")
        self.x = 120
        self.y = 560

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40 - 1, self.y + 40 -1

class Goblin_babarian_UI:
    def __init__(self):
        self.image = load_image("resources/images/UI/GB_botton.png")
        self.x = 200
        self.y = 560

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 40 , self.x + 40 - 1, self.y + 40 -1


