""""
WORKFLOW OF PROJECT:
1- Input fromuser(Rock , paper , scissor)
2- Computer choice(Computer will choose randomly not conditionally using random module of python)
3- Result print   
    
Cases:
A- Rock
Rock - Rock = tie 
Rock - Paper = Paper win 
Rock - scissor = Rock win 

B - Paper
Paper - Paper = tie
Paper - Rock = Paper win 
Paper - scissor = Scissor win 

C -Scissor
Scissor - Scissor = tie 
Scissor - Rock = Rock win 
Scissor - Paper = Scissor win
  
    
"""""

import random 
item_list = ["Rock" , "Paper " , "Scissor"]

user_choice = input("Enter your move = Rock , Paper , Scissor = ")
comp_choice = random.choice(item_list)  #this function help to pick randomly elements

print(f"User choice = {user_choice} , Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same : Match tie")
    
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer")
        
    else :
        print("Rock smashes scissor = You win")
        
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cut paper, Computer Win")
    else:
        print("Paper covers rock, You win")
        
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cute paper , You win")
    else:
        print("Rock smashes scissor , Computer win")