# The script of the game goes in this file.




# The game starts here.

label start:
    transform move_up:
        yalign 0.3  # Adjust this value to move characters higher

    default male_character = "Valley"

    scene cave with dissolve

    
        # First pair appears
    show cyrus neutral at left with moveinleft
    Cyrus "Alright, everyone. We need to decide what to do next."
    show mira neutral at right with moveinright
    Mira "I say we move forward. Staying here isn’t going to help."

    # Both characters disappear after speaking
    hide cyrus with dissolve
    hide mira with dissolve

    # Second pair appears
    show garrick neutral at left with moveinleft
    Garrick "Are you sure? We don’t even know what’s ahead."
    show veyla neutral at right with moveinright
    Veyla "Hah! Since when has uncertainty ever stopped us?"

    # Both characters disappear after speaking
    hide garrick with dissolve
    hide veyla with dissolve

    # Third pair appears
    show ethan neutral at left with moveinleft
    Ethan "Veyla has a point. But we should at least prepare before we rush in."
    show lila neutral at right with moveinright
    Lila "I don’t like this... Something feels off."


    Valley "I agree with Lila. Maybe we should take a moment to assess the situation."

    # Cyrus returns for final dialogue
    hide ethan with dissolve
    show cyrus neutral at left with moveinleft
    Cyrus "Fair enough. But we can’t sit here forever. What do you think, Valley?"



    menu:
        "We should move forward.":
            Valley "Let’s go. We’re wasting time."
            hide lila with dissolve
            show mira neutral at right with moveinright
            Mira "Finally, some action!"
            Cyrus "Alright, but stay close."
            hide cyrus with dissolve
            hide mira with dissolve

        "We should wait a bit longer.":
            Valley "No need to rush. Let’s think this through."
            Lila "Thank you. I just need a moment."
            hide lila with dissolve
            Cyrus "Caution isn’t a bad thing."
            hide cyrus with dissolve
            


        "Maybe we should split up.":
            Valley "What if we split up and cover more ground?"
            hide lila with dissolve
            show veyla neutral at right with moveinright
            Veyla "Now that’s an idea!"
            Cyrus "Dangerous, but it could work..."
            hide cyrus with dissolve 
            hide veyla with dissolve


    return

# The script of the game goes in this file.




