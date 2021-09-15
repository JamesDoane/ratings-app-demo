
# put your code here


ratings_dictionary = {}
menu=''

def read_ratings():
    #open the file
    ratings_file = open('./scores.txt', 'r')

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
    
    restaraunt_rated = input("What restaraunt are you reviewing?\n")
    restaraunt_rating = int(input("And how many stars, out of 5, would you rate the restaraunt?\n"))

    while restaraunt_rating < 1 and restaraunt_rating > 5 or None:
        restaraunt_rating = int(input("No seriously, out of 5, what would you rate the restaraunt?\n"))

    ratings_dictionary[restaraunt_rated] = restaraunt_rating

    go_again = input("Do you have another review to leave? y/n\n")

    if go_again == "y":
        user_rating()

def selection():
    menu = input("""Welcome to rating restaraunts. enter 1 to retrieve the restaraunts and their ratings. enter 2 to add
     a restaraunt. enter 3 to exit the program. \n""")
    return menu
    
def main():
    menu = selection()
    read_ratings()
    while menu != '3':
        if menu == '1':
            print_ratings()
            menu = selection()
        elif menu == '2':
            user_rating()
            menu = selection()
        else:
            menu = selection()
main()

