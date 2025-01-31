# Defining the Item Class
class Item:
    def __init__(self, item_name=None):
        self.name = item_name
        self.description = None

    # Getters and Setters
    def get_description(self):
        return self.description
    
    def set_description(self, item_description):
        self.description = item_description

    def get_name(self):
        return self.name
    
    def describe(self):
        if self.description:
            print(self.description)
        else:
            print("No description available.")

# Creating items

sword = Item("Sword")
spyglass = Item("Spyglass")
potion= Item("Potion")
magic_ring = Item("Magic Ring")

# Getting descriptions
sword.describe()
spyglass.describe()
potion.describe()
magic_ring.describe()

# Setting descriptions
sword.set_description("A sharp sword with a golden hilt.")
spyglass.set_description("A vintage magnifying glass with a brass frame.")
potion.set_description("A small vial filled with a glowing blue liquid.")
magic_ring.set_description("A silver ring with a blue gemstone.")

