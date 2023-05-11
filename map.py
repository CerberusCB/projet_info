import random
import time

from pygame import Vector2

import core
from projetinfo.player import Player
from projetinfo.projectile import Projectile


class Map:
    def __init__(self):
        self.maxplayer = 1
        self.maxasteroid = 10
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueurs = []
        self.asteroid = []
        self.projectile = []

    def spawn_player(self):
        pass

    def show(self):
        for j in self.joueurs:
            j.show()
        for v in self.asteroid:
            v.show()
        for p in self.projectile:
            p.draw()


    def addjoueur(self, p):
        if len(self.joueurs) < self.maxplayer:
            self.joueurs.append(p)

    def addasteroid(self, a):
        if len(self.asteroid) < self.maxasteroid:

            b = random.randint(0, 3)
            if b == 0 :
                self.asteroid.position


            self.asteroid.append(a)

    def addprojectile(self, p):
        proj = Projectile()
        if len(self.projectile) > 0:
            if time.time() - self.projectile[-1].startTime > 1:
                orientation = Vector2(p.orientation)
                orientation.scale_to_length(-20)
                p2 = p.position + orientation
                proj.acceleration = Vector2(p2)
                self.position = Vector2(p2)
                self.projectile.append(proj)


        else:
            self.projectile.append(proj)

        print(len(self.projectile))




