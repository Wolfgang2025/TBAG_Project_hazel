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

# Create Enemies and place them in rooms
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")  # Zombies are weak to cheese
dining_hall.set_character(dave)

karen = Enemy("Karen", "A mean vampire")
karen.set_conversation("Grrr... grrr... gooey!")
karen.set_weakness("garlic")  # Vampires are weak to garlic
ballroom.set_character(karen)

chuckie = Enemy("Chuckie", "A possessed doll")
chuckie.set_conversation("Weeep... weeep... wet!")
chuckie.set_weakness("water")  # Possessed dolls are weak to water
kitchen.set_character(chuckie)

harley = Enemy("Harley", "A creepy clown")
harley.set_conversation("Hahaha... I'm going to scare you!")
harley.set_weakness("fire")  # Clowns are weak to fire
# Note: Harley is not placed in any room. You can add them to a room if needed.

# Player inventory
player_inventory = []

# Game Loop: Let the player move between rooms and interact with characters
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    # Check for an inhabitant in the room
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    # Get user input for movement or interaction
    command = input("> ").lower().strip()

    # Handle movement
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    # Handle fighting an enemy
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            if inhabitant.is_alive():
                print(f"You are fighting {inhabitant.name}!")
                print(f"{inhabitant.name} says: {inhabitant.get_conversation()}")
                print(f"Hint: {inhabitant.name} is weak to {inhabitant.get_weakness()}.")
                weapon = input("What will you use to fight? ").lower().strip()
                if weapon in player_inventory:
                    if weapon == inhabitant.get_weakness():
                        print(f"You used {weapon} to defeat {inhabitant.name}!")
                        inhabitant.take_damage(10)  # Deal damage
                        if not inhabitant.is_alive():
                            print(f"{inhabitant.name} has been defeated!")
                            current_room.set_character(None)  # Remove enemy from the room
                    else:
                        print(f"The {weapon} has no effect on {inhabitant.name}!")
                else:
                    print(f"You don't have a {weapon} in your inventory!")
            else:
                print(f"{inhabitant.name} is already defeated.")
        else:
            print("There is no enemy here to fight!")
    # Handle picking up items (placeholder for future implementation)
    elif command == "pickup":
        item = current_room.get_item()
        if item is not None:
            print(f"You picked up a {item}!")
            player_inventory.append(item)
            current_room.remove_item()
        else:
            print("There is nothing to pick up here.")
    # Handle checking inventory
    elif command == "inventory":
        if player_inventory:
            print("Your inventory contains:")
            for item in player_inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")
    # Handle quitting the game
    elif command == "quit":
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid command. Try 'north', 'south', 'east', 'west', 'fight', 'pickup', 'inventory', or 'quit'.")