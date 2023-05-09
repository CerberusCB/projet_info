from pygame import Vector2

import core
from projectile.Projectile import Projectile


class Player:
    def __init__(self):
        self.size = 10
        self.vmax = 10
        self.accmax = 2
        self.position = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
        self.acceleration = Vector2(0, 0)
        self.speed = Vector2(0, 0)
        self.couleur = (255, 255, 255)
        self.projectile = []

    def move(self):
        self.speed += self.acceleration
        self.position += self.speed

        if self.speed.length() > self.vmax:
            self.speed.scale_to_length(self.vmax)

        if self.acceleration.length() > self.accmax:
            self.acceleration.scale_to_length(self.accmax)

    def show(self):
        core.Draw.circle(self.couleur, self.position, self.size)


    def on_edge(self):
        if self.position.x < 0:
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x > core.WINDOW_SIZE[0]:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = 0

    def shoot(self, proj):
        if core.getKeyPressList("SPACE"):
            self.projectile.append(proj)




