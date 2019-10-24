from random import choice
from donees import *


def Chose_word_within():  # work
    randword = choice(liste_mots)
    # print(randword)
    return randword


def Goodguess(arg):
    yes = list(arg)
    # print(yes)
    return yes


again = "y"

print("bienvenue dans le pendu")
while again == "y":
    win = False
    chance = 8
    word = Chose_word_within()
    # print(word)
    listed_word = Goodguess(word)
    # print ("*" * len(listed_word))
    # p_answer = input("proposer une lettre ou devinez le mot")
    validated_letter = []
    # displayed_word = ""
    while chance >= 1 and win != True:
        displayed_word = ""
        for each in listed_word:
            if each in validated_letter:
                displayed_word += each
                if displayed_word == word:
                    print("félicitation vous avez gagné")
                    win = True
                    break
            else:
                displayed_word += "*"
        print(displayed_word)
        print("proposer une lettre ou devinez le mot")
        p_answer = input("")
        if len(p_answer) == 1:
            if p_answer in validated_letter:
                print("vous l'avez déja dit")
            elif p_answer in listed_word:
                print("vous avez bon")
                validated_letter.append(p_answer)
            else:
                print("faux, vous perdez une chance")
                chance -= 1
                print(chance)
        elif len(p_answer) > 1:
            # logic de comparaison du mot
            if str(p_answer) == str(word):
                print("félicitation vous avez gagné")
                win = True
                break
            else:
                print(
                    "ce n'est pas le bon mot ou vous l'avez mal écrit vous perdez une chance")
                # print(f"vous avez entré {p_answer} la réponse etais {word}")
                chance -= 1
        else:
            print("vous avez entré un imput incorect ou invalide , re-essayez")
    if win == True:
        print("-----------------")
    else:
        print(f"vous avez perdu le mot etais {word}")
    print("envie de rejouer y/n")
    again = input("")
