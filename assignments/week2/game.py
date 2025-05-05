import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

items = []
locations = ["Ferris Wheel", "Bouncehouse", "Waterpark", "Haunted House", "Shop", "Roller Coaster"]

slow_print("Welcome to the Escape the Amusement Park Challenge!")
name = input("What is your name, brave adventurer? ")
slow_print(f"Hello {name}! Your mission is to find a hidden item and escape the amusement park alive...")
time.sleep(1)

ready = input("Are you ready to begin your journey? (yes/no): ").lower()
if ready != "yes":
    slow_print("Come back when you're ready. The park never sleeps...")
    exit()

sure = input("Are you sure the reward is worth the risk? (yes/no): ").lower()
if sure != "yes":
    slow_print("Then perhaps it's best to turn back now...")
    exit()

while True:
    try:
        choice = int(input("Choose your starting point (1-6):\n1. Ferris Wheel\n2. Bouncehouse\n3. Waterpark\n4. Haunted House\n5. Shop\n6. Roller Coaster\nEnter number: "))
        if 1 <= choice <= 6:
            break
        else:
            print("Please choose a number between 1 and 6.")
    except ValueError:
        print("That's not a valid number. Try again.")

location = locations[choice - 1]
slow_print(f"You approach the {location}...")
time.sleep(1)

if location == "Ferris Wheel":
    slow_print("The Ferris Wheel groans as it turns. You must answer a riddle to retrieve an item.")
    ans = input("What has keys but can't open locks? ").lower()
    if "piano" in ans:
        slow_print("Correct! You find a shiny KEY stuck to the seat.")
        items.append("Key")
    else:
        slow_print("Wrong answer! You fall out and climb back up empty-handed.")

elif location == "Bouncehouse":
    slow_print("You bounce high into the air. Solve this to grab what lies beneath.")
    ans = input("What bounces but has no legs? ").lower()
    if "ball" in ans:
        slow_print("Correct! A MAP flutters out from under the inflatable.")
        items.append("Map")
    else:
        slow_print("Wrong! You bounce away dizzy and confused.")

elif location == "Waterpark":
    slow_print("Waves crash around you. A quiz floats your way.")
    ans = input("I’m full of holes but hold water. What am I? ").lower()
    if "sponge" in ans:
        slow_print("Correct! You find a SNORKEL in the lazy river.")
        items.append("Snorkel")
    else:
        slow_print("Wrong! A splash knocks you under. You escape barely.")

elif location == "Haunted House":
    slow_print("Darkness surrounds you. A clown giggles in the corner...")
    clown_choice = input("Do you approach the clown? (yes/no): ").lower()
    if clown_choice == "yes":
        slow_print("Giggles grabs you! You're now part of the horror show forever.")
        exit()
    else:
        ans = input("A whisper asks: What gets sharper the more you use it? ").lower()
        if "brain" in ans or "mind" in ans:
            slow_print("Correct! You find a FLASHLIGHT and run! That was close.")
            items.append("Flashlight")
        else:
            slow_print("Wrong. But you run out before he sees you.")

elif location == "Shop":
    slow_print("The shelves are ransacked. Solve this to access the drawer.")
    ans = input("I speak without a mouth and hear without ears. What am I? ").lower()
    if "echo" in ans:
        slow_print("Correct! A CODE appears on the bag tag.")
        items.append("Code")
    else:
        slow_print("Wrong! A buzzer scares you off.")

elif location == "Roller Coaster":
    slow_print("The ride jerks violently. There's a locked cart here.")
    if "Key" in items and "Ticket" in items:
        slow_print("You unlock a secret cart. It launches through a hidden tunnel to the exit!")
        secret_escape = True
    else:
        ans = input("Solve: What runs but never walks? ").lower()
        if "river" in ans:
            slow_print("Correct! You find a TICKET under the seat.")
            items.append("Ticket")
        else:
            slow_print("Wrong! The coaster throws you back to the center of the park.")
        secret_escape = False

slow_print("You now must decide where to go next.")
second_choice = input("Where will you go next? (Haunted House/Shop/Roller Coaster): ").strip().title()

if second_choice == "Haunted House":
    if "Flashlight" in items:
        slow_print("Your flashlight lights the way. Behind a painting, you find the EXIT PASS!")
        items.append("Exit Pass")
    else:
        slow_print("Too dark to see... You stumble and are caught by Giggles the Clown!")
        exit()

elif second_choice == "Shop":
    if "Code" in items:
        slow_print("You enter the code on the cash register... A secret drawer opens! It's the hidden item!")
        items.append("Hidden Item")
    else:
        slow_print("You fumble with buttons but nothing happens.")

elif second_choice == "Roller Coaster":
    if "Key" in items and "Ticket" in items:
        slow_print("You unlock the secret cart again. It zooms you out through a tunnel!")
        secret_escape = True
    else:
        slow_print("You enjoy the ride but find nothing useful.")
        secret_escape = False

slow_print("Final decision time...")
final_action = input("Do you try to escape now? (yes/no): ").lower()

if final_action == "yes":
    if "Exit Pass" in items or ("Key" in items and "Ticket" in items and secret_escape):
        slow_print("\n🎉 Congratulations! You escaped the Amusement Park! 🎡")
    elif "Hidden Item" in items:
        slow_print("You found what you were looking for... but can you ever truly leave? 🤔")
    else:
        slow_print("You try to escape but the gates won't open... Suddenly, Giggles appears. Too late. 😱")
else:
    slow_print("You decide to explore more... but get lost. Eventually, you become part of the show. 🎭")

slow_print("Thanks for playing! 🎠")