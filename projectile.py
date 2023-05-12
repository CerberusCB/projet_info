import time

from pygame import Vector2

import core
from player import Player


class Projectile:
    def __init__(self):
        self.taille = 3
        self.vitesse = Vector2()
        self.acceleration = Vector2()
        self.vmax = 15
        self.accmax = 1
        self.position =  Vector2()
        self.dureevie = 3
        self.startTime = time.time()
        #self.orientation = Vector2()


    def draw(self):
        core.Draw.circle((255, 255, 255),self.position, self.taille)
        #orientation = Vector2(self.orientation


    def move(self):
        self.vitesse += self.acceleration
        self.position += self.vitesse

        if self.vitesse.length() > self.vmax:
            self.vitesse.scale_to_length(self.vmax)

        if self.acceleration.length() > self.accmax:
            self.acceleration.scale_to_length(self.accmax)