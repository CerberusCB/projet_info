import core
import partie
from etat import Etat
from partie import Partie


def setup():
    core.fullscreen = True
    core.WINDOW_SIZE = [1900, 1000]
    core.fps = 30
    core.memory("partie", Partie())
    core.memory("etat", Etat.demarage)

    core.memory("partie").addPlayer()





def  run():
    core.cleanScreen()

    if core.memory("etat") == Etat.demarage:
        core.memory("partie").ecran_demarage()

    if core.memory("etat") == Etat.choix_mode:
        core.memory("partie").ecran_choix_mode()
        core.memory("partie").reset_partie()


    if (core.memory("etat") == Etat.jeu):
        core.memory("partie").addasteroid()
        core.memory("partie").addennemie()
        core.memory("partie").addbonus()
        core.memory("partie").show()
        core.memory("partie").sortie()
        core.memory("partie").move()
        core.memory("partie").shoot()
        core.memory("partie").score_game()
        core.memory("partie").collision()
        core.memory("partie").gestion_pause()

    if core.memory("etat") == Etat.game_over:
        core.memory("partie").ecran_game_over()

    if core.memory("etat") == Etat.win:
        core.memory("partie").ecran_win()

    if core.memory("etat") == Etat.affichage_score:
        core.memory("partie").ecran_affichage_score()

    if core.memory("etat") == Etat.pause:
        core.memory("partie").ecran_pause()

core.main(setup, run)