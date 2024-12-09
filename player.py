import items
# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name, hall, inventory = None):
        self.name = name
        self.inventory = inventory if inventory is not None else {}
        self.history = []
        self.current_room = hall  
        self.hall = hall
        self.last_room = None
    
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
            # Avant de déplacer le joueur, sauvegarde la salle actuelle dans l'historique
                self.history.append(self.current_room)
                self.last_room = self.current_room  # Met à jour la dernière salle avant de changer
            # Déplacez le joueur dans la pièce suivante
                self.current_room = next_room
                print(f"Vous êtes maintenant dans {self.current_room.name}.")
        else:
            print(f"Commande de direction non valide : '{direction}'")
            return False

    # Affiche la description de la nouvelle salle et ses sorties
        print(self.current_room.get_long_description())
        print("Historique des salles:", self.get_history())
        return True

    
    
    def get_history(self):
       return (
            "\nVous avez déjà visité les pièces suivantes :\n" +
            "\n".join(f"- {room.name}" for room in self.history)
        )
    
    def get_inventory(self):

        if not self.inventory:
            return "Votre inventaire est vide."
        
        return "\n".join(
            f"- {key} : {item} "
            for key, item in self.inventory.items()  
        )
