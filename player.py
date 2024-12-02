# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.history = []
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
            # Vérifiez si la direction est valide
        if direction in self.current_room.exits:
            next_room = self.current_room.exits[direction]
        
        # Vérifiez si la direction mène à une pièce valide
            if next_room is None:
                print("\nAucune porte dans cette direction !\n")
                return False
            else:
            # Déplacez le joueur dans la pièce suivante
                self.current_room = next_room
                print(f"Vous êtes maintenant dans {self.current_room.name}.")
        else:
            print(f"Commande de direction non valide : '{direction}'")
            return False

    # Effectuez les actions après le déplacement
        print(self.current_room.get_long_description())
        self.history.append(next_room.name)
        print(self.get_history())
        return True
    
    
    def get_history(self):
       return (
            "\nVous avez déjà visité les pièces suivantes :\n" +
            "\n".join(f"- {room}" for room in self.history)
        )
