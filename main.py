import time


#Game into

#lameintro?
hashi = "##################"


def delay_print(s):
    for c in hashi:
        print(c, end='')
        time.sleep(.25)

#Get some usr data

username = input("What name do you give yourself? ")
userspecies = input("Pick your species: Mouse, Toad, or Bird")


while userspecies != "Mouse" or "Toad" or "Bird":
    userspecies = input("Dont be sassy with me, choose your species: Mouse, Toad, or Bird")

