# Defining the Room Class
class Room:
    def __init__(self, room_name=None):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None  # Ensuring character attribute is properly included

    # Getters and Setters
    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description if self.description else "No description available.")

    # Linking Rooms
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(f"\n{self.name}\n" + "-" * 25)
        print(self.description if self.description else "No description available.")

        for direction, room in self.linked_rooms.items():
            print(f"The {room.get_name()} is {direction}.")

    # Moving between rooms
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self

    # Character Management
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character


# Creating rooms
kitchen = Room("Kitchen")
hall = Room("Hallway")

# Setting descriptions
kitchen.set_description("An old room with a stone floor and a large wooden table.")
hall.set_description("A long hallway with a wooden floor and paintings on the wall.")

# Linking rooms
kitchen.link_room(hall, "north")
hall.link_room(kitchen, "south")

# Testing
kitchen.get_details()
print("\nMoving north...")
current_room = kitchen.move("north")
current_room.get_details()
