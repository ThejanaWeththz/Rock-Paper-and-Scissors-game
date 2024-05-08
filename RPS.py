import random

# Create Variables
name_list=["Rock","Paper","Scissors"]
player_score=0
cpu_score=0

# Interface
print("\t\tWelcome to the Rock,Paper,Scissors Game\n")
name=input("Enter Username : ")
print("\nPlayers in game|",name,"and Computer\n\nThe rules are simple: \t1. Paper wins over Rock\n\t\t\t2. Rock wins over Scissors\n\t\t\t3. Scissors win over Paper\n")

# Loop
while True:
    # Shuffle list
    random.shuffle(name_list)
    while True:
        # Input
        user_input=str(input("Enter your choice...(Rock,Paper,Scissors) : "))
        if user_input not in (name_list):
            print("Enter choice correctly...(Rock,Paper,Scissors)\n")
            continue
        # Repeat again
        if name_list[2]==user_input:
            print("Both chose the same name",name_list[2],"try again")
            random.shuffle(name_list)
            continue
        else:
            break
    if name_list[2]=="Rock" and user_input=="Paper":
        print("You Win, Computer selected",name_list[2])
        player_score+=1

    elif name_list[2]=="Scissors" and user_input=="Rock":
        print("You Win, Computer selected",name_list[2])
        player_score+=1

    elif name_list[2]=="Paper" and user_input=="Scissors":
        print("You Win, Computer selected",name_list[2])
        player_score+=1
        
    if name_list[2]=="Paper" and user_input=="Rock":
        print("You Loss, Computer selected",name_list[2])
        cpu_score+=1
    
    elif name_list[2]=="Rock" and user_input=="Scissors":
        print("You Loss, Computer selected",name_list[2])
        cpu_score+=1
        
    elif name_list[2]=="Scissors" and user_input=="Paper":
        print("You Loss, Computer selected",name_list[2])
        cpu_score+=1
        
    restart=input("Do you want to play again? (y/n) : ")
    if restart=="y":
        continue
    elif restart=="n":
        print("\nPoints awarded to = ",name,player_score)
        print("\nPoints awarder to Computer = ",cpu_score)
        break
    else:
        break
    
