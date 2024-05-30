import os
from random import randint

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#numPlayers = int(input("How many people want to play?: "))
numPlayers = int(4)

hands = []

for player in range(numPlayers):
    hand = []
    for card in range(52 // numPlayers):
        hand.append(randint(2,14))
    hand.sort()
    hands.append(hand)

activePlayer = 0
cardInPlay = [3]

cls()

while True:
    input(f"Player {activePlayer + 1}, is up!\nPress enter to continue")
    cls()
    selectingCards = True
    cardsToPlay = []
    cardInput = input(f"The card(s) currently in play: {cardInPlay}\nYou currently hold:\n{hands[activePlayer]}\nYou are going to play:\n{cardsToPlay}\nPlease enter a card you would like to play, or 'p' to pass:\n")
    if cardInput.lower() == "p":
        activePlayer += 1
        cls()
    elif int(cardInput) == 2:
        # Handle "bombs"
        pass
    elif cardInput.isnumeric() and int(cardInput) < 14 and int(cardInput) in hands[activePlayer] and int(cardInput) >= cardInPlay[0]:
        cls()
        count = int(input(f"How many {cardInput}s would you like to play, you have {hands[activePlayer].count(int(cardInput))} {cardInput}s?\n"))
        if count <= hands[activePlayer].count(int(cardInput)):
            for x in range(count):
                cardsToPlay.append(int(cardInput))
                hands[activePlayer].remove(int(cardInput))
            if cardInPlay[0] == int(cardInput):
                cardInPlay.extend(cardsToPlay)
                activePlayer += 2
            else:
                cardInPlay = cardsToPlay
                activePlayer += 1
            cls()
            selectingCards = False
        else: pass
    elif cardInput == "" and len(cardsToPlay) > 0:
        selectingCards = False
        pass
    else:
        cls()
        print("Not a valid selection, try again!")
    activePlayer = activePlayer % numPlayers
