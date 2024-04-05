import random 
import string 

# Dictionary to store player IDs
IDS = {"Muhammad Zain":"ABC"}    #Example ID for sample purpose 

def extractKey(my_dict, search_value):
    """
    Extracts the key associated with a given value in a dictionary.

    Args:
        my_dict (dict): The dictionary to search.
        search_value: The value to search for.

    Returns:
        The key associated with the search value, or None if not found.
    """
    for key, value in my_dict.items():
        if value == search_value:
            return key
    return None


#  Function to display the main menu 
def main_menu():
    """Displays the main menu options."""
    print("1. Start Game")
    print("2. Options")
    print("3. Exit")


""" Function to generate a new player ID """
def createID():
    """
    Generates a new player ID.

    Returns:
        A string representing the new player ID.
    """

    digits = random.randint(10,90)
    character = random.choice(string.ascii_letters)
    doubleDigits = random.randint(1000,9000)
    characterAnother = random.choice(string.ascii_letters)
    finalID = str(digits)+character+str(doubleDigits)+characterAnother
    return finalID

# Function to start the game 
def start_game():
    """Manages the starting of a new game or loading an existing one."""
    while True:
        print("1. New Game")
        print("2. Load Game")
        print("3. Help/Instructions")
        print("4. Exit")
        choice_1 = int(input("\nEnter your choice: "))
        if(choice_1==1):
            takeName= input("\nWelcome Newbie!\nEnter your name: ")
            print(f"\t\t\t\t\t\t\tName - {takeName}")
            newID = createID()
            print(f"\t\t\t\t\t\t\tID - {newID}")
            IDS[takeName]=newID
            print("Starting New Game....\n")
        elif(choice_1==2):
            takeID = input("Enter your ID: ")
            if(extractKey(IDS,takeID) != None):
                print(f"Welcome Back!\n\t\t\t\t\t\t\tName - {extractKey(IDS,takeID)}")
                print(f"\t\t\t\t\t\t\tID - {takeID}")
                print("Continue Game..\n")
            else:
                print("No ID found..\n")
                
        elif(choice_1==3):
            print("- INSTRUCTION -")
            print("If you are new to the game just press start game and enter your name, after that you will get your specific ID which you can use later for continue the game from where you left off.")
            print()
        elif(choice_1==4):
            break
        else:
            invalid_option()
        
# Function to display the game options
def show_options():
    print(" -- - -- - -- - -- -- Options -- --  -- -- - - -- - -- - ")
    print("w - forward")
    print("s - backward")
    print("a - move left")
    print("d - move right")
    print("z - shoot fire balls")
    print("r - reload weapon")
    print("i - pick an item")
    print("o - throw an item")
    print("b - call out your creature")
    print("c - cast a spell")
    print("f - use flashlight")
    print("t - talk to NPC")
    print("e - interact with environment")
    print("m - view map")
    print("q - quit game")

# Function to handle invalid options
def invalid_option():
    print("Invalid option.")


# Main function to run the game
def main():
    """Main function to run the game."""
    
    print("\n--------------------------POCKET ODYSSEY-------------------------\n\n")
    while True:
        main_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            show_options()
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break
        else:
            invalid_option()

if __name__ == "__main__":
    main()
