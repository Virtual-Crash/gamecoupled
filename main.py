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

stats = {
    "Mouse": {
        "attack":10,
        "defense":10,
        "hp":10
    },
    "Toad": {
        "attack":10,
        "defense":10,
        "hp":10
    },
    "Bird": {
        "attack":10,
        "defense":10,
        "hp":10
    }
}

def do_damage(attack, defense):
    damage_dealt = attack - (defense * 0.5)
    if damage_dealt > 0:
        return damage_dealt
    else:
        return 0

def take_damage(enemy_stats, damage_dealt):
    remaining_hp = enemy_stats["hp"] - damage_dealt
    if remaining_hp > 0:
        enemy_stats["hp"] = remaining_hp
    else:
        enemy_stats["hp"] = 0
    return enemy_stats

def battle_with_stats(user_species, to_fight):
    user_stats = stats[user_species]
    enemy_stats = stats[to_fight]
    multiplier = 1 # default multiplier

    if user_species == "Mouse":
        if to_fight == "Bird":
            multiplier = 2
        elif to_fight == "Toad":
            multiplier = 0.5
    elif user_species == "Toad":
        if to_fight == "Bird":
            multiplier = 0.5
        elif to_fight == "Mouse":
            multiplier = 2
    elif user_species == "Bird":
        if to_fight == "Toad":
            multiplier = 2
        elif to_fight == "Mouse":
            multiplier = 0.5
    damage_dealt = do_damage(user_stats["attack"] * multiplier, enemy_stats["defense"])
    enemy_stats = take_damage(enemy_stats, damage_dealt)
    print(f'You have done {damage_dealt}, the enemy has {enemy_stats["hp"]} hp remaining')
    
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
            
battle_with_stats(user_species, to_fight)
