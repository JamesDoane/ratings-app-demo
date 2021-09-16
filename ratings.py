
# put your code here
import random
import os

ratings_dictionary = {}
menu=''

def read_ratings():
    #open the file
    global ratings_dictionary
    ratings_dictionary = {}
    filename = input("what file would you like to read ratings from?")
    ratings_file = open(filename, 'r')

    # for loop to loop over each line in the open file, rstrip to take each line without taking 
    # the next, and split it at the semi-colon,removing the semi-colon from the results.
    # last line sets a new key:value pair equal to the two items in the lists created by the split function.
    for line in ratings_file:
        line2 = line.rstrip('\n').split(':')
        ratings_dictionary[line2[0]] = line2[1]

    ratings_file.close()

def print_ratings(): 
    # for each key in the ratings_dictionary print itself and the corresponding value
    for key in sorted (ratings_dictionary):
        print(key + " is rated at a " + str(ratings_dictionary[key]) + "\n")

    # good practice to close the file, so yeah.
    
def user_rating():
    print("\n")

    restaraunt_rated = input("What restaraunt are you reviewing?\n")
    restaraunt_rating = int(input("And how many stars, out of 5, would you rate the restaraunt?\n"))

    while restaraunt_rating < 1 and restaraunt_rating > 5 or None:
        restaraunt_rating = int(input("No seriously, out of 5, what would you rate the restaraunt?\n"))

    ratings_dictionary[restaraunt_rated] = restaraunt_rating

    go_again = input("Do you have another review to leave? y/n\n")

    if go_again == "y":
        user_rating()

def selection():
    counter = 0
    if counter == 0:
        menu = input("""Welcome to rating restaraunts. enter 1 to retrieve the restaraunts and their ratings. enter 2 to add
        a restaraunt. enter 3 to update a random rating. enter 4 to update a specific rating. 
        enter 5 to list files. enter 6 to import file data. enter 0 to exit the program.\n\n""")
        counter += 1
    return menu

def random_update():
    print("\n")
    to_update = random.choice(list(ratings_dictionary.items()))
    print(to_update[0] + " has a rating of " + to_update[1])
    new_rating = int(input("What should it's rating be instead?\n"))

    while new_rating < 1 and new_rating > 5 or None:
        new_rating = int(input("No seriously, out of 5, what would you rate the restaraunt?\n"))

    ratings_dictionary[to_update[0]] = new_rating


def update_rating():
    print("\n")
    to_update = input("Which restaurant would you like to update?\n")
    if ratings_dictionary.get(to_update):

        new_rating = int(input("What should it's rating be instead?\n"))

        while new_rating < 1 and new_rating > 5 or None:
            new_rating = int(input("No seriously, out of 5, what would you rate the restaraunt?\n"))
    
        ratings_dictionary[to_update] = new_rating

def list_directory():
    dir_list = os.listdir()
    for file in sorted(dir_list):
        if file.endswith(".txt"):
            print("\n" + file + "\n")

def main():
    menu = selection()
    while menu != '0':
        if menu == '1':
            print("\n")
            print_ratings()
            menu = selection()
        elif menu == '2':
            print("\n")
            user_rating()
            menu = selection()
        elif menu == '3':
            print("\n")
            random_update()
            menu = selection()
        elif menu == '4':
            print("\n")
            update_rating()
            menu = selection()
        elif menu == '5':
            print("\n")
            list_directory()
            menu = selection()
        elif menu == '6':
            read_ratings()
            menu = selection()
        else:
            menu = selection()

main()

