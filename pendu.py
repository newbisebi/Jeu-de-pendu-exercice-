# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:44:23 2018

@author: sebastien
"""

from fonctions import *
from donnees import *

init_scores()
joueur = choix_utilisateur()
mot_a_trouver = selection_mot()
jouer(mot_a_trouver, tentatives, joueur)