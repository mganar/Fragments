

label start:
    $ inventory = Inventory([], 0)
show screen inventory_screen  # Display the inventory permanently
# Scene 1: Renn's Introduction and Manipulation of Mira

scene cave_background with fade

# Introducing Renn
show renn grinning at left
renn "The Lord has a plan for us all. Those who trust in His will shall find salvation. Those who question Him... shall suffer."

# Renn addresses the group, speaking with charm
renn "I know you’re all scared. But there is a way out of this—through faith. Divine judgment has brought us here for a reason, and we must see it through."

# Some prisoners listen attentively, others remain skeptical
renn "But remember, survival isn’t just about being strong. It’s about knowing when to bend the knee, when to act with wisdom. Only the chosen will rise."

# Mira’s struggle, uncertain and fearful
show mira at center
mira "I... I don’t know if I can trust anyone here."

# Renn approaches her, his voice soothing
renn "Mira, sweet child, trust in me. You feel it, don’t you? The weight of the decisions ahead. Fear is natural, but so is faith. You need to choose who to trust."

# Renn manipulates her fear
renn "If you rely on them, on the prisoners... they’ll betray you. But me? I can see the path ahead. We can make it out together, but only if you listen and act swiftly. I know how to survive."

# Mira, swayed by his words, grows more uncertain but agrees
mira "But... how do I know you’re telling the truth?"

renn "You don’t. That’s the beauty of it, isn't it? Faith is never about certainty. It’s about action, about believing when no one else will. Don’t waste time questioning—take action before it’s too late."

# Renn smiles, satisfied with his manipulation
renn "I promise, Mira, I’ll make sure you’re safe. Just remember, survival comes first. We’ll make it through this... together."

# Scene Transition: Renn's Final Trickery

# Renn encounters the mimic
hide mira with dissolve
show mimic 
renn "Ah, a prisoner in need. You’ve come to the right person."

# Mimic, pretending to be a prisoner, speaks
mimic "I’m starving... can you help me? Find me food and water. I’ll give you something in return."

# Renn, thinking he's outsmarted the mimic, grins widely
renn "Of course. I have just what you need."

# The mimic asks for water, and Renn goes to fetch it
renn "Here, drink first. It's a deal, right?"

# Renn, eager to turn the tables, drinks first, not realizing the danger
renn "Mmm, tastes just fine. Now... your turn."

# As Renn finishes drinking, he begins to stiffen, realizing too late
renn "W-Wait... What is this? No... NO!"

# The mimic laughs menacingly as Renn’s body turns to stone
mimic "You should’ve known... you’ve played the game of deception too long."

# Renn’s final moment as he turns completely to stone
"show renn, now a statue, with a grim smile frozen on his face"
renn "So... this... is how it ends."
hide renn with dissolve

# Scene transition

# Scene 2: Garrick Steals His Revolver
scene cave_background with fade

# Introduction to Cyrus
cyrus "Stay in line, prisoners. You are here to work, not to complain."

# The player interacts with Cyrus
menu:
    "Remain silent.":
        cyrus "Good. Silence is a sign of respect for authority."
    "Challenge him.":
        cyrus "Do you think you have a say here? No, you do not. You are beneath me."

# Tension with Garrick
cyrus "Garrick, you're causing too much trouble. I’ll deal with you in due time."
show garrick angry at left with fade
cyrus "You think you can just steal from me?"

# Garrick takes the revolver
cyrus "This revolver is a symbol of authority. You don’t understand its power."
hide garrick angry
show garrick with fade
cyrus "You’re making a big mistake."

# Cyrus loses control
menu:
    "Stay calm.": 
        cyrus "So you think I can’t survive without it? You’re wrong."
    "Panic.": 
        cyrus "Get it together! Don’t you see the danger here?"

# Scene 2: Forced to Trust a Prisoner
# Cyrus reflects on his vulnerability
cyrus "I’ve always relied on my strength, my authority... but now, I’m vulnerable."
cyrus "Is this what it means to be weak? To rely on others?"

# Cyrus decides to trust
cyrus "Fine, if I have to trust you, I will. But this better not be a mistake."

# Scene 3: The Supernatural Becomes Undeniable
# Mysterious noise disrupts the moment
play sound "mysterious_noise.mp3"
cyrus "This... what is that? Is this some trick?"

# Cyrus admits uncertainty
cyrus "No... this is no trick. There’s something wrong with this cave. Something I don’t understand."

# Scene 4: The Standoff: Choosing Between a Guard & a Prisoner
# Reflection on leadership
show cyrus thoughtful at center
cyrus "Maybe it’s not about control after all."
menu:
    "You’re starting to see it now.":
        cyrus "Perhaps... but I still believe in duty. Duty over everything."
    "You’ve been holding on too long.":
        cyrus "Maybe you’re right. But the world I knew doesn’t exist here anymore."

# Scene 5: The Cigarette Scene: Reflection of Change
cyrus "Survival isn’t about control. It’s about trust. And right now, that’s all we’ve got."

# Scene 6: His Final Sacrifice
# Final choice
cyrus "I’ll make my choice. It’s not about power anymore."

# Scene transition
return
