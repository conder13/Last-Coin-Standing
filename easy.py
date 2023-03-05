import random
import time
def evaluate(coins, turn):
  if coins == 1 and turn == "player":
    return "computer"
  elif coins == 1 and turn == "computer":
    return "player"
  else:
    return "none"

def main():
  coins = int(input("Starting number of coins: "))
  while coins < 2 or coins > 200:
    print("You can't play with that amount! Maybe try a different number.")
    coins = int(input("Starting number of coins: "))
  time.sleep(1.2)
  evaluated = "none"
  turn = "player"

  while evaluated == "none":
    turn = "player"

    print("There are ",coins," left.")
    evaluated = evaluate(coins, turn)
    if evaluated != "none":
      break
    time.sleep(1.1)
    player_taken = int(input("How many would you like to take away?\n> "))
    coins = coins-player_taken
    while coins < 1 or player_taken > 3 or player_taken < 1:
      time.sleep(1)
      print("You can't take that much! Try a different number...")
      coins = coins+player_taken
      time.sleep(1)
      player_taken = int(input("How many would you like to take away?\n> "))
      coins = coins-player_taken
    time.sleep(1)
    print("There are ",coins," left.")
    time.sleep(0.8)
    turn = "computer"
    evaluated = evaluate(coins, turn)
    if evaluated != "none":
      break
    print("The computer is taking...")
    computer_taken = random.randint(1,3)
    time.sleep(1.7)
    coins = coins-computer_taken
    while coins < 1:
      coins = coins+computer_taken
      computer_taken = random.randint(1,3)
      coins = coins-computer_taken
    print("The computer took ",computer_taken," coins.")

    time.sleep(1)
  time.sleep(0.6)
  print("THE GAME HAS ENDED...")
  time.sleep(1)
  print("The winner is...")
  time.sleep(1.5)
  print("THE",evaluated,"!")

main()