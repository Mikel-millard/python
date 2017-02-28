#DND Game Simulator
#Current Functionality: Make basic character, roll for initiative

import random

#global variables
player = "Test"

#Player class
class player():
    def __init__(self):
        self

#Character class that defines what a character should look like
class character():

    #Gives parameters for character
    def __init__(self, name:str, sex:str, race:str, level:int, dex:int, strength:int):
        self.name = name
        self.sex = sex
        self.race = race
        self.level = level
        self.dex = dex
        self.strength = strength

    #Character level ups
    def levelUp(self, level_increase):
        self.level += level_increase

    #Dexterity increases
    def increaseDex(self, dex_increase):
        self.dex += dex_increase

    #Strength increases
    def increaseStrength(self, strength_increase):
        self.strength += strength_increase

    #Fucntions to return character details (will be made into a details() function later on
    def returnName(self):
        return self.name

    def returnSex(self):
        return self.sex

    def returnRace(self):
        return self.race

    def returnDex(self):
        return self.dex

    def returnStrength(self):
        return self.strength

    def returnLevel(self):
        return self.level

#Dice class to construct the numerous dice needed to play
class dice():
    def __init__(self, sides):
        self.sides = sides

    #Allows the created dice to be rolled
    def roll(self):
        return random.randint(1, self.sides)

#Makes a new character based on the information entered by the user
def makeNewCharacter():
    name = input("Please enter the name of your character: ")
    sex = input("Please enter the sex of your character: ")
    race = input("Please enter the race of your character: ")

    #This section ensures all numbers are entered as numbers
    while True:
        try:
            level = int(input("Please enter the level of your character (numerically): "))
        except ValueError:
            print("Character level should be a number.")
        else:
            break
    while True:
        try:
            dex = int(input("Please enter your character's dexterity (numerically): "))
        except ValueError:
            print("Character dexterity should be a number.")
        else:
            break
    while True:
        try:
            strength = int(input("Please enter your character's strength (numerically): "))
        except ValueError:
            print("Character strength should be a number.")
        else:
            break

    #Creates the new character and returns it
    new_character = character(name, sex, race, level, dex, strength)
    return new_character

#Allows the user to roll for initiative
def initiative(player = character): #Currently not working as intended
    d20 = dice(20)
    initiative_roll = d20.roll()
    return initiative_roll

#Creates a new battle
class battle():
    def __init__(self, monsters, players, encounter_level):
        self.monsters = monsters
        self.players = players
        self.encounter_level = encounter_level

def createNewBattle(self, monsters, players, encounter_level):
    battle(monsters, players, encounter_level)

#Fights a battle that was selected
def fightBattle(battle):
    battle = "battle"

#Makes interactive commands
def commands():

    #User needs to be able to create character, create encounter, roll initiative, and fight an
    #encounter, we need a while loop for entering the commands they want to do, an array of
    #the different commands available, and a way to exit the loop.
    commands_array = ["Create New Character", "Create New Battle", "Roll Initiative", "Fight Battle", "Exit"]
    print("\nCommands:")
    for i in range(len(commands_array)):
        print(commands_array[i])
    command = input("Please enter a command: ")
    print("Chosen command:", command)
    while (command != "Exit"):
        if (command == "Create New Character"):
            makeNewCharacter()
        elif (command == "Create New Battle"):
            createNewBattle()
        elif (command == "Roll Initiative"):
            player_for_ini = input("Which player would you like to roll for?")
            print(initiative(player_for_ini))
            command = "Exit"

        elif (command == "Fight Battle"):
            battle = input("Which battle would you like to fight?")
            fightBattle(battle)
        elif (command == "Exit"):
            print("Thanks for playing")
        else:
            print("Incorrect command was entered.")
            command = input("Please look at the commands again and enter a correct command. ")



#Main method, currently tests some of the code ive writrtgn
def main():
    player_one = makeNewCharacter()
    print("Name: ", player_one.returnName())
    print("Race: ", player_one.returnRace())
    print("Level: ", player_one.returnLevel())
    print("Dexterity: ", player_one.returnDex())
    print("Strength: ", player_one.returnStrength())
    print("Your initiative is: ", initiative(player_one))
    player_test = "Player"
    global player
    print(player)
    print(player_test)
    print(initiative())
    commands()

#Runs the main method
main()