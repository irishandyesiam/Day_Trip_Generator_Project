import random

destinations = ["San Diego.", "Chicago.", "Stillwater.", "Eau Claire."]
restaurants = ["The Pub.", "The Grill.", "The Seashack.", "The Vegan."]
mode_of_transportations = ["Train.", "Airplane.", "Bicycle.", "Dogsled."]
entertainments = ["Dancing.", "Watch a movie.", "Roller skating.", "Feeding pigeons."]

example_day = []

# greeting
print("Hello, and welcome to the Day Trip Generator. Please see your list below.")

# random generated day trip list

def destination():    
    rand_number = random.randrange(0,4)
    rand_out = (destinations[rand_number])
    return rand_out 
example_day.append (destination())

def restaurant():    
    rand_number = random.randrange(0,4)
    rand_out = (restaurants[rand_number])
    return rand_out
example_day.append (restaurant())

def mode_of_transportation():    
    rand_number = random.randrange(0,4)
    rand_out = (mode_of_transportations[rand_number])
    return rand_out
example_day.append (mode_of_transportation())

def entertainment():    
    rand_number = random.randrange(0,4)
    rand_out = (entertainments[rand_number])
    return rand_out
example_day.append (entertainment())

def generated_list():
    trips = ["Destination: ", "Restaurant: ", "Transportation: ", "Entertainment: "]
    length_of_list = len(trips)
    sequence = range(length_of_list)
    for item in sequence:
        print(trips[item] + example_day[item])
generated_list()

# no_loop_revision

def no_loop():
    print("Which feature do you want to try again?")
    answer = input("Destination, Restaurant, Transportation, or Entertainment. ")
    if answer == "Destination":
        revised = destination()
        example_day[0] = revised
        generated_list()
        confirm_day_trip()
    elif answer == "Restaurant":
        revised = restaurant()
        example_day[1] = revised
        generated_list()
        confirm_day_trip()
    elif answer == "Transportation":
        revised = mode_of_transportation()
        example_day[2] = revised
        generated_list()
        confirm_day_trip()
    elif answer == "Entertainment":
        revised = entertainment()
        example_day[3] = revised
        generated_list()
        confirm_day_trip()
    else:
        print("I didn't understand your answer.")
        
# confirm trip

def confirm_day_trip():
    is_satisfied = False
    while is_satisfied == False:
        is_satisfied = False
        print("Please review the list. See anything that you want to change?")
        answer = input("yes/no ")
        if answer == "no":
            print("Cool. Here is your completed trip.") 
            complete_trip()
            is_satisfied = True
        elif answer == "yes":
            print("Alrighty then.")
            no_loop()
        else:
            print("Please enter yes or no.")
            generated_list()
confirm_day_trip()

# complete trip

def complete_trip():
    is_satisfied = True
    while is_satisfied == True:
        generated_list()
        print("Please confirm one last time that this is your complete trip and you are satisfied with the results.")
        answer = input("yes/no ")
        if answer == "no":
            print("Okay, let's do it again.")
            no_loop()
        elif answer == "yes":
            print("Enjoy your day, be safe and come on back for more suggestions.")
            is_satisfied = False
        else:
            print("Please enter yes or no.")

    
# select trip feature
# def select_trip_feature():
#     is_satisfied = False
#     print("Which feature do you want to try again?")
#     answer = input("Destination, Restaurant, Transportation, or Entertainment.")
#     while is_satisfied == False:
#         if answer == "Destination":
#             revised = destination()
#             example_day[0] = revised
#             generated_list()
#             confirm_day_trip()
#         elif answer == "Restaurant":
#             revised = restaurant()
#             example_day[1] = revised
#             generated_list()
#             confirm_day_trip()
#         elif answer == "Transportation":
#             revised = mode_of_transportation()
#             example_day[2] = revised
#             generated_list()
#             confirm_day_trip()
#         elif answer == "Entertainment":
#             revised = entertainment()
#             example_day[3] = revised
#             generated_list()
#             confirm_day_trip()
#         else:
#             print("Please enter: Destination, Restaurant, Transportation, or Entertainment. ")
#             answer = input("Destination, Restaurant, Transportation, or Entertainment.")

# Function 1 - check for satisfiaction WHILE USER NOT SATISFIED, PROMPT FOR FEATURE TO RESELECT
# Function 2 - prompting for feature, re-generating new feature, and going back to first function (NO LOOP IN THIS FUNCTION) **how?**


# rand_rest = (restaurants[rand_number])
    # rand_mot = (mode_of_transportations[rand_number])
    # rand_enter = (entertainments[rand_number])
    # print(f"{rand_dest}, {rand_rest}, {rand_mot}, {rand_enter}")
# example_day = generate_day_trip(rand_dest)

# def generated_list():
#     trips = ["Destination:", "Restaurant:", "Transportation:", "Entertainment:"]
#     length_of_list = len(trips)
#     sequence = range(length_of_list)
#     for item in sequence:
#         print(trips[item] + selected_choice[item])
# generated_list()

# def destination():
#     is_satisfied = False
#     while is_satisfied == False:
#         rand_number = random.randrange(0,4)
#         rand_output = (destinations[rand_number])
#         print("Here is your random destination." , rand_output, "Does this work for you?")
#         answer = input("yes/no ")
#         if answer == "yes": 
#             print("Cool. Moving on.")
#             selected_choice.append(rand_output)
#             break
#         elif answer == "no":
#             print("Let's try again.")
#         else:
#             print("Please enter yes or no.")
#         return rand_output
# destination()