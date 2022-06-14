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
    """Deals a random card by its value in a standard Blackjack game.

    Returns:
        int: Returns a randomly generated card out of a list of card values in a standard Blackjack game.
    """
    card = random.choice(cards)
    return card

def scoreCalculator(hand):
    """Calculates the total score of cards in a hand

    Args:
        hand (int): The hand of cards to calculate the score of

    Returns:
        int: The sum of the score of the cards in the given hand
    """
    if sum(hand) > 21 and 11 in hand:    # Ace can be either 11 or 1, so if the players' score is over 21 and they have an ace (11), it will change to a 1
        hand.append(1)
        hand.remove(11)
    return sum(hand)
    
def resultDecider(playerScore, computerScore, playerCards, computerCards):
    """Decides whether the player or the computer wins in a game of Blackjack, by comparing the scores.
    If someones' score (either the computer or the player) exceeds 21, they went over and lose.
    If someone has blackjack, aka a score of 21 with only 2 cards, they win, unless their opponent also has blackjack, in which case there is a draw.
    Similarly, if each person has the same score, there is a draw.
    Otherwise, the person who is the closest to 21 without exceeding has won the game.

    Args:
        playerScore (int): The total score of the player's cards
        computerScore (int): The total score of the computer's cards
        playerCards (list(int)): The cards belonging to the player, where each card is its own score aka Q,K,J is 10, Ace is 11 unless score exceeds 21 where its 1
        computerCards (list(int)): The cards belonging to the computer, where each card is its own score aka Q,K,J is 10, Ace is 11 unless score exceeds 21 where its 1
    """
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
    """Plays blackjack with the user.
    The game starts by dealing the player and computer two cards.
    It calculates both the player and the computer's score. If the player or the computer has blackjack, the player will be forced to stand.
    Otherwise, the player can keep asking for "hits" (to draw another card) and aim to get 21 score but to not exceed it.
    Once the player chooses to stand, the computer will be dealt their cards unless/until the computer's score reaches 17 or higher, where they will be forced to stand also.
    If either the computer or the player exceeds 21, they will lose the game, and their opponent will be given the win.
    At the end of the game, the final cards will be shown and the result will be decided. Whoever is closer to 21 without exceeding 21 wins.
    The decks used do not extract the dealt card after each use (aka, once a card is dealt, there is still an equal chance of getting that same card again)
    If both the player and the computer have the same score, there will be a draw.
    """
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