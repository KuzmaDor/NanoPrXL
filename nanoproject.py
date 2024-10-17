import random
import games
from login import loginScreen

#getting the name of the player
name = loginScreen()

#amount of times player can act stupid before recieving angry messages
idiocracyLimit = 10

#list of angry messages players recieve for repeatedly failing to follow basic instructuions
angyMessog = {1:f'\n│ Hey {name}, how about you do something useful instead?\n', 
              2:'\n│ Are you proud of yourself?\n',
              3:f'\n│ Wow {name}, you are so funny\n',
              4:'\n│ hilarious\n',
              5:'\n│ bruh\n',
              6:'\n│ poggers\n',
              7:'\n│ Do you think your father would approve of this?\n',
              8:'\n│ Go take a shower\n',
              9:'\n│ Touch grass\n',
              10:f'\n│ Wow {name}, you must be so fun at parties\n',
              11:"\n│ That's why nobody likes you\n",
              12:f"\n│ Listen {name}, it's not that hard to follow basic instructions"
}

#list of games
games = {"Find the crossing": games.findTheCrossing, "Blackjack": games.blackJack, "Hangman": games.hangman, "Number guess": games.numberGuess}

#list of commands
commands = {"help": "Lists all available commands.", 
            "games": "Lists all availavle games.\nType the name of the game to start playing it.", 
            "quit": "Exits the application."}

#first thing the user sees after finishing logging in
print("\n╔══════════════════════╗ \
    \n║    NANO APP STORE    ║\n╚══════════════════════╝ \n\n│ Welcome to my humble store. \
\n│ Type 'help' to see the list of commands.\n")


#mainloop
while True:
    #commands
    command = input()

    if command == "" or (command.casefold() not in commands and command[0].upper() + command.lower()[1:] not in games):
        print("│ Unknown command\n")
        continue
    if command.casefold() == "help":
        print("-----------------------------------------------------------------\nHere are all available commands: \
    \n-----------------------------------------------------------------")
        for com in commands.keys(): print("-" + com + " => " + commands[com] + "\n")

    if command.casefold() == "quit":
        break

    if command.casefold() == "games":
        print("-----------------------------------------------------------------\nHere are the games i have in store: \
    \n-----------------------------------------------------------------")
        for game in games.keys(): print("-" + game)
        print("")
    
    #opening games(could've customised the arguments for the games that open, it would've taken 2.5 minutes, but i don't have to so i'm not going to)
    if command[0].upper() + command.lower()[1:] in games:
        games[command[0].upper() + command.lower()[1:]](name, idiocracyLimit, angyMessog)

