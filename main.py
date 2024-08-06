import time
import sys
from species import pick_species

sys.path.insert(0, '/charbuild')





#Game into

#lameintro?
hashi = "##################"


def delay_print(s):
    for c in hashi:
        print(c, end='')
        time.sleep(.25)

#Get some usr data

user_name = input("What name do you give yourself? ")
user_species = ""

pick_species(user_species)