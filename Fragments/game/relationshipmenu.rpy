# Initialization of characters and maxpoints
init python:
    characters = {
        "Cyrus":  {"affection": 50, "icon": "icon1.png", "introduced": False},
        "Mira":   {"affection": 50, "icon": "icon2.png", "introduced": False},
        "Garrick":{"affection": 50, "icon": "icon1.png", "introduced": False},
        "Veyla":  {"affection": 50, "icon": "icon2.png", "introduced": False},
        "Ethan":  {"affection": 50, "icon": "icon1.png", "introduced": False},
        "Lila":   {"affection": 50, "icon": "icon2.png", "introduced": False},
        "Renn":   {"affection": 50, "icon": "icon1.png", "introduced": False},
        "Mimic":  {"affection": 50, "icon": "icon1.png", "introduced": False},
        "Lucky":  {"affection": 50, "icon": "icon1.png", "introduced": False},
    }

    maxpoints = 100

    def emotions(points):
        if points >= 75:
            return "Happy", "#7CFC00"  # Light green
        elif points >= 50:
            return "Neutral", "#FFD700"  # Gold
        else:
            return "Upset", "#FF6347"  # Tomato red


    def introduce_character(name):
        if name in characters:
            characters[name]["introduced"] = True

    def remove_character(name):
        if name in characters:
            characters[name]["introduced"] = False

    def change_affection(name, delta):
        if name in characters:
            characters[name]["affection"] = max(0, min(maxpoints, characters[name]["affection"] + delta))

    def get_affection(name):
        if name in characters:
            return characters[name]["affection"]
        return None

# Default Ren'Py state variables
default relationships_visible = False  
default relationship_menu_unlocked = False

# Relationship menu toggle button
screen button:
    vbox xalign 0.95 yalign 0.0:
        if relationship_menu_unlocked:
            imagebutton:
                idle "button.png"
                hover "hoverbutton.png"
                action ToggleVariable("relationships_visible")

# Style for relationship menu
style relationmenustyles:
    padding (60, 60)
    background Frame("affs.png")
    xalign 0.5
    yalign 0.3

# Relationship menu screen
screen relationmenu():

    if relationship_menu_unlocked:
        key "r" action ToggleVariable("relationships_visible", True, False)

        if relationships_visible:
            window:
                style "relationmenustyles"

                vbox:
                    spacing 20

                    hbox:
                        xalign 0.5
                        label "{b}{color=#fff}{size=+5}Relationships{/b}{/color}"

                    for name, info in characters.items():
                        if info.get("introduced", False):
                            vbox:
                                spacing 5
                                xalign 0.5

                                $ emotion_text, emotion_color = emotions(info["affection"])

                                hbox:
                                    xalign 0.5
                                    spacing 10  # Space between icon and text
                                    add info["icon"] yalign 0.5
                                    label "{color=#FFFFFF}[name] is {/color}{color=" + emotion_color + "}" + emotion_text + "{/color}" yalign 0.5

                                hbox:
                                    xalign 0.5
                                    bar range maxpoints value info["affection"] xmaximum 500

