class Character:
    """Create a character."""

    def __init__(self, char_name, char_description):
        """Initialize the character with a name and description."""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Describe the character."""
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Set what the character will say when talked to."""
        self.conversation = conversation

    def talk(self):
        """Talk to the character."""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """Fight with the character."""
        print(self.name + " doesn't want to fight with you")
        return True

   
#Creating an Enemy class as a subclass of Character
class Enemy(Character):
    def __init__(self, char_name, char_description):
     super().__init__(char_name, char_description)
