import random

destinations = ["San Diego.", "Chicago.", "Stillwater.", "Eau Claire."]
restaurants = ["The Pub.", "The Grill.", "The Seashack.", "The Vegan."]
mode_of_transportations = ["Train.", "Airplane.", "Bicycle.", "Dogsled."]
entertainments = ["Dancing.", "Watch a movie.", "Roller skating.", "Feeding pigeons."]

selected_choice = []

# destination 
def destination():
    is_satisfied = False
    while is_satisfied == False:
        rand_number = random.randrange(0,4)
        rand_output = (destinations[rand_number])
        print("Here is your random destination." , rand_output, "Does this work for you?")
        answer = input("yes/no ")
        if answer == "yes": 
            print("Cool. Moving on.")
            selected_choice.append(rand_output)
            break
        elif answer == "no":
            print("Let's try again.")
        else:
            print("Please enter yes or no.")
        return rand_output
destination()

# restaurant
def restaurant():
    is_satisfied = False
    while is_satisfied == False:
        is_satisfied = False
        rand_number = random.randrange(0,4)
        rand_output = (restaurants[rand_number])
        print("Here is your random restaurant." , rand_output, "Does this work for you?")
        answer = input("yes/no ")
        if answer == "yes":
            print("Cool. Moving on.")
            selected_choice.append(rand_output)
            break
        elif answer == "no":
            print("Let's try again.")
        else:
            print("Please enter yes or no.")
restaurant()

# mode_of_transportations
def mode_of_transportation():
    is_satisfied = False
    while is_satisfied == False:
        is_satisfied = False
        rand_number = random.randrange(0,4)
        rand_output = (mode_of_transportations[rand_number])
        print("Here is your random mode of transportation." , rand_output, "Does this work for you?")
        answer = input("yes/no ")
        if answer == "yes":
            print("Cool. Moving on.")
            selected_choice.append(rand_output)
            break
        elif answer == "no":
            print("Let's try again.")
        else:
            print("Please enter yes or no.")
mode_of_transportation()

# entertainments
def entertainment():
    is_satisfied = False
    while is_satisfied == False:
        is_satisfied = False
        rand_number = random.randrange(0,4)
        rand_output = (entertainments[rand_number])
        print("Here is your random entertainment." , rand_output, "Does this work for you?")
        answer = input("yes/no ")
        if answer == "yes":
            print("Cool. Moving on.")
            selected_choice.append(rand_output)
            break
        elif answer == "no":
            print("Let's try again.")
        else:
            print("Please enter yes or no.")
entertainment()

# generated list
def generated_list():
    trips = ["Destination:", "Restaurant:", "Transportation:", "Entertainment:"]
    length_of_list = len(trips)
    sequence = range(length_of_list)
    for item in sequence:
        print(trips[item] + selected_choice[item])
generated_list()

# select trip feature
def select_trip_feature():
    print("Which feature do you want to try again?")
    answer = input("Destination, Restaurant, Transportation, or Entertainment.")
    is_satisfied = False
    while is_satisfied == False: # after getting new random feature, how do I get out of loop?
        if answer == "Destination":
            destination()
        elif answer == "Restaurant":
            restaurant()
        elif answer == "Transportation":
            mode_of_transportation()
        elif answer == "Entertainment":
            entertainment()
        else:
            print("Please enter: Destination, Restaurant, Transportation, or Entertainment. ")
select_trip_feature()

# confirm trip
def confirm_day_trip():
    is_satisfied = False
    while is_satisfied == False:
        is_satisfied = False
        print("Please confirm your day trip.")
        answer = input("yes/no ")
        if answer == "yes":
            print("Cool. Enjoy your day.")
            break
        elif answer == "no":
            print("Alrighty then.")
            select_trip_feature()
        else:
            print("Please enter yes or no.")
confirm_day_trip()
            

   
