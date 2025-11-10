# Quick Start Checklist

Follow these steps to get your visual novel running quickly.

---

## ☐ Phase 1: Setup (15 minutes)

### Install Ren'Py
- [ ] Download Ren'Py from https://www.renpy.org/
- [ ] Extract and launch the Ren'Py Launcher
- [ ] Create a new project (or choose existing folder)
- [ ] Note your project's `game/` folder location

### Copy Template Files
- [ ] Copy `script.rpy` to `game/script.rpy`
- [ ] Copy `screens.rpy` to `game/screens.rpy`
- [ ] Copy `options.rpy` to `game/options.rpy`
- [ ] Copy `gui.rpy` to `game/gui.rpy`

### Basic Configuration
- [ ] Open `options.rpy`
- [ ] Change `config.name` to your game's title
- [ ] Change `gui.about` to your description
- [ ] Change `build.name` to your project name (no spaces)

---

## ☐ Phase 2: Assets (30-60 minutes)

### Create Required Folders
```
game/
├── images/          (create this)
├── audio/           (create this)
└── gui/
    ├── characters/  (create this)
    ├── button/      (create this)
    └── overlay/     (create this)
```

### Prepare Backgrounds
- [ ] Choose 3-5 key background images
- [ ] Save as PNG or JPG in `game/images/`
- [ ] Rename clearly: `bg_school.png`, `bg_home.png`, etc.
- [ ] Test: Do they look good at 1920x1080?

### Prepare Character Sprites
**Option A: Quick Start (Recommended)**
- [ ] For each main character, create 3 versions:
  - happy/smiling
  - sad/upset  
  - neutral/serious
- [ ] Remove backgrounds → save as PNG with transparency
- [ ] Name format: `charactername_emotion.png`
- [ ] Example: `sakura_happy.png`, `sakura_sad.png`, `sakura_neutral.png`
- [ ] Place in `game/images/`

**Option B: Full Setup**
- [ ] Create 5-7 expressions per character
- [ ] Include: happy, sad, neutral, angry, surprised, embarrassed, thinking
- [ ] Consider multiple poses if needed

### Add Music
- [ ] Select 2-3 background music tracks
- [ ] Convert to MP3 or OGG if needed
- [ ] Place in `game/audio/`
- [ ] Name clearly: `main_theme.mp3`, `sad_theme.mp3`, etc.

### GUI Assets (Can skip initially)
- [ ] Main menu background: `game/gui/main_menu.png` (1920x1080)
- [ ] Character profile images: `game/gui/characters/` (400x600 recommended)
- [ ] Navigation arrows (optional): `game/gui/button/`

---

## ☐ Phase 3: Configuration (20 minutes)

### Update script.rpy

#### 1. Define Your Characters
- [ ] Replace example character names with yours
```python
# Replace these in script.rpy:
define sakura = Character("Sakura", color="#ff9999")
define mai = Character("Mai", color="#9999ff")
define yuki = Character("Yuki", color="#99ff99")
```

#### 2. Define Your Images
- [ ] Add your background definitions
```python
image bg school = "bg_school.png"
image bg home = "bg_home.png"
```

- [ ] Add your sprite definitions
```python
image sakura happy = "sakura_happy.png"
image sakura sad = "sakura_sad.png"
image sakura neutral = "sakura_neutral.png"
```

#### 3. Define Your Audio
- [ ] Uncomment and update audio definitions
```python
define audio.main_theme = "audio/main_theme.mp3"
define audio.sad_theme = "audio/sad_theme.mp3"
```

### Update screens.rpy

#### Update Route Selection
- [ ] Find `screen route_selection()` in screens.rpy
- [ ] Replace example routes with your routes:
```python
textbutton _("Sakura Route") action Start("route_sakura")
textbutton _("Mai Route") action Start("route_mai")
textbutton _("Common Route") action Start()
```

#### Update Character Profiles
- [ ] Find `character_profiles = [` in screens.rpy
- [ ] Update with your character information
- [ ] Update profile image paths

---

## ☐ Phase 4: Test Run (5 minutes)

### First Test
- [ ] Launch Ren'Py Launcher
- [ ] Select your project
- [ ] Click "Launch Project"
- [ ] Check main menu appears
- [ ] Try clicking "Start Game"
- [ ] Check if route selection appears

### Check for Errors
Common first-run issues:
- [ ] **"Image not found"** → Check file names match exactly
- [ ] **"Character not defined"** → Check character definitions in script.rpy
- [ ] **"Audio file not found"** → Check audio file paths
- [ ] **Menu doesn't appear** → Check screens.rpy copied correctly

### If Everything Works:
- [ ] Main menu shows ✓
- [ ] Route selection shows ✓
- [ ] Can enter a route ✓
- [ ] Background appears ✓
- [ ] Text displays ✓

---

## ☐ Phase 5: Add Content (Ongoing)

### Write Your First Scene
- [ ] Open `script.rpy`
- [ ] Find `label start:` (or create `label route_name:`)
- [ ] Add your first scene following this template:

```python
label my_first_scene:
    # Set background
    scene bg school
    with fade
    
    # Play music
    play music main_theme
    
    # Narration
    "It was a peaceful morning..."
    
    # Show character
    show sakura happy
    with dissolve
    
    # Dialogue
    sakura "Good morning!"
    
    mc "Morning, Sakura."
    
    # Continue story...
    jump next_scene
    
    return
```

### Test After Each Scene
- [ ] Save script.rpy
- [ ] In Ren'Py Launcher, click "Reload Script" (or press Shift+R in game)
- [ ] Test the new content
- [ ] Fix any errors before continuing

---

## ☐ Phase 6: Polish (Later)

### Once Basic Content is Working:
- [ ] Add transition effects (fade, dissolve, etc.)
- [ ] Add sound effects
- [ ] Create custom menu backgrounds
- [ ] Add character profile images
- [ ] Customize GUI colors in gui.rpy
- [ ] Add more music tracks
- [ ] Create additional character expressions
- [ ] Add conditional branching based on choices

---

## Troubleshooting Checklist

### Image Won't Show
- [ ] File is in `game/images/` folder?
- [ ] File name matches definition exactly? (case-sensitive!)
- [ ] PNG has transparency (for sprites)?
- [ ] Image is defined in script.rpy?
- [ ] Using `show` command correctly?

### Character Won't Talk
- [ ] Character defined in script.rpy?
- [ ] Using correct character variable name?
- [ ] Quotation marks around dialogue?

### Music Won't Play
- [ ] Audio file in `game/audio/` folder?
- [ ] File format supported (MP3, OGG, WAV)?
- [ ] Audio defined in script.rpy?
- [ ] Using `play music` command correctly?
- [ ] Volume not muted in preferences?

### Syntax Error
- [ ] Check indentation (4 spaces or 1 tab)
- [ ] Labels end with colon `:`?
- [ ] Quotes matching (`"` or `'`)?
- [ ] No spaces in label names?

### Route Selection Not Working
- [ ] screens.rpy copied to game folder?
- [ ] Route labels defined in script.rpy?
- [ ] Using `action Start("route_name")`?

---

## Minimum Viable VN Checklist

To have a working (if basic) VN, you need:
- [ ] 1 background image
- [ ] 1 character sprite (any expression)
- [ ] 1 music track (optional but recommended)
- [ ] Character defined in script.rpy
- [ ] One short scene written
- [ ] All .rpy template files in place

**That's it!** You can expand from there.

---

## Next Steps After Setup

1. **Write More Content**
   - Start with one route completely
   - Test frequently
   - Add branches later

2. **Expand Assets**
   - Add more character expressions as needed
   - Add more backgrounds when you write scenes requiring them
   - Add music variety when you need emotional range

3. **Polish UI**
   - Customize colors in gui.rpy
   - Add custom fonts
   - Create proper menu backgrounds
   - Add character profile images

4. **Test Thoroughly**
   - Play through each route
   - Test all choices
   - Check for typos and errors
   - Get feedback from others

5. **Build Distribution**
   - Once satisfied, use Ren'Py's "Build Distributions"
   - Test the built version
   - Share with testers or release!

---

## Time Estimates

- **Minimum setup to see something working:** 30 minutes
- **Basic playable demo (1 short route):** 2-3 hours
- **Full game (multiple routes, 2-4 hours play time):** 40-100+ hours

Don't rush! Focus on getting one scene perfect, then expand.

---

## Resources

- **Stuck?** Check README.md for detailed explanations
- **Converting script?** See SCRIPT_CONVERSION_GUIDE.md
- **Ren'Py questions?** https://www.renpy.org/doc/html/
- **Need help?** Lemma Soft Forums: https://lemmasoft.renai.us/forums/

---

Good luck with your visual novel! Take it one step at a time.
