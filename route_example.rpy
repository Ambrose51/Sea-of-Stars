## Example Character Route File
## This shows how to organize a complete character route in a separate file
## Save as: game/route_sakura.rpy (or whatever character name you use)

################################################################################
## Sakura Route
## This file contains all scenes and logic for Sakura's route
################################################################################

## Initialize route-specific variables
default sakura_affection = 0
default sakura_date_accepted = False
default sakura_confession_success = False
default sakura_scenes_completed = []

################################################################################
## Route Entry Point
################################################################################

label route_sakura:
    ## This is the main entry point for Sakura's route
    ## Called when player selects "Sakura Route" from main menu
    
    ## Initialize route
    $ sakura_affection = 50  # Starting affection
    $ sakura_route_active = True
    
    ## Start with the introduction scene
    jump sakura_intro

################################################################################
## Act 1: Introduction and Setup
################################################################################

label sakura_intro:
    scene bg school courtyard
    with fade
    
    play music main_theme fadeout 1.0 fadein 2.0
    
    "It's the first day of a new semester."
    
    "As I walk through the school courtyard, I notice cherry blossom petals dancing in the breeze."
    
    show sakura happy
    with dissolve
    
    sakura "Oh! Good morning!"
    
    mc "Morning, Sakura. The cherry blossoms are beautiful this year."
    
    show sakura happy at left
    with move
    
    sakura "Aren't they? I come here every morning just to see them."
    
    "Sakura twirls, her hair flowing in the wind as petals swirl around her."
    
    menu sakura_intro_choice:
        "How should I respond?"
        
        "That sounds peaceful.":
            $ sakura_affection += 5
            
            sakura "It really is! Would you like to join me sometime?"
            
            mc "I'd like that."
            
        "Sounds boring to me.":
            $ sakura_affection -= 10
            
            show sakura sad
            
            sakura "Oh... I suppose not everyone appreciates quiet moments."
            
            mc "Sorry, that came out wrong."
            
        "Maybe you could show me your favorite spot?":
            $ sakura_affection += 10
            
            show sakura happy
            
            sakura "Really? I'd love to! Let's go now!"
            
            jump sakura_special_spot
    
    jump sakura_first_class

label sakura_special_spot:
    scene bg sakura tree
    with fade
    
    "Sakura leads me to a secluded spot under the largest cherry tree."
    
    show sakura happy
    
    sakura "This is my secret place. I've never shown anyone else before."
    
    mc "It's amazing. Thank you for sharing it with me."
    
    $ sakura_affection += 15
    $ sakura_scenes_completed.append("special_spot")
    
    "We spend the next few minutes in comfortable silence, watching the petals fall."
    
    jump sakura_first_class

################################################################################
## Act 1: Daily Scenes
################################################################################

label sakura_first_class:
    scene bg classroom
    with fade
    
    "The morning classes pass by in a blur."
    
    "I find myself glancing at Sakura throughout the lecture."
    
    show sakura neutral
    with dissolve
    
    "She seems absorbed in taking notes, occasionally tucking a strand of hair behind her ear."
    
    "The teacher drones on about something I can't quite focus on."
    
    menu:
        "Pass a note to Sakura?":
            $ sakura_affection += 3
            jump sakura_note_passing
        
        "Focus on the lecture":
            jump sakura_lunch_time
        
        "Daydream":
            jump sakura_caught_daydreaming

label sakura_note_passing:
    "I quickly scribble a note and slide it across to Sakura's desk."
    
    show sakura happy
    
    "She reads it and giggles quietly, covering her mouth."
    
    "She writes something back and passes it over."
    
    "'You're going to get us in trouble!' it says, with a small smiley face."
    
    jump sakura_lunch_time

label sakura_caught_daydreaming:
    "Teacher" "And you there! Are you paying attention?"
    
    mc "Uh, yes! Of course!"
    
    show sakura neutral at right
    with dissolve
    
    "I notice Sakura hiding a smile as the teacher moves on."
    
    $ sakura_affection += 2
    
    jump sakura_lunch_time

label sakura_lunch_time:
    scene bg school rooftop
    with fade
    
    "Lunchtime. I head up to the rooftop, my usual spot."
    
    show sakura happy
    with dissolve
    
    sakura "Mind if I join you?"
    
    mc "Not at all. Have a seat."
    
    "Sakura sits down next to me, unpacking her lunch."
    
    sakura "I made too much today. Would you like some?"
    
    menu sakura_lunch_choice:
        "Sure, thanks!":
            $ sakura_affection += 8
            
            "She offers me a perfectly shaped rice ball."
            
            mc "This is really good! Did you make it yourself?"
            
            show sakura happy
            
            sakura "I did! I'm so glad you like it."
            
        "I'm okay, but thank you.":
            $ sakura_affection += 2
            
            sakura "Alright, but let me know if you change your mind!"
    
    "We eat together, chatting about nothing in particular."
    
    "It's... nice. Comfortable."
    
    jump sakura_after_school

################################################################################
## Act 1: After School Event
################################################################################

label sakura_after_school:
    scene bg school gate
    with fade
    
    "School's over for the day. As I head toward the gate..."
    
    show sakura neutral
    with dissolve
    
    sakura "Hey, wait up!"
    
    mc "Sakura? What's up?"
    
    show sakura happy
    
    sakura "I was wondering... are you free this weekend?"
    
    mc "This weekend? I think so. Why?"
    
    sakura "There's a festival in town. I thought maybe we could go together?"
    
    "She looks at me hopefully, her hands clasped together."
    
    menu sakura_festival_invitation:
        "This is an important choice. Think carefully."
        
        "I'd love to go with you!":
            $ sakura_affection += 20
            $ sakura_date_accepted = True
            
            show sakura happy
            
            sakura "Really? That's wonderful!"
            
            sakura "Let's meet at the shrine entrance at 6 PM on Saturday!"
            
            mc "It's a date."
            
            show sakura happy
            
            sakura "A... date. Yes."
            
            "I can see her cheeks turn slightly pink."
            
            jump sakura_day_1_end
        
        "Maybe... let me check my schedule?":
            $ sakura_affection += 5
            
            show sakura neutral
            
            sakura "Oh, of course. Let me know soon, okay?"
            
            mc "I will."
            
            "She seems a bit disappointed but understanding."
            
            jump sakura_festival_decision
        
        "I don't think I can make it.":
            $ sakura_affection -= 15
            
            show sakura sad
            
            sakura "Oh... I understand. Maybe another time."
            
            mc "Sorry..."
            
            hide sakura
            with dissolve
            
            "She walks away, and I feel a pang of regret."
            
            jump sakura_day_1_end

label sakura_festival_decision:
    scene bg home
    with fade
    
    "That evening, I think about Sakura's invitation."
    
    menu:
        "Accept the invitation (text her)":
            $ sakura_affection += 10
            $ sakura_date_accepted = True
            
            "I send her a text accepting the invitation."
            
            "My phone buzzes almost immediately with her enthusiastic response."
            
            jump sakura_day_1_end
        
        "Decline politely (text her)":
            $ sakura_affection -= 10
            
            "I send a polite text declining."
            
            "She responds with an understanding message, but I can sense the disappointment."
            
            jump sakura_day_1_end

label sakura_day_1_end:
    scene bg home
    with fade
    
    "Day 1 complete."
    
    ## Debug affection level
    "Current Sakura affection: [sakura_affection]"
    
    ## Continue to next day
    if sakura_date_accepted:
        jump sakura_festival_preparation
    else:
        jump sakura_day_2

################################################################################
## Act 2: Festival Date
################################################################################

label sakura_festival_preparation:
    scene bg home
    with fade
    
    "Saturday arrives. I spend extra time getting ready."
    
    "I want to make a good impression."
    
    jump sakura_festival_meeting

label sakura_festival_meeting:
    scene bg shrine entrance
    with fade
    
    play music festival_theme fadein 2.0
    
    "The festival is already in full swing when I arrive."
    
    "Lanterns illuminate the evening, and the air is filled with the sounds of laughter and festival music."
    
    show sakura yukata happy
    with dissolve
    
    sakura "There you are!"
    
    "Sakura stands waiting, wearing a beautiful yukata with cherry blossom patterns."
    
    mc "Wow... you look amazing."
    
    show sakura yukata happy
    
    sakura "Thank you... You look nice too."
    
    $ sakura_affection += 5
    
    sakura "Shall we go?"
    
    jump sakura_festival_activities

label sakura_festival_activities:
    scene bg festival
    
    "We walk through the festival together."
    
    menu sakura_festival_activity:
        "What should we do first?"
        
        "Try the food stalls":
            jump sakura_festival_food
        
        "Play some games":
            jump sakura_festival_games
        
        "Watch the performances":
            jump sakura_festival_performance

label sakura_festival_food:
    "We stop at a takoyaki stand."
    
    show sakura yukata happy
    
    sakura "These look delicious!"
    
    "We share a serving, laughing as we blow on the hot pieces."
    
    $ sakura_affection += 5
    
    jump sakura_festival_shrine

label sakura_festival_games:
    "We try our luck at a goldfish scooping game."
    
    show sakura yukata happy
    
    "Sakura manages to catch three goldfish while I can barely catch one."
    
    sakura "You need a gentler touch!"
    
    "She laughs, and I can't help but smile at her joy."
    
    $ sakura_affection += 7
    
    jump sakura_festival_shrine

label sakura_festival_performance:
    "We find a spot to watch traditional dancers."
    
    show sakura yukata happy
    
    "Sakura watches with fascination, her eyes reflecting the lantern light."
    
    $ sakura_affection += 6
    
    jump sakura_festival_shrine

label sakura_festival_shrine:
    scene bg shrine
    with fade
    
    "We make our way to the shrine at the heart of the festival."
    
    show sakura yukata neutral
    
    sakura "Want to make a wish?"
    
    mc "Sure."
    
    "We each toss a coin and bow our heads in prayer."
    
    "I steal a glance at Sakura, wondering what she's wishing for."
    
    show sakura yukata happy
    
    sakura "What did you wish for?"
    
    menu:
        "If I tell you, it won't come true.":
            $ sakura_affection += 5
            
            sakura "I suppose that's true."
            
        "I wished for your happiness.":
            $ sakura_affection += 15
            
            show sakura yukata happy
            
            sakura "Really? That's... that's so sweet."
            
        "I wished for us to always be together.":
            $ sakura_affection += 20
            
            show sakura yukata happy
            
            "Her eyes widen, and she looks down shyly."
            
            sakura "I... I wished for the same thing."
    
    jump sakura_festival_fireworks

label sakura_festival_fireworks:
    scene bg festival hill
    with fade
    
    "As the evening winds down, we find a quiet spot on a hill overlooking the festival."
    
    show sakura yukata happy
    
    sakura "The fireworks should start soon."
    
    "We sit together, the sounds of the festival drifting up to us."
    
    play sound "audio/sfx/fireworks.ogg"
    
    "Suddenly, the sky erupts in color."
    
    "Boom! Boom! Boom!"
    
    "Brilliant reds, blues, and golds paint the night sky."
    
    show sakura yukata happy
    
    "I glance at Sakura. She's watching the fireworks with wonder."
    
    "Without thinking, I reach for her hand."
    
    "She looks at me in surprise, then smiles and interlaces her fingers with mine."
    
    $ sakura_affection += 25
    
    sakura "This is perfect..."
    
    "We watch the rest of the fireworks together, hand in hand."
    
    jump sakura_festival_end

label sakura_festival_end:
    scene bg shrine entrance
    with fade
    
    stop music fadeout 3.0
    
    "The festival is over, and it's time to say goodbye."
    
    show sakura yukata happy
    
    sakura "Thank you for tonight. I had an amazing time."
    
    mc "Me too. We should do this again sometime."
    
    show sakura yukata happy
    
    sakura "I'd really like that."
    
    "There's a moment of hesitation, and then she leans in and gives me a quick kiss on the cheek."
    
    show sakura yukata happy
    
    sakura "Goodnight!"
    
    "She runs off before I can respond, leaving me standing there, touching my cheek."
    
    $ sakura_affection += 30
    
    jump sakura_day_3

################################################################################
## Continue with more scenes, leading to confession and ending
################################################################################

label sakura_day_2:
    ## Additional scenes for non-festival path
    "Day 2 scene placeholder"
    jump sakura_day_3

label sakura_day_3:
    ## More story development
    "Day 3 scene placeholder"
    
    if sakura_affection >= 100:
        jump sakura_confession
    else:
        jump sakura_day_4

label sakura_confession:
    scene bg sakura tree
    with fade
    
    play music emotional_theme fadein 2.0
    
    "Sakura asked me to meet her at our special place."
    
    show sakura nervous
    with dissolve
    
    sakura "Thank you for coming."
    
    mc "Of course. What did you want to talk about?"
    
    show sakura nervous
    
    sakura "I... There's something I need to tell you."
    
    "She takes a deep breath."
    
    sakura "Ever since we first met, I felt something special."
    
    sakura "The more time we spend together, the stronger this feeling grows."
    
    sakura "I... I've fallen in love with you."
    
    "Cherry blossom petals drift down around us, as if nature itself is holding its breath."
    
    menu sakura_confession_response:
        "This is the most important choice."
        
        "I love you too, Sakura.":
            $ sakura_confession_success = True
            
            show sakura happy
            
            sakura "Really? You mean it?"
            
            mc "With all my heart."
            
            "She rushes forward and embraces me."
            
            sakura "I'm so happy!"
            
            jump sakura_good_ending
        
        "I care about you, but...":
            $ sakura_confession_success = False
            
            show sakura sad
            
            sakura "I... I understand."
            
            sakura "Thank you for being honest with me."
            
            jump sakura_friend_ending

################################################################################
## Endings
################################################################################

label sakura_good_ending:
    scene bg sakura tree
    
    "From that day forward, Sakura and I were together."
    
    "Through all seasons, our love remained as constant as the cherry blossoms that return each spring."
    
    show sakura happy
    
    sakura "I love you."
    
    mc "I love you too."
    
    "THE END - Sakura Route: True Ending"
    
    $ persistent.sakura_true_ending = True
    
    return

label sakura_friend_ending:
    scene bg school
    
    "Though we didn't become a couple, our friendship remained strong."
    
    "Sakura moved on, eventually finding happiness with someone else."
    
    "And I was genuinely happy for her."
    
    "Sometimes, love means letting go."
    
    "THE END - Sakura Route: Friendship Ending"
    
    $ persistent.sakura_friend_ending = True
    
    return

label sakura_day_4:
    ## More story if affection not high enough
    "Placeholder for additional scenes"
    return

################################################################################
## Helper Labels
################################################################################

label sakura_check_affection:
    ## Debug function to check current affection
    "Sakura affection: [sakura_affection]"
    return
