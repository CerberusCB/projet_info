import core
import partie
from etat import Etat
from partie import Partie


def setup():
    core.WINDOW_SIZE = [1920, 1080]
    core.fps = 30
    core.memory("partie", Partie())
    core.memory("etat", Etat.demarage)

    core.memory("partie").addPlayer()
    core.memory("partie").addasteroid()




def  run():
    core.cleanScreen()

    if core.memory("etat") == Etat.demarage:
        core.memory("partie").ecran_demarage()

    if core.memory("etat") == Etat.jeu:
        core.memory("partie").addennemie()
        core.memory("partie").show()
        core.memory("partie").sortie()
        core.memory("partie").move()
        core.memory("partie").shoot()
        core.memory("partie").score_game()
        core.memory("partie").collision()

    if core.memory("etat") == Etat.game_over:
        exit()

    if core.memory("etat") == Etat.win:
        exit()




core.main(setup, run)