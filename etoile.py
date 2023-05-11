import random

import pygame
from pygame import Rect
from pygame import Vector2

import core
#t

class Etoile:
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.couleur = (255, 255, 0)
        self.orientation = Vector2(-1, 1)

    def show(self):
        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(0)
        p1 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(10)
        orientation = orientation.rotate(45)
        p2 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(90)
        p3 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(10)
        orientation = orientation.rotate(135)
        p4 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(180)
        p5 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(10)
        orientation = orientation.rotate(225)
        p6 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(270)
        p7 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(10)
        orientation = orientation.rotate(315)
        p8 = self.position + orientation

        core.Draw.polygon(self.couleur, (self.position, p1, p2, p3, p4, p5, p6, p7, p8), 2)
        core.Draw.circle(self.couleur, core.getMouseLocation(), self.size, 2)
