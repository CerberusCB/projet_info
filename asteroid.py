import random

from pygame import Vector2

import core
#random.randint(0, core.WINDOW_SIZE[0]), random.randint(0, core.WINDOW_SIZE[1])

class Asteroid:
    def __init__(self, s=50):
        self.size = s
        self.vmax = 7
        self.accmax = 2
        b = random.randint(0, 3)
        if b == 0:
            self.position = Vector2(0, random.uniform(0, core.WINDOW_SIZE[1]))
        if b == 1:
            self.position = Vector2(random.uniform(0, core.WINDOW_SIZE[0]), 0)
        if b == 2:
            self.position = Vector2(core.WINDOW_SIZE[0], random.uniform(0, core.WINDOW_SIZE[1]))
        if b == 3:
            self.position = Vector2(random.uniform(0, core.WINDOW_SIZE[0]), core.WINDOW_SIZE[1])
        self.acceleration = Vector2(random.uniform(0, 0), random.uniform(0, 0))
        self.speed = Vector2(random.uniform(-7, 7), random.uniform(-7, 7))
        self.couleur = (255, 55, 55)

        self.p1 = Vector2(random.randint((self.size)/2 - 3, (self.size)/2 + 5))
        self.p1 = self.p1.rotate(0)
        self.p2 = Vector2(random.randint((self.size)/2 - 3, (self.size)/2 + 5))
        self.p2 = self.p2.rotate(45)
        self.p3 = Vector2(random.randint((self.size)/2 - 3, (self.size)/2 + 5))
        self.p3 = self.p3.rotate(90)
        self.p4 = Vector2(random.randint((self.size)/2 - 3, (self.size)/2 + 5))
        self.p4 = self.p4.rotate(135)
        self.p5 = Vector2(random.randint((self.size)/2 - 3, (self.size)/2 + 5))
        self.p5 = self.p5.rotate(180)
        self.p6 = Vector2(random.randint((self.size)/2 - 3, (self.size)/2 + 5))
        self.p6 = self.p6.rotate(225)
        self.p7 = Vector2(random.randint((self.size)/2 - 3, (self.size)/2 + 5))
        self.p7 = self.p7.rotate(270)
        self.p8 = Vector2(random.randint((self.size)/2 - 3, (self.size)/2 + 5))
        self.p8 = self.p8.rotate(315)


    def show(self):
        #core.Draw.circle(self.couleur, self.position, self.size)
        p1 = self.p1 + self.position
        p2 = self.p2 + self.position
        p3 = self.p3 + self.position
        p4 = self.p4 + self.position
        p5 = self.p5 + self.position
        p6 = self.p6 + self.position
        p7 = self.p7 + self.position
        p8 = self.p8 + self.position

        core.Draw.polygon(self.couleur, (self.position, p1, p2, p3, p4, p5, p6, p7, p8), 2)

    def move(self):
        self.speed += self.acceleration
        self.position += self.speed

        if self.speed.length() > self.vmax:
            self.speed.scale_to_length(self.vmax)

        if self.acceleration.length() > self.accmax:
            self.acceleration.scale_to_length(self.accmax)


    def on_edge(self):
        if self.position.x < 0:
            self.position.x = core.WINDOW_SIZE[0]
        if self.position.x > core.WINDOW_SIZE[0]:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = core.WINDOW_SIZE[1]
        if self.position.y > core.WINDOW_SIZE[1]:
            self.position.y = 0

    def collision(self):
        pass
