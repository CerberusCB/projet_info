import core
from partie import Partie


def setup():
    core.WINDOW_SIZE = [1080, 1080]
    core.fps = 30
    core.memory("partie", Partie())

    core.memory("partie").addPlayer()
    core.memory("partie").addasteroid()




def  run():
    core.cleanScreen()
    core.memory("partie").show()
    core.memory("partie").sortie()
    core.memory("partie").move()
    core.memory("partie").shoot()
    core.memory("partie").collision()
    core.memory("partie").score_game()




core.main(setup, run)