#-----------------------------------------------------------------------------
# Name:        Darts Game
# Purpose:     To simulate a darts game online using only python
#
# Author:      Danny Kenneth
# Created:     14-Feb-2024
# Updated:     23-Feb-2024
#-----------------------------------------------------------------------------
#inporting the neccessary libraries
import random


# initalizing global variables
username = ""
score = 0
computerScore = 0
roundScore = 0
targetNumber = 0
throwingAngle = -1
gamemodeChosen = False




# Introducing the user to the game and setting them up for the game


print("Hello there! Welcome to the Darts Simulator! In this simulator, you will need to bring your score down to 0 in order to win You will be versing against a bot (random number generator). \n")
username = (input("What is your name? "))


print(f'''\n Hello {username}! There are two different versions of darts. They are the "301 Game" and the "501 Game. Type "1" for the 301 Game and "2" for the 501 Game. For more info and the rules for each game, type "3". \n''')
gamemode = float(input("Gamemode: "))


# Checking what input the user sent for `gamemode` and giving the right output  based on that input


while gamemodeChosen != True:


  if gamemode == 1.0:
    gamemode = int(gamemode)
    print("\n You chose the 301 Game.")
    score = 301
    computerScore = 301
    gamemodeChosen = True




  elif gamemode == 2.0:
    gamemode = int(gamemode)
    print("\n You chose the 501 Game.")
    score = 501
    computerScore = 501
    gamemodeChosen = True


  # gamemode and general rules
  elif gamemode == 3.0:
    print("")
    print("General Game Rules")
    (print(""))
    print("- In all versions of the dart game, the following rules are as follows:")
    print("- The Objective of the game is to bring your score down to 0 by throwing a dart on a target called a dart board")
    print("- In each round, only 3 darts can be thrown per player")
    print("")
    print("301 Game Rules:")
    print("- In the 301 game, you can not start deducting points until you hit a double ring or a bullseye.")
    print("")
    print("501 Game Rules:")
    print("- In the 501 game, it doesn't matter how you start the game. All that matters is that you follow the rules in `General Game Rules`.")
    print("")
    gamemode = float(input('''Type "1" for the 301 Game and "2" for the 501 Game. '''))


  # this block of code will run if the user inputed an invalid number
  else:
    print("")
    print("The chosen number is not valid. Please try again with either 1, 2, 3.")
    gamemode = float(input('''Type "1" for the 301 Game and "2" for the 501 Game. '''))




  #
if gamemodeChosen == True:
  inGame = 1


# using a random number generator to simulate a dice roll to find out who will go first
print("\n Finding out who will go first...")
userRandomNumber = random.randint(1, 6)
computerRandomNumber = random.randint(1, 6)


if userRandomNumber > computerRandomNumber:
  print("You will go first.")
  playerFirst = True
else:
  print("The Computer will go first.")
  playerFirst = False


# adding an input to allow the user to see who goes first before continuing
print("")
input('''Press the "Enter" key to continue.''')
print("")


# Getting the angle that the user wishes to throw their dart at
# if the computer goes first, then get two random numbers and multiply them tpgether to get the score for that turn
while score > 0 or computerScore > 0:
  if playerFirst == True:


    #this block of code will repeat 3 times
    for turnOne in range(3):


      # this block of code will ask the user to choose what number they want to target
      while targetNumber < 1 or targetNumber > 20:
        targetNumber = int(input("Which base number would you like to target (this number gets multiplied based on which ring the dart lands on). (Allowed Inputs: 1 - 20) - "))
        if targetNumber < 1 or targetNumber > 20:
          print("The number you inputed is not allowed. Please try again.")
          targetNumber = int(input("Which base number would you like to target (this number gets multiplied based on which ring the dart lands on). (Allowed Inputs: 1 - 20) - "))


# this block of code will ask the user the angle they want to throw the dart at
      while throwingAngle < 0:
        throwingAngle = float(input("What angle would you like to throw the dart at? (input range allowed: 0 - 5.7) - "))
        if throwingAngle < 0:
          print("The following angle you inputed is not allowed. Please try again.")
          throwingAngle = float(input("What angle would you like to throw the dart at? (input range allowed: 0 - 5.7) - "))


# This block of code will determine where the dart lands based on the angle and input the points taken off in gamemode 1
      if gamemode == 1:
        if throwingAngle <= 0.2:
          print(f"You hit a bullseye! You subtracted 50 points from your score.")
          score -= 50
        elif throwingAngle < 3.54:
          print(f"You hit a {targetNumber}! However, since you didn't hit a double, treble or bullseye, you didn't deduct any points.")
        elif throwingAngle <= 3.6:
          print(f"You hit a {targetNumber * 3}!")
          score -= (targetNumber * 3)
        elif throwingAngle < 5.6:
          print(f"You hit a {targetNumber}! However, since you didn't hit a double, treble or bullseye, you didn't deduct any points.")
        elif throwingAngle <= 5.7:
          print(f"You hit a {targetNumber * 2}!")
          score -= (targetNumber * 2)
        else:
          print("You shot past the dartboard. No points deducted.")


# This block of code will determine where the dart lands based on the angle and input the points taken off in gamemode 2
      elif gamemode == 2:
        if throwingAngle <= 0.2:
          print(f"You hit a bullseye! You subtracted 50 points from your score.")
          score -= 50
        elif throwingAngle < 3.54:
          print(f"You hit a {targetNumber}!")
          score -= targetNumber
        elif throwingAngle <= 3.6:
          print(f"You hit a {targetNumber * 3}!")
          score -= (targetNumber * 3)
        elif throwingAngle < 5.6:
          print(f"You hit a {targetNumber}!")
          score -= targetNumber
        elif throwingAngle <= 5.7:
          print(f"You hit a {targetNumber * 2}!")
          score -= (targetNumber * 2)
        else:
          print("You shot past the dartboard. No points deducted.")
      targetNumber = 0
      throwingAngle = -1
     
      print("")
# this block of code will determien when the scores reaches below 0 and says who wins, then exits the program
      if score < 0:
        print("The Player has won the game!")
        exit()
      print(f"\n Your current score is {score} \n.")
      input('''Press the "Enter" key to continue.''')
      print("")


# this block of code will run if the computer won the random number generator. In this block of code, two different random number generators with range 20 and 3 will be multiplied to determien the score for the turn
  if playerFirst == False:
    for computerTurn in range(3):
        roundScore = (random.randint(1, 20) * random.randint(1, 3))
        print(f"The computer scored {roundScore} points.")
        print("")
        score -= roundScore


        # this block of code will determien when the scores reaches below 0 and says who wins, then exits the program
        if computerScore < 0:
            print("The Computer has won the game!")
            exit()
        print(f"\n The computer's current score is {score} \n.")
        input('''Press the "Enter" key to continue.''')
        print("")


# the rest of the code is a repetition of the code above with the two players switched for the second scenario when the computer goes first instead
  for turnTwo in range(1, 4):
      if playerFirst == True:
          for computerTurnTwo in range(3):
            roundScore = (random.randint(1, 20) * random.randint(1, 3))
            print(f"The computer scored {roundScore} points.")
            print("")
            score -= roundScore


      else:
        for turnOne in range(3):
          while targetNumber < 1 or targetNumber > 20:
            targetNumber = int(input("Which base number would you like to target (this number gets multiplied based on which ring the dart lands on). (Allowed Inputs: 1 - 20) - "))
            if targetNumber < 1 or targetNumber > 20:
              print("The number you inputed is not allowed. Please try again.")
              targetNumber = int(input("Which base number would you like to target (this number gets multiplied based on which ring the dart lands on). (Allowed Inputs: 1 - 20) - "))
       
          while throwingAngle < 0:
            throwingAngle = float(input("What angle would you like to throw the dart at? (input range allowed: 0 - 5.7) - "))
            if throwingAngle < 0:
              print("The following angle you inputed is not allowed. Please try again.")
              throwingAngle = float(input("What angle would you like to throw the dart at? (input range allowed: 0 - 5.7) - "))
       
          if gamemode == 1:
            if throwingAngle <= 0.2:
              print(f"You hit a bullseye! You subtracted 50 points from your score.")
              score -= 50
            elif throwingAngle < 3.54:
              print(f"You hit a {targetNumber}! However, since you didn't hit a double, treble or bullseye, you didn't deduct any points.")
            elif throwingAngle <= 3.6:
              print(f"You hit a {targetNumber * 3}!")
              score -= (targetNumber * 3)
            elif throwingAngle < 5.6:
              print(f"You hit a {targetNumber}! However, since you didn't hit a double, treble or bullseye, you didn't deduct any points.")
            elif throwingAngle <= 5.7:
              print(f"You hit a {targetNumber * 2}!")
              score -= (targetNumber * 2)
            else:
              print("You shot past the dartboard. No points deducted.")
       
          elif gamemode == 2:
            if throwingAngle <= 0.2:
              print(f"You hit a bullseye! You subtracted 50 points from your score.")
              score -= 50
            elif throwingAngle < 3.54:
              print(f"You hit a {targetNumber}!")
              score -= targetNumber
            elif throwingAngle <= 3.6:
              print(f"You hit a {targetNumber * 3}!")
              score -= (targetNumber * 3)
            elif throwingAngle < 5.6:
              print(f"You hit a {targetNumber}!")
              score -= targetNumber
            elif throwingAngle <= 5.7:
              print(f"You hit a {targetNumber * 2}!")
              score -= (targetNumber * 2)
            else:
              print("You shot past the dartboard. No points deducted.")
          targetNumber = 0
          throwingAngle = -1
       
          print("")
       
          if score < 0:
            print("The Player has won the game!")
            exit()
          print(f"\n Your current score is {score} \n.")
        input('''Press the "Enter" key to continue.''')
        print("")
       
