from dataclasses import dataclass
from typing import Optional, Union, Dict

class CharacterValidationError(Exception):
  pass

@dataclass
class Character:
  name: str
  health: int
  strength: int
  dexterity: int
  intelligence: int
  cosmetics: Dict[str, str]  # Dictionary to store cosmetic options (key: option name, value: option value)

  def validate_choice(self, choice: Optional[str], options: Optional[list[str]]) -> bool:
    """Validates player choices against available options.

    Args:
      choice: The player's chosen option.
      options: A list of valid options.

    Returns:
      True if the choice is valid, False otherwise.
    """
    if choice is None or options is None:
      raise CharacterValidationError("Missing input for validation: choice or options cannot be None")

    try:
      return choice.lower() in [option.lower() for option in options]
    except AttributeError:
      print(f"Invalid input type of choices. Exepected string, got {type(choice)}")
      return False
    

  def update_stats(self, stat: str, value: int) -> Union['Character', str]:
    """Updates a character's stat.

    Args:
      stat: The stat to update (e.g., "health", "strength").
      value: The amount to change the stat by.

    Returns:
      The updated character object if stat is valid, error otherwise.
    """
    if stat not in ["health", "strength", "dexterity", "intelligence"]:
        raise CharacterValidationError(f"Invalid stat: {stat}")
    try:
        setattr(self, stat, getattr(self, stat) + value)
        return self
    except TypeError:
        raise CharacterValidationError("Invalid value type for stat update")

  def update_cosmetics(self, option: str, new_value: str):
    """Updates a character's cosmetic option.

    Args:
      option: The cosmetic option to update (e.g., "hairstyle", "clothing").
      new_value: The new value for the chosen option.
    """
    if not isinstance(option, str) or not isinstance(new_value, str):
      raise CharacterValidationError("Option and new value must be strings")

    if option not in self.cosmetics:
        raise CharacterValidationError(f"Invalid cosmetic option: {option}")

    self.cosmetics[option] = new_value


  def display_customization(self):
    """Displays the character's current customization options."""
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Strength: {self.strength}")
    print(f"Dexterity: {self.dexterity}")
    print(f"Intelligence: {self.intelligence}")
    print("Cosmetics:")
    for option, value in dict(self.cosmetics).items():
      print(f"- {option}: {value}")


#Sample test case
'''
my_char = Character("Brooke", 100, 10, 0, 5, {"hairstyle": "short"})
my_char.display_customization()

# Valid choices
valid_weapon_options = ["sword", "axe", "staff"]
valid_hair_options = ["short", "long", "ponytail"]

print(my_char.validate_choice("axe", valid_weapon_options))  # True (case-insensitive)
print(my_char.validate_choice(10, valid_hair_options))  # False (not a string)

#Updating player stats
my_char.update_stats("strength", 20) #Increases the strength by 20
my_char.update_stats("intelligence", 4) #Increses the intelligence by 4
print(my_char.__repr__)'''