from random import randint

def Flipcoin(howmuch=1):
	if howmuch == 1:
		coin = randint(0, 1)
		# result = "non_lance"
		if coin == 0:
			result = "pile"
		else:
			result = "face"
		print(result)
	else:
		pilecount = 0
		facecount = 0
		for flip in range(0,howmuch):
			coin = randint(0, 1)
			if coin == 0:
				print("pile")
				pilecount += 1
			else:
				print("face")
				facecount += 1
		print(f"pile : {pilecount}, face : {facecount}")


# Flipcoin()
# le nombre-argument entré permet d'avoir plusieur jet puis un total et comparatif, jette juste la piece et retourn la valeur si howmuch = 1