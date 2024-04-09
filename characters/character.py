from typing import Tuple
from .customize import Customization

class Hero:
    """Base class for defining a hero character."""

    def __init__(self, name: str, gender: str, attributes=None, abilities=None):
        """Initialize a new instance of Hero.

        Args:
            name (str): The name of the hero.
            gender (str): The gender of the hero ('male' or 'female').
            attributes (dict, optional): Dictionary containing initial attributes of the hero. Defaults to None.
            abilities (dict, optional): Dictionary containing initial abilities of the hero. Defaults to None.
        """
        self.name = name
        self.gender = gender
        self.attributes = attributes if attributes is not None else {}
        self.abilities = abilities if abilities is not None else {}
        self.appearance = Customization()

    def __str__(self):
        """Return a string representation of the hero."""
        return (f"{self.name} ({self.gender}) \n"
                f"Attributes: {self.attributes},\n"
                f"Abilities: {self.abilities},\n"
                f"Appearance: {self.appearance.__dict__}")

    def set_appearance(self, appearance: Tuple[str, str, str, str]):
        """Set the appearance of the hero.

        Args:
            appearance (Tuple[str, str, str, str]): A tuple containing hair, shirt, pants, and shoes colors respectively.
        """
        self.appearance.customize_appearance(appearance)


class Mage(Hero):
    """Class representing a Mage hero character."""

    def __init__(self, gender: str):
        """Initialize a new instance of Mage.

        Args:
            gender (str): The gender of the mage hero ('male' or 'female').
        """
        attributes = {'recovery': 2, 'training': 1, 'exp_gain': 1, 'nurturing': 1, 'exp_level': 0}
        abilities = {'luck': 2, 'respect': 1, 'courage': 1}
        names = {'male': 'Alexander Hayes', 'female': 'Sheila Brooks'}
        super().__init__(names[gender], gender, attributes, abilities)


class Student(Hero):
    """Class representing a Student hero character."""

    def __init__(self, gender: str):
        """Initialize a new instance of Student.

        Args:
            gender (str): The gender of the student hero ('male' or 'female').
        """
        attributes = {'recovery': 1, 'training': 1, 'exp_gain': 2, 'nurturing': 2, 'exp_level': 0}
        abilities = {'luck': 1, 'respect': 2, 'courage': 1}
        names = {'male': 'Ethan Reynolds', 'female': 'Nicky Heart'}
        super().__init__(names[gender], gender, attributes, abilities)


class Athlete(Hero):
    """Class representing an Athlete hero character."""

    def __init__(self, gender: str):
        """Initialize a new instance of Athlete.

        Args:
            gender (str): The gender of the athlete hero ('male' or 'female').
        """
        attributes = {'recovery': 1, 'training': 1.5, 'exp_gain': 1, 'nurturing': 1, 'exp_level': 0}
        abilities = {'luck': 1, 'respect': 1, 'courage': 1.5}
        names = {'male': 'Grant Brooks', 'female': 'Amelia Brooks'}
        super().__init__(names[gender], gender, attributes, abilities)


class Fighter(Hero):
    """Class representing a Fighter hero character."""

    def __init__(self, gender: str):
        """Initialize a new instance of Fighter.

        Args:
            gender (str): The gender of the fighter hero ('male' or 'female').
        """
        attributes = {'recovery': 1.5, 'training': 1, 'exp_gain': 1.5, 'nurturing': 1, 'exp_level': 0}
        abilities = {'luck': 1, 'respect': 1.5, 'courage': 2}
        names = {'male': 'Mike Zander', 'female': 'Olivia Morgan'}
        super().__init__(names[gender], gender, attributes, abilities)
