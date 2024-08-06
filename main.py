import time


#Game into

#lameintro?
hashi = "##################"


def delay_print(s):
    for c in hashi:
        print(c, end='')
        time.sleep(.25)

#Get some usr data

username = input("What name do you give yourself?\n>")
userspecies = input("Pick your species: Mouse, Toad, or Bird\n>")


while userspecies not in ["Mouse", "Toad", "Bird"]:
    userspecies = input("Dont be sassy with me, Pick your species: Mouse, Toad, or Bird\n>")

to_fight = input("What do you want to fight? (Mouse, Toad, Bird)\n>")

while to_fight not in ["Mouse", "Toad", "Bird"]:
    to_fight = input("Don't be sassy with me, What do you want to fight? (Mouse, Toad, Bird)\n>")

def win():
    print(f"Congratulations on your stunning victory {username}")
def lose():
    print(f"{username} you have lost...")
def tie():
    print(f"Whoa {username} You tied!")


if userspecies == "Mouse":
    if to_fight == "Bird":
        win()
    elif to_fight == "Toad":
        lose()
    elif to_fight == "Mouse":
        tie()
elif userspecies == "Toad":
    if to_fight == "Bird":
        lose()
    elif to_fight == "Toad":
        tie()
    elif to_fight == "Mouse":
        win()
elif userspecies == "Bird":
    if to_fight == "Bird":
        tie()
    elif to_fight == "Toad":
        win()
    elif to_fight == "Mouse":
        lose()
