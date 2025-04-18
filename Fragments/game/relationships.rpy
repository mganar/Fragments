
# init python:
    
#     def get_relationship_status(value):
#         if value <= -5:
#             return "Hated", "#FF0000"  # Red for Hated
#         elif value < 0:
#             return "Unfriendly", "#FFA500"  # Orange for Unfriendly
#         elif value == 0:
#             return "Neutral", "#808080"  # Gray for Neutral
#         elif value <= 5:
#             return "Friendly", "#00FF00"  # Green for Friendly
#         else:
#             return "Trusted", "#0000FF"  # Blue for Trusted

# default relationship_visible = False

# screen relationship_screen():

#     key "r" action ToggleVariable("relationship_visible", True, False)

#     if relationship_visible:
#         frame:
#             xalign 0.0
#             yalign 0.2
#             padding (20, 20)
#             background "#33333388"

#             vbox:
#                 spacing 10
#                 label "Relationships" xalign 0.5

#                 if len(relationships) == 0:
#                     text "You haven't met anyone yet." xalign 0.5
#                 else:
#                     for name, value in relationships.items():
#                         hbox:
#                             spacing 15
#                             xalign 0.5
#                             text f"{name}:" size 22
#                             $ status, color = get_relationship_status(value)
#                             text status size 22 color color
