
#Defining the Room Class

class Room():

    #Defining the properties of the Room class (Constructor)
    def __init__(self, room_name=None):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}


    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def describe(self):
        print(f"The {self.name} is {self.description}")

    #Adding a link between rooms (directions)

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    #Adding a method to move between rooms
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]

        else:
            print("You can't go that way")
            return self
    

#Create rooms

#For now I will keep everything in one file so I can understand the game logic better. 
#Later I will split the classes into separate files, and import them into the main file. That is if the game gets too big.
#For now, I will keep everything in one file.

# Create rooms
kitchen = Room("Kitchen")
kitchen.set_description("A room with delicious smells and shining appliances.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A grand hall with a long wooden table.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor.")

#Set Up Room Navigation Loop

# Game loop to move between rooms

#Summary of What This Code Does
#Starts the player in the kitchen.
#Enters an infinite loop, displaying the current room's name and description.
#Prompts the user for a direction (e.g., "north", "south").
#Moves the player to the new room based on their input.
#If the direction is invalid, stays in the same room and prompts again.

current_room = kitchen
while True:
    print("\n")
    print(f"You are in the {current_room.get_name()}")
    print(current_room.get_description())
    command = input("Which direction do you want to go? ")
    current_room = current_room.move(command)


# Link rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")


living_room = Room("Living Room")
living_room.set_description("a cozy place to relax with a fireplace.")
living_room.describe()

# Step 3: Add another room instance
kitchen = Room("Kitchen")
kitchen.set_description("a place with modern appliances and delicious smells.")
kitchen.describe()

# Step 4: Print the room names
print("Room Names:")
print(living_room.get_name())
print(kitchen.get_name())
