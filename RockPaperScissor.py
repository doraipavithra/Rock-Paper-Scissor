"""
DESCRPTION OF THE PROJECT
1- Input from the user(Rock, Paper, Scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Print Result

CASES:
A- Rock
Rock - Rock = TIE
Rock - Paper = Paper WIN
Rock - Scissor = Rock WIN

B- Paper
Paper - Paper = TIE
Paper - Rock = Paper WIN
Paper - Scissor = Scissor WIN

C- SCISSOR
Scissor - Scissor = TIE
Scissor - Rock = Rock WIN
Scissor - Paper = Scissor WIN
"""

import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice {comp_choice}")

if user_choice == comp_choice:
    print(" Both choose the same : Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock = Computer WIN")
    else:
        print(" Rock Breaks Scissor = YOU WIN")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("scissor cuts the paper = COMPUTER WIN")
    else:
        print("Paper covers the rock = YOU WIN")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock breaks the Scissor = COMPUTER WIN")
    else:
        print("scissor cuts the paper = YOU WIN")