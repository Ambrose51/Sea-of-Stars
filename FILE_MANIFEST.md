# Visual Novel Template - File Manifest

## Overview
This package contains everything you need to start building your visual novel in Ren'Py. Below is a description of each file and what it's used for.

---

## Core Template Files (Required)

### 1. **script.rpy**
**Purpose:** Main story script file  
**Goes in:** `game/script.rpy`  
**Contains:**
- Character definitions
- Image definitions (backgrounds and sprites)
- Audio definitions
- Main story labels and scenes
- Route entry points

**You will edit this file to:**
- Define your characters
- Add your image and audio assets
- Write your story scenes
- Create character routes

---

### 2. **screens.rpy**
**Purpose:** User interface and menu screens  
**Goes in:** `game/screens.rpy`  
**Contains:**
- Main menu with route selection
- Character profiles screen
- Save/load screens
- Preferences/options screen
- Game menu navigation
- In-game UI elements

**You will edit this file to:**
- Customize route selection buttons
- Add character profile information
- Adjust menu styling (optional)

---

### 3. **options.rpy**
**Purpose:** Game configuration and settings  
**Goes in:** `game/options.rpy`  
**Contains:**
- Game title and version info
- Audio/video settings
- Window management
- Save directory configuration
- Build settings

**You will edit this file to:**
- Set your game's title
- Configure game metadata
- Adjust default preferences

---

### 4. **gui.rpy**
**Purpose:** GUI styling and visual customization  
**Goes in:** `game/gui.rpy`  
**Contains:**
- Color schemes
- Font definitions
- Button styles
- Layout positioning
- UI element sizing

**You will edit this file to:**
- Change colors and themes
- Customize fonts
- Adjust UI appearance

---

## Documentation Files (Reference)

### 5. **README.md**
**Purpose:** Comprehensive setup and usage guide  
**Use for:**
- Understanding the project structure
- Learning Ren'Py basics
- Finding examples of common patterns
- Troubleshooting common issues
- Understanding how to organize your assets

**Key sections:**
- Folder structure explanation
- Image preparation guide
- Scene writing examples
- Music integration
- Sprite creation tips
- Customization options

---

### 6. **QUICK_START.md**
**Purpose:** Step-by-step checklist to get started quickly  
**Use for:**
- Following a structured setup process
- Ensuring you don't miss critical steps
- Troubleshooting during initial setup
- Understanding minimum requirements

**Follow this for:**
- First-time setup
- Quick reference during development
- Debugging common issues

---

### 7. **SCRIPT_CONVERSION_GUIDE.md**
**Purpose:** Guide for converting existing scripts to Ren'Py format  
**Use for:**
- Converting scripts from other formats
- Understanding Ren'Py syntax
- Learning by example
- Batch conversion strategies

**Helpful if you:**
- Have scripts in Word/Google Docs
- Are porting from another engine
- Need syntax reference
- Want to automate conversion

---

## Example Files (Learning Resources)

### 8. **route_example.rpy**
**Purpose:** Complete example of a character route  
**Use for:**
- Understanding route structure
- Seeing affection system in action
- Learning branching paths
- Understanding variable usage

**This file shows:**
- How to organize a full route
- Affection/relationship mechanics
- Multiple endings
- Choice consequences
- Scene transitions
- Event progression

**Note:** This is an EXAMPLE only. Don't put it in your actual game folder unless you want to use it as a template. Study it and adapt the patterns for your own routes.

---

## How to Use These Files

### Step 1: Setup
1. Install Ren'Py
2. Create a new project
3. Copy the 4 core template files (.rpy) into your `game/` folder

### Step 2: Read Documentation
1. Start with **QUICK_START.md** - follow the checklist
2. Reference **README.md** when you need detailed explanations
3. Use **SCRIPT_CONVERSION_GUIDE.md** if converting existing scripts

### Step 3: Customize
1. Edit **options.rpy** - set your game title and info
2. Edit **script.rpy** - define characters, images, audio
3. Edit **screens.rpy** - update route selection and character profiles
4. Edit **gui.rpy** (optional) - customize colors and fonts

### Step 4: Add Content
1. Place your assets in appropriate folders
2. Write your scenes in **script.rpy**
3. Test frequently in Ren'Py

### Step 5: Learn from Examples
1. Study **route_example.rpy** to understand route structure
2. Adapt patterns for your own routes
3. Reference examples in **README.md**

---

## File Dependencies

```
options.rpy
└── Defines game configuration

gui.rpy
└── Defines visual styling

screens.rpy
├── Uses gui.rpy for styling
└── Displays menus and UI

script.rpy
├── Uses definitions from options.rpy
└── Main game entry point
    ├── Defines characters
    ├── Defines images
    ├── Defines audio
    └── Contains all story content
```

---

## What You Need to Provide

These files provide the STRUCTURE. You need to provide:

1. **Story Content**
   - Your script/dialogue
   - Scene descriptions
   - Character development

2. **Visual Assets**
   - Background images
   - Character sprites
   - UI graphics (optional)
   - Character profile images (optional)

3. **Audio Assets**
   - Background music
   - Sound effects (optional)
   - Voice acting (optional)

4. **Customization**
   - Character names and info
   - Route names and paths
   - Color schemes (optional)
   - Fonts (optional)

---

## File Editing Priority

If you're overwhelmed, edit files in this order:

1. **options.rpy** - 5 minutes
   - Set game title
   - Set game info

2. **script.rpy** - Ongoing
   - Define your characters (10 minutes)
   - Define your images (15 minutes)
   - Write your story (ongoing)

3. **screens.rpy** - 15 minutes
   - Update route selection
   - Update character profiles

4. **gui.rpy** - Optional
   - Only edit if you want custom colors/fonts
   - Can be done later

---

## Minimum Working Setup

To see something working, you only need to edit:
- **options.rpy** (game title)
- **script.rpy** (1 character, 1 background, 1 scene)

Everything else can wait!

---

## Getting Help

- Check **README.md** for detailed explanations
- Check **QUICK_START.md** for troubleshooting
- Visit Ren'Py documentation: https://www.renpy.org/doc/html/
- Ask on Lemma Soft Forums: https://lemmasoft.renai.us/forums/

---

## License Note

These template files are provided as-is for you to use and modify for your visual novel project. You own your game and all content you create with these templates.

The template structure is free to use. Ren'Py itself is licensed under LGPL, which means you can create commercial games with it.

---

## Version Info

Template Version: 1.0  
Compatible with: Ren'Py 7.4+, Ren'Py 8.0+  
Created: 2025

---

Good luck with your visual novel!
