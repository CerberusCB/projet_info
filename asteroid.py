import random

from pygame import Vector2

import core
#random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1])

class Asteroid:
    def __init__(self):
        self.size = 50
        self.vmax = 7
        self.accmax = 2
        b = random.randint(0, 3)
        if b == 0:
            self.position = Vector2(0, random.uniform(0, core.WINDOW_SIZE[1]))
        if b == 1:
            self.position = Vector2(random.uniform(0, core.WINDOW_SIZE[0]), 0)
        if b == 2:
            self.position = Vector2(core.WINDOW_SIZE[0], random.uniform(0, core.WINDOW_SIZE[1]))
        if b == 3:
            self.position = Vector2(random.uniform(0, core.WINDOW_SIZE[0]), core.WINDOW_SIZE[1])
        self.acceleration = Vector2(random.uniform(0, 0), random.uniform(0, 0))
        self.speed = Vector2(random.uniform(-7, 7), random.uniform(-7, 7))
        self.couleur = (255, 255, 255)

    def show(self):
        core.Draw.circle((255, 55, 55), self.position, self.size)

    def move(self):
        self.speed += self.acceleration
        self.position += self.speed

        if self.speed.length() > self.vmax:
            self.speed.scale_to_length(self.vmax)

        if self.acceleration.length() > self.accmax:
            self.acceleration.scale_to_length(self.accmax)

    def on_edge(self):
        if self.position.x < 0:
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x > core.WINDOW_SIZE[0]:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = 0

    def collision(self):
        pass
