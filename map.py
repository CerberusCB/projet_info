import random
import time

from pygame import Vector2

import core
import etoile
from projectile import Projectile

class Map:
    def __init__(self):
        self.maxplayer = 1
        self.maxasteroid = 10
        self.maxetoiles = 20
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueurs = []
        self.asteroid = []
        self.projectile = []
        self.etoiles =[]

    def spawn_player(self):
        pass

    def show(self):
        for j in self.joueurs:
            j.show()
        for e in self.etoiles:
            e.show()
        for v in self.asteroid:
            v.show()
        for p in self.projectile:
            p.draw()



    def addjoueur(self, p):
        if len(self.joueurs) < self.maxplayer:
            self.joueurs.append(p)

    def addasteroid(self, a):
        if len(self.asteroid) < self.maxasteroid:
            self.asteroid.append(a)

    def addetoile(self,e):
        if len(self.etoiles)<self.maxetoiles:
            self.etoiles.append(e)

    def addprojectile(self, p):
        proj = Projectile()
        if len(self.projectile) > 0:
            if time.time() - self.projectile[-1].startTime > 0.5:
                self.projectile.append(proj)
        else:
            self.projectile.append(proj)

        orientation = Vector2(core.getMouseLocation()) - p.position
        orientation.scale_to_length(-20)
        p2 = p.position + orientation
        proj.acceleration = Vector2(p2)

        print(len(self.projectile))





