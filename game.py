# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from items import sword, clé

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : Afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : Quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : Se déplacer dans une direction cardinale (N, E, S, O) ou aller de haut en bas (U, D)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : Revenir en arrière", Actions.back, 0)
        self.commands["back"] = back
        check = Command("check", " : Afficher l'inventaire du joueur", Actions.check, 0)
        self.commands["check"] = check
        look = Command("look" , " : Regarder autour de soi", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " : Prendre un objet", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " : Déposer un objet", Actions.drop, 1)
        self.commands["drop"] = drop
        

        # Setup rooms

        hall=Room("le hall d'acceuil", "Prêt à commencer votre job de rêve.", {})
        self.rooms.append(hall)
        ascenseur=Room("l'ascenseur.", "Direction le 52ème étage.", {sword,clé} )
        self.rooms.append(ascenseur)
        couloir1 = Room("à l'intersection des couloirs", "", {})
        self.rooms.append(couloir1)
        couloirdroit1 = Room("dans le couloir Est du 52ème étage", "", {})
        self.rooms.append(couloirdroit1)
        couloirbas1 = Room("dans le couloir Nord du 52ème étage", "", {})
        self.rooms.append(couloirbas1)
        couloirgauche1 = Room("dans le couloir Ouest du 52ème étage", "",{})
        self.rooms.append(couloirgauche1)
        couloirhaut1 = Room("dans le couloir Sud du 52ème étage", "",{})
        self.rooms.append(couloirhaut1)
        
        
        bureau1 = Room("dans le bureau de gestion.", "Les stratégies d'entreprise sont décidées ici.",{})
        self.rooms.append(bureau1)
        bureau2 = Room("dans le bureau de finance.", "L'argent de l'entreprise est géré ici.",{})
        self.rooms.append(bureau2)
        bureau3 = Room("dans le bureau de gestion du personnel.", "Les RH travaillent ici.",{})
        self.rooms.append(bureau3)
        bureau4 = Room("dans le bureau de trading.", "Les traders travaillent ici.",{})
        self.rooms.append(bureau4)

        
        bureau5 = Room("dans le placard à balais", "",{})
        self.rooms.append(bureau5)
        bureau6 = Room("dans la salle de repos.", "Les employés viennent se détendre ici",{})
        self.rooms.append(bureau6)
        bureau7 = Room("dans le bureau de j'ai pas encore d'idée", "Idée.",{})
        self.rooms.append(bureau7)
        bureau8 = Room("dans la salle des machines", "Tous les serveurs sont entreposés ici.",{})
        self.rooms.append(bureau8)
        
        
        couloir2 = Room("à l'intersection des couloirs", "dans à l'intersection 53ème étage",{})
        self.rooms.append(couloir2)
        couloirdroit2 = Room("dans le couloir Est du 53ème étage", "",{})
        self.rooms.append(couloirdroit2)
        couloirbas2 = Room("dans le couloir Nord du 53ème étage", "",{})
        self.rooms.append(couloirbas2)
        couloirgauche2 = Room("dans le couloir Ouest du 53ème étage", "",{})
        self.rooms.append(couloirgauche2)
        couloirhaut2 = Room("dans le couloir Sud du 53ème étage", "",{})
        self.rooms.append(couloirhaut2)

        # Create exits for rooms

        hall.exits = {"N" : ascenseur, "E" : None, "S" : None, "O" : None}
        ascenseur.exits = {"N" : couloirbas1, "E" : None, "S" : None, "O" : None}


        couloir1.exits = {"N" : couloirhaut1, "E" : couloirdroit1, "S" : couloirbas1, "O" : couloirgauche1}
        couloirgauche1.exits = {"N" : bureau1, "E" : couloir1, "S" : bureau3, "U" : couloirgauche2}
        couloirbas1.exits = {"N" : couloir1, "E" : bureau4, "U" : couloirbas2, "O" : bureau3}
        couloirdroit1.exits = {"N" : bureau2, "U" : couloirdroit2, "S" : bureau4, "O" : couloir1}
        couloirhaut1.exits = {"U" : couloirhaut2, "E" : bureau2, "S" : couloir1, "O" : bureau1}
       
        couloir2.exits = {"N" : couloirhaut2, "E" : couloirdroit2, "S" : couloirbas2, "O" : couloirgauche2}
        couloirgauche2.exits = {"N" : bureau5, "E" : couloir2, "S" : bureau7, "D" : couloirgauche1}
        couloirbas2.exits = {"N" : couloir2, "E" : bureau8, "D" : couloirbas1, "O" : bureau7}
        couloirdroit2.exits = {"N" : bureau6, "D" : couloirdroit1, "S" : bureau8, "O" : couloir2}
        couloirhaut2.exits = {"D" : couloirhaut1, "E" : bureau6, "S" : couloir2, "O" : bureau5}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "), hall, {})
        self.player.current_room = hall

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]
        if not command_word :
            return
        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans la tour Allianz pour votre premier jour.")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
