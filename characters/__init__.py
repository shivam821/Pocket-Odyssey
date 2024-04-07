HAIR_OPTIONS = ['Brown', 'Blond', 'Black', 'Red']
CLOTHES_COLOURS = ['Black', 'Green', 'Blue', 'Yellow']
SHIRT_OPTIONS = ['Short', 'Medium', 'Long', 'Vest']
PANTS_OPTIONS = ['Slacks', 'Jeans', 'Jorts', 'Shorts']
SHOES_OPTIONS = ['Sandals', 'Sneakers', 'Formal', 'Trainers']


from .character import Mage, Student, Athlete, Fighter
hero_set = [Mage,Student,Athlete,Fighter]
hero_set_names = [hero.__name__ for hero in hero_set]
character = []

def select_gender():
    """Prompt the player to select their gender."""
    while True:
        try:
            gender = int(input("1. Male or 2. Female ? "))
            if gender == 1:
                return 'male'
            elif gender == 2:
                return 'female'
            else:
                print("Please choose either 1 or 2.")
        except ValueError:
            print("Please enter either 1 or 2.")

def select_hero_class(character_gender):
    """Prompt the player to select their hero class."""
    print("Choose your starting Hero class:")
    player_options = {}
    for index, hero in enumerate(hero_set):
        player = hero(character_gender)
        player.set_appearance((
            HAIR_OPTIONS[index],
            SHIRT_OPTIONS[index],
            PANTS_OPTIONS[index],
            SHOES_OPTIONS[index])
        )
        player_options[index] = player
        print(f"Option {index + 1}")
        print(f"{player}")
        print("_" * 150 + '\n')

    while True:
        try:
            player_selection = int(input("Enter the number of your choice: ")) - 1
            if player_selection in range(len(hero_set)):
                chosen_hero = player_options[player_selection]
                return chosen_hero
            else:
                print("Please choose a number within the range.")
        except ValueError:
            print("Please enter a valid number.")

def character_selection():
    """Allow the player to select their character (gender and hero class)."""
    print("Welcome to the world of Pocket Beasts!")
    character_gender = select_gender()
    chosen_hero = select_hero_class(character_gender)
    return chosen_hero

if __name__ == '__main__':
    chosen_hero = character_selection()
    # character.append(character_gender)
    character.append(chosen_hero)
