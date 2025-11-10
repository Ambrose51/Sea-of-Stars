# Script Conversion Example

This guide shows you how to convert a traditional visual novel script into Ren'Py format.

---

## Example: Traditional Script Format

```
=== SCENE 1: THE MEETING ===
LOCATION: School Courtyard
TIME: Morning
MUSIC: Peaceful Morning Theme
BACKGROUND: bg_school_courtyard.png

[The protagonist walks through the courtyard]

NARRATION: It was a beautiful spring morning. Cherry blossoms drifted through the air.

[SAKURA appears, looking cheerful]
SPRITE: Sakura - Happy

SAKURA: Oh! Good morning!

PROTAGONIST: Morning, Sakura. You're here early.

SAKURA: I wanted to see the cherry blossoms at their peak!

[Sakura's expression changes to thoughtful]
SPRITE: Sakura - Thoughtful

SAKURA: Hey, can I ask you something?

PROTAGONIST: Sure, what is it?

SAKURA: There's a festival this weekend. Would you like to go together?

[CHOICE MENU]
CHOICE 1: "I'd love to!"
    -> Jump to: sakura_festival_accept
CHOICE 2: "I'm not sure..."
    -> Jump to: sakura_festival_hesitant
CHOICE 3: "I can't, sorry."
    -> Jump to: sakura_festival_decline

=== END SCENE ===
```

---

## Converted to Ren'Py Format

```python
## Scene 1: The Meeting

label scene_1_meeting:
    # Set up the scene
    scene bg school courtyard
    with fade
    
    play music "audio/peaceful_morning.mp3" fadeout 1.0 fadein 1.0
    
    # Narration
    "It was a beautiful spring morning. Cherry blossoms drifted through the air."
    
    # Show character
    show sakura happy
    with dissolve
    
    # Dialogue
    sakura "Oh! Good morning!"
    
    mc "Morning, Sakura. You're here early."
    
    sakura "I wanted to see the cherry blossoms at their peak!"
    
    # Change expression
    show sakura thoughtful
    
    sakura "Hey, can I ask you something?"
    
    mc "Sure, what is it?"
    
    sakura "There's a festival this weekend. Would you like to go together?"
    
    # Choice menu
    menu:
        "I'd love to!":
            jump sakura_festival_accept
        
        "I'm not sure...":
            jump sakura_festival_hesitant
        
        "I can't, sorry.":
            jump sakura_festival_decline
    
    return

## Continuation scenes based on choices

label sakura_festival_accept:
    show sakura happy
    with dissolve
    
    sakura "Really? That's wonderful!"
    
    mc "It sounds like fun. I'm looking forward to it."
    
    sakura "Me too! Let's meet at the entrance at 6 PM!"
    
    # Continue story...
    jump scene_2_preparation
    
    return

label sakura_festival_hesitant:
    show sakura sad
    with dissolve
    
    sakura "Oh... I understand if you're busy..."
    
    mc "No, it's not that. I just need to check something first."
    
    show sakura neutral
    
    sakura "Okay. Let me know soon, alright?"
    
    # This might affect relationship later
    $ sakura_affection -= 5
    
    jump scene_2_decision
    
    return

label sakura_festival_decline:
    show sakura sad
    with dissolve
    
    sakura "I see... That's okay."
    
    mc "Sorry, I really can't make it."
    
    sakura "Don't worry about it. Maybe another time."
    
    hide sakura
    with dissolve
    
    # Significant relationship impact
    $ sakura_affection -= 20
    
    jump scene_2_alone
    
    return
```

---

## Conversion Rules

### 1. Scene Headers → Labels
```
=== SCENE 1: THE MEETING ===
```
Becomes:
```python
label scene_1_meeting:
```

**Tips:**
- Use lowercase with underscores
- Make labels descriptive
- No spaces in label names

### 2. Location/Background → scene command
```
BACKGROUND: bg_school_courtyard.png
```
Becomes:
```python
scene bg school courtyard
with fade
```

**Note:** Image files can be referenced with spaces in code, but file names should use underscores.

### 3. Music → play music
```
MUSIC: Peaceful Morning Theme
```
Becomes:
```python
play music "audio/peaceful_morning.mp3" fadeout 1.0 fadein 1.0
```

### 4. Narration → Plain text
```
NARRATION: It was a beautiful spring morning.
```
Becomes:
```python
"It was a beautiful spring morning."
```

### 5. Character Sprites → show command
```
[SAKURA appears, looking cheerful]
SPRITE: Sakura - Happy
```
Becomes:
```python
show sakura happy
with dissolve
```

### 6. Changing Expressions → show command
```
[Sakura's expression changes to thoughtful]
SPRITE: Sakura - Thoughtful
```
Becomes:
```python
show sakura thoughtful
```
(No need to hide first - show automatically replaces)

### 7. Dialogue
```
SAKURA: Oh! Good morning!
PROTAGONIST: Morning, Sakura.
```
Becomes:
```python
sakura "Oh! Good morning!"
mc "Morning, Sakura."
```

### 8. Choices → menu
```
[CHOICE MENU]
CHOICE 1: "I'd love to!"
    -> Jump to: sakura_festival_accept
CHOICE 2: "I'm not sure..."
    -> Jump to: sakura_festival_hesitant
```
Becomes:
```python
menu:
    "I'd love to!":
        jump sakura_festival_accept
    
    "I'm not sure...":
        jump sakura_festival_hesitant
```

---

## Advanced Conversions

### Sound Effects
```
[SFX: Door opens]
```
Becomes:
```python
play sound "audio/sfx/door_open.ogg"
```

### Multiple Characters on Screen
```
[SAKURA on left, MAI on right]
```
Becomes:
```python
show sakura happy at left
show mai neutral at right
```

### Character Exits
```
[SAKURA leaves]
```
Becomes:
```python
hide sakura
with dissolve
```

### Timed Pauses
```
[Pause for 2 seconds]
```
Becomes:
```python
pause 2.0
```

### Screen Shake (for dramatic effect)
```
[Screen shakes]
```
Becomes:
```python
with hpunch  # horizontal shake
# or
with vpunch  # vertical shake
```

### Variables/Flags
```
[Set: SAKURA_ROUTE_ACTIVE = TRUE]
[Set: SAKURA_AFFECTION += 10]
```
Becomes:
```python
$ sakura_route_active = True
$ sakura_affection += 10
```

### Conditional Dialogue
```
IF SAKURA_AFFECTION > 50:
    SAKURA: I really enjoy spending time with you.
ELSE:
    SAKURA: Thanks for hanging out.
```
Becomes:
```python
if sakura_affection > 50:
    sakura "I really enjoy spending time with you."
else:
    sakura "Thanks for hanging out."
```

---

## Full Example with Variables

### Traditional Format
```
=== SCENE: ROOFTOP CONFESSION ===

[Check affection level]
IF SAKURA_AFFECTION >= 70:
    [SAKURA appears, nervous]
    SAKURA: There's something I need to tell you...
    
    PROTAGONIST: What is it?
    
    SAKURA: I... I've fallen in love with you.
    
    [CHOICE]
    CHOICE 1: "I love you too."
        [Set: SAKURA_ROMANCE = TRUE]
        -> Jump to: sakura_good_ending
    CHOICE 2: "I'm sorry..."
        [Set: SAKURA_ROMANCE = FALSE]
        -> Jump to: sakura_friend_ending

ELSE:
    [SAKURA appears, friendly]
    SAKURA: Thanks for meeting me here!
    -> Jump to: sakura_normal_scene
```

### Ren'Py Format
```python
label scene_rooftop_confession:
    scene bg rooftop
    with fade
    
    play music "audio/emotional_theme.mp3" fadein 2.0
    
    if sakura_affection >= 70:
        show sakura nervous
        with dissolve
        
        sakura "There's something I need to tell you..."
        
        mc "What is it?"
        
        sakura "I... I've fallen in love with you."
        
        menu:
            "I love you too.":
                $ sakura_romance = True
                jump sakura_good_ending
            
            "I'm sorry...":
                $ sakura_romance = False
                jump sakura_friend_ending
    
    else:
        show sakura happy
        with dissolve
        
        sakura "Thanks for meeting me here!"
        
        jump sakura_normal_scene
    
    return
```

---

## Batch Conversion Tips

### 1. Use Find & Replace
- Replace character names with their variable names
- Replace common phrases (e.g., "BACKGROUND:" → "scene bg ")

### 2. Text Editor Regex
Many text editors support regex find/replace:
- Find: `NARRATION: (.+)`
- Replace: `"$1"`

### 3. Organize by Scenes
- Convert one scene at a time
- Test each scene as you go
- Keep original script for reference

### 4. Create a Conversion Guide
Make a quick reference for your specific script format:
```
Your Format          →  Ren'Py Format
--------------------------------------------
[BG: X]             →  scene bg x
[CHAR: X - Y]       →  show x y
[SFX: X]            →  play sound "audio/sfx/x.ogg"
CHAR: "text"        →  char "text"
```

---

## Testing Your Converted Script

After conversion:
1. Launch in Ren'Py
2. Check for syntax errors
3. Verify images appear correctly
4. Test all choice paths
5. Confirm variables work as expected
6. Check audio plays correctly

---

## Common Conversion Mistakes

### ❌ Wrong
```python
scene "bg_school"  # Don't use quotes for image names
```
### ✓ Correct
```python
scene bg school
```

---

### ❌ Wrong
```python
sakura: "Hello"  # Colon instead of space
```
### ✓ Correct
```python
sakura "Hello"
```

---

### ❌ Wrong
```python
menu:
"First choice":  # Missing indentation
    jump somewhere
```
### ✓ Correct
```python
menu:
    "First choice":
        jump somewhere
```

---

### ❌ Wrong
```python
label my scene:  # Space in label name
```
### ✓ Correct
```python
label my_scene:
```

---

## Automation Ideas

For large scripts, consider creating a simple conversion script:
- Python script to parse your format
- Convert to Ren'Py syntax automatically
- Handles most common patterns
- Manual review for special cases

---

This guide should help you convert your existing script into Ren'Py format efficiently!
