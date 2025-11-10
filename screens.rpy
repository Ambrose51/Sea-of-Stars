## This file contains screens for the game menus and UI elements.

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")

style button:
    properties gui.button_properties("button")

style button_text:
    properties gui.button_text_properties("button")

style label_text:
    properties gui.text_properties("label", accent=True)

style prompt_text:
    properties gui.text_properties("prompt")

################################################################################
## In-game screens
################################################################################

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

## Make the namebox available for styling through the say screen.
style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

################################################################################
## Main Menu Screen
################################################################################

screen main_menu():
    tag menu
    
    ## This ensures that any other menu screen is replaced.
    style_prefix "main_menu"
    
    add gui.main_menu_background
    
    ## The main menu buttons
    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        
        has vbox:
            spacing 20
            xalign 0.5
            
        text "{size=60}Sea of Stars{/size}":
            xalign 0.5
            text_align 0.5
            
        null height 20
        
        textbutton _("Start Game") action ShowMenu("route_selection")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Character Profiles") action ShowMenu("character_profiles")
        textbutton _("Options") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Quit") action Quit(confirm=not main_menu)

style main_menu_frame:
    background Frame("gui/overlay/main_menu.png", gui.frame_borders, tile=gui.frame_tile)
    padding gui.frame_borders.padding

style main_menu_vbox:
    xalign 0.5
    xsize 400
    xmaximum 400

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    xalign 0.5

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_button:
    properties gui.button_properties("main_menu_button")
    xminimum 350

style main_menu_button_text:
    properties gui.button_text_properties("main_menu_button")
    xalign 0.5

################################################################################
## Route Selection Screen
################################################################################

screen route_selection():
    tag menu
    
    add gui.main_menu_background
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        
        has vbox:
            spacing 15
            xalign 0.5
            
        text "{size=50}Select Your Route{/size}":
            xalign 0.5
            text_align 0.5
            
        null height 20
        
        ## Add your routes here - example routes below
        textbutton _("Character A Route") action Start("route_a")
        textbutton _("Character B Route") action Start("route_b")
        textbutton _("Character C Route") action Start("route_c")
        textbutton _("Common Route") action Start()
        
        null height 20
        
        textbutton _("Return") action ShowMenu("main_menu")

style route_selection_frame:
    background Frame("gui/overlay/main_menu.png", gui.frame_borders, tile=gui.frame_tile)
    padding gui.frame_borders.padding

style route_selection_button:
    properties gui.button_properties("main_menu_button")
    xminimum 500

style route_selection_button_text:
    properties gui.button_text_properties("main_menu_button")
    xalign 0.5

################################################################################
## Character Profiles Screen
################################################################################

## Define character profile data and load from JSON
init python:
    import json
    import os

    def load_character_data():
        """Load all character JSON files from Character Sheets directory"""
        character_profiles = []
        char_sheets_dir = os.path.join(config.basedir, "Character Sheets")

        if os.path.exists(char_sheets_dir):
            for filename in os.listdir(char_sheets_dir):
                if filename.startswith("char_") and filename.endswith(".json"):
                    filepath = os.path.join(char_sheets_dir, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            char_data = json.load(f)
                            character_profiles.append(char_data)
                    except Exception as e:
                        print("Error loading {}: {}".format(filename, e))

        return character_profiles if character_profiles else []

    # Load character data at init time
    character_profiles = load_character_data()
    current_profile = 0

screen character_profiles():
    tag menu

    add gui.main_menu_background

    if not character_profiles:
        ## No characters found
        frame:
            xalign 0.5
            yalign 0.5
            padding (40, 30)

            vbox:
                spacing 20
                text "No character sheets found" size 30
                text "Place character JSON files in the 'Character Sheets' folder" size 18
                textbutton _("Return") action ShowMenu("main_menu") xalign 0.5
    else:
        $ profile = character_profiles[current_profile]

        ## Navigation buttons - simple text buttons for now
        if current_profile > 0:
            textbutton "<":
                xalign 0.05
                yalign 0.5
                action SetVariable("current_profile", current_profile - 1)

        if current_profile < len(character_profiles) - 1:
            textbutton ">":
                xalign 0.95
                yalign 0.5
                action SetVariable("current_profile", current_profile + 1)

        ## Main character sheet display
        viewport:
            xalign 0.5
            yalign 0.5
            xsize 1200
            ysize 650
            scrollbars "vertical"
            mousewheel True

            vbox:
                spacing 15
                xsize 1150

                ## Header - Character Name and Basic Info
                frame:
                    xfill True
                    padding (20, 15)
                    background "#20253580"

                    vbox:
                        spacing 5
                        text "[profile[characterName]]":
                            size 48
                            bold True
                            color "#ffd700"

                        if profile.get("characterQuote"):
                            text "\"{0}\"".format(profile["characterQuote"]):
                                size 20
                                italic True
                                color "#b8c5ff"

                ## Core Identity
                frame:
                    xfill True
                    padding (20, 15)
                    background "#20253560"

                    hbox:
                        spacing 40

                        vbox:
                            spacing 8
                            text "Identity" size 24 bold True color "#6b8cff"
                            text "Role: {0}".format(profile.get("role", "N/A")) size 18
                            text "Rank: {0}".format(profile.get("rank", "N/A")) size 18
                            text "Origin: {0}".format(profile.get("originNode", "N/A")) size 18

                        vbox:
                            spacing 8
                            text "State" size 24 bold True color "#6b8cff"
                            text "Sephira: {0}".format(profile.get("sephiraState", "N/A")) size 18
                            text "Ascension: {0}".format(profile.get("ascensionState", "N/A")) size 18
                            text "Blood: {0}".format(profile.get("bloodPattern", "N/A")) size 18

                        vbox:
                            spacing 8
                            text "Attributes" size 24 bold True color "#6b8cff"
                            text "Genotype: {0}".format(profile.get("genotype", "N/A")) size 18
                            text "Potential: {0}".format(profile.get("potential", "N/A")) size 18
                            text "Grudge: {0}".format(profile.get("grudgeLevel", "N/A")) size 18

                ## Statistics
                if profile.get("statistics"):
                    frame:
                        xfill True
                        padding (20, 15)
                        background "#20253560"

                        vbox:
                            spacing 10
                            text "Statistics" size 24 bold True color "#ffd700"

                            grid 3 3:
                                spacing 20
                                xfill True

                                for stat_name, stat_value in sorted(profile["statistics"].items()):
                                    hbox:
                                        spacing 10
                                        text "{0}:".format(stat_name.capitalize()) size 18 min_width 150
                                        text "{0}".format(stat_value) size 18 bold True color "#98fb98"

                ## Soul State
                if profile.get("soulState"):
                    frame:
                        xfill True
                        padding (20, 15)
                        background "#20253560"

                        vbox:
                            spacing 10
                            text "Soul-State Status" size 24 bold True color "#b19cd9"

                            grid 4 2:
                                spacing 20
                                xfill True

                                for soul_stat, soul_value in sorted(profile["soulState"].items()):
                                    hbox:
                                        spacing 10
                                        text "{0}:".format(soul_stat.capitalize()) size 18 min_width 180
                                        text "{0}".format(soul_value) size 18 bold True color "#dda0dd"

                ## Alignments
                frame:
                    xfill True
                    padding (20, 15)
                    background "#20253560"

                    vbox:
                        spacing 10
                        text "Alignments & Affinities" size 24 bold True color "#ff6b9d"

                        if profile.get("emotionalMeridians"):
                            hbox:
                                spacing 10
                                text "Emotional Meridians:" size 18 bold True
                                text ", ".join(profile["emotionalMeridians"]) size 18

                        if profile.get("conceptualAlignments"):
                            hbox:
                                spacing 10
                                text "Conceptual:" size 18 bold True
                                text ", ".join([a.replace("em-", "").replace("ca-", "").title() for a in profile["conceptualAlignments"]]) size 16

                        if profile.get("worldlineAffinities"):
                            hbox:
                                spacing 10
                                text "Worldline:" size 18 bold True
                                text ", ".join([a.replace("ca-", "").replace("wa-", "").title() for a in profile["worldlineAffinities"]]) size 16

                ## Powers
                if profile.get("powers") and profile["powers"]:
                    frame:
                        xfill True
                        padding (20, 15)
                        background "#20253560"

                        vbox:
                            spacing 10
                            text "Powers" size 24 bold True color "#ffa500"

                            for power in profile["powers"]:
                                vbox:
                                    spacing 5
                                    text "• {0}".format(power.get("name", "Unknown Power")) size 20 bold True
                                    if power.get("description"):
                                        text "  {0}".format(power["description"]) size 16

                ## Additional Info
                if profile.get("additionalRules"):
                    frame:
                        xfill True
                        padding (20, 15)
                        background "#20253560"

                        vbox:
                            spacing 8
                            text "Additional Rules" size 24 bold True color "#87ceeb"
                            text "{0}".format(profile["additionalRules"]) size 16

        ## Return button
        textbutton _("Return to Main Menu"):
            xalign 0.5
            yalign 0.97
            action ShowMenu("main_menu")

################################################################################
## Game Menu Screen
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
    
    frame:
        style "game_menu_outer_frame"

        hbox:
            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        has vbox
                        transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:
                    transclude
    
    use navigation
    
    textbutton _("Return"):
        style "return_button"
        action Return()
    
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120
    
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

################################################################################
## Navigation Screen
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"
        
        xpos gui.navigation_xpos
        yalign 0.5
        
        spacing gui.navigation_spacing
        
        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
        
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Options") action ShowMenu("preferences")
        
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()
        
        textbutton _("About") action ShowMenu("about")
        
        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

################################################################################
## About Screen
################################################################################

screen about():
    tag menu
    
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            
            if gui.about:
                text "[gui.about!t]\n"
            
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

style about_label:
    padding (30, 30)

style about_label_text:
    size gui.label_text_size

style about_text:
    size gui.text_size
    xalign 0.5
    text_align 0.5
    layout "subtitle"

################################################################################
## Load and Save Screens
################################################################################

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    
    use game_menu(title):
        
        fixed:
            
            ## Ensure buttons work even if not in correct order
            order_reverse True
            
            button:
                style "page_label"
                
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                
                input:
                    style "page_label_text"
                    value page_name_value
            
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                
                xalign 0.5
                yalign 0.5
                
                spacing gui.slot_spacing
                
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    
                    $ slot = i + 1
                    
                    button:
                        action FileAction(slot)
                        
                        has vbox
                        
                        add FileScreenshot(slot) xalign 0.5
                        
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        
                        text FileSaveName(slot):
                            style "slot_name_text"
                        
                        key "save_delete" action FileDelete(slot)
            
            hbox:
                style_prefix "page"
                
                xalign 0.5
                yalign 1.0
                
                spacing gui.page_spacing
                
                textbutton _("<") action FilePagePrevious()
                
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")
                
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)
                
                textbutton _(">") action FilePageNext()

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

style slot_time_text:
    size gui.slot_time_text_size
    color gui.idle_small_color

style slot_name_text:
    size gui.slot_name_text_size

################################################################################
## Preferences Screen
################################################################################

screen preferences():
    tag menu
    
    use game_menu(_("Options"), scroll="viewport"):
        
        vbox:
            
            hbox:
                box_wrap True
                
                if renpy.variant("pc") or renpy.variant("web"):
                    
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                
                null width 200
                
                vbox:
                    style_prefix "slider"
                    label _("Text Speed")
                    
                    bar value Preference("text speed")
                    
                    label _("Auto-Forward Time")
                    
                    bar value Preference("auto-forward time")
                
                vbox:
                    
                    if config.has_music:
                        label _("Music Volume")
                        
                        hbox:
                            bar value Preference("music volume")
                    
                    if config.has_sound:
                        label _("Sound Volume")
                        
                        hbox:
                            bar value Preference("sound volume")
                            
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    
                    if config.has_voice:
                        label _("Voice Volume")
                        
                        hbox:
                            bar value Preference("voice volume")
                            
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                        
                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing
                            
                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_label:
    xsize 250

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_label:
    xsize 250

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_label:
    xsize 250

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

################################################################################
## History Screen
################################################################################

screen history():
    tag menu
    
    predict False
    
    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        
        style_prefix "history"
        
        for h in _history_list:
            
            window:

                hbox:
                    spacing 10

                    if h.who:
                        label h.who:
                            style "history_name"
                            substitute False

                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False
        
        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_allow_tags = set()

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xsize gui.history_name_width
    xalign 1.0
    yalign 0.5

style history_name_text:
    min_width gui.history_name_width
    text_align 1.0

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

################################################################################
## Help Screen
################################################################################

screen help():
    tag menu
    
    default device = "keyboard"
    
    use game_menu(_("Help"), scroll="viewport"):
        
        style_prefix "help"
        
        vbox:
            spacing 15
            
            hbox:
                
                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
                
                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
            
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():
    
    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")
    
    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")
    
    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")
    
    hbox:
        label _("Escape")
        text _("Accesses the game menu.")
    
    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")
    
    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")
    
    hbox:
        label "Page Up"
        text _("Rolls back to earlier dialogue.")
    
    hbox:
        label "Page Down"
        text _("Rolls forward to later dialogue.")
    
    hbox:
        label "H"
        text _("Hides the user interface.")
    
    hbox:
        label "S"
        text _("Takes a screenshot.")
    
    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

screen mouse_help():
    
    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")
    
    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")
    
    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")
    
    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")
    
    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")

screen gamepad_help():
    
    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")
    
    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")
    
    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")
    
    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")
    
    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")
    
    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0

################################################################################
## Confirm Screen
################################################################################

screen confirm(message, yes_action, no_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_frame:
    background Frame(["gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt:
    xalign 0.5
    text_align 0.5
    layout "subtitle"

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
