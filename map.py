import random
import time
import pygame

from pygame import Vector2

import core
import etoile
from asteroid import Asteroid
from etat import Etat
from player import Player
from projectile import Projectile

class Map:
    def __init__(self):
        self.init_done = False
        self.difficulty = 0
        self.score = 0
        self.ast_detruit = 0
        self.enn_detruit = 0
        self.maxplayer = 1
        self.maxasteroid = 1
        self.taille = Vector2(core.WINDOW_SIZE)
        self.joueur = None
        self.ennemie = None
        self.asteroid = []
        self.projectile = []
        self.enn_projectile = []
        self.starttime = time.time()
        self.time_spawn_bonus = time.time()
        self.starttime_bonus = time.time()
        self.bonus = []
        self.nb_5sec = 0

#----------------------------debut des fonction--------------------------------------------------------------
    def show(self):
        z=0
        if self.ennemie is not None:
            self.ennemie.show()
        if (time.time() - self.joueur.starttime < self.joueur.duree_invincibilite):
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
        for b in self.bonus:
            b.show()
        core.Draw.text((255, 255, 255), ("SCORE : " + str(self.score)), ((core.WINDOW_SIZE[0]/2), 100), 20)

# ----------------------------ajout des joueur, asteroid et projectile--------------------------------------------------------------
    def addjoueur(self, p):
        self.joueur = p

    def addennemie(self, e):
        self.ennemie = e

    def addbonus(self, b):

        if len(self.bonus) == 0:
            if time.time() - self.time_spawn_bonus > 20:
                if self.difficulty == 3:
                    b.speed = Vector2(random.randint(-4, 4), random.randint(-4, 4))
                self.bonus.append(b)
        else:
            self.time_spawn_bonus = time.time()

    def addasteroid(self, a, add):
        if (len(self.asteroid) < self.maxasteroid) and self.init_done == False:
            self.asteroid.append(a)
        if self.init_done ==True and add == True:
            self.asteroid.append(a)


    def addprojectile_player(self):
        proj = Projectile()
        orientation = Vector2(core.getMouseLocation()) - self.joueur.position
        orientation.scale_to_length(30)
        proj.position = Vector2(self.joueur.position) + orientation
        proj.acceleration = Vector2(orientation)
        if time.time() - self.starttime_bonus > 5:
            self.joueur.fire_rate = 0.5
        if len(self.projectile) > 0:
            if time.time() - self.projectile[-1].startTime > self.joueur.fire_rate:
                self.projectile.append(proj)
        else:
            self.projectile.append(proj)

    def addprojectile_ennemie(self):
        enn_proj = Projectile()
        enn_proj2 = Projectile()
        if self.ennemie is not None:
            preshot = (Vector2(self.joueur.acceleration) * (self.joueur.position.distance_to(self.ennemie.position)) / 5)
            if self.difficulty == 3:
                enn_orientation = Vector2(self.joueur.position) + preshot - self.ennemie.position
            else:
                enn_orientation = Vector2(self.joueur.position) - self.ennemie.position
            enn_orientation.scale_to_length(30)
            enn_proj.position = Vector2(self.ennemie.position + enn_orientation)
            enn_proj.acceleration = Vector2(enn_orientation)
            if self.difficulty == 2:
                if time.time() - self.ennemie.shoottime > 3:
                    self.enn_projectile.append(enn_proj)
                    self.ennemie.shoottime = time.time()
            if self.difficulty == 3:
                if time.time() - self.ennemie.shoottime > 1:
                    self.enn_projectile.append(enn_proj)
                    self.ennemie.shoottime = time.time()


            if self.difficulty == 4:
                enn_orientation = Vector2(self.joueur.position) + preshot - self.ennemie.position
                enn_orientation2 = Vector2(self.joueur.position) - self.ennemie.position
                enn_orientation.scale_to_length(30)
                enn_orientation2.scale_to_length(30)
                enn_proj.position = Vector2(self.ennemie.position + enn_orientation)
                enn_proj.acceleration = Vector2(enn_orientation)
                enn_proj2.position = Vector2(self.ennemie.position + enn_orientation2)
                enn_proj2.acceleration = Vector2(enn_orientation2)
                if time.time() - self.ennemie.shoottime > 1:
                    self.enn_projectile.append(enn_proj)
                    self.enn_projectile.append(enn_proj2)
                    self.ennemie.shoottime = time.time()


# ----------------------------verification des collision et division--------------------------------------------------------------
    def collision(self):
        for a in self.asteroid:
            if self.joueur.position.distance_to(a.position) - self.joueur.size < a.size:
                self.joueur.lose_life()
                if self.joueur.life == 0:
                    core.memory("etat", Etat.game_over)
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
                    core.memory("etat", Etat.game_over)
                self.ennemie = None
            if self.ennemie is not None:
                for p in self.projectile:
                    if self.ennemie is not None:
                        if p.position.distance_to(self.ennemie.position) - p.taille < self.ennemie.size:
                            self.projectile.remove(p)
                            self.ennemie = None
                            self.enn_detruit += 1
        for e in self.enn_projectile:
            if self.joueur.position.distance_to(e.position) - self.joueur.size < e.taille:
                self.joueur.lose_life()
                self.enn_projectile.remove(e)
                if self.joueur.life == 0:
                    core.memory("etat", Etat.game_over)
        for b in self.bonus:
            if self.joueur.position.distance_to(b.position) - self.joueur.size < b.size:
                if b.type == 0:
                    self.joueur.life += 1
                if b.type == 1:
                    self.joueur.duree_invincibilite = 5
                    self.joueur.starttime = time.time()
                if b.type == 2:
                    self.starttime_bonus = time.time()
                    self.joueur.fire_rate = 0.25
                self.bonus.remove(b)




    def division(self, a):
        for i in range(0, 2):
            if a.size == 50:
                b = Asteroid(36)
                b.position = Vector2(a.position)
                b.speed = Vector2(random.uniform(-7, 7), random.uniform(-7, 7))
                self.addasteroid(b, True)
            if a.size == 36 :
                b = Asteroid(24)
                b.position = Vector2(a.position)
                b.speed = Vector2(random.uniform(-7, 7), random.uniform(-7, 7))
                self.addasteroid(b, True)

# ----------------------------calcul du score--------------------------------------------------------------
    def calcul_score(self):
        if time.time() - self.starttime > 5:
            self.nb_5sec += 1
            self.starttime = time.time()
        self.score = (self.ast_detruit * 10) + (self.nb_5sec * 10) + (self.joueur.life * 100) + (self.enn_detruit * 100)
        if (len(self.asteroid)) == 0:
            core.memory("etat", Etat.win)


