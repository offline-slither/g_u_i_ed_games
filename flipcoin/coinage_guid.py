from random import randint
from tkinter import *

fenetre = Tk()
rslt = StringVar()
default=PhotoImage(file="c_template.png")
head=PhotoImage(file="face.png")
tail=PhotoImage(file="dollar.png")

var_image = default


def Flip_a_coin():
	coin = randint(0, 1)
	# result = "non_lance"
	if coin == 0:
		var_image = tail
		rslt.set("pile")

	else:
		var_image = head
		rslt.set("face")
	mainbutton.configure(image=var_image)

field_label = Label(fenetre, text="pile ou face")
mainbutton = Button(fenetre, image=var_image, command=Flip_a_coin)
you_got = Label(fenetre, textvariable=rslt)



field_label.pack()
mainbutton.pack()
you_got.pack()
fenetre.mainloop()