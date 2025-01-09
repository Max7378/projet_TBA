"""
 Module actions: contient les fonctions pour exécuter les commandes du jeu.
"""


# Messages d'erreur pour les commandes avec paramètres incorrects.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
    Classe Actions contenant les commandes disponibles pour le jeu.
    """

    def __init__(self):
        pass

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Permet de déplacer le joueur dans une direction donnée.
        """
        joueur = game.player
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        directions = {
            "NORD": "N", "N": "N", "nord": "N", "n": "N", "Nord": "N",
            "EST": "E", "E": "E", "est": "E", "e": "E", "Est": "E",
            "SUD": "S", "S": "S", "sud": "S", "s": "S", "Sud": "S",
            "OUEST": "O", "O": "O", "ouest": "O", "o": "O", "Ouest": "O",
        }

        direction = directions.get(list_of_words[1], None)
        if direction:
            joueur.move(direction)
            return True

        print("Direction non valide.")
        return False

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Permet de quitter le jeu.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        joueur = game.player
        print(f"\nMerci {joueur.name} d'avoir joué. Au revoir.\n")
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Affiche la liste des commandes disponibles.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print(f"\t- {command}")
        print()
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de revenir à la salle précédente.
        """
        joueur = game.player
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"Usage incorrect de la commande '{command_word}'")
            return False

        if not joueur.history:
            joueur.current_room = joueur.hall
            print(joueur.current_room.get_long_description())
            return False

        previous_room = joueur.history.pop()
        joueur.current_room = previous_room
        print(f"Vous êtes revenu dans : {previous_room.name}.")
        print(joueur.current_room.get_long_description())
        return True

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Affiche l'inventaire du joueur.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(game.player.get_inventory())
        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Affiche l'inventaire de la salle actuelle.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        print(game.player.current_room.get_inventory())
        return True

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un objet dans la salle actuelle.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        room_inventory = game.player.current_room.inventory

        for item in room_inventory:
            if item_name == item.name:
                game.player.inventory[item.name] = item
                room_inventory.remove(item)
                print(f"Vous avez pris {item.name}.")
                return True

        print("Objet non trouvé.")
        return False

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de lâcher un objet de son inventaire dans la salle actuelle.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        item_name = list_of_words[1]
        player_inventory = game.player.inventory

        if item_name in player_inventory:
            item = player_inventory.pop(item_name)
            game.player.current_room.inventory.add(item)
            print(f"Vous avez lâché {item_name}.")
            return True

        print("Objet non trouvé dans votre inventaire.")
        return False

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler à un PNJ dans la salle actuelle.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False  # Il semble que cela soit fait pour gérer une erreur de syntaxe.

        npc_name = list_of_words[1]
        room_characters = game.player.current_room.character

        if npc_name in room_characters:
            message = room_characters[npc_name].get_msg()
            print(message)
            return True  # Le joueur a parlé avec le PNJ, renvoie True pour signifier le succès.

        print("Personnage non trouvé dans la salle.")
        return False  # Si le personnage n'est pas trouvé, retourne False pour l'échec.
