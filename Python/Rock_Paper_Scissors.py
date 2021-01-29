#choices you can pick
import random
from random import choice

choices = ('rock', 'paper', 'scissors')

#All possibilities for the game.
possibilities = ([["Won", "Won", "Won"],
                    ["Won", "Lost", "Won"],
                    ["Lost", "Won", "Won"],
                    ["Lost", "Lost", "Lost"],
                    ["Lost", "Won", "Lost"],
                    ["Won", "Lost", "Lost"],
                    ["Lost", "Lost", "Won"],
                    ["Won", "Won", "Lost"]])

#This will keep track of the score.
summary = [0, 0, 0]
summary2 = [0, 0, 0]
summary3 = [0, 0, 0]

#This will pick what kind of game the player wants to start.
starting = True
while starting:
    #This will ask the ammount of people you want to play with.
    print("\n \nWith how many people would you like to play?")
    print("A. 1 player (CPU)")
    print("B. 2 players")
    print("C. 3 players")

    people = input("\n Choose with how many players you want to play? \n ")
    if people == "A":
        print("\n starting a 1 player game.")

        #Round 1
        round1 = True
        while round1:
            print("\n ROUND 1")

            #Computer picks a random number between 1 and 3.
            comp_choice = random.randint(1, 3)

            #gives the number 1, 2 and 3 names.
            if comp_choice == 1: 
                comp_choice_name = 'Rock'
            elif comp_choice == 2: 
                comp_choice_name = 'paper'
            elif comp_choice == 3:
                comp_choice_name = 'scissor'

            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You tied try again.")
                elif comp_choice == 2:
                    print("You lost this round.")
                    summary[0] = -1
                    round1 = False
                elif comp_choice == 3:
                    print("You won this round.")
                    summary[0] = 1
                    round1 = False
                else:
                    print("\nplease pick a valid answer.")

            #player picks paper.
            elif player1 == "B":
                print("\nPlayer1 chose paper!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You Won this round.")
                    summary[0] = 1
                    round1 = False
                elif comp_choice == 2:
                    print("You tied try again.")
                elif comp_choice == 3:
                    print("You lost this round.")
                    summary[0] = -1
                    round1 = False
                else:
                    print("\nplease pick a valid answer.")

            #player picks scissors.
            elif player1 == "C":
                print("\nPlayer1 chose scissors!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You lost this round.")
                    summary[0] = -1
                    round1 = False
                elif comp_choice == 2:
                    print("You won this round.")
                    summary[0] = 1
                    round1 = False
                elif comp_choice == 3:
                    print("You tied this round.")
                else:
                    print("\nplease pick a valid answer.")
                
            else:
                print("\nplease pick a valid answer.")

        #Round 2
        round2 = True
        while round2:
            print("\n ROUND 2")

            #Computer picks a random number between 1 and 3.
            comp_choice = random.randint(1, 3)

            #gives the number 1, 2 and 3 names.
            if comp_choice == 1: 
                comp_choice_name = 'Rock'
            elif comp_choice == 2: 
                comp_choice_name = 'paper'
            elif comp_choice == 3:
                comp_choice_name = 'scissor'

            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You tied try again.")
                elif comp_choice == 2:
                    print("You lost this round.")
                    summary[1] = -1
                    round2 = False
                elif comp_choice == 3:
                    print("You won this round.")
                    summary[1] = 1
                    round2 = False
                else:
                    print("\nplease pick a valid answer.")

            #player picks paper.
            elif player1 == "B":
                print("\nPlayer1 chose paper!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You Won this round.")
                    summary[1] = 1
                    round2 = False
                elif comp_choice == 2:
                    print("You tied try again.")
                elif comp_choice == 3:
                    print("You lost this round.")
                    summary[1] = -1
                    round2 = False
                else:
                    print("\nplease pick a valid answer.")

            #player picks scissors.
            elif player1 == "C":
                print("\nPlayer1 chose scissors!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You lost this round.")
                    summary[1] = -1
                    round2 = False
                elif comp_choice == 2:
                    print("You won this round.")
                    summary[1] = 1
                    round2 = False
                elif comp_choice == 3:
                    print("You tied this round.")
                else:
                    print("\nplease pick a valid answer.")
                
            else:
                print("\nplease pick a valid answer.")

        #Round 3
        round3 = True
        while round3:
            print("\n ROUND 3")

            #Computer picks a random number between 1 and 3.
            comp_choice = random.randint(1, 3)

            #gives the number 1, 2 and 3 names.
            if comp_choice == 1: 
                comp_choice_name = 'Rock'
            elif comp_choice == 2: 
                comp_choice_name = 'paper'
            elif comp_choice == 3:
                comp_choice_name = 'scissor'

            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You tied try again.")
                elif comp_choice == 2:
                    print("You lost this round.")
                    summary[2] = -1
                    round3 = False
                elif comp_choice == 3:
                    print("You won this round.")
                    summary[2] = 1
                    round3 = False
                else:
                    print("\nplease pick a valid answer.")

            #player picks paper.
            elif player1 == "B":
                print("\nPlayer1 chose paper!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You Won this round.")
                    summary[2] = 1
                    round3 = False
                elif comp_choice == 2:
                    print("You tied try again.")
                elif comp_choice == 3:
                    print("You lost this round.")
                    summary[2] = -1
                    round3 = False
                else:
                    print("\nplease pick a valid answer.")

            #player picks scissors.
            elif player1 == "C":
                print("\nPlayer1 chose scissors!")
                print("Computer choice is: " + comp_choice_name)
                if comp_choice == 1:
                    print("You lost this round.")
                    summary[2] = -1
                    round3 = False
                elif comp_choice == 2:
                    print("You won this round.")
                    summary[2] = 1
                    round3 = False
                elif comp_choice == 3:
                    print("You tied this round.")
                else:
                    print("\nplease pick a valid answer.")              

    elif people =="B":
        print("\n starting a 2 player game.")

        #Round 1
        round1 = True
        while round1:
            print("\n ROUND 1")
            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player2 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player1 picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                
                if player1 == "A" and player2 == "A":
                    print("You both tied try again.")
                elif player1 == "A" and player2 == "B":
                    print("player2 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    round1 = False
                elif player1 == "A" and player2 == "C":
                    print("player1 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    round1 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Paper.
            if player1 == "B":
                print("\nPlayer1 chose Paper!")
                
                if player1 == "B" and player2 == "B":
                    print("You both tied try again.")
                elif player1 == "B" and player2 == "C":
                    print("player2 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    round1 = False
                elif player1 == "B" and player2 == "A":
                    print("player1 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    round1 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Scissors.
            if player1 == "C":
                print("\nPlayer1 chose scissors!")
                
                if player1 == "C" and player2 == "C":
                    print("You both tied try again.")
                elif player1 == "C" and player2 == "A":
                    print("player2 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    round1 = False
                elif player1 == "C" and player2 == "B":
                    print("player1 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    round1 = False
                else:
                    print("\nplease pick a valid answer.")

        #Round 2
        round2 = True
        while round2:
            print("\n ROUND 2")
            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player2 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player1 picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                
                if player1 == "A" and player2 == "A":
                    print("You both tied try again.")
                elif player1 == "A" and player2 == "B":
                    print("player2 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    round2 = False
                elif player1 == "A" and player2 == "C":
                    print("player1 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    round2 = False

            #player1 picks Paper.
            if player1 == "B":
                print("\nPlayer1 chose Paper!")
                
                if player1 == "B" and player2 == "B":
                    print("You both tied try again.")
                elif player1 == "B" and player2 == "C":
                    print("player2 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    round2 = False
                elif player1 == "B" and player2 == "A":
                    print("player1 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    round2 = False

            #player1 picks Scissors.
            if player1 == "C":
                print("\nPlayer1 chose scissors!")
                
                if player1 == "C" and player2 == "C":
                    print("You both tied try again.")
                elif player1 == "C" and player2 == "A":
                    print("player2 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    round2 = False
                elif player1 == "C" and player2 == "B":
                    print("player1 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    round2 = False   

        #Round 3
        round3 = True
        while round3:
            print("\n ROUND 3")
            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player2 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player1 picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                
                if player1 == "A" and player2 == "A":
                    print("You both tied try again.")
                elif player1 == "A" and player2 == "B":
                    print("player2 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    round3 = False
                elif player1 == "A" and player2 == "C":
                    print("player1 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    round3 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Paper.
            if player1 == "B":
                print("\nPlayer1 chose Paper!")
                
                if player1 == "B" and player2 == "B":
                    print("You both tied try again.")
                elif player1 == "B" and player2 == "C":
                    print("player2 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    round3 = False
                elif player1 == "B" and player2 == "A":
                    print("player1 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    round3 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Scissors.
            if player1 == "C":
                print("\nPlayer1 chose scissors!")
                
                if player1 == "C" and player2 == "C":
                    print("You both tied try again.")
                elif player1 == "C" and player2 == "A":
                    print("player2 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    round3 = False
                elif player1 == "C" and player2 == "B":
                    print("player1 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    round3 = False
                else:
                    print("\nplease pick a valid answer.")

        else:
            print("\nplease pick a valid answer.")

    elif people =="C":
        print("\n starting a 3 player game.")

        #Round 1
        round1 = True
        while round1:
            print("\n ROUND 1")
            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player2 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player3 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player1 picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                
                if player1 == "A" and player2 == "A" and player3 == "A":
                    print("You all tied try again.")
                elif player1 == "A" and player2 == "B" and player3 == "C":
                    print("everyone beats eachother noone wins.")
                elif player1 == "A" and player2 == "C" and player3 == "B":
                    print("everyone beats eachother noone wins.")
                elif player1 == "A" and player2 == "B" and player3 == "A":
                    print("player2 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "A" and player2 == "B" and player3 == "B":
                    print("player2 and player3 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    summary3[0] = 1
                    round1 = False
                elif player1 == "A" and player2 == "C" and player3 == "C":
                    print("player1 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "A" and player2 == "B" and player3 == "A":
                    print("player1 and player3 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    summary3[0] = 1
                    round1 = False
                elif player1 == "A" and player2 == "A" and player3 == "B":
                    print("player1 and player2 won this round.")
                    summary[0] = 1
                    summary2[0] = 1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "A" and player2 == "A" and player3 == "B":
                    print("player3 won this round.")
                    summary[0] = -1
                    summary2[0] = -1
                    summary3[0] = 1
                    round1 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Paper.
            if player1 == "B":
                print("\nPlayer1 chose Paper!")
                
                if player1 == "B" and player2 == "B" and player3 == "B":
                    print("You all tied try again.")
                elif player1 == "B" and player2 == "A" and player3 == "C":
                    print("everyone beats eachother noone wins.")
                elif player1 == "B" and player2 == "C" and player3 == "A":
                    print("everyone beats eachother noone wins.")
                elif player1 == "B" and player2 == "C" and player3 == "B":
                    print("player2 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "B" and player2 == "C" and player3 == "C":
                    print("player2 and player3 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    summary3[0] = 1
                    round1 = False
                elif player1 == "B" and player2 == "A" and player3 == "A":
                    print("player1 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "B" and player2 == "A" and player3 == "B":
                    print("player1 and player3 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    summary3[0] = 1
                    round1 = False
                elif player1 == "B" and player2 == "B" and player3 == "A":
                    print("player1 and player2 won this round.")
                    summary[0] = 1
                    summary2[0] = 1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "B" and player2 == "B" and player3 == "C":
                    print("player3 won this round.")
                    summary[0] = -1
                    summary2[0] = -1
                    summary3[0] = 1
                    round1 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Scissors.
            if player1 == "C":
                print("\nPlayer1 chose scissors!")
                
                if player1 == "C" and player2 == "C" and player3 == "C":
                    print("You all tied try again.")
                elif player1 == "C" and player2 == "A" and player3 == "B":
                    print("everyone beats eachother noone wins.")
                elif player1 == "C" and player2 == "B" and player3 == "A":
                    print("everyone beats eachother noone wins.")
                elif player1 == "C" and player2 == "A" and player3 == "C":
                    print("player2 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "C" and player2 == "A" and player3 == "A":
                    print("player2 and player3 won this round.")
                    summary[0] = -1
                    summary2[0] = 1
                    summary3[0] = 1
                    round1 = False
                elif player1 == "C" and player2 == "B" and player3 == "B":
                    print("player1 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "C" and player2 == "B" and player3 == "C":
                    print("player1 and player3 won this round.")
                    summary[0] = 1
                    summary2[0] = -1
                    summary3[0] = 1
                    round1 = False
                elif player1 == "C" and player2 == "C" and player3 == "B":
                    print("player1 and player2 won this round.")
                    summary[0] = 1
                    summary2[0] = 1
                    summary3[0] = -1
                    round1 = False
                elif player1 == "C" and player2 == "C" and player3 == "A":
                    print("player3 won this round.")
                    summary[0] = -1
                    summary2[0] = -1
                    summary3[0] = 1
                    round1 = False
                else:
                    print("\nplease pick a valid answer.")

        #Round 2
        round2 = True
        while round2:
            print("\n ROUND 2")
            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player2 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player3 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player1 picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                
                if player1 == "A" and player2 == "A" and player3 == "A":
                    print("You all tied try again.")
                elif player1 == "A" and player2 == "B" and player3 == "C":
                    print("everyone beats eachother noone wins.")
                elif player1 == "A" and player2 == "C" and player3 == "B":
                    print("everyone beats eachother noone wins.")
                elif player1 == "A" and player2 == "B" and player3 == "A":
                    print("player2 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "A" and player2 == "B" and player3 == "B":
                    print("player2 and player3 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    summary3[1] = 1
                    round2 = False
                elif player1 == "A" and player2 == "C" and player3 == "C":
                    print("player1 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "A" and player2 == "B" and player3 == "A":
                    print("player1 and player3 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    summary3[1] = 1
                    round2 = False
                elif player1 == "A" and player2 == "A" and player3 == "B":
                    print("player1 and player2 won this round.")
                    summary[1] = 1
                    summary2[1] = 1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "A" and player2 == "A" and player3 == "B":
                    print("player3 won this round.")
                    summary[1] = -1
                    summary2[1] = -1
                    summary3[1] = 1
                    round2 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Paper.
            if player1 == "B":
                print("\nPlayer1 chose Paper!")
                
                if player1 == "B" and player2 == "B" and player3 == "B":
                    print("You all tied try again.")
                elif player1 == "B" and player2 == "A" and player3 == "C":
                    print("everyone beats eachother noone wins.")
                elif player1 == "B" and player2 == "C" and player3 == "A":
                    print("everyone beats eachother noone wins.")
                elif player1 == "B" and player2 == "C" and player3 == "B":
                    print("player2 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "B" and player2 == "C" and player3 == "C":
                    print("player2 and player3 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    summary3[1] = 1
                    round2 = False
                elif player1 == "B" and player2 == "A" and player3 == "A":
                    print("player1 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "B" and player2 == "A" and player3 == "B":
                    print("player1 and player3 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    summary3[1] = 1
                    round2 = False
                elif player1 == "B" and player2 == "B" and player3 == "A":
                    print("player1 and player2 won this round.")
                    summary[1] = 1
                    summary2[1] = 1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "B" and player2 == "B" and player3 == "C":
                    print("player3 won this round.")
                    summary[1] = -1
                    summary2[1] = -1
                    summary3[1] = 1
                    round2 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Scissors.
            if player1 == "C":
                print("\nPlayer1 chose scissors!")
                
                if player1 == "C" and player2 == "C" and player3 == "C":
                    print("You all tied try again.")
                elif player1 == "C" and player2 == "A" and player3 == "B":
                    print("everyone beats eachother noone wins.")
                elif player1 == "C" and player2 == "B" and player3 == "A":
                    print("everyone beats eachother noone wins.")
                elif player1 == "C" and player2 == "A" and player3 == "C":
                    print("player2 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "C" and player2 == "A" and player3 == "A":
                    print("player2 and player3 won this round.")
                    summary[1] = -1
                    summary2[1] = 1
                    summary3[1] = 1
                    round2 = False
                elif player1 == "C" and player2 == "B" and player3 == "B":
                    print("player1 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "C" and player2 == "B" and player3 == "C":
                    print("player1 and player3 won this round.")
                    summary[1] = 1
                    summary2[1] = -1
                    summary3[1] = 1
                    round2 = False
                elif player1 == "C" and player2 == "C" and player3 == "B":
                    print("player1 and player2 won this round.")
                    summary[1] = 1
                    summary2[1] = 1
                    summary3[1] = -1
                    round2 = False
                elif player1 == "C" and player2 == "C" and player3 == "A":
                    print("player3 won this round.")
                    summary[1] = -1
                    summary2[1] = -1
                    summary3[1] = 1
                    round2 = False
                else:
                    print("\nplease pick a valid answer.")

        #Round 3
        round3 = True
        while round3:
            print("\n ROUND 3")
            player1 = input("\n It's player 1's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player2 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")
            player3 = input("\n It's player 2's turn. \nA. Rock \nB. Paper \nC. Scissors \n \n User turn: ")

            #player1 picks rock.
            if player1 == "A":
                print("\nPlayer1 chose rock!")
                
                if player1 == "A" and player2 == "A" and player3 == "A":
                    print("You all tied try again.")
                elif player1 == "A" and player2 == "B" and player3 == "C":
                    print("everyone beats eachother noone wins.")
                elif player1 == "A" and player2 == "C" and player3 == "B":
                    print("everyone beats eachother noone wins.")
                elif player1 == "A" and player2 == "B" and player3 == "A":
                    print("player2 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "A" and player2 == "B" and player3 == "B":
                    print("player2 and player3 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    summary3[2] = 1
                    round3 = False
                elif player1 == "A" and player2 == "C" and player3 == "C":
                    print("player1 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "A" and player2 == "B" and player3 == "A":
                    print("player1 and player3 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    summary3[2] = 1
                    round3 = False
                elif player1 == "A" and player2 == "A" and player3 == "B":
                    print("player1 and player2 won this round.")
                    summary[2] = 1
                    summary2[2] = 1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "A" and player2 == "A" and player3 == "B":
                    print("player3 won this round.")
                    summary[2] = -1
                    summary2[2] = -1
                    summary3[2] = 1
                    round3 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Paper.
            if player1 == "B":
                print("\nPlayer1 chose Paper!")
                
                if player1 == "B" and player2 == "B" and player3 == "B":
                    print("You all tied try again.")
                elif player1 == "B" and player2 == "A" and player3 == "C":
                    print("everyone beats eachother noone wins.")
                elif player1 == "B" and player2 == "C" and player3 == "A":
                    print("everyone beats eachother noone wins.")
                elif player1 == "B" and player2 == "C" and player3 == "B":
                    print("player2 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "B" and player2 == "C" and player3 == "C":
                    print("player2 and player3 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    summary3[2] = 1
                    round3 = False
                elif player1 == "B" and player2 == "A" and player3 == "A":
                    print("player1 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "B" and player2 == "A" and player3 == "B":
                    print("player1 and player3 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    summary3[2] = 1
                    round3 = False
                elif player1 == "B" and player2 == "B" and player3 == "A":
                    print("player1 and player2 won this round.")
                    summary[2] = 1
                    summary2[2] = 1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "B" and player2 == "B" and player3 == "C":
                    print("player3 won this round.")
                    summary[2] = -1
                    summary2[2] = -1
                    summary3[2] = 1
                    round3 = False
                else:
                    print("\nplease pick a valid answer.")

            #player1 picks Scissors.
            if player1 == "C":
                print("\nPlayer1 chose scissors!")
                
                if player1 == "C" and player2 == "C" and player3 == "C":
                    print("You all tied try again.")
                elif player1 == "C" and player2 == "A" and player3 == "B":
                    print("everyone beats eachother noone wins.")
                elif player1 == "C" and player2 == "B" and player3 == "A":
                    print("everyone beats eachother noone wins.")
                elif player1 == "C" and player2 == "A" and player3 == "C":
                    print("player2 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "C" and player2 == "A" and player3 == "A":
                    print("player2 and player3 won this round.")
                    summary[2] = -1
                    summary2[2] = 1
                    summary3[2] = 1
                    round3 = False
                elif player1 == "C" and player2 == "B" and player3 == "B":
                    print("player1 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "C" and player2 == "B" and player3 == "C":
                    print("player1 and player3 won this round.")
                    summary[2] = 1
                    summary2[2] = -1
                    summary3[2] = 1
                    round3 = False
                elif player1 == "C" and player2 == "C" and player3 == "B":
                    print("player1 and player2 won this round.")
                    summary[2] = 1
                    summary2[2] = 1
                    summary3[2] = -1
                    round3 = False
                elif player1 == "C" and player2 == "C" and player3 == "A":
                    print("player3 won this round.")
                    summary[2] = -1
                    summary2[2] = -1
                    summary3[2] = 1
                    round3 = False
                else:
                    print("\nplease pick a valid answer.")

        else:
            print("\nplease pick a valid answer.")

    #This will determine which rounds you won and which you lost.
    #Score for player1
    if summary == [1, 1, 1]:
        print("Player1 Score:")
        print(possibilities[0])
    elif summary == [1, -1, 1]:
        print("Player1 Score:")
        print(possibilities[1])
    elif summary == [-1, 1, 1]:
        print("Player1 Score:")
        print(possibilities[2])
    elif summary == [-1, -1, -1]:
        print("Player1 Score:")
        print(possibilities[3])
    elif summary == [-1, 1, -1]:
        print("Player1 Score:")
        print(possibilities[4])
    elif summary == [1, -1, -1]:
        print("Player1 Score:")
        print(possibilities[5])

    #Score for player2
    if summary2 == [1, 1, 1]:
        print("\nPlayer2 Score:")
        print(possibilities[0])
    elif summary2 == [1, -1, 1]:
        print("\nPlayer2 Score:")
        print(possibilities[1])
    elif summary2 == [-1, 1, 1]:
        print("\nPlayer2 Score:")
        print(possibilities[2])
    elif summary2 == [-1, -1, -1]:
        print("\nPlayer2 Score:")
        print(possibilities[3])
    elif summary2 == [-1, 1, -1]:
        print("\nPlayer2 Score:")
        print(possibilities[4])
    elif summary2 == [1, -1, -1]:
        print("\nPlayer2 Score:")
        print(possibilities[5])
    
    #Score for player3
    if summary3 == [1, 1, 1]:
        print("Player3 Score:")
        print(possibilities[0])
    elif summary3 == [1, -1, 1]:
        print("Player3 Score:")
        print(possibilities[1])
    elif summary3 == [-1, 1, 1]:
        print("Player3 Score:")
        print(possibilities[2])
    elif summary3 == [-1, -1, -1]:
        print("Player3 Score:")
        print(possibilities[3])
    elif summary3 == [-1, 1, -1]:
        print("Player3 Score:")
        print(possibilities[4])
    elif summary3 == [1, -1, -1]:
        print("Player3 Score:")
        print(possibilities[5])


    again = input("\nWould you like to play again? \n \n Y/N \nAnswer: ")
    if again == "n" or again == "N":
        print("\n Thanks for playing!")
        break
    elif again == "y" or again == "Y":
        starting = True
    else:
        print("\n Please pick between Y/N")







#Thousand lines pog! :)