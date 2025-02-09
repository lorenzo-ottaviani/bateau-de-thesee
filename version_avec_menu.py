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
        self.history = []

    def add_part(self, part):
        """
        Add a part to the ship.
        :param part: One of the ship parts.
        :return: ∅
        """
        self.__parts[part.name] = part
        self.history.append(f"Added part: {part.name} made of {part.material}")

    def get_parts(self):
        """
        Display the dictionary of the parts.
        :return: The dictionary.
        """
        return self.__parts

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
        self.history.append(f"Replaced part: {part_name} with {new_part.name} made of {new_part.material}.")

    def change_part(self, part_name, new_material):
        """
        Modifie one of the ship part.
        :param part_name: Name of the part to be modified.
        :param new_material: The new material of the part.
        :return: ∅
        """
        self.__parts[part_name].change_material(new_material)
        self.history.append(f"Changed material of {part_name} with {new_material}.")

    def display_history(self):
        """
        Display the history of modifications.
        :return: ∅
        """
        print(f"\nModification history of the ship {self.name}:\n")
        if not self.history:
            print("No modifications yet.")
        else:
            for entry in self.history:
                print(entry)


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


class Galleon(Ship):
    """ Class to manage a Galleon. """

    def __init__(self, name):
        """
        Initialisation of the class.
        :param name: Name of the racing ship.
        """
        super().__init__(name)
        self.create_galleon()

    def create_galleon(self):
        """
        Create the galleon.
        :return: ∅
        """
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
        self.add_part(sail)
        self.add_part(hull)
        self.add_part(mast)
        self.add_part(rudder)
        self.add_part(oar)
        self.add_part(anchor)
        self.add_part(deck)
        self.add_part(rope)
        self.add_part(boom)
        self.add_part(keel)


def main(view_menu=True):
    """
    Main function of the program.
    :param view_menu: Display the menu if true.
    :return: ∅
    """

    def display_menu():
        """
        Display the menu on the terminal.
        :return: ∅
        """
        print("\nWelcome to Thesee's ship experience!\n")
        print("In this menu, you can choose between different options:")
        print("\n1: Change a piece of the galleon")
        print("2: Change a material of one of the piece")
        print("3: Display ship details")
        print("4: Display modification history")
        print("5: Exit\n")

    galleon_ship = Galleon("Queen Elisabeth")

    if view_menu is True:
        display_menu()

    menu_option = input("Choose your option (enter '1' to '5'): ")

    match menu_option:

        case "1":
            piece = input("Enter the name of the part to be changed: ")
            new_name = input("Enter the name of the new part: ")
            new_material = input("Enter the material of the new part: ")
            new_part = Part(new_name, new_material)
            galleon_ship.replace_part(piece, new_part)
            main()

        case "2":
            piece = input("Enter the name of the part to be modified: ")
            new_material = input("Enter the new material: ")
            galleon_ship.change_part(piece, new_material)
            main()

        case "3":
            galleon_ship.display_state()
            main(view_menu=False)

        case "4":
            galleon_ship.display_history()
            main(view_menu=False)

        case "5":  # Exit the program.
            exit()

        case _:  # The user entered an invalid input.
            print("Invalid input!\n")
            main(view_menu=False)  # Come back to choice of menu options.


if __name__ == "__main__":  # The program will be run only if executed directly, not if it called from another program.
    main()
