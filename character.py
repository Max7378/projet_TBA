import random
from room import Room
from game import DEBUG

class Character():

    # Define the constructor.
    def __init__(self, name, description, current_room, msg):
        self.name = name
        self.description = description
        self.current_room = current_room  
        self.msg = msg

    def __str__(self):
         return f"{self.name} : {self.description} "

    def move(self) :
        l = ["N", "S", "O", "E"]
        if random.choice([True, False]):
            new_direction = random.choice(l)
            if self.current_room.exits[new_direction] == None :
                if DEBUG :
                    print("Le pnj est en face d'une porte donc ne bouge pas de salle")
                self.current_room = self.current_room
                return False
            else :
                next_room = self.current_room.exits[new_direction]
                self.current_room = next_room
                if DEBUG :
                    print("Le pnj a changé de salle")
                return True
        if DEBUG :
            print("Le pnj ne bouge pas")
        return False
    
    def get_msg(self):
        if not self.msg:
            raise ValueError("La liste des messages ne peut pas être vide.")
        
        # Retirer et retourner le premier message, puis le remettre à la fin pour un comportement cyclique
        message = self.msg.pop(0)
        self.msg.append(message)
        print(message)
