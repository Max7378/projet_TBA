# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.history = []
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
       # Vérifier si la direction existe dans les sorties de la pièce actuelle
        if direction in self.current_room.exits:
        # Obtenir la pièce suivante
            next_room = self.current_room.exits[direction]
        
        # Si la direction mène à une sortie vide (None), afficher un message d'erreur
            if next_room is None:
                print("\nAucune porte dans cette direction !\n")
                return False
        
        # Sinon, effectuer le déplacement vers la pièce suivante
            self.current_room = next_room
            return True
        else:
        # Si la direction n'existe pas dans les sorties, afficher un message d'erreur
            print(f"Commande de direction non valide : '{direction}'")
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
