# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.history = []
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        self.history.append(next_room.name)
        print(self.get_history())
        return True
    
    
    def get_history(self):
       return (
            "\nVous avez déjà visité les pièces suivantes :\n" +
            "\n".join(f"- {room}" for room in self.history)
        )
