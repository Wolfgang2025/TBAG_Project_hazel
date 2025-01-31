from character import Character

dracula = Character("Dracula", "An aristocratic vampire")
dracula.describe()

dracula.set_conversation("Hello, and what brings you to my castle?")
dracula.talk()

mina = Character("Mina", "A noblewoman")
mina.describe()

mina.set_conversation("Hello, kind sir. I am lost.")
mina.talk()

lucy = Character("Lucy", "A beautiful maiden")
lucy.describe()

lucy.set_conversation("Get away from me, you monster!")
lucy.talk()

jonathan = Character("Jonathan", "A handsome young man")
jonathan.describe()

jonathan.set_conversation("I am here to save you, my love.")
jonathan.talk()

############################################

#Debug

from character import Enemy
dave = Enemy("Dave", "A smelly zombie")

dave.describe()

# Add some conversation for Dave when he is talked to
dave.set_conversation("Hello there! I am going to join your OOP game very soon")

# Trigger a conversation with Dave
dave.talk()

# Set a weakness
dave.set_weakness("cheese")

# Fight with dave
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)

#Enemies

dave = Enemy("Dave", "A smelly zombie")
dave.set_weakness("cheese")

karen = Enemy("Karen", "A mean vampire")
karen.set_weakness("garlic")

chuckie = Enemy("Chuckie", "A possessed doll")
chuckie.set_weakness("water")

harley = Enemy("Harley", "A creepy clown")
harley.set_weakness("fire")

