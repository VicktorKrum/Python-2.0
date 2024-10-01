import random

game_choice= ["rock", "paper", "scissor"]
def get_choices():
      player_choice = input("Enter a choice(rock, paper, scissor):")
      computer_choice = random.choice(game_choice)
      global choices
      choices = {"player": player_choice, "computer": computer_choice}
      return choices



def check_win(computer, player):
  print(f"You chose {player}, computer chose {computer}")
  if (computer==player):
    print ("It's a tie!")
  elif (computer== "paper"):
    if (player=="scissor"):
      return 'Scissor cuts paper! You are winner'
    else:
      return 'Paper covers rock! You are loser'
  
  elif (player== "paper"):
    if (computer=="scissor"):
      return 'Scissor cuts paper! computer wins'
    else:
      return 'Paper covers rock! computer loses'

  elif (player== "rock"):
    if (computer=="scissor"):
      return 'rock broke scissor! you win!'
    else:
      return 'Paper covers rock! computer wins'
  



get_choices()
result= check_win(choices["player"], choices["computer"])
print(result)
