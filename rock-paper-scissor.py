import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move:")
comp_choice = random.choice(item_list)
print(f"User choice = {user_choice}\nComputer choice = {comp_choice}")
if user_choice == comp_choice:
    print("Both user and computer chose some move: Match tie");
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Computer won");
    else:
        print("User won");
elif user_choice == "Paper":
    if comp_choice  == "Scissor":
        print("Computer won");
    else:
        print("User won");
elif user_choice == "Scissor":
    if comp_choice  == "Rock":
        print("Computer won");
    else:
        print("User won");


