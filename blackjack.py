import random
from replit import clear
from art import logo

"""return a random card from the deck"""
#card deck deal random card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
#check for Blackjack on initial deal
def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
    #alt if sum(cards) == 21 and len(cards) == 2:
        return 0
    #acount for A = 11 && A == 1    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    #keep return statement out of the if loops  
    return sum(cards)

#play game function 
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

  #underscore is ok because there is no var, it just needs to loop twice
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}\n")
    print(f"Computer's First Card: {computer_cards[0]}\n")

    if user_score == 0 or user_score > 21 or computer_score == 0:
      is_game_over = True
    else:
      another_card = input("Would you like another card? y/n ")  
      if another_card == "y":
        #adds another card to the hand
        user_cards.append(deal_card())
      else: 
        is_game_over = True  

  def compare(user_score, computer_score):
    if user_score == computer_score:
      return("Ok, We'll call it a draw!")
      if user_score > 21 and computer_score > 21:
        return("You both Lose!")
    elif user_score == 0:
      return ("You Win with Blackjack!")
    elif computer_score == 0:
      return("Computer Wins with Blackjack!")  
    elif user_score > 21:
      return(f"You went over with a score of {user_score} Computer Wins")
    elif computer_score > 21:
      return(f"Computer went over with a score of {computer_score} User Wins")    
    elif user_score > computer_score:
      return "You win"  
    else: 
      return "You Lose"  

  #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
  print (compare(user_score, computer_score))
  print(f"\nYour final hand: {user_cards}, final score: {user_score}")
  print(f"\nComputer's final hand: {computer_cards}, final score: {computer_score}")  
  #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("\nDo you want to play a game of blackjack? y/n ") == "y":
  clear()
  play_game()
