from enum import Enum


class Etat(Enum):
    demarage = 0,
    jeu = 1,
    game_over = 2,
    win = 3,
    choix_mode = 4
    affichage_score = 5
    pause = 6
