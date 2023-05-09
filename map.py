from pygame import Vector2

import core
from agario.player import Player


class Map:
    def __init__(self):
        self.maxplayer = 1
        self.maxasteroid = 10
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueurs = []
        self.asteroid = []

    def spawn_player(self):
        pass

    def show(self):
        for j in self.joueurs:
            j.show()
        for v in self.asteroid:
            v.show()


    def addjoueur(self, p):
        if len(self.joueurs) < self.maxplayer:
            self.joueurs.append(p)

    def addasteroid(self,a):
        if len(self.asteroid) < self.maxasteroid:
            self.asteroid.append(a)
