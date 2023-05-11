import random

import pygame
from pygame import Rect
from pygame import Vector2

import core


class Etoile:
    def __init__(self):
        self.position = Vector2(random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1]))
        self.couleur = (255, 255, 0)
        self.orientation = Vector2(0, 1)
        self.size = 2

    def show(self):
        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(36)
        p1 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(10)
        orientation = orientation.rotate(72)
        p2 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(108)
        p3 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(10)
        orientation = orientation.rotate(144)
        p4 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(180)
        p5 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(10)
        orientation = orientation.rotate(216)
        p6 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(252)
        p7 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(10)
        orientation = orientation.rotate(288)
        p8 = self.position + orientation

        orientation = Vector2(self.orientation)
        orientation.scale_to_length(20)
        orientation = orientation.rotate(324)
        p9 = self.position + orientation


        core.Draw.polygon(self.couleur, (self.position, p1,p2,p3,p4,p5,p6,p7,p8,p9), self.size)
        #core.Draw.circle(self.couleur, core.getMouseLocation(), self.size, 2)
