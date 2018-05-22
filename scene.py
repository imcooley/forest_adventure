paths = ['left', 'middle', 'right']
middle_path_creatures = ['dryad', 'witch', 'centaur']

# Map
"""
--------
     | S |
     / | \
| L1 | M1 | R1 |
   | X |  X |
| L2 | M2 | R2 |



"""

def start_path(pi):
    #os.system('clear')
    print("\nYou find yourself leisurely walking through the woods when the path splits three ways.")
    print("Which path do you take?")
    for path in paths:
        print(path.capitalize())

    path = input("> ").lower()
    if path == "middle":
        get_middle_path(pi)

def get_middle_path(pi):
    #os.system('clear')
    print("\nTaking the middle ground you walk forward.")
    print("\nAt first this seem like the rest of the forest. Ah, how peaceful!")
    print("\n\n\n\t\t\t***LEAVES RUSTLE***")
    print("\n\n\nYou are met by a beautiful dryad, an evil looking witch, and a massive centuar.")
    print("\nWitch:Three paths before you, three behind.")
    print("Dryad: Don't be mislead, follow your head.")
    print("Centuar: For if you don't you will surely will be dead.")

    print("They seem to want you pick one of them, though the choice seems dubious.")
    print("Who do you pick?")
    for middle_path_creature in middle_path_creatures:
        print(middle_path_creature.capitalize())

    middle_path_creature = input("> ").lower
    # if middle_path_creature in 
    # print(middle_path_creature)
    # print(pi.player_race)
    # if middle_path_creature == "dryad" and pi.player_race == "human":
    #     print(f"Well a good choice one would think, but little did you know this Dryad holds a grudge to all {pi.player_race}")
    #     print("The Dryad pulls a bow out and impales you through the heart. Too bad...")
    #     exit(0)
    # elif middle_path_creature == "dryad" and pi.player_race == "elf":
    #     print('she loves you')
    #     print('you are free to go')
    # elif middle_path_creature == "dryad" and pi.player_race == "dwarf":
    #     print("vile short one")
    #     print("trys to shoot you")
    # else:
    #     exit(0)