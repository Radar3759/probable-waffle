import random

#ASCII art from https://www.udemy.com/course/100-days-of-code
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors Ultimate Challenge!\n")

def rock_paper_scissors():
#PLAYER 
  choice = int(input("\nType '0' for Rock, '1' for Paper, '2' for Scissors: "))

  if choice == 0:
    print("\nYou selected rock.")
    print(rock)
  elif choice == 1:
    print("\nYou selected paper.")
    print(paper)
  elif choice == 2:
    print("\nYou selected scissors.")
    print(scissors)
  else:
    print("Please type 0, 1, or 2")

  #COMPUTER   
  computer_num = (random.randint(0, 2))
  #print(f"Computer chose {computer_num}")

  if computer_num == 0:
    print("\nComputer selected rock.")
    print(rock)
  elif computer_num == 1:
    print("\nComputer selected paper.")
    print(paper)
  else:
    print("\nComputer selected scissors.")
    print(scissors)
  #WHO WINS
  if choice == 0 and computer_num == 2:
    print("You Win!!")
  elif choice == 2 and computer_num == 0:
    print("You Lose!")  
  elif computer_num > choice:
    print("You Lose!")
  elif choice > computer_num:
    print("You Win!")
  elif computer_num == choice:
    print("Ok, We'll call it a draw!") 
  #PLAY AGAIN   
  play_again = input("\nWould you like to play again? Y / N ? ")
  if play_again.lower() == "y":
    rock_paper_scissors()
  else:
      print("\nOk, Thanks for playing!")  
rock_paper_scissors()


