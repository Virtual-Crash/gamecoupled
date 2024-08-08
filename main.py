import time
from species import pick_species

#Game into

#lameintro?
hashi = "##################"


def delay_print(s):
    for c in hashi:
        print(c, end='')
        time.sleep(.25)

#Get some usr data

username = input("What name do you give yourself?\n>")
tmp_species = ""

user_species = pick_species(tmp_species)

to_fight = input("What do you want to fight? (Mouse, Toad, Bird)\n>")

while to_fight not in ["Mouse", "Toad", "Bird"]:
    to_fight = input("Don't be sassy with me, What do you want to fight? (Mouse, Toad, Bird)\n>")

def win():
    print(f"Congratulations on your stunning victory {username}")
def lose():
    print(f"{username} you have lost...")
def tie():
    print(f"Whoa {username} You tied!")

def battle(user_species, to_fight):
    #can get here, but missing user species
    print(user_species + " vs " + to_fight)
    if user_species == "Mouse":
        print('1')
        if to_fight == "Bird":
            win()
        elif to_fight == "Toad":
            lose()
        elif to_fight == "Mouse":
            tie()
    elif user_species == "Toad":
        if to_fight == "Bird":
            lose()
        elif to_fight == "Toad":
            tie()
        elif to_fight == "Mouse":
            win()
    elif user_species == "Bird":
        if to_fight == "Bird":
            tie()
        elif to_fight == "Toad":
            win()
        elif to_fight == "Mouse":
            lose()
            
battle(user_species, to_fight)
