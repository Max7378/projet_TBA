import random
from room import Room


class Character():

    # Define the constructor.
    def __init__(self, name, description, current_room, msg):
        self.name = name
        self.description = description
        self.current_room = current_room  
        self.msg = msg

    def __str__(self):
         return f"{self.name} : {self.description} "
