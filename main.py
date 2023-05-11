import core
from partie import Partie


def setup():
    core.WINDOW_SIZE = [800, 800]
    core.fps = 30
    core.memory("partie", Partie())
    core.memory("projectile", [])
    core.memory("etoiles", [])
    core.memory("partie").addPlayer()
    core.memory("partie").addasteroid()
    core.memory("partie").addetoile()


def  run():
    core.cleanScreen()
    core.memory("partie").show()
    core.memory("partie").sortie()
    core.memory("partie").move()
    core.memory("partie").shoot()



core.main(setup, run)