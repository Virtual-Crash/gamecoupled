def pick_species (species) :
    species = input("Pick your species: Mouse, Toad, or Bird:\n>")

    if species == "Mouse" :
        print("The bravest of creatures, good choice")
    elif species == "Bird" :
        print("Your speed and quick thinking skills are above all others")
    elif species == "Toad" :
        print("The strong and study, are revered by all")
    else :
        species = input("Dont be sassy with me, choose your species: Mouse, Toad, or Bird\n>")
        
    return species