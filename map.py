import random
import time

from pygame import Vector2

import core
import etoile
from asteroid import Asteroid
from player import Player
from projectile import Projectile


class Map:
    def __init__(self):
        self.init_done = False
        self.score = 0
        self.ast_detruit = 0
        self.enn_detruit = 0
        self.maxplayer = 1
        self.maxasteroid = 0
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueur = None
        self.ennemie = None
        self.asteroid = []
        self.projectile = []
        self.enn_projectile = []
        self.starttime = time.time()
        self.nb_5sec = 0


#----------------------------debut des fonction--------------------------------------------------------------
    def show(self):
        z=0
        if self.ennemie is not None:
            self.ennemie.show()
        if (time.time() - self.joueur.starttime < self.joueur.duree_invincibilite) and self.joueur.life < 3:
            self.joueur.couleur = (255, 255, 0)
        else:
            self.joueur.couleur = (255, 255, 255)
        self.joueur.show()
        for v in self.asteroid:
            v.show()
        for p in self.projectile:
            p.draw()
        for ep in self.enn_projectile:
            ep.draw()
        core.Draw.text((255, 255, 255), ("SCORE : " + str(self.score)), ((core.WINDOW_SIZE[0]/2), 100), 20)

# ----------------------------ajout des joueur, asteroid et projectile--------------------------------------------------------------
    def addjoueur(self, p):
        self.joueur = p

    def addennemie(self, e):
        self.ennemie = e

    def addasteroid(self, a):
        if (len(self.asteroid) < self.maxasteroid) and self.init_done == False:
            self.asteroid.append(a)
        self.init_done = True
        if self.init_done ==True:
            self.asteroid.append(a)


    def addprojectile_player(self):
        proj = Projectile()
        orientation = Vector2(core.getMouseLocation()) - self.joueur.position
        orientation.scale_to_length(30)
        proj.position = Vector2(self.joueur.position) + orientation
        proj.acceleration = Vector2(orientation)
        if len(self.projectile) > 0:
            if time.time() - self.projectile[-1].startTime > 0.5:
                self.projectile.append(proj)
        else:
            self.projectile.append(proj)

    def addprojectile_ennemie(self):
        enn_proj = Projectile()
        if self.ennemie is not None:
            enn_orientation = Vector2(self.joueur.position) - self.ennemie.position
            enn_orientation.scale_to_length(30)
            enn_proj.position = Vector2(self.ennemie.position + enn_orientation)
            enn_proj.acceleration = Vector2(enn_orientation)
            if time.time() - self.ennemie.shoottime > 5:
                self.enn_projectile.append(enn_proj)
                self.ennemie.shoottime = time.time()


# ----------------------------verification des collision et division--------------------------------------------------------------
    def collision(self):
        for a in self.asteroid:
            if self.joueur.position.distance_to(a.position) - self.joueur.size < a.size:
                self.joueur.lose_life()
                if self.joueur.life == 0:
                    self.joueur = None
            for p in self.projectile:
                if p.position.distance_to(a.position) - p.taille < a.size:
                    self.division(a)
                    self.asteroid.remove(a)
                    self.ast_detruit += 1
                    self.projectile.remove(p)
        if self.ennemie is not None:
            if self.joueur.position.distance_to(self.ennemie.position) - self.joueur.size < self.ennemie.size:
                self.joueur.lose_life()
                self.enn_detruit += 1
                if self.joueur.life == 0:
                    self.joueur = None
                self.ennemie = None
            if self.ennemie is not None:
                for p in self.projectile:
                    if p.position.distance_to(self.ennemie.position) - p.taille < self.ennemie.size:
                        self.projectile.remove(p)
                        self.ennemie = None
                        self.enn_detruit += 1
        for e in self.enn_projectile:
            if self.joueur.position.distance_to(e.position) - self.joueur.size < e.taille:
                self.joueur.lose_life()
                self.enn_projectile.remove(e)
                if self.joueur.life == 0:
                    self.joueur = None



    def division(self, a):
        for i in range(0, 2):
            if a.size == 50:
                b = Asteroid(36)
                b.position = Vector2(a.position)
                b.speed = Vector2(random.uniform(-7, 7), random.uniform(-7, 7))
                self.addasteroid(b)
            if a.size == 36 :
                b = Asteroid(24)
                b.position = Vector2(a.position)
                b.speed = Vector2(random.uniform(-7, 7), random.uniform(-7, 7))
                self.addasteroid(b)

# ----------------------------calcul du score--------------------------------------------------------------
    def calcul_score(self):
        if time.time() - self.starttime > 5:
            self.nb_5sec += 1
            self.starttime = time.time()
        self.score = (self.ast_detruit * 10) + (self.nb_5sec * 10) + (self.joueur.life * 100) + (self.enn_detruit * 100)



