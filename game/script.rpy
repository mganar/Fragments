

label start:
    $ inventory = Inventory([], 0)

    
    show screen inventory_screen  # Display the inventory permanently




    
    transform move_up:
        yalign 0.3  # Adjust this value to move characters higher

    default male_character = "Valley"

    scene cave with dissolve

    # Show the Continue button
    

    # First pair appears
    show cyrus neutral at left with moveinleft
    Cyrus "Alright, everyone. We need to decide what to do next. How many items do you have Valley"
    
    $ inventory.list_items()

    show mira neutral at right with moveinright
    Mira "Here's a chest key, I left my other one at home but you can have it"
    $ inventory.add_item(chest_key)

    # Both characters disappear after speaking
    hide cyrus with dissolve
    hide mira with dissolve

    # Second pair appears
    show garrick neutral at left with moveinleft
    Garrick "You're going to need this too."
    $ inventory.add_item(door_key)

    

    show veyla neutral at right with moveinright
    Veyla "Hah! Can you hold 3 items?"
    $ inventory.add_item(cash)
    Veyla "Welp looks like you can't. Sorry"
    $ inventory.list_items()

    

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

    

    # Decision Menu
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
