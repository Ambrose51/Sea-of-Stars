## The script of the game goes in this file.

################################################################################
## Configuration
################################################################################

## Splashscreen - runs on first launch, then shows main menu
label splashscreen:
    return

## Main menu label - required for Ren'Py to show the main menu screen on launch
label main_menu:
    return

################################################################################
## Character Definitions
################################################################################

## Define your characters here. The color argument colorizes the name of the
## character.

define narrator = Character(None, kind=nvl)  # For narration
define mc = Character("Protagonist", color="#c8ffc8")  # Main character

## Example characters - customize these with your character names and colors
define char_a = Character("Character A", color="#c8c8ff")
define char_b = Character("Character B", color="#ffc8c8")
define char_c = Character("Character C", color="#ffffc8")

################################################################################
## Images
################################################################################

## Define images for backgrounds
## Place your background images in the game/images folder
## Example: game/images/bg_school.png

image bg school = "bg_school.png"
image bg home = "bg_home.png"
image bg street = "bg_street.png"

## Define images for character sprites
## Place your character sprites in the game/images folder
## Format: game/images/charactername_pose_expression.png

## Character A sprites
image char_a happy = "char_a_happy.png"
image char_a sad = "char_a_sad.png"
image char_a neutral = "char_a_neutral.png"

## Character B sprites
image char_b happy = "char_b_happy.png"
image char_b sad = "char_b_sad.png"
image char_b neutral = "char_b_neutral.png"

## Character C sprites
image char_c happy = "char_c_happy.png"
image char_c sad = "char_c_sad.png"
image char_c neutral = "char_c_neutral.png"

################################################################################
## Music and Sound
################################################################################

## Define your music tracks
## Place your music files in the game/audio folder

## Example music definitions
# define audio.main_theme = "audio/main_theme.mp3"
# define audio.sad_theme = "audio/sad_theme.mp3"
# define audio.happy_theme = "audio/happy_theme.mp3"

## Example sound effects
# define audio.door_open = "audio/sfx/door_open.ogg"
# define audio.phone_ring = "audio/sfx/phone_ring.ogg"

################################################################################
## Game Start
################################################################################

## This is the main entry point of your game.
## If no specific route is chosen, this will run.

label start:
    ## Start label - show main menu if called directly
    ## This should only be called from the route selection screen with a specific route

    ## Jump directly to main menu to prevent auto-start
    jump main_menu

################################################################################
## Common Route Scenes
################################################################################

label look_around:
    hide char_a
    with dissolve
    
    "You look around the area."
    
    "There's so much to see..."
    
    return

label char_a_intro:
    char_a happy "I'm so glad you want to talk to me!"
    
    mc "Nice to meet you."
    
    char_a neutral "What brings you here today?"
    
    return

################################################################################
## Character Routes
################################################################################

## Character A Route
label route_a:
    scene bg school
    with fade
    
    # play music main_theme fadeout 1.0 fadein 1.0
    
    "You've entered Character A's route."
    
    show char_a happy
    with dissolve
    
    char_a "Welcome to my story!"
    
    ## Continue your story here
    ## You can split this into multiple labels for organization
    
    "To be continued..."
    
    return

## Character B Route
label route_b:
    scene bg street
    with fade
    
    # play music main_theme fadeout 1.0 fadein 1.0
    
    "You've entered Character B's route."
    
    show char_b neutral
    with dissolve
    
    char_b "Oh, you're here."
    
    ## Continue your story here
    
    "To be continued..."
    
    return

## Character C Route
label route_c:
    scene bg home
    with fade
    
    # play music main_theme fadeout 1.0 fadein 1.0
    
    "You've entered Character C's route."
    
    show char_c happy
    with dissolve
    
    char_c "I've been waiting for you!"
    
    ## Continue your story here
    
    "To be continued..."
    
    return

################################################################################
## Utility Labels
################################################################################

## This is called when the game ends normally
label end:
    "The End"
    
    ## You can show credits here or return to main menu
    return
