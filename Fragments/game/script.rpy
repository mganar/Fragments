﻿label start:
    $ inventory = Inventory([], 0)

    show screen inventory_screen  # Display the inventory permanently

label scene_1_opener:
    scene cafeteria with fade


    show valley_happy at center  # Show a happy expression for Valley
    
    valleyNar "There’s a certain rhythm to prison life. The dull hum of fluorescent lights overhead, the clatter of plastic trays on metal tables, the low murmur of conversation that never quite goes away."
    
    valleyNar "Sometimes it feels like background music to a life I never asked for."
    
    valleyNar "I can’t undo what I did. All I can do is carry it. So I do."
    
    show valley_sad at center with dissolve  # Show a sad expression for Valley
    
    valleyNar "I’d been sitting there in the cafeteria for who knows how long, hunched over a lunch I wasn’t interested in, letting my thoughts drift."
    
    valleyNar "You’d think I’d resent this place—feel anger, or desperation. But mostly, I’m just… numb."
    
    valleyNar "It's not that I enjoy being here—I don't. But I deserve this, so I'm serving my time."
    
    valleyNar "I don’t fight back. I don’t protest. I just lay low when I can and mind my business."
    
    valleyNar "Approaching prison life this way is quite boring, just the same old things. Same roll call, same bland meals, same ship repairs and tasks, same forced exercise—routine after routine."
    
    valleyNar "Even drifting in space has lost its wonder. It’s exhausting, but there’s a strange comfort in the monotony. If nothing changes, then nothing gets worse."
    
    valleyNar "I just have to hold out long enough."
    
    valleyNar "Long enough to protect the people who ended up here with me. My friends. They deserve better than this."
    
    scene prison_common_area with fade

    show valley at center with dissolve
    
    valleyNar "Some days, I almost forget where we are. We laugh, complain about the food, pass the time like any other group stuck together for too long."
    
    valleyNar "It feels normal. But it isn’t. Not really."
    
    valleyNar "Because no matter how easy the routine becomes, I know what’s waiting for me at the end of it—freedom. A fresh start. And I don’t know if I am worthy of that."
    
    valleyNar "Because no matter where I go, I’ll always carry this weight."
    
    scene fire_memory with fade

    show valley at center with dissolve
    
    valleyNar "The thought lingers, settling deep in my chest like a stone, and before I can push it down, the memories come creeping in."
    
    valleyNar "The smell hits first. Iron. Thick and suffocating, coating my tongue."
    
    valleyNar "Then the sounds—the crackling of fire, the warped groan of metal bending in the heat, the wet, gurgling breath that wasn’t supposed to be there."
    
    valleyNar "Fire moves fast. Faster than you think. It spreads like it’s alive, latching onto everything it touches, devouring without hesitation."
    
    valleyNar "I can still hear the way the walls groaned under the heat, the flickering glow turning everything into silhouettes."
    
    valleyNar "I didn’t mean for it to go that far. I didn’t mean for them to still be inside."
    
    valleyNar "I reached for them—God, I reached for them—but I hesitated. I hesitated."
    
    valleyNar "The heat burned against my skin, the metal searing into my palms, and I stopped. I froze. I was scared. I was so damn scared."
    
    valleyNar "Their voices called for me, hoarse, desperate. They knew I was there."
    
    valleyNar "And I just—stood there. Watching."
    
    valleyNar "The last thing I saw was their hand, stretching toward me, fingertips blackened, reaching—"
    
    valleyNar "And I ran."
    
    valleyNar "I just -"

label scene_2_0_banter:

    # Lila's entrance
    play sound "slam.ogg"  # Sound of the tray crashing
    "SLAM. A tray crashes onto the table, jolting me out of my trance."
    "I blink hard—sharp breath in, pulse still uneven."
    
    hide valley
    show valley_surprised at left with dissolve
    show lila_angry at right with dissolve # Show an angry expression for Lila
    lila "Aaaand once again, I grace you with my divine presence!"
    
    # Lila making a dramatic entrance
    "Her voice rings across the cafeteria, turning a few heads."
    valleyNar "Subtle? Not in her dictionary."
   
    
    
    "Behind her, Lucky shuffles over, tray in hand, eyes on the floor like he wants to disappear."
    hide lila_angry with dissolve
    show lila_happy at center with dissolve# Show a happy expression for Lila
    show lucky_sad at right with moveinright  # Show a sad expression for Lucky
    lucky "Thanks for that grand entrance, Lila. Real subtle."
    
    # Lucky's reaction to Lila's entrance
    "I got a peek at his face, half-amused, half-mortified."
    lucky "Thanks for that grand entrance, Lila. Real subtle."
    
    "He drops onto the table. I blink a few times, trying to catch up. My mind had wandered too far."
    valley "Feels strange being back in the present."
    
    # Lucky notices the protagonist's untouched tray
    lucky "..."
    "Lucky glances at my untouched tray. He doesn’t say anything, but I catch the concern in his eyes."

    # Lila sits down and begins the conversation
    lila "So..."
    lila "About that little favor I am owed..."
    
    # Lucky and protagonist exchange looks
    hide lila
    
    "Lucky and I exchanged glances."
    
    valleyNar "I already know where this is going."
    
    lucky "What favor?"
    "Lucky mouths at me."
    show lila_happy at center  # Show a happy expression for Lila
    
    # Lila's dramatic response
    lila "Oh, don’t you dare play dumb!"
    "She grips her tray dramatically, as if preparing to launch it at him."
    
    lila "You and Valley lost fair and square last week! I should be crowned Champion of the Throne, as per our agreement."
    
    # Lila's game revealed
    valleyNar "Right. Her game. Some janky, made-up card game she invented—"
    valleyNar "Rules changed every round, cards got thrown, and a ranking system only she understood."
    
    lucky "Lila, you cheated."
    lila "Creative problem-solving is not cheating."
    
    lucky "Swapping out your cards mid-round is literally cheating."
    
    # Lila's response and dismissal
    lila "Listen, if you two actually paid attention, you’d see the hidden genius behind the mechanics."
    
    lucky "I am surprised you even know what mechanics even mean."
    
    lila "..."
    valleyNar "Lila waves him off, then her eyes drift slowly to his tray. Her grin widens."
    
    lila "Last place was you, Lucky."
    lila "You know what that means..."
    
    lucky "Lila. No."
    
    # The brownie situation
    "Before she can swipe his brownie—I casually push my own tray toward her."
    
    valley "Here, take mine. I already owe Lucky a sweet from last week. Let him have his today."
    
    "Lila pauses. Raises an eyebrow."
    valleyNar "Sweets are like gold down here, it’s one of the only highlights of the day."
    lila "..."
    
    valleyNar "Lila shrugged, deciding not to question it."
    
    valleyNar "With a hum of victory, she swipes the brownie off my tray instead. She takes a slow, indulgent bite."
    
    lila "Mmm."
    "She leans back."
    lila "That’s the taste of victory."
    
    # Lucky reacts
    lucky "You idiot, you just stained your suit."
    
    "Lila freezes mid-bite. Looks down."
    valleyNar "Fashion is everything to her. She restitched her entire prisoner suit to look like a piece of designer clothing somehow."
    
    valleyNar "Then I saw it, a dark smudge of chocolate on her pristine collar."
    
    lucky "Karma."
    "Lucky grins."

    # Lila's reaction to the stain
    lila "..."
    valleyNar "Lila’s outraged expression is priceless."
    
    # Valley's reaction
    valleyNar "I let out a quiet chuckle—the tension in my chest loosening just a little."
    
    # Lila offers the brownie
    lila "You want a piece back?"
    valley "Nah, I’m good. You two fight over it."
    
    lucky "Next time, I’m calling the rules. And no swapping cards."
    
    # Lila's reply
    lila "Fine by me. Just know that I already have three different super smart strategic ways to win bubbling in my mind already."
    

    # Valley watches the playful exchange
    valleyNar "I let their playful exchange wash over me. It’s almost normal. In a place that’s anything but."
    valleyNar "I swallow down the ache in my chest, force another small smile, and let their chatter carry me away from my guilt just for a second longer."
    
    # Final line to indicate things will get serious later
    valleyNar "But in Cronemire Prison, true peace never lasts."

    return
