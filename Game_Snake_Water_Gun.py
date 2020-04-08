# Game
# Snake water gun

import random

choices=["Snake","Water","Gun"]
player=input("Enter player name : ")
play_again="Y"
while(play_again.upper()=="Y"):
    games = 10
    computer_points = 0
    player_points = 0
    draw = 0
    while (games>0):
        print(f"------------- Game number : {11-games} -------------")
        print(f"Score : COMPUTER : {computer_points} | {player.upper()} : {player_points} | DRAW : {draw}")
        computer_choice = random.choice(choices)
        user_choice=input("Please enter your choice [Snake/Watr/Gun] 'S' for Snake 'W' for Water 'G' for Gun  :  ")

        if(user_choice.upper()=="S" and computer_choice=="Water") \
                or (user_choice.upper()=="W" and computer_choice=="Gun")\
                or (user_choice.upper()=="G" and computer_choice=="Snake"):
            player_points=player_points+1
            print("You win the match...!!!")
        elif(user_choice.upper()=="S" and computer_choice=="Snake") \
                or (user_choice.upper()=="W" and computer_choice=="Water")\
                or (user_choice.upper()=="G" and computer_choice=="Gun"):
            draw=draw+1
            print("Draw the match...!!!")
        else:
            computer_points=computer_points+1
            print("You lost the match...!!!")
        games=games-1

    print("--"*50)
    print(f"| {' '* 48}|")
    print(f"| Scorecard : COMPUTER : {computer_points} | {player.upper()} : {player_points} | DRAW : {draw}")
    if player_points>computer_points:
        print(f"| {player.upper()} win the series.....!!! Congratulations....!!!")
    elif player_points<computer_points:
        print(f"| COMPUTER win the series.....!!!")
    else:
        print(f"| Series Drawn ")
    print(f"| {' ' * 48}|")
    print("--" * 50)

    play_again=input("Do u want to play again?  Y/N : ")
print("Thanks for playing the game... !!!")
