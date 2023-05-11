import time

from pygame import Vector2

import core
from projetinfo.asteroid import Asteroid
from projetinfo.map import Map
from projetinfo.player import Player


class Partie:
    def __init__(self):
        self.map = Map()

    def show(self):
        self.map.show()

    def shoot(self):
        p = Player()
        if core.getMouseLeftClick():
            self.map.addprojectile(p)
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
        for j in self.map.joueurs:
            j.on_edge()
        for a in self.map.asteroid:
            a.on_edge()

    def move(self):
        for j in self.map.joueurs:
                if core.getKeyPressList("z"):
                    j.acceleration.y-=1
                if core.getKeyPressList("s"):
                    j.acceleration.y+=1
                if core.getKeyPressList("q"):
                    j.acceleration.x-=1
                if core.getKeyPressList("d"):
                    j.acceleration.x+=1
                j.move()
        for a in self.map.asteroid:
            a.move()
        for p in self.map.projectile:
            p.move()

