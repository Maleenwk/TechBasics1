# Escape the Amusement Park - Refactored Version

# This refactored version introduces structured code using:
# - A main() function
# - Constants
# - Modular functions with arguments and return values
# - Clear naming conventions and comments

import time


# Constants

LOCATIONS = ["Ferris Wheel", "Bouncehouse", "Waterpark", "Haunted House", "Shop", "Roller Coaster"]
INTRO_ART = """
          🎠🎡🎢🎠🎡🎢🎠🎡🎢🎠🎡🎢🎠🎡🎢
         _______________________________________
        |                                       |
        |   ESCAPE THE AMUSEMENT PARK 🎢🎠🎡   |
        |_______________________________________|
       /                                        \\
      /  🎪      🎠      🎡       🎢       🎪   \\
     /____________________________________________\\ 
    |    ||     ||     ||     ||     ||     ||     |
    |    ||     ||     ||     ||     ||     ||     |
    |____||_____||_____||_____||_____||_____||_____|
"""


# Helper Functions

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def ask_riddle(question, answer):
    """Ask a riddle and return True if the answer is correct."""
    user_answer = input(question + " ").lower()
    return answer in user_answer

def choose_location():
    while True:
        try:
            choice = int(input("Choose your starting point (1-6):\n1. Ferris Wheel\n2. Bouncehouse\n3. Waterpark\n4. Haunted House\n5. Shop\n6. Roller Coaster\nEnter number: "))
            if 1 <= choice <= 6:
                return LOCATIONS[choice - 1]
            else:
                print("Please choose a number between 1 and 6.")
        except ValueError:
            print("That's not a valid number. Try again.")


# Scene Functions

def ferris_wheel_scene(items):
    slow_print("The Ferris Wheel groans as it turns. You must answer a riddle to retrieve an item.")
    if ask_riddle("What has keys but can't open locks?", "piano"):
        slow_print("Correct! You find a shiny KEY stuck to the seat.")
        items.append("Key")
    else:
        slow_print("Wrong answer! You fall out and climb back up empty-handed.")

def bouncehouse_scene(items):
    slow_print("You bounce high into the air. Solve this to grab what lies beneath.")
    if ask_riddle("What bounces but has no legs?", "ball"):
        slow_print("Correct! A MAP flutters out from under the inflatable.")
        items.append("Map")
    else:
        slow_print("Wrong! You bounce away dizzy and confused.")

def waterpark_scene(items):
    slow_print("Waves crash around you. A quiz floats your way.")
    if ask_riddle("I'm full of holes but hold water. What am I?", "sponge"):
        slow_print("Correct! You find a SNORKEL in the lazy river.")
        items.append("Snorkel")
    else:
        slow_print("Wrong! A splash knocks you under. You escape barely.")

def haunted_house_scene(items):
    slow_print("Darkness surrounds you. A clown giggles in the corner...")
    if input("Do you approach the clown? (yes/no): ").lower() == "yes":
        slow_print("Giggles grabs you! You're now part of the horror show forever.")
        return False
    else:
        if ask_riddle("What gets sharper the more you use it?", "mind") or ask_riddle("", "brain"):
            slow_print("Correct! You find a FLASHLIGHT and run! That was close.")
            items.append("Flashlight")
        else:
            slow_print("Wrong. But you run out before he sees you.")
    return True

def shop_scene(items):
    slow_print("The shelves are ransacked. Solve this to access the drawer.")
    if ask_riddle("I speak without a mouth and hear without ears. What am I?", "echo"):
        slow_print("Correct! A CODE appears on the bag tag.")
        items.append("Code")
    else:
        slow_print("Wrong! A buzzer scares you off.")

def roller_coaster_scene(items):
    secret_escape = False
    slow_print("The ride jerks violently. There's a locked cart here.")
    if "Key" in items and "Ticket" in items:
        slow_print("You unlock a secret cart. It launches through a hidden tunnel to the exit!")
        secret_escape = True
    else:
        if ask_riddle("What runs but never walks?", "river"):
            slow_print("Correct! You find a TICKET under the seat.")
            items.append("Ticket")
        else:
            slow_print("Wrong! The coaster throws you back to the center of the park.")
    return secret_escape


# Main Game Flow

def main():
    print(INTRO_ART)
    items = []
    slow_print("Welcome to the Escape the Amusement Park Challenge!")
    name = input("What is your name, brave adventurer? ")
    slow_print(f"Hello {name}! Your mission is to find a hidden item and escape the amusement park alive...")

    if input("Are you ready to begin your journey? (yes/no): ").lower() != "yes":
        slow_print("Come back when you're ready. The park never sleeps...")
        return
    if input("Are you sure the reward is worth the risk? (yes/no): ").lower() != "yes":
        slow_print("Then perhaps it's best to turn back now...")
        return

    location = choose_location()
    secret_escape = False

    if location == "Ferris Wheel":
        ferris_wheel_scene(items)
    elif location == "Bouncehouse":
        bouncehouse_scene(items)
    elif location == "Waterpark":
        waterpark_scene(items)
    elif location == "Haunted House":
        if not haunted_house_scene(items):
            return
    elif location == "Shop":
        shop_scene(items)
    elif location == "Roller Coaster":
        secret_escape = roller_coaster_scene(items)

    second_location = input("Where will you go next? (Haunted House/Shop/Roller Coaster): ").strip().title()

    if second_location == "Haunted House":
        if "Flashlight" in items:
            slow_print("Your flashlight lights the way. Behind a painting, you find the EXIT PASS!")
            items.append("Exit Pass")
        else:
            slow_print("Too dark to see... You stumble and are caught by Giggles the Clown!")
            return
    elif second_location == "Shop":
        if "Code" in items:
            slow_print("You enter the code on the cash register... A secret drawer opens! It's the hidden item!")
            items.append("Hidden Item")
        else:
            slow_print("You fumble with buttons but nothing happens.")
    elif second_location == "Roller Coaster":
        secret_escape = roller_coaster_scene(items)

    # Final decision
    if input("Do you try to escape now? (yes/no): ").lower() == "yes":
        if "Exit Pass" in items or secret_escape:
            slow_print("\n🎉 Congratulations! You escaped the Amusement Park! 🎡")
        elif "Hidden Item" in items:
            slow_print("You found what you were looking for... but can you ever truly leave? 🤔")
        else:
            slow_print("You try to escape but the gates won't open... Suddenly, Giggles appears. Too late. 😱")
    else:
        slow_print("You decide to explore more... but get lost. Eventually, you become part of the show. 🎭")

    slow_print("Thanks for playing! 🎠")


# Start the game

if __name__ == "__main__":
    main()
