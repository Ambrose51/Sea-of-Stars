## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.

## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
define config.name = _("Your Visual Novel Title")

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.
define gui.show_name = True

## The version of the game.
define config.version = "1.0"

## Text that is placed on the game's about screen.
define gui.about = _p("""
Your visual novel description here.

Created with Ren'Py.
""")

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.
define build.name = "YourVNTitle"

## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one to False will hide the appropriate mixer.
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.
# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"

## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.
# define config.main_menu_music = "main-menu-theme.mp3"

## Transitions #################################################################

## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.
define config.enter_transition = dissolve
define config.exit_transition = dissolve

## Between screens of the game menu.
define config.intra_transition = dissolve

## A transition that is used after a game has been loaded.
define config.after_load_transition = None

## Used when entering the main menu after the game has ended.
define config.end_game_transition = dissolve

## Window management ###########################################################

## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
define config.window = "auto"

## Transitions used to show and hide the dialogue window
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.
default preferences.text_cps = 50

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.
default preferences.afm_time = 15

## Save directory ##############################################################

## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
define config.save_directory = "YourVNTitle-1234567890"

## Icon ########################################################################

## The icon displayed on the taskbar or dock.
define config.window_icon = "gui/window_icon.png"

## Build configuration #########################################################

init python:
    ## This is used to exclude certain files from being included in the built
    ## distributions.
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    
    ## Additional build.classify commands can be added here

    ## This is used to document the files that are included in the build.
    build.documentation('*.html')
    build.documentation('*.txt')
