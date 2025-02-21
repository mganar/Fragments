# The script of the game goes in this file.




# The game starts here.

label start:

    default male_character = "Steven"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cave with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "sylvie happy.png" to the images
    # directory.

    show sylvie normal at left with dissolve and moveinleft

   
    # These display lines of dialogue.
    sylvie "Hi! What's your name?"
    show steven happy at right with dissolve and moveinright
    menu:
        "My name is Steven.":

            sylvie "That's what I thought!"
        "My name is Marcus.":
            $ male_character = "Marcus"
            sylvie "I'm sorry, I thought you were Steven"
        "Say nothing.":
            jump say_nothing

    steven  "What's your name?"
    sylvie "My name is Sylvie"


    # This ends the game.

    return

label say_nothing:
sylvie "I should get going..."
return