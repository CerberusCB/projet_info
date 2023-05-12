import time

from pygame import Vector2

import core
import projectile
from asteroid import Asteroid

from map import Map
from player import Player


class Partie:
    def __init__(self):
        self.map = Map()

    def show(self):
        self.map.show()

    def shoot(self):
        if core.getMouseLeftClick():
            self.map.addprojectile()
        for a in self.map.projectile:
            if time.time() - a.startTime > a.dureevie:
                self.map.projectile.remove(a)

    def addPlayer(self):
        p = Player()
        self.map.addjoueur(p)

    def addasteroid(self):
        for i in range(0, self.map.maxasteroid):
            self.map.addasteroid(Asteroid())



    def sortie(self):
        self.map.joueur.on_edge()
        for a in self.map.asteroid:
            a.on_edge()

    def move(self):
        if core.getKeyPressList("z"):
            self.map.joueur.acceleration.y-=1
        if core.getKeyPressList("s"):
            self.map.joueur.acceleration.y+=1
        if core.getKeyPressList("q"):
            self.map.joueur.acceleration.x-=1
        if core.getKeyPressList("d"):
            self.map.joueur.acceleration.x+=1
        self.map.joueur.move()
        for a in self.map.asteroid:
            a.move()
        for p in self.map.projectile:
            p.move()

    def collision(self):
        self.map.collision()

    def score_game(self):
        self.map.calcul_score()