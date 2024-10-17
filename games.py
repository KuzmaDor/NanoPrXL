import random
from threading import Timer
import re
from string import ascii_letters

def findTheCrossing(name, idiocracyLimit, angyMessog):
    idiocracyCounter = 0
    answerExplainMsg = ""
    print("\n╔═════════════════════════╗ \
    \n║    FIND THE CROSSING    ║\n╚═════════════════════════╝ \n")
    print("│ Welcome to this battle of wits! You are about to \
have a race with the computer to see who can calculate\n│ the point of intersection of two lines faster. Think you \
are faster than the machine?\n")
    
    print(f"\n│ Need help figuring out how to play?(y/n) ", end="")
    #giving player the option to get the explanation
    while True:

        help = input()
        if help.casefold() == "y":
            with open("crossingrules.txt", "r") as rules:
                print(f"\n{rules.read()}")
            break
        elif help.casefold() == "n":
            print("\n│ Ok, good luck then")
            break
        else:
            idiocracyCounter+=1
            if idiocracyCounter>=idiocracyLimit: print(angyMessog[random.randint(1, len(angyMessog))])
            else: print(f"\n│ {name} just type 'y' or 'n', i'm not asking for much\n")

    print("\n│ Choose your difficulty: \
    \n│ 1 = smallest numbers, slowest computer \
    \n│ 2 = larger numbers, faster computer \
    \n│ 3 = largest numbers, fastest computer \
    \n\n")

    #choosing difficulty
    while True:
        try:
            diff = int(input("│ Your choise: "))
            difficulty = {1:(-10, 10, 17, 35), 2:(-50, 75, 12, 25), 3:(-1000, 1100, 7, 15)}
            #this looks stupid but it's the only way(that i know of)
            point1 = (random.randint(difficulty[diff][0], difficulty[diff][1]), random.randint(difficulty[diff][0], difficulty[diff][1]))
            point2 = (random.randint(difficulty[diff][0], difficulty[diff][1]), random.randint(difficulty[diff][0], difficulty[diff][1]))
            point3 = (random.randint(difficulty[diff][0], difficulty[diff][1]), random.randint(difficulty[diff][0], difficulty[diff][1]))
            point4 = (random.randint(difficulty[diff][0], difficulty[diff][1]), random.randint(difficulty[diff][0], difficulty[diff][1]))
            break
        except:
            idiocracyCounter+=1
            if idiocracyCounter>=idiocracyLimit: print(angyMessog[random.randint(1, len(angyMessog))])
            else: print("\n│ bruh\n")

    #solving the math, "the computer's answer"
    try:
        a1 = (point2[1] - point1[1]) / (point2[0] - point1[0])
        b1 = point1[1] - a1 * point1[0]
        a2 = (point4[1] - point3[1]) / (point4[0] - point3[0])
        b2 = point3[1] - a2 * point3[0]
        x = (b2 - b1) / (a1 - a2)
        y = a1 * x + b1
    except ZeroDivisionError:
        correctAnswer = 0
        answerExplainMsg = " because you can't divide by zero."
    else:
        correctAnswer = (round(x), round(y))
        if a1 == a2:
            correctAnswer = 0
            answerExplainMsg = " because the lines are parallel"

    print(f"\n│ Alright let's begin.\n\n~~~~~~epic~transition~~~~~~\n\
\n│ There are two lines: 'a' and 'b'.\n│ Line 'a' has two points: A{point1} and B{point2}.\n│ \
Line 'b' also has two points: C{point3} and D{point4}.\n│ Give the coordinates of the intersection and round them to the nearest digit")
    
    print(f"\n*computer* This town isn't big enough for two math wizards, {name}. Prepare to be destroyed!")

    #timed input of the player's answer
    timeout = random.randint(difficulty[diff][2], difficulty[diff][3])
    t = Timer(timeout, print, [f"\n*computer* I got it!\n\n│ Ok, computer got it first, \
just submit what you currently have."])
    t.start()
    answer = input("\n│ Quick! Type in your answer:\n\n")
    t.cancel()

    #getting the useful info out of the answer
    answerDigits = re.findall(r'[-+]?\d+', answer)
    
    #checking if the answer is correct
    try:
        if correctAnswer == 0:
            if answerDigits == correctAnswer:
                print(f"\n│ ~~Hooray, you're a nerd~~ , the correct answer is indeed {correctAnswer}{answerExplainMsg}\n")
            elif answerDigits != correctAnswer:
                print(f"\n│ ~~Wrong! idiot!~~ The answer is {correctAnswer}{answerExplainMsg}\n")
        elif int(answerDigits[0]) == round(x) and int(answerDigits[1]) == round(y):
            print(f"\n│ ~~Hooray, you're a nerd~~ , the correct answer is indeed {correctAnswer}\n")
        elif len(answerDigits) < 2:
            print(f"\n│ ~~You call that an answer?~~ Well it ain't one. Take it seriously next time. \
\n│ Anyway the correct answer was {correctAnswer}\n")
        else:
            print(f"\n│ ~~Wrong! idiot!~~ The answer is {correctAnswer}\n")
    except:
        print(f"\n│ ~~No answer, bummer~~\n│ Anyway the correct answer was {correctAnswer}\n")

    print("│ Alright, thanks for playing 'Find the crossing', what do you want to do next? \
\n│ (Type 'help' to see the list of commands)\n")

def blackJack(name, idiocracyLimit, angyMessog):
    idiocracyCounter = 0
    #defining the deck
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }

    #making the deck
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)


    #calculating the value of the hand
    def handValue(hand):
        value = 0
        ace_count = 0
        for card in hand:
            value += values[card[0]]
            if card[0] == 'Ace':
                ace_count += 1
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value

    #showing cards + value
    def showHand(hand, name):
        print(f"\n│ {name}'s Hand: ", end="")
        for card in hand:
            print(f'{card[0]} of {card[1]}', end=", ")
        print(f"Value: {handValue(hand)}")

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    print("\n╔═════════════════╗ \
    \n║    BLACKJACK    ║\n╚═════════════════╝ \n")

    print("│ Welcome to the game of jacking and blacking. \
\n│ Bet responsibly, don't cause trouble and listen to your parents.")
    
    print(f"\n│ Need help figuring out how to play?(y/n) ", end="")

    #giving player the option to get the explanation of how the game works
    while True:
        help = input()
        if help.casefold() == "y":
            with open("blackjackrules.txt", "r") as rules:
                print(f"\n{rules.read()}")
                print("\n│ *Dealer* Enough talking, sit down and play.")
            break
        elif help.casefold() == "n":
            print("\n│ Ok, good luck")
            break
        else:
            idiocracyCounter+=1
            if idiocracyCounter>=idiocracyLimit: print(angyMessog[random.randint(1, len(angyMessog))])
            else: print(f"\n│ {name} just type 'y' or 'n', i'm not asking for much\n")

    print("\n~~~~~~epic~transition~~~~~~")
    showHand(player_hand, name)
    print(f"│ Dealer's Hand: {dealer_hand[0][0]} of {dealer_hand[0][1]}, [Hidden]")
    
    #player's turn
    while True:
        choice = input("\n│ Do you want to (h)it or (s)tand? ").casefold()
        if choice == 'h':
            player_hand.append(deck.pop())
            showHand(player_hand, name)
            if handValue(player_hand) > 21:
                print("│ ~~Busted! Dealer wins, womp womp, go cry~~")
                print("\n│ Alright, thanks for playing Blackjack, what do you want to do next? \
\n│ (Type 'help' to see the list of commands)\n")
                return
        elif choice == 's':
            break
        else:
            print("\n│ Invalid choise")
    
    #dealer's turn
    while handValue(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    #dealer's final hand
    showHand(dealer_hand, 'Dealer')
    
    #calculating who won
    player_value = handValue(player_hand)
    dealer_value = handValue(dealer_hand)
    
    if dealer_value > 21 or player_value > dealer_value:
        print("│ ~~You won! Hooray!~~\n\n│ *dealer* God damn it, i'll get you next time!!")
    elif player_value < dealer_value:
        print("│ ~~Dealer wins, womp womp~~")
    else:
        print("│ ~~Tie~~... boooooooooring")
        
    print("\n│ Alright, thanks for playing Blackjack, what do you want to do next? \
\n│ (Type 'help' to see the list of commands)\n")

#barebones, purely for the XL
def hangman(name, notUsingThatBcsThisIsBarebones1, notUsingThatBcsThisIsBarebones2):        
    words = ['python', 'anaconda', 'apple', 'orange', 'purple', 'color', 'painter', 'artwork']
    
    def display_word(word, guessedLetters):
        return ' '.join([letter if letter in guessedLetters else '_' for letter in word])

    word = random.choice(words)
    guessedLetters = set()
    attempts = 6

    print(f"Hi {name}, let's hang a person for not guessing a word")
    print(display_word(word, guessedLetters))
    
    while attempts > 0:
        guess = input("\nGuess a letter: ").casefold()
        
        if guess not in ascii_letters or guess == "":
            print("a LETTER pls")

        elif guess in guessedLetters:
            print("You have already guessed that letter")

        elif guess in word:
            guessedLetters.add(guess)
            print(f"Yup, that's there {display_word(word, guessedLetters)}")

        else:
            attempts -= 1
            guessedLetters.add(guess)
            print(f"Wrong! You have {attempts} attempts left.")
            print(display_word(word, guessedLetters))

        if all(letter in guessedLetters for letter in word):
            print(f"Yippie, you won! Let's get that poor guy off the rope. The word was: {word}")
            break
    else:
        print(f"Sorry, you lost. The guy gets hung, womp womp The word was: {word}")


#barebones, purely for the XL
def numberGuess(name, notUsingThatBcsThisIsBarebones1, notUsingThatBcsThisIsBarebones2):
    number = random.randint(1, 100)
    attempts = 5
    guessedNumbers = []
    print(f"Hello {name} and welcome to this fun and exciting game. \
Guess a number from 1 to 100\n")
    while attempts > 0:
        guess = input("Your guess: ")
        if guess == number:
            print(f"Wow you are so smart and not just lucky! The number was indeed {number}")
            return
        else:
            attempts -= 1
            print(f"WRONG!!!! You have {attempts} more attempts")
            if guess in guessedNumbers:
                print(f"Also you've already tried the number {guess}")
            guessedNumbers.append(guess)
    print("Lmao you lost")