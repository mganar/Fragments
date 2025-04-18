# # Track inventory visibility
# default inventory1_visible = False
# default drink = 1
# default treat = 1
# default item = ""

# # INVENTORY SCREEN
# screen call_invScreen():

#     key "l" action ToggleVariable("inventory1_visible", True, False)

#     if inventory1_visible:

#         add "inventoryBar.png"  # background image

#         if drink <= 0:
#             use drinkLocked
#         else:
#             use drinkUnlocked

#         if treat <= 0:
#             use treatLocked
#         else:
#             use treatUnlocked

#         use closeInv


# # Hide inventory UI
# label call_hideScreensUI:
#     $ inventory1_visible = False
#     hide screen drinkLocked
#     hide screen drinkUnlocked
#     hide screen treatLocked
#     hide screen treatUnlocked
#     hide screen closeInv
#     return


# # DRINK & TREAT SCREENS
# screen drinkLocked():
#     imagebutton:
#         xpos 200
#         ypos 650
#         idle "emptySpace.png"

# screen drinkUnlocked():
#     imagebutton:
#         xpos 200
#         ypos 650
#         auto "drink_%s.png"
#         action [SetVariable("drink", drink - 1),
#                 SetVariable("item", "drink"),
#                 Jump("remove_item")]

# screen treatLocked():
#     imagebutton:
#         xpos 650
#         ypos 650
#         idle "emptySpace.png"

# screen treatUnlocked():
#     imagebutton:
#         xpos 650
#         ypos 650
#         auto "treat_%s.png"
#         action [SetVariable("treat", treat - 1),
#                 SetVariable("item", "treat"),
#                 Jump("remove_item")]


# # CLOSE INVENTORY BUTTON
# screen closeInv():
#     imagebutton:
#         xalign 1.0
#         yalign 0.0
#         xoffset -30
#         yoffset 30
#         auto "map_%s.png"
#         action Jump("call_hideScreensUI")


# # WHEN AN ITEM IS USED
# label remove_item:
#     hide screen call_invScreen
#     "You handed over [item]"
#     jump call_hideScreensUI


# # OPTIONAL: Button for inventory (HUD style)
# screen button:
#     imagebutton:
#         xpos 0.9
#         ypos 0.1
#         auto "inventory_%s.png"
#         action ToggleVariable("inventory1_visible", True, False)


# # KEYBIND SETUP
# init python:
#     config.keymap['inventory'] = [ 'i' ]
