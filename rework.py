import random

destinations = ["San Diego.", "Chicago.", "Stillwater.", "Eau Claire."]
restaurants = ["The Pub.", "The Grill.", "The Seashack.", "The Vegan."]
mode_of_transportations = ["Train.", "Airplane.", "Bicycle.", "Dogsled."]
entertainments = ["Dancing.", "Watch a movie.", "Roller skating.", "Feeding pigeons."]

example_day = []

# greeting
print("Hello, here is your randomly generated day trip. Please review.")
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