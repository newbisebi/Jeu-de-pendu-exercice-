# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:44:48 2018

@author: sebastien
"""
import random
import pickle
from donnees import *
from collections import defaultdict

def init_scores():
    try:
        open("scores","rb")
    except FileNotFoundError:
        scores = defaultdict(list)
        scores["init"] = [0]
        with open("scores","wb") as fichier_scores:
            pickler = pickle.Pickler(fichier_scores)
            pickler.dump(scores)
        print("Nouveau fichier de scores créé !")
        
def get_scores():
    with open("scores","rb") as fichier_scores:
        pickler = pickle.Unpickler(fichier_scores)
        scores = pickler.load()
    return scores

def write_score(scores):
    with open("scores","wb") as fichier_scores:
        pickler = pickle.Pickler(fichier_scores)
        pickler.dump(scores)
      
def choix_utilisateur():
    nom = input("Entrez le nom du joueur")
    return nom.capitalize()

def ajouter_score(joueur, nouveau_score):
    scores = get_scores()
    scores[joueur].append(nouveau_score)
    write_score(scores)
    
def afficher_score_joueur(joueur):
    scores = get_scores()[joueur]
    scores = ", ".join([str(score) for score in scores])
    print("Voici la liste de vos scores : ", scores)
    
       
def format_mot(mot):
    mot = mot.lower()
    mot = mot.replace("é","e")
    mot = mot.replace("è","e")
    mot = mot.replace("ê","e")
    mot = mot.replace("ë","e")
    mot = mot.replace("î","i")
    mot = mot.replace("ï","i")
    return mot

def selection_mot():
    mot = random.choice(liste_mots) 
    return format_mot(mot)

def afficher_mot(mot, lettres_trouvees):
    """
    Affiche le mot recherché en remplaçant les lettres non trouvées
    par des *
    """
    lettres_non_trouvees = [lettre for lettre in mot if lettre not in lettres_trouvees]
    for lettre in lettres_non_trouvees:
        mot = mot.replace(lettre, '*')
    print(mot)
    
def compare(mot_a_trouver, lettres_trouvees):
    """
    Compare le jeu de lettre de deux mots
    eg. "aabbcc" égale "cba" ==> true
    """
    lettres_a_trouver = sorted(set(list(mot_a_trouver)))
    lettres_trouvees = sorted(set(lettres_trouvees))
    if lettres_a_trouver == lettres_trouvees: return True ; return False

def jouer(mot, tentatives, joueur): 
    print("C'est parti ! Vous avez droit à {} tentatives".format(tentatives))
    lettres_trouvees = []
    #On boucle autant de fois que de tentative
    while tentatives > 0:
        nouvelle_lettre = input("Choisissez une lettre de l'alphabet").lower()
        
        #On vérifie qu'une seule lettre est rentrée
        if len(nouvelle_lettre) != 1:
            print("Veuillez rentrer une seule lettre")
            continue
    
        #Actions si la lettre est bonne
        if nouvelle_lettre in mot:
            lettres_trouvees.append(nouvelle_lettre)
            if compare(mot, lettres_trouvees):
                print ("Bravo !")
                ajouter_score(joueur, tentatives)
                break
            
        #Actions si la lettre n'est pas bonne
        else:
            tentatives-=1
        
        #Actions dans tous les cas : 
        afficher_mot(mot, lettres_trouvees)
        print("Il vous reste {} tentatives".format(tentatives))
        
    print("C'est terminé ! Le mot à trouver était {}".format(mot))
    if tentatives == 0:
        ajouter_score(joueur, 0)
    afficher_score_joueur(joueur)