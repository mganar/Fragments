# Default affection variables for characters
default characters = [
    {"name": "Lila", "affection": 50, "icon": "/icon1.png", "introduced": False},
    {"name": "Lucky", "affection": 50, "icon": "/icon2.png", "introduced": False},
    # Add more characters, set "introduced": False initially
]

default maxpoints = 100  # Max affection points

# Function to return character emotion based on affection points
init python:
    def emotions(points):
        if points >= 75:
            return "Happy"
        elif points >= 50:
            return "Neutral"
        else:
            return "Upset"
    # Use this function in script.rpy when a character is introduced, so they show up in the relationship menu
    def introduce_character(name):
        for c in characters:
            if c["name"] == name:
                c["introduced"] = True
# Use this function to change a character's affection by a certain amount
    def change_affection(name, delta):
        for c in characters:
            if c["name"] == name:
                c["affection"] += delta

# Button screen to trigger the relationship menu
screen button:
    vbox xalign 0.95 yalign 0:
        imagebutton:
            idle "/button.png"
            hover "/hoverbutton.png"
            action ToggleVariable("relationships_visible")  # This will toggle between True and False

# This code defines the style of the menu!
style relationmenustyles:
    padding (60, 60)
    background Frame("/affs.png")  # If you rename the background picture, change this code too.
    xalign 0.5
    yalign 0.3

# Variable to track relationship menu visibility
default relationships_visible = False  

# Relationship menu screen
screen relationmenu():
    # This uses a hotkey 'r' to toggle visibility of the relationship menu
    key "r" action ToggleVariable("relationships_visible", True, False)  # Toggle relationship menu visibility
    
    if relationships_visible:
        window:
            style "relationmenustyles"

            vbox:
                spacing 20

                # Title!
                hbox:
                    xalign 0.5  # Centered
                    label "{b}{color=#fff}{size=+5}Relationships{/b}{/color}"

                # Display each character's relationship status
                $ character_count = 0
                $ num_characters = len(characters)
                
                # Loop through the characters and create the relationship bars dynamically
                for character in characters:
                    if character.get("introduced", False):
                        hbox:
                            xalign 0.5
                            add character['icon'] yalign 0.5  # Character's icon
                        hbox:
                            xalign 0.5
                            label "{b}{color=#fff}" + character['name'] + " is " + emotions(character['affection']) + " {/b}{/color}" yalign 0.5  # Character's affection status
                        hbox:
                            xalign 0.5
                            bar range maxpoints value character['affection'] xmaximum 500  # Affection bar

