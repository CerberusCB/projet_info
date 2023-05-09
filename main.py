import core
from projetinfo.partie import Partie
from projetinfo.player import Player


def setup():
    core.WINDOW_SIZE = [1920, 1080]
    core.fps = 30
    core.memory("partie", Partie())
    core.memory("player", Player())

    core.memory("partie").addPlayer()
    core.memory("partie").addasteroid()



def  run():
    core.cleanScreen()
    core.memory("partie").show()
    core.memory("partie").sortie()
    core.memory("partie").move()
    core.memory("player").shoot()



core.main(setup, run)