import core
from projetinfo.map import Map
from projetinfo.partie import Partie
from projetinfo.player import Player
#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


def setup():
    core.WINDOW_SIZE = [800, 800]
    core.fps = 30
    core.memory("partie", Partie())
    core.memory("projectile", [])

    core.memory("partie").addPlayer()
    core.memory("partie").addasteroid()



def  run():
    core.cleanScreen()
    core.memory("partie").show()
    core.memory("partie").sortie()
    core.memory("partie").move()
    core.memory("partie").shoot()



core.main(setup, run)