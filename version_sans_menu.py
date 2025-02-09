class Part:
    """ Class to manage parts of a ship. """

    def __init__(self, name, material):
        """
        Initialisation of the class.
        :param name: Name of a part.
        :param material: His material.
        """
        self.name = name
        self.material = material

    def change_material(self, new_material):
        """
        Change the material use to make one of the part.
        :param new_material: The new material.
        :return: ∅
        """
        self.material = new_material

    def __str__(self):
        """
        Display information about one part of the skip.
        :return: The information.
        """
        infos = f"{self.name.capitalize()} is a part of the ship, it's make on {self.material}."
        return infos


class Ship:
    """ Class to manage a ship."""

    def __init__(self, name):
        """
        Initialisation of the class.
        :param name: Name of the ship.
        """
        self.name = name
        self.__parts = {}

    def add_part(self, part):
        """
        Add a part to the ship.
        :param part: One of the ship parts.
        :return: ∅
        """
        self.__parts[part.name] = part

    def display_state(self):
        """
        Display all the details about the ship parts.
        :return: ∅
        """
        print(f"\nThe ship {self.name} consists of the following parts:\n")
        for part in self.__parts.values():
            print(part.__str__())

    def replace_part(self, part_name, new_part):
        """
        Replace one of the ship part.
        :param part_name: Name of the part to replace.
        :param new_part: The new part to be added to the ship.
        :return: ∅
        """
        self.__parts[part_name] = new_part

    def change_part(self, part_name, new_material):
        """
        Modifie one of the ship part.
        :param part_name: Name of the part to be modified.
        :param new_material: The new material of the part.
        :return: ∅
        """
        self.__parts[part_name].change_material(new_material)


class RacingShip(Ship):
    """ Class to manage a racing ship. """

    def __init__(self, name, max_speed):
        """
        Initialisation of the class.
        :param name: Name of the racing ship.
        :param max_speed: His maximum speed.
        """
        super().__init__(name)
        self.__max_speed = max_speed

    def display_speed(self):
        """
        Display the racing ship maximum speed.
        :return: His maximum speed.
        """
        return self.__max_speed


# Creation of the different parts of a traditional ship.
sail = Part("sail", "cotton")
hull = Part("hull", "oak wood")
mast = Part("mast", "pine wood")
rudder = Part("rudder", "ash wood")
oar = Part("oar", "cherry wood")
anchor = Part("anchor", "iron")
deck = Part("deck", "teak wood")
rope = Part("rope", "hemp")
boom = Part("boom", "cedar wood")
keel = Part("keel", "mahogany wood")

# Creation of the traditional ship.
galleon = Ship("galleon")

galleon.add_part(sail)
galleon.add_part(hull)
galleon.add_part(mast)
galleon.add_part(rudder)
galleon.add_part(oar)
galleon.add_part(anchor)
galleon.add_part(deck)
galleon.add_part(rope)
galleon.add_part(boom)
galleon.add_part(keel)

# Display ship details.
galleon.display_state()

# Modification of the material of the mast
print(f"\nThe ID of the 'mast' object before modification is {id(mast)}")
galleon.change_part("mast", "cedar wood")
print(f"\nThe ID of the 'mast' object after modification is {id(mast)}")

# Display again ship details after the modification
galleon.display_state()
