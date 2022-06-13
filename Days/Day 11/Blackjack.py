############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.          <--- I chose this difficulty ( we love a challenge )

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random
import os
from BlackjackArt import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def cardDealer():
    card = random.choice(cards)
    return card
def scoreCalculator(cards):
    if sum(cards) > 21 and 11 in cards:    # Ace can be either 11 or 1, so if the players' score is over 21 and they have an ace (11), it will change to a 1
        cards.append(1)
        cards.remove(11)
    return sum(cards)
    
def resultDecider(playerScore, computerScore, playerCards, computerCards):
    if playerScore == computerScore:
        return("Draw 🙃")
    elif playerScore == 21 and len(playerCards) == 2:
        return("Win with a Blackjack 😎")
    elif computerScore == 21 and len(computerCards) == 2:
        return("Lose, opponent has Blackjack 😱")
    elif playerScore > 21:
        return("You went over. You lose 😭")
    elif computerScore > 21:
        return("Opponent went over. You win 😁")
    elif playerScore > computerScore:
        return("You Win! 😃")
    elif computerScore > playerScore:
        return("You lose 😤")

def BlackJack():
    Stand = False
    print(logo)
    playerCards = []
    computerCards = []
    
    for i in range(2):            # Deals first two cards
        playerCards.append(cardDealer())
        computerCards.append(cardDealer())
        
    while not Stand:
        playerScore = scoreCalculator(playerCards)
        computerScore = scoreCalculator(computerCards)
        print(f"    Your cards: {playerCards}, current score: {playerScore}")
        print(f"    Computer's first card: {computerCards[0]}")
        if (playerScore == 21 and len(playerCards) == 2) or (computerScore == 21 and len(computerCards) == 2) or playerScore > 21:
            Stand = True
        else:
            hitStatus = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if hitStatus == 'y':
                playerCards.append(cardDealer())
            else:
                Stand = True

    # Continue dealing computer cards, as dealers will be forced to continue playing until their total score is 17 or higher
    while computerScore < 17:
        computerCards.append(cardDealer())
        computerScore = scoreCalculator(computerCards)

    print(f"    Your final hand: {playerCards}, final score: {playerScore}")
    print(f"    Computer's final hand: {computerCards}, final score: {computerScore}")
    print(resultDecider(playerScore=playerScore, computerScore=computerScore, playerCards=playerCards, computerCards=computerCards))
        

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    BlackJack()