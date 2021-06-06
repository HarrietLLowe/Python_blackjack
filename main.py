#Blackjack game!
from art import logo

import random
import replit

#dealing cards to user and computer
def deal_card():
  """Returns a random card"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

#calculating the scores
def calculate_score(cards):
  """Calculates the score of the user or computer"""
  if sum(cards) == 21 and len(cards) == 2:
    return "BlackJack" 
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#checking scores 
def compare(user_score, computer_score):
  """Checks the user score with the computer score and returns the final result of the game"""
  if user_score == computer_score:
    print("It's a draw!\n")
  elif computer_score == 0:
    print("You lose, computer has Blackjack.\n")
  elif user_score == 0:
    print("You win! You have Blackjack!\n")
  elif user_score > 21:
    print("You lose, over 21.\n")
  elif computer_score > 21:
    print("You win, computer went over 21.\n")
  elif user_score > computer_score:
    print("You win.\n")
  elif computer_score > user_score:
    print("You lose.\n")

#the game - using the play function to reiterate this section 
def play():
  """Carries out the logic of Blackjack"""
  print(logo)
  game_over = False 

  user_cards = []
  computer_cards = []

  user_cards.append(deal_card()) #could you a for loop with a range of (2) to repeat this code twice
  user_cards.append(deal_card())
  print(f"Your cards: {user_cards}")

  #only showing user 1 card from the computer
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())
  computer_cards_hidden = computer_cards[0]
  print(f"Computer's first card: {computer_cards_hidden}")

  while not game_over: 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else: 
      new_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if new_card == "y":
        user_cards.append(deal_card())
        print(f"Your cards are: {user_cards}")
      else:
        game_over = True
  
      while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

  print(f"Your final score is {user_score} and your opponent's final score is {computer_score}")
  compare(user_score, computer_score)

  again = input("Do you want to play again? Type 'y' or 'no'.")
  if again == "y":
    replit.clear()
    play()    

play()