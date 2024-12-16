# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = set()
        self.exits = {}
        self.character = {}


    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\n Vous êtes dans {self.name}. {self.description}\n\n{self.get_exit_string()}\n"

   
    def get_inventory(self):

       if not self.inventory :
             if not self.character :
                 return "La pièce est vide"

       if not self.inventory :
            return ''.join(f"    - {str(character)}\n" for character in self.character.values())
            
       if self.inventory :
            print("\nLa pièce contient :")
            return ''.join(f"    - {str(item)}\n" for item in self.inventory) + ''.join(f"    - {str(character)}\n" for character in self.character.values())