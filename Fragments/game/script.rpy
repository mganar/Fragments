label start:
    $ inventory = Inventory([], 0)

    show screen inventory_screen  # Display the inventory permanently
    show screen button
    show screen button1
    show screen open_relationship_menu
label scene_1_opener:

    valley "Hey, what's this?"
    "You find a crumpled bill under the tray."
    $ inventory.add_item(chest_key)
    $ inventory_menu_unlocked = True
    "Press 'I' to see you inventory!"
    scene cafeteria with fade

    if keycard in inventory.items:
        "You swipe the keycard. The door clicks open."
    else:
        "The door won’t budge. You need a keycard."

    show valley_happy at center  # Show a happy expression for Valley
    
    "There’s a certain rhythm to prison life. The dull hum of fluorescent lights overhead, the clatter of plastic trays on metal tables, the low murmur of conversation that never quite goes away."
    
    "Sometimes it feels like background music to a life I never asked for."
    
    "I can’t undo what I did. All I can do is carry it. So I do."
    
    show valley_sad at center with dissolve  # Show a sad expression for Valley
    
    "I’d been sitting there in the cafeteria for who knows how long, hunched over a lunch I wasn’t interested in, letting my thoughts drift."
    
    "You’d think I’d resent this place—feel anger, or desperation. But mostly, I’m just… numb."
    
    "It's not that I enjoy being here—I don't. But I deserve this, so I'm serving my time."
    
    "I don’t fight back. I don’t protest. I just lay low when I can and mind my business."
    
    "Approaching prison life this way is quite boring, just the same old things. Same roll call, same bland meals, same ship repairs and tasks, same forced exercise—routine after routine."
    
    "Even drifting in space has lost its wonder. It’s exhausting, but there’s a strange comfort in the monotony. If nothing changes, then nothing gets worse."
    
    "I just have to hold out long enough."
    
    "Long enough to protect the people who ended up here with me. My friends. They deserve better than this."
    
    scene prison_common_area with fade

    show valley at center with dissolve
    
    "Some days, I almost forget where we are. We laugh, complain about the food, pass the time like any other group stuck together for too long."
    
    "It feels normal. But it isn’t. Not really."
    
    "Because no matter how easy the routine becomes, I know what’s waiting for me at the end of it—freedom. A fresh start. And I don’t know if I am worthy of that."
    
    "Because no matter where I go, I’ll always carry this weight."
    
    scene fire_memory with fade

    show valley at center with dissolve
    
    "The thought lingers, settling deep in my chest like a stone, and before I can push it down, the memories come creeping in."
    
    "The smell hits first. Iron. Thick and suffocating, coating my tongue."
    
    "Then the sounds—the crackling of fire, the warped groan of metal bending in the heat, the wet, gurgling breath that wasn’t supposed to be there."
    
    "Fire moves fast. Faster than you think. It spreads like it’s alive, latching onto everything it touches, devouring without hesitation."
    
    "I can still hear the way the walls groaned under the heat, the flickering glow turning everything into silhouettes."
    
    "I didn’t mean for it to go that far. I didn’t mean for them to still be inside."
    
    "I reached for them—God, I reached for them—but I hesitated. I hesitated."
    
    "The heat burned against my skin, the metal searing into my palms, and I stopped. I froze. I was scared. I was so damn scared."
    
    "Their voices called for me, hoarse, desperate. They knew I was there."
    
    "And I just—stood there. Watching."
    
    "The last thing I saw was their hand, stretching toward me, fingertips blackened, reaching—"
    
    "And I ran."
    
    "I just —"

label scene_2_0_banter:

    # Lila's entrance
    play sound "slam.ogg"  # Sound of the tray crashing
    "SLAM. A tray crashes onto the table, jolting me out of my trance."
    "I blink hard—sharp breath in, pulse still uneven."
    
    hide valley
    show valley_surprised at left with dissolve
    show lila_angry at right with dissolve # Show an angry expression for Lila
    lila "Aaaand once again, I grace you with my divine presence!"
    $ introduce_character("Lila")
    
        # Example choice affecting Lila's relationship
    menu:
        "How do you respond to Lila's entrance?"
        
        "Laugh and play along":
            $ change_affection("Lila", 5)
            lila "See? Someone appreciates my flair."
            
        "Roll your eyes":
            $ change_affection("Lucky", -3)
            lila "Rude! I bring life to this dead place."
    

    $ relationship_menu_unlocked = True
    "You can press 'R' to check you reltionship with other characters in the game!"



    if get_affection("Mira") > 10:
        lila "You've always had my back, you know?"
    else:
            lila "Tch. You're always so cold to me."
  
    # Lila making a dramatic entrance
    "Her voice rings across the cafeteria, turning a few heads."
    "Subtle? Not in her dictionary."
   
    "Behind her, Lucky shuffles over, tray in hand, eyes on the floor like he wants to disappear."
    hide lila_angry with dissolve
    show lila_happy at center with dissolve  # Show a happy expression for Lila
    show lucky_sad at right with moveinright  # Show a sad expression for Lucky
    lucky "Thanks for that grand entrance, Lila. Real subtle."
    $ introduce_character("Lucky")
 

    # Lucky's reaction to Lila's entrance
    "I got a peek at his face, half-amused, half-mortified."
 
    
    "He drops onto the table. I blink a few times, trying to catch up. My mind had wandered too far."
    valley "Feels strange being back in the present."
    
    # Lucky notices the protagonist's untouched tray
    hide lucky_sad
    show lucky at right
    lucky "..."
    "Lucky glances at my untouched tray. He doesn’t say anything, but I catch the concern in his eyes."

    # Lila sits down and begins the conversation
    lila "So..."
    lila "About that little favor I am owed..."
    # Player makes a choice here
    menu(time=5, timeout="left_hanging"):
        "Give Lila the brownie":
            $ change_affection("Lila", 30)
            $ change_affection("Lucky", -30)
         
            valley "Here, take mine. I already owe Lucky a sweet from last week. Let him have his today."
            "Sweets are like gold down here, it’s one of the only highlights of the day."
            lila "Mmm."
            lila "That’s the taste of victory."
        "Defend Lucky’s brownie":
            $ change_affection("Lila", -30)
            $ change_affection("Lucky", +30)

            valley "Back off, Lila. Lucky earned that brownie."
            lila "Wow. Harsh."
            "Her grin falters for just a second."
            lucky "Thanks, Valley. Appreciate it."
    label left_hanging:
        "Your silence means everything"
        

   

    # Lucky and protagonist exchange looks
    hide lila_happy
    "Lucky and I exchanged glances."
    "I already know where this is going."
    lucky "What favor?"
    "Lucky mouths at me."
   
    show lila_happy
    # Lila's dramatic response
    lila "Oh, don’t you dare play dumb!"
    "She grips her tray dramatically, as if preparing to launch it at him."
    
    lila "You and Valley lost fair and square last week! I should be crowned Champion of the Throne, as per our agreement."
    
    # Lila's game revealed
    "Right. Her game. Some janky, made-up card game she invented—"
    "Rules changed every round, cards got thrown, and a ranking system only she understood."
    
    lucky "Lila, you cheated."
    lila "Creative problem-solving is not cheating."
    
    lucky "Swapping out your cards mid-round is literally cheating."
    
    # Lila's response and dismissal
    lila "Listen, if you two actually paid attention, you’d see the hidden genius behind the mechanics."
    
    lucky "I am surprised you even know what mechanics even mean."
    
    lila "..."
    "Lila waves him off, then her eyes drift slowly to his tray. Her grin widens."
    
    lila "Last place was you, Lucky."
    lila "You know what that means..."
    
    lucky "Lila. No."
    
    # The brownie situation
    "Before she can swipe his brownie—I casually push my own tray toward her."
    
    valley "Here, take mine. I already owe Lucky a sweet from last week. Let him have his today."
    
    "Lila pauses. Raises an eyebrow."
    "Sweets are like gold down here, it’s one of the only highlights of the day."
    lila "..."
    
    "Lila shrugged, deciding not to question it."
    
    "With a hum of victory, she swipes the brownie off my tray instead. She takes a slow, indulgent bite."
    
    lila "Mmm."
    "She leans back."
    lila "That’s the taste of victory."
    
    # Lucky reacts
    lucky "You idiot, you just stained your suit."
    
    "Lila freezes mid-bite. Looks down."
    "Fashion is everything to her. She restitched her entire prisoner suit to look like a piece of designer clothing somehow."
    
    "Then I saw it, a dark smudge of chocolate on her pristine collar."
    
    lucky "Karma."
    "Lucky grins."

    # Lila's reaction to the stain
    lila "..."
    "Lila’s outraged expression is priceless."
    
    # Valley's reaction
    "I let out a quiet chuckle—the tension in my chest loosening just a little."
    
    # Lila offers the brownie
    lila "You want a piece back?"
    valley "Nah, I’m good. You two fight over it."
    
    lucky "Next time, I’m calling the rules. And no swapping cards."
    
    # Lila's reply
    lila "Fine by me. Just know that I already have three different super smart strategic ways to win bubbling in my mind already."
    

    # Valley watches the playful exchange
    "I let their playful exchange wash over me. It’s almost normal. In a place that’s anything but."
    "I swallow down the ache in my chest, force another small smile, and let their chatter carry me away from my guilt just for a second longer."
    
    # Final line to indicate things will get serious later
    "But in Cronemire Prison, true peace never lasts."

    


label scene_3_cafeteria_chaos:


    "They say lunch is supposed to be the most peaceful time of day around here."
    "Personally, I wouldn’t describe it as peaceful—the food they serve is borderline a war crime."
    "But it’s one of the few times I get to sit and talk with the friends I made."

    "Normally, the cafeteria is just a cramped, echoing box, filled with the dull clatter of trays and the low murmur of conversation."
    "Everyone knows who not to mess with and who to sit with."
    "I’d found a semi-quiet spot by the so-called 'windows'—which are really just torn holes in the wall."

    "My table is the same as always."
    "Just me, Lucky, and Lila."
    "It used to be four of us."
    "We still carry her with us—"
    "We even save her seat despite it always being empty."
    "We don’t talk about her being gone. We just kind of continue as if she is still here."
    "This place already has a bad mood to it, and some things are too heavy to say out loud."
    "Better to keep it that way."
    hide lila_happy
    show lila normal 
    show lucky normal at right with dissolve

    "We poke at our trays—mushy potatoes, watery peas, and something that might have once been meat—trying to choke it down while talking about anything other than prison life."
    "Maybe the next game we’d play, or the plans for when we finally got out."

    "It was an unspoken rule between us: no judgment."
    "We never asked each other what we did to end up here—not unless the other person wanted to tell."
    "It kept things simple, made sure our friendship wasn’t built on guilt or distrust."
    "We were here for who we were now, not whatever mistakes had landed us in this place."
    "It was Lucky who came up with that pact, and I am quite glad he did."

    "Still, I had plans to keep us together once we were free. It’s not like I had anyone waiting for me on the outside."

    show lila grin at center with dissolve

    lila "Alright!"
    "Lila suddenly tosses her fork down with an air of absolute authority."
    
    lucky "Oh no."

    "Lucky glances up, already wary."

    lila "Once we’re out of here, we’re opening a restaurant."

    hide lucky
    
    show lucky surprised at right 

    "I pause mid-bite, blinking." 
    "That was not where I thought this was going."
    lucky "You? Owning a restaurant? What, so you can boss us around all day?"

    show lila smug at center

    "Lila grows a completely serious expression."
    lila "That’s the point."
    lucky "That’s a terrible point."

    show lila smug2 

    lila "You say that now, but just imagine it. I run the front—customers love me, obviously."
    lila "Lucky, you’ll handle the finances, since, you know—you're the nerd."

    show lucky shocked at right

    "Lucky’s mouth drops wide open."
    lucky "Excuse me—"
    hide lila shocked
    show lila excited 

    lila "Gin, our top cook, I can help her cause I am the sweetest of all time and memorized— all. her. recipes."
    
    "I smile at that."

    show lila thinking
    "Then she turns to me, tilting her head as if considering."
    valley "What? What’s my job?"

    show lila smug
    lila "You’re in charge of the taste-testing, of course."

  
    hide lila_happy 
    show lila shocked 

   
   
    valley "Yeah, that’s real smart. Put me in charge of eating the product and see how long we last before we go bankrupt."


   
    "Lila gasps dramatically, clutching her chest."
    lila "Valley, I am offended that you think I wouldn’t factor your gluttony into my business model."

    show lucky angry
    lucky "No—no, cause let’s go back to that nerd comment—"

    "I almost laugh, shaking my head."

    "As he continues, I start to look around the cafeteria like I always do."
    hide valley_surprised with dissolve
    hide lila shocked with dissolve
    hide lucky angry with dissolve
    "I can’t help but notice something is off today."
    "Some sort of tension."
    "If you’re around here long enough, you start to understand and get used to how things are supposed to feel."

    "The guards weren’t just their usual bored selves—they were watching. Focused."
    "The prisoners seemed too… off."
    "Small groups whispering in corners, a few guys standing instead of sitting, too quiet in a place that usually never shut up."

    "My gut told me something was coming."

    play sound "thud.ogg"

    "Before I can look around further, I hear a—"



    "THUD."

    "A chair scrapes violently against the floor."
    "A tray crashes."
    "A sharp inhale echoes across the hall, and then—"
    play music "tense_music.ogg"
    "silence"


    "A voice cuts through the tension like a blade."

    show garrick normal with dissolve
    garrick "Watch where you’re going, stupid."



    "Even if I hadn’t heard him, I would’ve felt him."
    "Garrick has this way of being noticed without making a scene—because he doesn’t have to."
    "His presence alone is enough."

    "The guy he just shoved is frozen in place."
    "His tray had gone flying, splattering mashed potatoes and peas all over the ground."
    "He twitches, debating whether to pick it up or run the hell away."

    show garrick angry
    garrick "Pick it up."

    "Not a request. A threat."

    "The prisoner hesitates."
    "The cafeteria holds its breath."

    pause 1.0

    play sound "splat.ogg"

    "And then—"
    
    "SPLAT."

label scene_3_1_instant_regret:

    scene cafeteria with fade

    "Time stopped."
    "Every single person at the nearby tables went stiff."
    "For a second, I couldn’t process it. The nearby tables near us grew instantly rigid."

    show lila shocked at left
    show lucky shocked at right

    "Lila’s eyes went wide; Lucky’s mouth hung open."
    "Actually, Lucky’s whole body hung open."
    "He was staring at his hand, which was still raised—like he was trying to throw a baseball in gym class."
    "Only, this was no gym class."

    show lucky thinking
    "Lucky blinked once, his expression oddly impressed with himself."
    lucky "Wow. Direct hit…"

    show valley shocked
    "I felt a prickling along the back of my neck. My stomach turned cold. Did he really just—?"
    
    valley "Lucky… what the hell did you just do?"

    show lucky nervous
    "He didn’t answer immediately. He just kept examining his hand—turning it over and back, as if the betrayal lay in his own fingers."
    
    lucky "Honestly, I—I don’t know."
    lucky "I saw it happening, and then my arm just… did the thing, y’know?"

    valley "What thing?!"

    show lila grin
    "I flicked my gaze to Lila."
    "She was vibrating—desperately holding in laughter."
    "She had that look in her eye, the one that screamed, 'This is about to get interesting.'"

    scene cafeteria with fade

    show garrick normal at center with dissolve
    "Across the room, Garrick slowly wiped the potatoes off his face."
    "No emotion. No reaction."

    show garrick angry
    "But I could see it—the subtle clench of his jaw, the tension in his grip."

    "And then, he took a step forward."

    show garrick angry at right with move

    show lucky terrified at left
    "Lucky stiffened. His forced smile twitched."
    lucky "Soooo… that was fun, right?"
    lucky "You have to admit, great trajectory, solid impact—"

    "He paused, swallowing hard."

    lucky "Please don’t kill me."

    "He then started walking."
    "Right. Toward. Us."

    show garrick lunge at center with move
    "Garrick lunged."

    show lucky panic at left
    hide lucky panic with dissolve
    play sound "yelping.ogg"
    "Lucky yelped and ducked under the table."
    
    play sound "table_hit.ogg"
    "Garrick’s hand swiped through empty air, colliding with the tabletop and making everything rattle."

    valley "I couldn’t believe we picked a fight with Garrick of all people."

    return

