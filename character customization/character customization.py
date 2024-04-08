from dataclasses import dataclass

@dataclass
class Character:
  name: str
  health: int
  strength: int
  dexterity: int
  intelligence: int
  cosmetics: dict[str, str]  # Dictionary to store cosmetic options (key: option name, value: option value)

  def validate_choice(self, choice, options):
    """Validates player choices against available options.

    Args:
      choice: The player's chosen option.
      options: A list of valid options.

    Returns:
      True if the choice is valid, False otherwise.
    """
    return choice.lower() in [option.lower() for option in options]

  def update_stats(self, stat, value):
    """Updates a character's stat.

    Args:
      stat: The stat to update (e.g., "health", "strength").
      value: The amount to change the stat by.
    """
    if stat in ["health", "strength", "dexterity", "intelligence"]:
      setattr(self, stat, getattr(self, stat) + value)
    else:
      print(f"Invalid stat: {stat}")

  def update_cosmetics(self, option, new_value):
    """Updates a character's cosmetic option.

    Args:
      option: The cosmetic option to update (e.g., "hairstyle", "clothing").
      new_value: The new value for the chosen option.
    """
    if option in self.cosmetics:
      self.cosmetics[option] = new_value
    else:
      print(f"Invalid cosmetic option: {option}")

  def display_customization(self):
    """Displays the character's current customization options."""
    print(f"Name: {self.name}")
    print(f"Health: {self.health}")
    print(f"Strength: {self.strength}")
    print(f"Dexterity: {self.dexterity}")
    print(f"Intelligence: {self.intelligence}")
    print("Cosmetics:")
    for option, value in self.cosmetics.items():
      print(f"- {option}: {value}")
