# Visual Novel Folder Structure

## Complete Project Structure

```
YourVisualNovel/
│
├── game/                           # Main game folder - all your content goes here
│   │
│   ├── script.rpy                 # ← COPY HERE: Main story file
│   ├── options.rpy                # ← COPY HERE: Game configuration
│   ├── screens.rpy                # ← COPY HERE: UI and menus
│   ├── gui.rpy                    # ← COPY HERE: Visual styling
│   │
│   ├── images/                    # ← CREATE THIS: All visual assets
│   │   ├── bg_school.png          # Background images
│   │   ├── bg_home.png
│   │   ├── bg_street.png
│   │   ├── bg_cafe.png
│   │   │
│   │   ├── sakura_happy.png       # Character sprites
│   │   ├── sakura_sad.png
│   │   ├── sakura_neutral.png
│   │   ├── mai_happy.png
│   │   └── ... (more sprites)
│   │
│   ├── audio/                     # ← CREATE THIS: Music and sounds
│   │   ├── main_theme.mp3
│   │   ├── sad_theme.mp3
│   │   ├── happy_theme.mp3
│   │   ├── tense_theme.mp3
│   │   │
│   │   └── sfx/                   # Sound effects (optional)
│   │       ├── door_open.ogg
│   │       ├── phone_ring.ogg
│   │       └── footsteps.ogg
│   │
│   ├── gui/                       # ← CREATE THESE: GUI assets
│   │   ├── main_menu.png          # Main menu background (1920x1080)
│   │   ├── game_menu.png          # In-game menu background (1920x1080)
│   │   ├── window_icon.png        # Window icon (256x256)
│   │   │
│   │   ├── characters/            # Character profile images
│   │   │   ├── sakura_profile.png (recommended: 400x600)
│   │   │   ├── mai_profile.png
│   │   │   └── yuki_profile.png
│   │   │
│   │   ├── button/                # Navigation buttons (optional)
│   │   │   ├── arrow_left_idle.png
│   │   │   ├── arrow_left_hover.png
│   │   │   ├── arrow_right_idle.png
│   │   │   └── arrow_right_hover.png
│   │   │
│   │   └── overlay/               # Menu overlays (optional)
│   │       ├── main_menu.png
│   │       └── game_menu.png
│   │
│   ├── tl/                        # Translations (created by Ren'Py)
│   │   └── None/                  # Default language
│   │
│   ├── saves/                     # Save files (created by Ren'Py)
│   │
│   └── cache/                     # Cache (created by Ren'Py)
│
├── renpy/                         # Ren'Py engine (don't modify)
│
├── lib/                           # Python libraries (don't modify)
│
└── [YourVNTitle].exe             # Windows executable (after building)
```

---

## What Goes Where

### Core Game Files (.rpy)
**Location:** `game/`

These are the template files you downloaded:
- `script.rpy` - Your story
- `screens.rpy` - Menus and UI
- `options.rpy` - Settings
- `gui.rpy` - Styling

---

### Backgrounds
**Location:** `game/images/`  
**Format:** PNG or JPG  
**Recommended size:** 1920x1080 (16:9 ratio)

**Naming convention:**
```
bg_[location].png
```

**Examples:**
- `bg_school.png`
- `bg_classroom.png`
- `bg_cafeteria.png`
- `bg_library.png`
- `bg_gym.png`
- `bg_home_livingroom.png`
- `bg_home_bedroom.png`
- `bg_street.png`
- `bg_park.png`

---

### Character Sprites
**Location:** `game/images/`  
**Format:** PNG with transparency  
**Recommended height:** 1080-1920 pixels

**Naming convention:**
```
[charactername]_[expression].png
```

**Examples:**
```
sakura_happy.png
sakura_sad.png
sakura_neutral.png
sakura_angry.png
sakura_surprised.png
sakura_embarrassed.png
sakura_thinking.png

mai_happy.png
mai_sad.png
mai_neutral.png
...
```

**With poses:**
```
sakura_standing_happy.png
sakura_sitting_happy.png
sakura_uniform_happy.png
sakura_casual_happy.png
```

---

### Music
**Location:** `game/audio/`  
**Format:** MP3, OGG, or WAV  
**MP3 recommended** for compatibility

**Naming convention:**
```
[descriptor]_theme.mp3
```

**Examples:**
- `main_theme.mp3` - Main menu / general
- `happy_theme.mp3` - Cheerful scenes
- `sad_theme.mp3` - Emotional scenes
- `tense_theme.mp3` - Dramatic scenes
- `romantic_theme.mp3` - Romance scenes
- `battle_theme.mp3` - Action scenes
- `mystery_theme.mp3` - Mystery scenes

---

### Sound Effects (Optional)
**Location:** `game/audio/sfx/`  
**Format:** OGG or WAV  
**OGG recommended** for size

**Examples:**
- `door_open.ogg`
- `door_close.ogg`
- `footsteps.ogg`
- `phone_ring.ogg`
- `message_received.ogg`
- `bell.ogg`
- `rain.ogg`
- `thunder.ogg`

---

### GUI Assets

#### Main Menu Background
**Location:** `game/gui/main_menu.png`  
**Size:** 1920x1080  
**Format:** PNG or JPG

#### Game Menu Background
**Location:** `game/gui/game_menu.png`  
**Size:** 1920x1080  
**Format:** PNG or JPG

#### Window Icon
**Location:** `game/gui/window_icon.png`  
**Size:** 256x256  
**Format:** PNG

#### Character Profiles
**Location:** `game/gui/characters/`  
**Recommended size:** 400x600  
**Format:** PNG

---

## Organizing Routes (Advanced)

For better organization, you can split routes into separate files:

```
game/
├── script.rpy               # Main file with definitions
├── route_common.rpy         # Common route scenes
├── route_sakura.rpy         # Sakura's complete route
├── route_mai.rpy            # Mai's complete route
├── route_yuki.rpy           # Yuki's complete route
└── endings.rpy              # All ending scenes
```

Each route file would contain all scenes for that character's path.

---

## Asset Checklist

### Minimum Required:
- [ ] 1-3 background images
- [ ] 1 character sprite (any expression)
- [ ] 1 main menu background (can reuse a game background)
- [ ] 1 music track (optional but recommended)

### Standard Setup:
- [ ] 5-10 background images
- [ ] 3-5 sprites per main character
- [ ] 3-5 music tracks
- [ ] Character profile images
- [ ] Window icon

### Full Polish:
- [ ] 15+ background images
- [ ] 5-10 sprites per character
- [ ] Multiple poses per character
- [ ] 8+ music tracks
- [ ] Sound effects
- [ ] Custom GUI graphics
- [ ] Character profile images
- [ ] Custom fonts

---

## File Size Guidelines

### Backgrounds
- 1920x1080 PNG: 1-5 MB each
- 1920x1080 JPG: 200-800 KB each
- Use JPG for photos/realistic backgrounds
- Use PNG for artistic/illustrated backgrounds

### Sprites
- Character sprite PNG: 500 KB - 2 MB each
- Ensure transparency is preserved
- Compress if needed (PNG optimization)

### Music
- MP3 (128-192 kbps): 2-4 MB per minute
- OGG: Slightly smaller than MP3
- Keep tracks under 5 minutes if looping

### Sound Effects
- OGG: 10-100 KB each
- Keep short (1-3 seconds)

---

## Creating Folders

### Windows:
```batch
cd path\to\your\project\game
mkdir images
mkdir audio
mkdir audio\sfx
mkdir gui
mkdir gui\characters
mkdir gui\button
mkdir gui\overlay
```

### Mac/Linux:
```bash
cd path/to/your/project/game
mkdir -p images
mkdir -p audio/sfx
mkdir -p gui/characters
mkdir -p gui/button
mkdir -p gui/overlay
```

---

## Quick Reference

| Asset Type | Location | Format | Size |
|------------|----------|--------|------|
| Backgrounds | `game/images/` | PNG/JPG | 1920x1080 |
| Sprites | `game/images/` | PNG | 1080-1920h |
| Music | `game/audio/` | MP3/OGG | Any |
| SFX | `game/audio/sfx/` | OGG/WAV | Any |
| Main Menu BG | `game/gui/` | PNG/JPG | 1920x1080 |
| Profiles | `game/gui/characters/` | PNG | 400x600 |
| Window Icon | `game/gui/` | PNG | 256x256 |

---

## Don't Modify These Folders

- `renpy/` - Ren'Py engine files
- `lib/` - Python libraries  
- `game/cache/` - Generated cache
- `game/saves/` - Player save files
- `game/tl/` - Translations (unless translating)

---

## Build Output

After building your game, you'll see:
```
YourVN-1.0-pc/        # Windows/Linux build
YourVN-1.0-mac/       # Mac build
YourVN-1.0-web/       # Web build (if enabled)
```

---

This structure will keep your project organized and make it easier to find and manage your assets!
