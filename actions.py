# Description: The actions module.
import player
# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        if list_of_words[1] in ["NORD", "N", "nord", "n", "Nord"]:
            list_of_words[1] = "N"
        if list_of_words[1] in ["EST", "E", "est", "e", "Est"]:
            list_of_words[1] = "E"
        if list_of_words[1] in ["SUD", "S", "sud", "s", "Sud"]:
            list_of_words[1] = "S"
        if list_of_words[1] in ["OUEST", "O", "ouest", "o", "Ouest"]:
            list_of_words[1] = "O"
        
        # Get the direction from the list of words.
        direction = list_of_words[1]
        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    

    def back(game, list_of_words, number_of_parameters):
        """
    Permet au joueur de revenir à la salle précédente.
    
    Args:
        game (Game): L'objet du jeu.
        list_of_words (list): Liste des mots dans la commande.
        number_of_parameters (int): Le nombre de paramètres attendus par la commande.

    Returns:
        bool: True si la commande est exécutée avec succès, False sinon.
    """
    # Vérifier si l'historique des salles est vide ou contient qu'une seule salle
        if len(game.player.history) <= 1:  # Si l'historique contient 1 ou moins de salles, le joueur est déjà à son point de départ
            game.player.current_room = game.player.hall
            print(game.player.current_room.get_long_description())
            return False
    
    # Vérifier que le nombre de paramètres est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"Usage incorrect de la commande '{command_word}'")
            return False
    
    # Récupérer la salle précédente à partir de l'historique
        previous_room = game.player.history[-1]  # La deuxième dernière salle dans l'historique
        print(f"Vous êtes revenu dans : {previous_room.name}.")
    
        game.player.current_room = previous_room
    
        print(game.player.current_room.get_long_description())

        game.player.history.pop()  # La salle actuelle est en dernière position, donc on la retire
        return True

    def check(game, list_of_words, number_of_parameters):
        
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(game.player.get_inventory())

    
    def look(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        if not game.player.current_room.inventory :
            print("\nIl n'y a rien ici\n")
            
        if game.player.current_room.inventory :
            print("\nLa pièce contient :")
            for item in game.player.current_room.inventory :
                print(f"    - {str(item)}\n")

   
    def take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        item = list_of_words[1]
        for key in game.player.current_room.inventory:
            if item == key.name:  
                game.player.inventory[key.name] = key 
                game.player.current_room.inventory.remove(key)  
                print(f"Vous avez pris {item}.")
                break
       
                
    def drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        item = list_of_words[1]
        if item  in game.player.inventory :
            item_obj = game.player.inventory[item]
            game.player.current_room.inventory.add(item_obj)
            del game.player.inventory[item]