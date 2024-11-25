# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

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

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        
        # Setup rooms


        couloir1 = Room("Intersection des couloirs", "Vous êtes dans à l'intersection")
        self.rooms.append(couloir1)
        couloirdroit1 = Room("Couloir Est du 52ème étage", "Vous êtes dans le couloir Est du 52ème étage.")
        self.rooms.append(couloirdroit1)
        couloirbas1 = Room("Couloir Nord du 52ème étage", "Vous êtes dans le couloir Nord du 52ème étage.")
        self.rooms.append(couloirbas1)
        couloirgauche1 = Room("Couloir Ouest du 52ème étage", "Vous êtes dans le couloir Ouest du 52ème étage.")
        self.rooms.append(couloirgauche1)
        couloirhaut1 = Room("Couloir Sud du 52ème étage", "Vous êtes dans le couloir Sud du 52ème étage.")
        self.rooms.append(couloirhaut1)
        bureau1 = Room("Bureau de gestion", "Stratégies d'entreprise sont décidées ici.")
        self.rooms.append(bureau1)
        bureau2 = Room("Bureau de finance", "L'argent de l'entreprise est géré ici.")
        self.rooms.append(bureau2)
        bureau3 = Room("Bureau de gestion du personnel", "Les RH travaillent ici.")
        self.rooms.append(bureau3)
        bureau4 = Room("Bureau de trading", "Les traders travaillent ici.")
        self.rooms.append(bureau4)
        castle = Room("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)

        # Create exits for rooms

        couloir1.exits = {"N" : , "E" : bureau1, "S" : None, "O" : cafe}
        cafe.exits = {"N" : None, "E" : couloir1, "S" : None, "O" : None}
        bureau1.exits = {"N" : None, "E" : None, "S" : None, "O" : couloir1}
        cottage.exits = {"N" : None, "E" : None, "S" : None, "O" : None}
        swamp.exits = {"N" : None, "E" : None, "S" : None, "O" : castle}
        castle.exits = {"N" : None, "E" : swamp, "S" : None, "O" : None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = swamp

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

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name}, la tour Allianz vous attend avec impatience")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
