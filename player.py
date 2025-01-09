"""
Module defining the Player class for the game.
"""

class Player:
    """
    Represents a player in the game.

    Attributes:
        name (str): The name of the player.
        inventory (dict): The player's inventory.
        history (list): The list of rooms visited by the player.
        current_room (Room): The current room the player is in.
        hall (Room): The initial room (hall) of the player.
        last_room (Room): The last room the player was in.
    """

    def __init__(self, name, hall):
        """
        Initializes a Player instance.

        Args:
            name (str): The name of the player.
            hall (Room): The starting room of the player.
        """
        self.name = name
        self.inventory = {}
        self.history = []
        self.current_room = hall
        self.hall = hall
        self.last_room = None

    def move(self, direction):
        """
        Moves the player to a different room based on the given direction.

        Args:
            direction (str): The direction to move (e.g., "N", "S", "E", "W").

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]

            if next_room is None:
                print("\nAucune porte dans cette direction !\n")
                return False

            # Save current room to history before moving
            self.history.append(self.current_room)
            self.last_room = self.current_room
            self.current_room = next_room
        else:
            print(f"Commande de direction non valide : '{direction}'")
            return False

        # Display the description of the new room
        print(self.current_room.get_long_description())
        print("Historique des salles:", self.get_history())
        return True

    def get_history(self):
        """
        Retrieves the history of rooms visited by the player.

        Returns:
            str: A formatted string listing all previously visited rooms.
        """
        if not self.history:
            return "Vous n'avez visité aucune salle pour le moment."
        return (
            "\nVous avez déjà visité les pièces suivantes :\n" +
            "\n".join(f"- {room.name}" for room in self.history)
        )

    def get_inventory(self):
        """
        Retrieves the inventory of the player.

        Returns:
            str: A formatted string listing all items in the player's inventory.
        """
        if not self.inventory:
            return "Votre inventaire est vide."

        inventory_list = "\nVous disposez des items suivants :\n"
        for item in self.inventory.values():
            inventory_list += f"    - {str(item)}\n"
        return inventory_list
