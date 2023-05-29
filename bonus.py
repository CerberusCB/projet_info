import random
import time

from pygame import Vector2

import core



class Bonus:
    def __init__(self):
        self.starttime = time.time()
        self.speed = Vector2(0, 0)
        self.type = random.randint(0, 2)
        self.size = 20
        self.position = Vector2(random.randint(20, core.WINDOW_SIZE[0]), random.randint(20, core.WINDOW_SIZE[1]))
        self.couleur = (55, 255, 55)

    def move(self):
        self.position += self.speed

    def on_edge(self):
        if self.position.x < 0:
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x > core.WINDOW_SIZE[0]:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = 0

    def show(self):
        core.Draw.circle(self.couleur, self.position, self.size)


