import random
import time

from pygame import Vector2

import core


class Ennemie:
    def __init__(self):
        self.size = 20
        self.vmax = 7
        self.accmax = 2
        self.direction_spawn = random.randint(0,2)
        if self.direction_spawn == 1:
            self.position = Vector2(core.WINDOW_SIZE[0], random.randint(20, core.WINDOW_SIZE[1] -20))
            self.acceleration = Vector2(random.randint(-3, 1), 0)
        else:
            self.position = Vector2(random.randint(20, core.WINDOW_SIZE[0] -20), core.WINDOW_SIZE[1])
            self.acceleration = Vector2(0, random.randint(-3, 1))
        self.acceleration = Vector2(random.randint(-3, 1), 0)
        self.speed = Vector2(0, 0)
        self.couleur = (200, 0, 200)
        self.shoottime = time.time()

    def move(self):
        a = random.randint(0, 10)
        if a >= 5:
            if self.direction_spawn == 1:
                self.acceleration = Vector2(random.randint(-3, 3), 0)
            else:
                self.acceleration = Vector2(0, random.randint(-3, 3))
        self.speed += self.acceleration
        self.position += self.speed

        if self.speed.length() > self.vmax:
            self.speed.scale_to_length(self.vmax)
        if self.acceleration.length() > self.accmax:
            self.acceleration.scale_to_length(self.accmax)

    def show(self):
        core.Draw.circle(self.couleur, self.position, self.size, 2)
        core.Draw.line(self.couleur, self.position - (22, 0), self.position + (22, 0), 7)

    def on_edge(self):
        if self.position.x < 0:
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x > core.WINDOW_SIZE[0]:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = 0
