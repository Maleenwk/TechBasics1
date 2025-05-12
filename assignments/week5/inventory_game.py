# Game idea: Supermarket/ store

import time

# --- Game State ---
inventory = []

items_in_room = [
    {"name": "Apple", "type": "food", "description": "A juicy red apple. Healthy and sweet."},
    {"name": "Chocolate", "type": "junk", "description": "Tasty but not healthy."},
    {"name": "Broccoli", "type": "food", "description": "A green vegetable full of vitamins."},
    {"name": "Soda", "type": "junk", "description": "High in sugar."},
    {"name": "Chips", "type": "junk", "description": "Crunchy and salty, but not healthy."},
    {"name": "Banana", "type": "food", "description": "A potassium-rich snack."},
    {"name": "Donuts", "type": "junk", "description": "Just a hint here: this is Homer Simpson's favourite. You might want to reconsider"},
    {"name": "Almonds", "type": "food", "description": "Good for your heart and your Tummy."},
    {"name": "Quinoa", "type": "food", "description": "High in Protein."},
    {"name": "Fruit Juice", "type": "junk", "description": "This drink seems to contain more sugar than actual fruit. Better make your own."},
    {"name": "Spinach", "type": "food", "description": "Small green leaves, these should help with your iron deficiency."},
    {"name": "Salmon", "type": "food", "description": "Ethically sourced and very fresh."},
    {"name": "Ice Cream", "type": "junk", "description": "So yummy but so much sugar."},
    {"name": "Sweet Potato", "type": "food", "description": "The fiber will help with digestion."},
    {"name": "Plain Yoghurt", "type": "food", "description": "The perfect base to add all your healthy fruits to."},
    {"name": "Cake", "type": "junk", "description": "Decorated nicely, but you probably shouldn't eat it all by yourself."},
    {"name": "Chickpeas", "type": "food", "description": "A healthy plant-based protein option."},
    {"name": "Avocado", "type": "food", "description": "A small green fruit containing healthy fats."},
    {"name": "Carrot", "type": "food", "description": "Good for your eyesight"},
    {"name": "Fried Chicken", "type": "junk", "description": "a little protein with a lot of Grease."},
    {"name": "Energy Drink", "type": "junk", "description": "This Caffeinated sugar drink will have your heart working overtime."},
    {"name": "Blueberries", "type": "food", "description": "Packed with Antioxidants."},
    {"name": "Candy", "type": "junk", "description": "After the sugar high comes the energy low."}
]

MAX_INVENTORY_SIZE = 5

# --- Functions ---

def show_inventory():
    if not inventory:
        print("Your shopping basket is empty.")
    else:
        print("Items in your shopping basket:")
        for item in inventory:
            print(f"- {item['name']} ")

def show_room_items():
    if not items_in_room:
        print("The shelves are empty.")
    else:
        print("Items available on the shelves:")
        for item in items_in_room:
            print(f"- {item['name']}")

def find_item(item_name, item_list):
    for item in item_list:
        if item["name"].lower() == item_name.lower():
            return item
    return None

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your basket is full. Drop something before picking up more.")
        return

    item = find_item(item_name, items_in_room)
    if item:
        inventory.append(item)
        items_in_room.remove(item)
        print(f"You added {item['name']} to your basket.")
    else:
        print(f"{item_name} is not on the shelves.")

def drop(item_name):
    item = find_item(item_name, inventory)
    if item:
        inventory.remove(item)
        items_in_room.append(item)
        print(f"You put back {item['name']}.")
    else:
        print(f"{item_name} is not in your basket.")

def use(item_name):
    item = find_item(item_name, inventory)
    if item:
        if item["type"] == "food":
            print(f"You eat the {item['name']}. Yum! Don't forget to pay for it at checkout!")
            inventory.remove(item)
        elif item["type"] == "junk":
            print(f"You snack on the {item['name']}, but maybe it's not the healthiest choice... people are looking at you sideways for eating from the shelves before paying for it.")
            inventory.remove(item)
        else:
            print(f"You can't use {item['name']} right now.")
    else:
        print(f"{item_name} is not in your basket.")

def examine(item_name):
    item = find_item(item_name, inventory) or find_item(item_name, items_in_room)
    if item:
        print(f"{item['name']}: {item['description']}")
    else:
        print(f"{item_name} is nowhere to be found.")

def check_victory():
    healthy_items = [item for item in inventory if item["type"] == "food"]
    if len(healthy_items) >= 5:
        print("\n🎉 Congratulations! You've collected 5 healthy foods and completed your shopping!")
        return True
    return False

# --- Game Loop ---

def game_loop():
    print("The sliding doors open and you feel the cool breeze of the air conditioning as you step into the supermarket")
    time.sleep (2)
    print("As you take one of the shopping baskets stacked next to the entrance you set yourself a goal")
    time.sleep(2)
    print("Your Goal is to shop for 5 healthy food items")
    time.sleep(2)
    print("Disclaimer: All Food can be healthy in moderation, This game is purely for fun and shouldn't be taken too seriously")
    time.sleep(3)
    print("Type 'help' for a list of commands.")

    while True:
        command = input("\n> ").strip().lower()
        if command == "help":
            print("Commands: inventory, look, pickup [item], drop [item], use [item], examine [item], quit")
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            item_name = command[7:]
            pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            drop(item_name)
        elif command.startswith("use "):
            item_name = command[4:]
            use(item_name)
        elif command.startswith("examine "):
            item_name = command[8:]
            examine(item_name)
        elif command == "quit":
            print("Thanks for shopping with us. Goodbye!")
            break
        else:
            print("Unknown command. Type 'help' to see available commands.")

        if check_victory():
            break

if __name__ == "__main__":
    game_loop()