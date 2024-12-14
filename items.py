class Item :

    def __init__(self, name, description, weight):
        self.name = name
        self. description = description
        self.weight = weight

    def __str__(self):
         return f"{self.name} : {self.description} ({self.weight} kg)"

dexscreener = Item("DexScreener" , "Application de trading de memecoins" , "0.3")
sword = Item("sword", "épée" , "2")
clé = Item("clé", "test", "0.1")
