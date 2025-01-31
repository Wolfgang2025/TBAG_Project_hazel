# Import necessary classes
from room import Room
from character import Enemy

# Instantiate Rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

# Set Room Descriptions
kitchen.set_description("An old room with a stone floor and a large wooden table.")
ballroom.set_description("A glitzy and grand art deco hall.")
dining_hall.set_description("A grand room with a long oak table and heavy crystal chandeliers.")

# Link Rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Create an Enemy and place it in the Dining Hall
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

# Game Loop: Let the player move between rooms and interact with characters
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    # Check for an inhabitant in the room
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    # Get user input for movement
    command = input("> ").lower().strip()
    current_room = current_room.move(command)
