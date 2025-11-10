# Sea of Stars Character Sheet System

An interactive web-based character sheet system for the Sea of Stars RPG, with Google Sheets integration.

## Features

### Web Application
- **Interactive Character Sheets**: Full character creation and editing
- **Multiple Save Slots**: Save and load multiple characters in browser
- **Import/Export**: JSON export/import for backup and sharing
- **Google Doc Import**: Paste text from Google Docs for quick import
- **Auto-save**: Automatic saving every 30 seconds
- **Print-friendly**: Clean printing layout
- **Responsive Design**: Works on desktop, tablet, and mobile

### Character Data
- Character identity (name, sponsor, rank, role, etc.)
- Emotional Meridians (Virtues/Vices)
- Conceptual Alignments
- Worldline Affinities
- Soul-State Status (8 stats)
- Statistic Makeup (9 stats)
- Traits and Powers (dynamic add/remove)
- Additional rules section

## Setup

### Using the Web App (GitHub Pages)

1. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: Select your branch (`claude/character-sheet-webpage-011CUUgke7DKKs6deu7M2j8C` or `main`)
   - Folder: `/ (root)`
   - Save

2. **Access your site**:
   - Your site will be live at: `https://[username].github.io/Sea-of-Stars/`

### Google Sheets Integration

#### Prerequisites
- Python 3.7 or higher
- Google account
- Google Sheets with character data

#### Setup Steps

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up Google Cloud credentials**:

   **Option A: OAuth (Recommended for personal use)**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project (or select existing)
   - Enable Google Sheets API
   - Go to "Credentials" → "Create Credentials" → "OAuth client ID"
   - Application type: "Desktop app"
   - Download the JSON file
   - Rename it to `credentials.json` and place in this directory

   **Option B: Service Account (For automated/server use)**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project (or select existing)
   - Enable Google Sheets API
   - Go to "Credentials" → "Create Credentials" → "Service Account"
   - Download the JSON key file
   - Rename it to `service_account.json` and place in this directory
   - Share your Google Sheet with the service account email address

3. **Run the import script**:
   ```bash
   python import_from_sheets.py
   ```

4. **Follow the prompts**:
   - Enter your Google Spreadsheet ID (from the URL)
   - Enter sheet name (default: "Character Database")
   - First run will open a browser for OAuth authorization

5. **Character data exported to**:
   - `characters/` directory
   - Individual JSON files per character
   - `characters/index.json` with character list

## Project Structure

```
Sea-of-Stars/
├── index.html              # Main character sheet HTML
├── style.css               # Cosmic-themed styling
├── script.js               # Character sheet logic
├── import_from_sheets.py   # Google Sheets import script
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── characters/            # Exported character data (created by import script)
│   ├── index.json
│   └── char_*.json
├── credentials.json       # OAuth credentials (not in git)
├── service_account.json   # Service account key (not in git)
└── token.pickle           # Cached OAuth token (not in git)
```

## Usage

### Creating a New Character (Web App)
1. Click "New Character"
2. Fill in character details
3. Character auto-saves every 30 seconds
4. Click "Save Character" to manually save

### Importing from Google Docs
1. Open your Google Doc character sheet
2. Select All (Ctrl+A / Cmd+A)
3. Copy (Ctrl+C / Cmd+C)
4. Click "Import from Doc" in the web app
5. Paste the text
6. Click "Import Character"

### Importing from Google Sheets
1. Run `python import_from_sheets.py`
2. Enter your spreadsheet ID
3. Characters will be exported to `characters/` folder
4. Update web app to load from these JSON files (see below)

### Loading JSON Files in Web App

To load pre-exported character data:

```javascript
// In script.js, add this method to CharacterSheet class:
async loadFromJSON(characterId) {
  const response = await fetch(`characters/${characterId}.json`);
  const data = await response.json();
  this.loadCharacterData(data);
}
```

## Google Sheets Database Structure

Your Apps Script creates sheets with these columns:

| Column | Field |
|--------|-------|
| A | Character Name |
| B | Doc URL |
| C | Last Updated |
| D | Theme |
| E | Sponsor |
| F | True Sephira State |
| G | Sea of Stars Rank |
| H | Sea of Stars Role |
| I | Origin Node |
| J | Potential |
| K | Grudge Level |
| L | Genotype |
| M | Blood Pattern |
| N | Ascension State |
| O-V | Soul-State Status (8 stats) |
| W-AE | Statistic Makeup (9 stats) |
| AF | Emotional Meridians (Active) |
| AG | Conceptual Alignments (Active) |
| AH | Worldline Affinities (Active) |
| AI | Base Powerset Name |
| AJ | First Name Color |
| AK | Last Name Color |

## Alignment ID Format

The web app uses specific IDs for alignments:

- **Emotional Meridians**: `em-charity`, `em-hope`, etc.
- **Conceptual Alignments**: `ca-creation`, `ca-decay`, etc.
- **Worldline Affinities**: `wa-aether`, `wa-bond`, etc.

The import script automatically converts your Google Sheets data to these formats.

## Customization

### Colors
Edit CSS variables in `style.css`:
```css
:root {
    --primary-bg: #0a0e27;
    --accent-color: #6b8cff;
    --accent-gold: #ffd700;
    /* ... */
}
```

### Adding Custom Fields
1. Add HTML input in `index.html`
2. Add to `gatherCharacterData()` in `script.js`
3. Add to `loadCharacterData()` in `script.js`

## Security Notes

**Important**: Never commit these files to git:
- `credentials.json` (OAuth credentials)
- `service_account.json` (Service account key)
- `token.pickle` (Cached token)
- `characters/*.json` (May contain sensitive character data)

Add them to `.gitignore`:
```
credentials.json
service_account.json
token.pickle
characters/
```

## Troubleshooting

### Import Script Issues

**"No credentials found"**
- Make sure `credentials.json` or `service_account.json` exists
- Check file permissions

**"Permission denied" on Google Sheets**
- For OAuth: Make sure you authorized the app
- For Service Account: Share the sheet with the service account email

**"Module not found"**
- Run `pip install -r requirements.txt`

### Web App Issues

**Import from Doc doesn't work**
- Hard refresh the page (Ctrl+Shift+R)
- Check browser console for errors
- Make sure you're copying plain text (not formatted)

**Stats not importing**
- Stats must be in format: "StatName NumberValue"
- Example: "Cognition 5"

## License

This is a personal RPG character sheet system. Modify as needed for your campaign!

## Credits

Built with Google Apps Script, Google Sheets API, and vanilla JavaScript.
