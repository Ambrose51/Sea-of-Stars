# Visual Novel Setup Guide

## Getting Started

### 1. Install Ren'Py
- Download from: https://www.renpy.org/
- Extract and run the Ren'Py Launcher
- Click "Create New Project" or use an existing project folder

### 2. Project Structure

Your Ren'Py project should have this folder structure:

```
YourVNProject/
├── game/
│   ├── script.rpy          # Main story script (PROVIDED)
│   ├── options.rpy         # Game configuration (PROVIDED)
│   ├── screens.rpy         # Menu screens and UI (PROVIDED)
│   ├── gui.rpy             # GUI styling (PROVIDED)
│   ├── images/             # Your visual assets
│   │   ├── bg_school.png
│   │   ├── bg_home.png
│   │   ├── bg_street.png
│   │   ├── char_a_happy.png
│   │   ├── char_a_sad.png
│   │   └── ... (more sprites)
│   ├── audio/              # Your music and sounds
│   │   ├── main_theme.mp3
│   │   ├── sad_theme.mp3
│   │   └── sfx/
│   │       ├── door_open.ogg
│   │       └── ...
│   └── gui/                # GUI assets
│       ├── main_menu.png   # Main menu background
│       ├── game_menu.png   # In-game menu background
│       ├── window_icon.png # Window icon
│       ├── characters/     # Character profile images
│       │   ├── char_a_profile.png
│       │   ├── char_b_profile.png
│       │   └── char_c_profile.png
│       ├── button/
│       │   ├── arrow_left_idle.png
│       │   ├── arrow_left_hover.png
│       │   ├── arrow_right_idle.png
│       │   └── arrow_right_hover.png
│       └── overlay/
│           ├── main_menu.png
│           └── game_menu.png
```

### 3. Setup Instructions

1. **Copy the provided .rpy files** into your project's `game/` folder:
   - script.rpy
   - options.rpy
   - screens.rpy
   - gui.rpy

2. **Prepare your images:**
   - Background images → `game/images/`
   - Character sprites → `game/images/`
   - Profile images → `game/gui/characters/`
   - Menu backgrounds → `game/gui/`

3. **Add your music:**
   - Place music files in `game/audio/`
   - Supported formats: MP3, OGG, WAV

4. **Customize the configuration:**
   - Edit `options.rpy` to set your game title and info
   - Edit `gui.rpy` to adjust colors and fonts

---

## How to Use This Template

### Character Definitions

In `script.rpy`, define your characters:

```python
define char_name = Character("Display Name", color="#hexcolor")
```

Example:
```python
define sakura = Character("Sakura", color="#ff9999")
```

### Image Definitions

Define your backgrounds and sprites in `script.rpy`:

```python
# Backgrounds
image bg school = "bg_school.png"
image bg home = "bg_home.png"

# Character sprites
image sakura happy = "sakura_happy.png"
image sakura sad = "sakura_sad.png"
```

### Music Definitions

```python
define audio.main_theme = "audio/main_theme.mp3"
define audio.sad_music = "audio/sad_theme.mp3"
```

### Writing Scenes

Basic scene structure:

```python
label scene_name:
    # Change background
    scene bg school
    with fade
    
    # Play music
    play music main_theme fadeout 1.0 fadein 1.0
    
    # Show character sprite
    show sakura happy
    with dissolve
    
    # Dialogue
    sakura "Hello! This is my dialogue."
    
    mc "And this is the protagonist's response."
    
    # Narration (no character name)
    "The sun was setting over the school."
    
    # Hide character
    hide sakura
    with dissolve
    
    # Jump to another scene
    jump next_scene
    
    return
```

### Creating Menus/Choices

```python
menu:
    "What should I do?"
    
    "Talk to Sakura":
        jump sakura_talk
    
    "Go home":
        jump go_home
    
    "Look around":
        "You look around the area."
        jump scene_continue
```

### Route System

The template includes a route selection screen. Routes are defined as:

```python
label route_a:
    # Your route content here
    return
```

Update the route selection in `screens.rpy`:

```python
screen route_selection():
    # ...
    textbutton _("Sakura Route") action Start("route_sakura")
    textbutton _("Mai Route") action Start("route_mai")
```

---

## Character Profiles

Edit the character profile data in `screens.rpy`:

```python
character_profiles = [
    {
        "name": "Sakura",
        "image": "gui/characters/sakura_profile.png",
        "age": "18",
        "height": "165cm",
        "bio": "A cheerful student who loves reading...",
        "likes": "Reading, tea",
        "dislikes": "Loud noises"
    },
    # Add more characters...
]
```

---

## Sprite Creation Guide

### Option 1: Simple Full Sprites
- Create complete images for each pose/expression combination
- Example: `sakura_standing_happy.png`, `sakura_standing_sad.png`
- Easier to manage, but takes more space

### Option 2: Layered Sprites (Advanced)
- Create separate layers: base body, expressions, clothing
- More flexible, less space
- Requires more setup in Ren'Py

### Recommended Sprite Specs:
- **Format:** PNG with transparency
- **Height:** 1080-1920 pixels (for 1080p display)
- **Position:** Bottom-aligned (feet at bottom of image)
- **Canvas size:** Wider than the character to allow positioning

### Quick Sprite Setup:
1. Open your character art in an image editor (GIMP, Photoshop, etc.)
2. Remove background → save as PNG with transparency
3. Create variations for different expressions
4. Name consistently: `charactername_expression.png`

---

## Common Visual Effects

### Transitions
```python
with fade          # Fade to black, then fade in
with dissolve      # Crossfade
with wipeleft      # Wipe from right to left
with pixellate     # Pixellate transition
```

### Scene Changes
```python
scene bg newlocation
with fade
```

### Character Positioning
```python
show sakura happy at left     # Position on left
show sakura happy at center   # Position at center
show sakura happy at right    # Position on right
```

### Audio Control
```python
play music filename fadeout 1.0 fadein 1.0
stop music fadeout 2.0
play sound "door_open.ogg"
```

---

## Customization

### Colors (in gui.rpy)
```python
define gui.text_color = '#ffffff'        # Regular text
define gui.accent_color = '#cc6699'      # Accent color
define gui.hover_color = '#e0a0c0'       # Button hover
```

### Fonts (in gui.rpy)
```python
define gui.text_font = "YourFont.ttf"
define gui.name_text_font = "YourFont.ttf"
```

Place custom fonts in `game/` folder.

### Main Menu Background
Replace `game/gui/main_menu.png` with your background image.

---

## Converting Your Script

If you have your script in a document format:

### Basic Format:
```
[Background: School]
[Music: Main Theme]
[Show: Sakura, Happy]

SAKURA: Hello! How are you today?

PROTAGONIST: I'm doing well, thanks for asking.

[Narration] The sun shone brightly through the windows.

[Menu Choice]
> Talk about school
> Ask about her day
> Say goodbye
```

Convert to Ren'Py format:

```python
scene bg school
play music main_theme
show sakura happy

sakura "Hello! How are you today?"

mc "I'm doing well, thanks for asking."

"The sun shone brightly through the windows."

menu:
    "Talk about school":
        jump school_talk
    "Ask about her day":
        jump ask_day
    "Say goodbye":
        jump goodbye
```

---

## Testing Your Game

1. Open Ren'Py Launcher
2. Select your project
3. Click "Launch Project"
4. Test all routes and choices
5. Check for missing images/sounds (Ren'Py will show errors)

---

## Building for Distribution

1. In Ren'Py Launcher, select "Build Distributions"
2. Choose platforms: Windows, Mac, Linux
3. Click "Build"
4. Distributable files will be in the `build/` folder

---

## Common Issues & Solutions

### Missing Images
**Error:** "Image 'bg_school' not found"
**Solution:** Check that `bg_school.png` is in `game/images/` and properly defined

### Music Not Playing
**Solution:** 
- Check file path in audio definition
- Ensure file format is supported (MP3, OGG, WAV)
- Check volume settings in preferences

### Character Not Showing
**Solution:**
- Verify image is defined in script.rpy
- Check that `show` command uses correct image name
- Ensure PNG has transparency

### Syntax Errors
**Solution:**
- Check indentation (Ren'Py uses Python-style indentation)
- Verify quotes are matching (" or ')
- Make sure labels end with colon `:`

---

## Next Steps

1. **Customize the template** with your game's name and info
2. **Add your assets** (images, music, sprites)
3. **Write/convert your script** into Ren'Py format
4. **Set up character profiles** in screens.rpy
5. **Test thoroughly** before building distribution

---

## Additional Resources

- **Ren'Py Documentation:** https://www.renpy.org/doc/html/
- **Ren'Py Cookbook:** https://www.renpy.org/wiki/renpy/doc/cookbook/Cookbook
- **Lemma Soft Forums:** https://lemmasoft.renai.us/forums/

---

## Quick Reference

### Essential Commands
```python
# Scene management
scene bg_name
show sprite_name
hide sprite_name

# Audio
play music "filename"
stop music
play sound "filename"

# Transitions
with fade
with dissolve

# Text
"Narration text"
character "Dialogue text"

# Flow control
jump label_name
call label_name
return

# Choices
menu:
    "Choice text":
        # Actions
```

---

Good luck with your visual novel! Feel free to modify and expand this template as needed.
