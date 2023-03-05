import random
import time
def evaluate(coins, computerTurn):
  if coins == 1 and computerTurn == False:
    return 10
  elif coins == 1 and computerTurn == True:
    return -10
  else:
    return 0

def isMovesLeft(coins):
  if coins > 1:
    return True
  else:
    return False

def minimax(coins, computerTurn):
  score = evaluate(coins, computerTurn)
  if score == 10:
    return score

  if score == -10:
    return score

  if isMovesLeft(coins) == False:
    return 0

  if computerTurn == True:
    best = -1000
    for i in range(1,5):
      best = max(best, minimax(coins-i, not computerTurn))

    return best

  else:
    best = 1000

    for i in range(1, 5):
      best = min(best, minimax(coins-i, not computerTurn))

    return best

def findBestMove(coins):
  bestVal = -1000
  bestMove = -1

  for i in range(1,5):
    moveVal = minimax(i, True)
    if moveVal > bestVal:
      bestVal = moveVal
      bestMove = i
  return bestMove

def main():
  coins = int(input("Starting number of coins: "))
  while coins < 2 or coins > 200:
    print("You can't play with that amount! Maybe try a different number.")
    coins = int(input("Starting number of coins: "))
  time.sleep(1.2)
  evaluated = 0

  while evaluated == 0:

    print("There are ",coins," left.")
    evaluated = evaluate(coins, False)
    if evaluated != 0:
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
    evaluated = evaluate(coins, True)
    if evaluated != 0:
      break
    print("The computer is taking...")
    computer_taken = findBestMove(coins)
    time.sleep(1.7)
    print("The computer took ",computer_taken," coins.")
    coins = coins-computer_taken

    time.sleep(1)
  time.sleep(0.6)
  print("THE GAME HAS ENDED...")
  time.sleep(1)
  print("The winner is...")
  time.sleep(1.5)
  if evaluated == True:
    winner = "computer"
  else:
    winner = "player"
  print("THE",winner,"!")

main()