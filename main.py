import json
import os

class Pocket_Beast:
    def __init__(self, name, level=0):
      self.name = name
      self.level = level

    def train(self):
      self.level += 1
      print(f'You have trained {self.name} and increased their level to {self.level}')

    def status(self):
      print(f'{self.name} current level is {self.level}')
      
    def display_info(self):
        print(f'{self.name}:')
        print(pocket_beasts_info[self.name])
        print()

    @staticmethod
    def display_usernames(directory):
        files = os.listdir(directory)
        usernames = [file[:-5] for file in files if file.endswith('.json')]
        return usernames

    def battle(self, current_username, directory):
        if self.level > 10:
            all_users = self.display_usernames(directory)
            other_users = [user for user in all_users if user != current_username]
            if other_users:
                print("Users available for battle:")
                print("\n".join(other_users))
            else:
                print("No other users are available for battle.")
        else:
            print("Your pocket beast's level is not above 10. Train more to participate in battles.")


    


print('Welcome to Pocket Odyssey: Evolve to Greatness! Choose your Pocket Beast and train it to level 100 and beyond. Embark on an epic journey of evolution and adventure. Are you ready to become a legendary trainer?')
print()

print('\n1. New Game\n2. Load Game\n3. Exit')
print()

user_choice = input('Enter your choice (1/2/3): ')
print()

if user_choice == '1':
    input_user_name = input('Enter your username: ')

    pocket_beasts_info = {
        'Leafy': 'A charming Grass-type Pocket Beast with vibrant green foliage. Known for its agile movements and soothing aura, Leafy harnesses the power of nature in battle, using razor-sharp leaves and revitalizing abilities to overcome opponents.',
        'Flarey': 'A fierce Fire-type Pocket Beast, Flarey blazes with fiery intensity. With its fiery mane and sharp claws, Flarey commands the power of flames, unleashing scorching attacks that leave opponents engulfed in flames and ashes.',
        'Splashy': 'An energetic Water-type Pocket Beast, Splashy brims with aquatic grace. With its sleek blue body and shimmering scales, Splashy harnesses the power of the ocean, drenching opponents with powerful water-based attacks and riding waves to victory.',
        'Sparky': 'A spirited Electric-type Pocket Beast, Sparky crackles with electric energy. With its electrifying fur and sharp claws, Sparky commands the power of lightning, zapping opponents with shocking speed and agility, leaving them stunned in its wake.'
    }

    pocket_beasts = pocket_beasts_info.keys()

    print('These are the Pocket Beasts you can choose from:')
    for index, beast in enumerate(pocket_beasts, start=1):
        print(f"{index}. {beast} ({pocket_beasts_info[beast].split('.')[0]})")
    print()

    while True:
        pocket_beast_name = input('Enter your pocket_beast name: ').capitalize()
        
        if pocket_beast_name in pocket_beasts:
            pocket_beast = Pocket_Beast(pocket_beast_name)
            print()

            pocket_beast.display_info()

            print(f'Hi {input_user_name}!. You can interact with {pocket_beast_name} by typing:\n1. Train: To increase the level of the Pocket Beast\n2. Battle: To battle other players.\n3. Status: To check the current level.\n4. Exit: To exit.\n')

            while True:
                user_choice = input(' > ').lower()

                if user_choice == 'train':
                    pocket_beast.train()
                elif user_choice =='battle' :
                    pocket_beast.battle()
                elif user_choice == 'status':
                    pocket_beast.status()
                elif user_choice == 'exit':
                    break
                else:
                    print('Invalid input. Please choose a valid option (train, status, or exit).\n')

            print('Goodbye!')
            break
        else:
            print('Sorry, the entered pet name is not valid. Please choose a pet name from the available options.\n')


    user_name = input_user_name.capitalize()
    save_file_name = input_user_name + '.json'
    save_data = {
        'username': input_user_name.capitalize(),
        'pocket_beast_name': pocket_beast_name,
        'pocket_beast_level': pocket_beast.level
    }
    with open(save_file_name, 'w') as save_json_file:  # Using 'with' for automatic file closing
        json.dump(save_data,save_json_file, indent=4)
    print(f'Game saved with the name {save_file_name}')

elif user_choice == '2':
    input_user_name = input('Enter your username: ')
    user_name = input_user_name.capitalize()
    save_file_name = input_user_name + '.json'
    if os.path.exists(save_file_name):
        print(f'File {input_user_name}.json is found.')
        with open(save_file_name, 'r') as save_json_file:
            save_data = json.load(save_json_file)
            json_string = json.dumps(save_data, indent=6)
            print()
            print("User Data:")
            print(f"Username: {save_data['username']}")
            print(f"Pocket Beast Name: {save_data['pocket_beast_name']}")
            print(f"Pocket Beast Level: {save_data['pocket_beast_level']}")
            print()

            pocket_beast = Pocket_Beast(save_data["pocket_beast_name"], save_data["pocket_beast_level"])

            while True:
                print(f'Hi {input_user_name}!. You can interact with {save_data["pocket_beast_name"]} by typing:\n1. Train: To increase the level of the Pocket Beast\n2. Battle: To battle other players.\n3. Status: To check the current level.\n4. Exit: To exit.\n')

                user_choice = input(' > ').lower()

                if user_choice == 'train':
                    pocket_beast.train()
                    # Update level in save_data after training
                    save_data['pocket_beast_level'] = pocket_beast.level
                    with open(save_file_name, 'w') as save_json_file:  # Save updated data to JSON file
                        json.dump(save_data, save_json_file, indent=4)
                elif user_choice == 'status':
                    pocket_beast.status()
                elif user_choice == 'battle':
                    pocket_beast.battle(save_data['username'], '.')  # Pass current username and directory
                elif user_choice == 'exit':
                    print('Goodbye!')
                    break
                else:
                    print('Invalid input. Please choose a valid option (train, status, or exit).\n')
    else:
        print(f'No existing file found for user {user_name}')
        print()
    
elif user_choice == '3':
    exit()
else:
    print('Enter a valid input')