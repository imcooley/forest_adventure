import sys
import os
from player import Player
import random

def player_name():
    os.system('clear')
    counter = 0
    max_attempts = 5
    while True:
        if counter != None and counter > max_attempts:
            sys.exit()
        print("What's your name")
        name = input(">> ").lower()
        try:
            if not name:
                raise ValueError                
        except ValueError:
            print(f"Please enter your name, you have {max_attempts - counter} attempts left before exiting.")
            counter += 1
        else: 
            return name

def player_race():
    os.system('clear')
    counter = 0
    max_attempts = 5
    player_races = ['dwarf', 'elf', 'human']
    while True:
        if counter != None and counter > max_attempts:
            sys.exit()
        print("What race would you like to play")

        for player_race in player_races:
            print(player_race.title())

        player_race = input(">> ").lower()
        try:
            if player_race not in player_races:
                raise ValueError                
        except ValueError:
            print(f"Please select a vaild race {max_attempts - counter} attempts left before exiting.")
            counter += 1
        else: 
            return player_race

def player_class():
    counter = 0
    max_attempts = 5
    player_classes = ['cleric', 'mage', 'warrior']
    while True:
        if counter != None and counter > max_attempts:
            sys.exit()
        print("What class would you like to play")

        for player_class in player_classes:
            print(player_class.title())

        player_class = input(">> ").lower()
        try:
            if player_class not in player_classes:
                raise ValueError                
        except ValueError:
            print(f"Pleaes select a vaild race {max_attempts - counter} attempts left before exiting.")
            counter += 1
        else: 
            return player_class

def greetings(pi):
    #print(pi.player_class)
    titles = ['mighty', 'honorable', 'kindly', 'magnanimous', 'noble']
    print(f"Welcome {random.choice(titles).title()} {pi.player_name.title()}")
    print(f"It is a pleasure to have a {pi.player_race.title()}", \
        f"{pi.player_class.title()} of such renown come to Elduwin Forst.")