import time

from pygame import Vector2
from pygame.rect import Rect

import core
import projectile
from asteroid import Asteroid
from ennemie import Ennemie
from etat import Etat

from map import Map
from player import Player


class Partie:
    def __init__(self):
        self.map = Map()
        self.difficulty = 0
        self.starttime = time.time()


    def ecran_demarage(self):

        coord_debut_asteroid = Vector2((core.WINDOW_SIZE[0] /2 - core.WINDOW_SIZE[0] /8, core.WINDOW_SIZE[1] /2 - core.WINDOW_SIZE[1] /4))
        coord_debut_launch_game = Vector2((core.WINDOW_SIZE[0] /2 - core.WINDOW_SIZE[0] /10, core.WINDOW_SIZE[1] * 0.6))
        coord_debut_exit = Vector2((core.WINDOW_SIZE[0] / 2 - core.WINDOW_SIZE[0] / 15), core.WINDOW_SIZE[1] * 0.8)
        rect1 = Rect(coord_debut_launch_game.x -2, coord_debut_launch_game.y +3, 350, 65)
        rect2 = Rect(coord_debut_exit.x - 2, coord_debut_exit.y + 3, 127, 65)

        core.Draw.text((255, 255, 255), "ASTEROID", coord_debut_asteroid, 100)
        core.Draw.text((255, 255, 255), "Launch Game", coord_debut_launch_game, 65)
        core.Draw.text((255, 255, 255), "EXIT", coord_debut_exit, 65)

        if rect1.collidepoint(core.getMouseLocation()):
            core.Draw.rect((255, 255, 255), rect1, 5)
            if core.getMouseLeftClick():
                core.memory("etat", Etat.choix_mode)


        if rect2.collidepoint(core.getMouseLocation()):
            core.Draw.rect((255, 255, 255), rect2, 5)
            if core.getMouseLeftClick():
                exit()

    def ecran_choix_mode(self):

        coord_debut_choose_game_difficulty = Vector2(core.WINDOW_SIZE[0] /4, core.WINDOW_SIZE[1] /4 )
        coord_debut_EASY = Vector2((core.WINDOW_SIZE[0] /4, core.WINDOW_SIZE[1] /2))
        coord_debut_MEDIUM = Vector2((core.WINDOW_SIZE[0] / 2, core.WINDOW_SIZE[1] / 2))
        coord_debut_HARD = Vector2((core.WINDOW_SIZE[0] * 0.75, core.WINDOW_SIZE[1] / 2))
        coord_debut_exit = Vector2((core.WINDOW_SIZE[0] / 4 - core.WINDOW_SIZE[0] / 15), core.WINDOW_SIZE[1] * 0.8)
        rect1 = Rect(coord_debut_EASY.x -2, coord_debut_EASY.y +3, 150, 65)
        rect2 = Rect(coord_debut_exit.x - 2, coord_debut_exit.y + 3, 127, 65)
        rect3 = Rect(coord_debut_MEDIUM.x - 2, coord_debut_MEDIUM.y + 3, 220, 65)
        rect4 = Rect(coord_debut_HARD.x - 2, coord_debut_HARD.y + 3, 156, 65)

        core.Draw.text((255, 255, 255), "Choose game difficulty", coord_debut_choose_game_difficulty, 100)
        core.Draw.text((255, 255, 255), "EASY", coord_debut_EASY, 65)
        core.Draw.text((255, 255, 255), "MEDIUM", coord_debut_MEDIUM, 65)
        core.Draw.text((255, 255, 255), "HARD", coord_debut_HARD, 65)
        core.Draw.text((255, 255, 255), "EXIT", coord_debut_exit, 65)


        if rect1.collidepoint(core.getMouseLocation()):
            core.Draw.rect((255, 255, 255), rect1, 5)
            if core.getMouseLeftClick():
                self.difficulty = 1
                self.map.difficulty = 1
                self.map.maxasteroid = 8
                core.memory("etat", Etat.jeu)

        if rect3.collidepoint(core.getMouseLocation()):
            core.Draw.rect((255, 255, 255), rect3, 5)
            if core.getMouseLeftClick():
                self.difficulty = 2
                self.map.difficulty = 2
                self.map.maxasteroid = 10
                core.memory("etat", Etat.jeu)

        if rect4.collidepoint(core.getMouseLocation()):
            core.Draw.rect((255, 255, 255), rect4, 5)
            if core.getMouseLeftClick():
                self.difficulty = 3
                self.map.difficulty = 3
                self.map.maxasteroid = 15
                core.memory("etat", Etat.jeu)

        if rect2.collidepoint(core.getMouseLocation()):
            core.Draw.rect((255, 255, 255), rect2, 5)
            if core.getMouseLeftClick():
                core.memory("etat", Etat.demarage)


    def show(self):
        self.map.show()

    def shoot(self):
        if core.getMouseLeftClick():
            self.map.addprojectile_player()
        for a in self.map.projectile:
            if time.time() - a.startTime > a.dureevie:
                self.map.projectile.remove(a)
        for e in self.map.enn_projectile:
            if time.time() - e.startTime > e.dureevie:
                self.map.enn_projectile.remove(e)
        self.map.addprojectile_ennemie()

    def addPlayer(self):
        p = Player()
        self.map.addjoueur(p)

    def addasteroid(self):
        for i in range(0, self.map.maxasteroid):
            self.map.addasteroid(Asteroid(), False)
        self.map.init_done = True

    def addennemie(self):
        if self.difficulty > 1:
            if core.memory("etat") == Etat.jeu:
                if self.map.ennemie is None:
                    if self.difficulty == 2:
                        if time.time() - self.starttime > 20:
                            e = Ennemie()
                            self.map.addennemie(e)
                    if self.difficulty == 3:
                        if time.time() - self.starttime > 5:
                            e = Ennemie()
                            self.map.addennemie(e)
                if self.map.ennemie is not None:
                    self.starttime = time.time()


    def sortie(self):
        self.map.joueur.on_edge()
        for a in self.map.asteroid:
            a.on_edge()
        if self.map.ennemie is not None:
            self.map.ennemie.on_edge()

    def move(self):
        if core.getKeyPressList("n"):
            for a in self.map.asteroid:
                self.map.asteroid.remove(a)
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
        for e in self.map.enn_projectile:
            e.move()
        if self.map.ennemie is not None:
            self.map.ennemie.move()


    def collision(self):
        self.map.collision()

    def score_game(self):
        self.map.calcul_score()