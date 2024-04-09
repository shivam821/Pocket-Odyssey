from typing import Tuple

class Customization:
    """Class to manage customization options for a character."""

    def __init__(self):
        """Initialize a new instance of Customization."""
        self.hair_color = None
        self.shirt = None
        self.pants = None
        self.shoes = None

    def customize_appearance(self, appearance: Tuple[str, str, str, str]):
        """Customize hair color, shirt, pants, and shoes colors.

        Args:
            color (Tuple[str, str, str, str]): A tuple containing hair, shirt, pants, and shoes colors respectively.
        """
        self.hair_color = appearance[0]
        self.shirt = appearance[1]
        self.pants = appearance[2]
        self.shoes = appearance[3]

class Backpack:
    """A backpack for the hero to store items."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the backpack."""
        self.items.append(item)

    def remove_item(self, item):
        """Remove an item from the backpack."""
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item.name} is not in the backpack.")

    def display_items(self):
        """Display all items in the backpack."""
        print("Items in the backpack:")
        for item in self.items:
            print(f"- {item.name}: {item.description}")
