from random import randint
from tkinter import *
# global js_core,ai_score
# preset variable
# -----------------------------------------------------------
js_core = 0
ai_score = 0

J1choice = "default"
AIchoice = "default"
goodluck = False
badluck = False


fenetre = Tk()

image_pi=PhotoImage(file="pierre.png")
image_pa=PhotoImage(file="papier.png")
image_ci=PhotoImage(file="ciseaux.png")


def Thencompare(param):
	AIchoice = randint(0, 2)
	if AIchoice == 1:
		AIchoice = "pierre"
	elif AIchoice == 2:
		AIchoice = "papier"
	else:
		AIchoice = "ciseaux"
	golden = False
	unesur4 = randint(1, 5)
	if unesur4 == 3:
		golden = True
	
	# if un_ou_autre == 1:
	# 	goodluck = True                if i didn't cheat using "command" in the 3 radio buttons
	# 	badluck = False
	
	# elif un_ou_autre == 2:
	# 	oodluck = Fa
	# 	badluck = False

	# elif un_ou_autre == 3:
	# 	goodluck = False
	# 	badluck = True
	
	# print(f"l'ordi joue {AIchoice}")
	J1choice = param
	# print(J1choice)
	global js_core
	global ai_score
	global promptinit
	if J1choice == AIchoice:
		promptinit.set(f"égalité par {J1choice}")
	elif J1choice == "pierre":
		if AIchoice == "ciseaux" and badluck == True and golden == True:
			promptinit.set("l'ordi bat votre pierre avec papier")
		elif AIchoice == "ciseaux":
			promptinit.set(f"vous avez gagné par {J1choice} contre {AIchoice}")
			js_core += 1
		elif AIchoice == "papier" and goodluck == True and golden == True:
			promptinit.set("vous avez gagné par pierre contre ciseaux")
			js_core += 1
		elif AIchoice == "papier":
			promptinit.set(f"l'ordi bat votre {J1choice} avec {AIchoice}")
			ai_score += 1
	elif J1choice == "papier":
		if AIchoice == "pierre" and badluck == True and golden == True:
			promptinit.set("l'ordi bat votre papier avec ciseaux")
		elif AIchoice == "pierre":
			promptinit.set(f"vous avez gagné par {J1choice} contre {AIchoice}")
			js_core += 1
		elif AIchoice == "ciseaux" and goodluck == True and golden == True:
			promptinit.set("vous avez gagné par papier contre pierre")
			js_core += 1
		elif AIchoice == "ciseaux":
			promptinit.set(f"l'ordi bat votre {J1choice} avec {AIchoice}")
			ai_score += 1
	elif J1choice == "ciseaux":
		if AIchoice == "papier" and badluck == True and golden == True:
			promptinit.set("l'ordi bat votre ciseaux avec pierre")
		elif AIchoice == "papier":
			promptinit.set(f"vous avez gagné par {J1choice} contre {AIchoice}")
			js_core += 1
		elif AIchoice == "pierre" and goodluck == True and golden == True:
			promptinit.set("vous avez gagné par ciseaux contre papier")
			js_core += 1
		elif AIchoice == "pierre":
			promptinit.set(f"l'ordi bat votre {J1choice} avec {AIchoice}")
			ai_score += 1
	else:
		promptinit.set("vous avez entré un input incorrect donc vous perdez un point")
		# shoudn't happen in the GUI
		ai_score += 1
	# retours.update()
	sc1.set(f"vore score : ={js_core}")
	sc2.set(f"l'ordi : ={ai_score}")
	# print("goodluck")
	# print(goodluck)
	# print("----")
	# print("badluck")
	# print(badluck)
	# print("----")
	# print("golden")
	# print(golden)
	# print("----")
	# print("un_ou_autre")
	# print(un_ou_autre)
	# votre_score.update()
	# pc_score.update()
	# print(f"votre score est de {js_core} contre {ai_score}")
	# fenetre.update()


def Pierre():
	J1choice = "pierre"
	# print(f"joueur lance {J1choice}")
	Thencompare(J1choice)

def Papier():
	J1choice = "papier"
	# print(f"joueur lance {J1choice}")
	Thencompare(J1choice)

def Ciseaux():
	J1choice = "ciseaux"
	# print(f"joueur lance {J1choice}")
	Thencompare(J1choice)
def SetDiff1():
	global goodluck
	global badluck
	goodluck = True
	badluck = False
def SetDiff2():
	global goodluck
	global badluck
	goodluck = False
	badluck = False
def SetDiff3():
	global goodluck
	global badluck
	goodluck = False
	badluck = True

# -----------------------------------------------------------

base_cadre = Frame(fenetre,borderwidth=1)
cadre1 = Frame(fenetre, width=700, height=80,borderwidth=1)
radio_cadre = Frame(fenetre, borderwidth=1, background='teal')
cadre2 = Frame(fenetre, width=2000, height=100,borderwidth=1)
PPC_center = Frame(radio_cadre,borderwidth=1,background='purple')
choice_center = Frame(cadre1,borderwidth=1,background='teal')
field_label = Label(base_cadre, text="Bonjour et bienvenue dans pierre papier ciseaux")
field_label2 = Label(base_cadre, text="choisisez une difficulté")
field_labelinstru = Label(cadre1, text="choissisez votre mouvement")
bouton_quitter = Button(cadre2, text="Quitter", command=fenetre.quit)
scorezone = Frame(fenetre,borderwidth=1)
textzone = Frame(fenetre,borderwidth=1)

promptinit = StringVar()

retours = Label(textzone, textvariable=promptinit)

sc1 = StringVar()
votre_score = Label(scorezone, textvariable=sc1)
sc2 = StringVar()
pc_score = Label(scorezone, textvariable=sc2)

# bouton_image = Button(cadre1, image=img_pic, command=fenetre.quit)

bouton_pi = Button(choice_center, image=image_pi, command=Pierre)
bouton_pa = Button(choice_center, image=image_pa, command=Papier)
bouton_ci = Button(choice_center, image=image_ci, command=Ciseaux)


# variable_textuelle = StringVar()
# ligne_texte = Entry(base_cadre, textvariable=variable_textuelle, width=30)

# on_off = IntVar()
# checky_breeky = Checkbutton(base_cadre, text="cochez si vous voulez", variable=on_off)
# on peut interroger la variable du checker a traver on_off.get()
# Notez qu'à l'instar d'un bouton, vous pouvez lier la case à cocher à une commande qui sera appelée quand son état change.

un_ou_autre = IntVar()
un_ou_autre.set(2)


choix_1 = Radiobutton(PPC_center, text ="Facile",variable =un_ou_autre, value=1, indicatoron=0, command=SetDiff1)
choix_2 = Radiobutton(PPC_center, text ="Normal",variable =un_ou_autre, value=2, indicatoron=0, command=SetDiff2)
choix_3 = Radiobutton(PPC_center, text ="Difficile",variable =un_ou_autre, value=3, indicatoron=0, command=SetDiff3)

# choix_4 = Radiobutton(base_cadre, text ="Maitre",variable =un_ou_autre, value="4")

# Pour récupérer la valeur associée au bouton actuellement sélectionné, interrogez la variable :
# un_ou_autre.get()

# button.invoke()


base_cadre.pack(fill=BOTH)
radio_cadre.pack(fill=BOTH)
cadre1.pack(fill=BOTH)
cadre2.pack(side=BOTTOM)
field_label.pack()
field_label2.pack()
# ligne_texte.pack() dis
# checky_breeky.pack()
field_labelinstru.pack()
choice_center.pack(anchor=CENTER)
choix_1.pack(side=LEFT)
choix_2.pack(side=LEFT)
choix_3.pack(side=LEFT)
# choix_1.grid(row=1, column=1)
# choix_2.grid(row=2, column=1)
# choix_3.grid(row=3, column=1)
PPC_center.pack(anchor=CENTER)
bouton_pi.pack(side=LEFT)
bouton_pa.pack(side=LEFT)
bouton_ci.pack(side=LEFT)
bouton_pi.pack(side=LEFT)
# bouton_image.pack()
# choix_4.pack() unl
# liste1.pack()
textzone.pack(anchor=CENTER)
retours.pack()
scorezone.pack(fill=BOTH, side=BOTTOM)
votre_score.pack(side=LEFT)
pc_score.pack(side=RIGHT)
bouton_quitter.pack()
fenetre.mainloop()