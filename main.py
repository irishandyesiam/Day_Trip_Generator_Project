import random

# Task 1: As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 

destinations = ["San Diego.", "Chicago.", "Stillwater.", "Eau Claire."]
restaurants = ["The Pub.", "The Grill.", "The Seashack.", "The Vegan."]
mode_of_transportation = ["Train.", "Airplane.", "Bicycle.", "Dogsled."]
entertainment = ["dancing.", "watch a Movie.", "roller skating.", "feeding pigeons."]


# Task 2: As a user, I want a destination to be randomly selected for my day trip. 




# destination 

rand_number = random.randrange(0,4)
rand_dest = (destinations[rand_number])

print("Here is your random destination." , rand_dest, "Does this work for you?")

is_satisfied = False
while is_satisfied == False:
    answer = input("yes/no")
    if answer == "yes":
        print("Cool. Moving on.")
        break
    elif answer == "no":
        print("Let's try again.", rand_dest)
    else:
        print("Please enter yes or no.")
# while yes_no 



# while yes_no == "y" or "n":
#     if yes_no == "y":
#         print("Cool. Moving on.")
#         break
#     elif yes_no == "n":
#         print("Let's try again.")
    
    
   

# # restaurant
# rand_number = random.randrange(0,4)
# rand_restr = (restaurants[rand_number])

# which_restr = input("Would you like me to recommend a restaurant? y/n")
# for answer in which_restr:
#     if answer == "y":
#         print("Okay, you will be dining at",rand_restr)
   

# # mode of transportation
# rand_number = random.randrange(0,4)
# rand_mod = (mode_of_transportation[rand_number])

# which_mod = input("Would you like me to recommend a mode of transportation? y/n")
# for answer in which_mod:
#     if answer == "y":
#         print("Okay, you will be traveling via", rand_mod)

# # entertainment
# rand_number = random.randrange(0,4)
# rand_entr = (entertainment[rand_number])

# which_entr = input("Would you like me to recommend a mode of transportation? y/n")
# for answer in which_entr:
#     if answer == "y":
#         print("Okay, your entertainment will be", rand_entr)