import random

destinations = ["San Diego.", "Chicago.", "Stillwater.", "Eau Claire."]
restaurants = ["The Pub.", "The Grill.", "The Seashack.", "The Vegan."]
mode_of_transportations = ["Train.", "Airplane.", "Bicycle.", "Dogsled."]
entertainments = ["dancing.", "watch a Movie.", "roller skating.", "feeding pigeons."]

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
# print(returned rand_output)


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

def generated_list():
    trips = ["Destination:", "Transportation:", "Restaurant:", "Entertainment:"]
    for item in trips:
        print(item)
generated_list()
print(selected_choice)
   

   
