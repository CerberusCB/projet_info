import time

import pygame
from pygame import Vector2

import core


class Player:
    def __init__(self):
        self.life = 15
        self.size = 17
        self.vmax = 7
        self.accmax = 2
        self.position = Vector2(core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2)
        self.acceleration = Vector2(0, 0)
        self.speed = Vector2(0, 0)
        self.couleur = (255, 255, 255)
        self.orientation = Vector2(-1, 1)
        self.starttime = time.time()

    def move(self):
        self.speed += self.acceleration
        self.position += self.speed
        if self.speed.length() > self.vmax:
            self.speed.scale_to_length(self.vmax)

        if self.acceleration.length() > self.accmax:
            self.acceleration.scale_to_length(self.accmax)
        self.orientation = Vector2(core.getMouseLocation()) - self.position

    def show(self):
        #core.Draw.circle(self.couleur, self.position, self.size)
        orientation = Vector2(self.orientation)
        orientation.scale_to_length(30)
        orientation = orientation.rotate(140)
        p1 = self.position + orientation
        orientation = Vector2(self.orientation)
        orientation.scale_to_length(30)
        orientation = orientation.rotate(-140)
        p3 = self.position + orientation
        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        p2 = self.position + orientation

        core.Draw.text(self.couleur, ("LIFE REMAINING : " + str(self.life)), (200, 100), 20)

#t
        core.Draw.polygon(self.couleur, (self.position, p1, p2, p3), 2)
        core.Draw.circle(self.couleur, core.getMouseLocation(), self.size, 2)


    def on_edge(self):
        if self.position.x < 0:
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x > core.WINDOW_SIZE[0]:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = 0

    def lose_life(self):
        if time.time() - self.starttime > 2:
            self.life -= 1
            self.starttime = time.time()
            print(self.life)





