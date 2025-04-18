init python:
    
    class Inventory():
        MAX_ITEMS = 2  # Maximum number of items allowed

        def __init__(self, items, no_of_items):
            self.items = items
            self.no_of_items = no_of_items

        def add_item(self, item):
            if self.no_of_items >= self.MAX_ITEMS:
                renpy.say("", f"Inventory full! You can't carry more than {self.MAX_ITEMS} items.")
                return
            
            self.items.append(item)
            self.no_of_items += 1
            renpy.say("", f"{item.name.capitalize()} has been added to your inventory.") 
            renpy.restart_interaction()  # Refresh screen

        def remove_item(self, item):
            if item in self.items:
                self.items.remove(item)
                self.no_of_items -= 1
                renpy.restart_interaction()  # Refresh screen
            else:
                renpy.say("", f"You don't have {item.name} in your inventory.")

        def list_items(self):
            if len(self.items) < 1:
                Valley("I'm not carrying anything.")
            else:
                for item in self.items:
                    if item.name.lower() == "cash":
                        Valley(f"I have {item.name}, which I can use to buy things.")
                    else:
                        Valley(f"I have a {item.name} that {item.description}.")

    class InventoryItem():
        def __init__(self, name, description, image):
            self.name = name
            self.description = description
            self.image = image

# Variable to track inventory visibility
default inventory_visible = False  

# Inventory Screen (Fixed)
screen inventory_screen():
    key "i" action ToggleVariable("inventory_visible", True, False)  # Toggle inventory visibility

    if inventory_visible:
        frame:
            xalign 1.0  # Align to the right
            yalign 0.2  # Adjust vertical position
            padding (20, 20)
            background "#33333388"  # Semi-transparent dark background

            vbox:
                spacing 10
                label "Inventory" xalign 0.5

                for item in inventory.items:
                    vbox:  # Center name and image together
                        xalign 0.5  # Center the entire vbox
                        spacing 5
                        text f"{item.name.capitalize()}" size 22 xalign 0.5  # Center text
                        image item.image xsize 100 ysize 100 xalign 0.5  # Center image

                        

define door_key = InventoryItem("door key", "unlocks doors", "key")
define chest_key = InventoryItem("chest key", "unlocks chests", "key")
define cash = InventoryItem("cash", "used to purchase", "dollar")
define water = InventoryItem("water", "hydrates character", "water")
define keycard = InventoryItem("keycard", "unlocks the restricted hallway", "keycard.png")
