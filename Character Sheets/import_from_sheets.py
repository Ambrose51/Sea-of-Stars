#!/usr/bin/env python3
"""
Sea of Stars Character Data Importer
Fetches character data from Google Sheets and exports to JSON files
"""

import json
import os
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

# If modifying these scopes, delete the file token.pickle
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Column mappings based on your Apps Script headers
COLUMN_MAP = {
    'Character Name': 0,
    'Doc URL': 1,
    'Last Updated': 2,
    'Theme': 3,
    'Sponsor': 4,
    'True Sephira State': 5,
    'Sea of Stars Rank': 6,
    'Sea of Stars Role': 7,
    'Origin Node': 8,
    'Potential': 9,
    'Grudge Level': 10,
    'Genotype': 11,
    'Blood Pattern': 12,
    'Ascension State': 13,
    # Soul State Stats (14-21)
    'Cognition': 14,
    'Memory': 15,
    'Emanation': 16,
    'Comprehension': 17,
    'Stagnation': 18,
    'Inversion': 19,
    'Dissonance': 20,
    'Resonance': 21,
    # Main Stats (22-30)
    'Power': 22,
    'Agility': 23,
    'Tenacity': 24,
    'Discipline': 25,
    'Empathy': 26,
    'Presence': 27,
    'Reasoning': 28,
    'Intuition': 29,
    'Synchronicity': 30,
    # Alignments
    'Emotional Meridians (Active)': 31,
    'Conceptual Alignments (Active)': 32,
    'Worldline Affinities (Active)': 33,
    'Base Powerset Name': 34,
    'First Name Color': 35,
    'Last Name Color': 36
}


def get_credentials():
    """
    Get Google Sheets API credentials
    Supports both OAuth and Service Account authentication
    """
    creds = None

    # Check for existing token
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Try service account first
            if os.path.exists('service_account.json'):
                creds = service_account.Credentials.from_service_account_file(
                    'service_account.json', scopes=SCOPES)
            # Fall back to OAuth flow
            elif os.path.exists('credentials.json'):
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
            else:
                raise FileNotFoundError(
                    "No credentials found. Please provide either:\n"
                    "1. credentials.json (OAuth) - download from Google Cloud Console\n"
                    "2. service_account.json - create a service account in Google Cloud Console"
                )

    return creds


def parse_alignment_list(alignment_str):
    """
    Parse comma-separated alignment string into list of IDs
    Example: "Passion, Will, Desire" -> ["em-passion", "em-will", "em-desire"]
    """
    if not alignment_str:
        return []

    # Mapping for alignment categories
    emotional_meridians = ['Charity', 'Hope', 'Joy', 'Justice', 'Love', 'Mercy', 'Passion', 'Will', 'Wonder',
                          'Ambition', 'Desire', 'Envy', 'Fear', 'Hatred', 'Judgement', 'Regret', 'Sadness', 'Wrath']
    conceptual_alignments = ['Creation', 'Decay', 'Destruction', 'Eternity', 'Growth', 'Rebirth', 'Silence', 'Space', 'Time',
                            'Chaos', 'Death', 'Life', 'Nature', 'Negative', 'Order', 'Positive', 'Soul', 'Stasis']
    worldline_affinities = ['Aether', 'Bond', 'Flow', 'Miracle', 'Permanence', 'Phantasia', 'Quintessence', 'Twilight', 'Void']

    items = [item.strip() for item in alignment_str.split(',')]
    result = []

    for item in items:
        if not item:
            continue

        # Determine category and create ID
        if item in emotional_meridians:
            id_str = f"em-{item.lower()}"
        elif item in conceptual_alignments:
            id_str = f"ca-{item.lower()}"
        elif item in worldline_affinities:
            id_str = f"wa-{item.lower()}"
        else:
            # Default to lowercase with hyphens
            id_str = item.lower().replace(' ', '-')

        result.append(id_str)

    return result


def row_to_character(row):
    """
    Convert a spreadsheet row to a character data dictionary
    """
    # Helper function to safely get cell value
    def get_cell(col_name):
        idx = COLUMN_MAP.get(col_name)
        if idx is not None and idx < len(row):
            value = row[idx]
            # Remove leading apostrophe if present (from Origin Node text formatting)
            if isinstance(value, str) and value.startswith("'"):
                return value[1:]
            return value
        return ''

    # Helper to get int value
    def get_int(col_name, default=0):
        try:
            return int(get_cell(col_name) or default)
        except (ValueError, TypeError):
            return default

    character = {
        'id': f"char_{get_cell('Character Name').replace(' ', '_').lower()}",
        'characterName': get_cell('Character Name'),
        'characterQuote': '',  # Not in spreadsheet
        'theme': get_cell('Theme'),
        'sponsor': get_cell('Sponsor'),
        'sephiraState': get_cell('True Sephira State'),
        'rank': get_cell('Sea of Stars Rank'),
        'role': get_cell('Sea of Stars Role'),
        'originNode': get_cell('Origin Node'),
        'potential': get_cell('Potential'),
        'grudgeLevel': get_int('Grudge Level'),
        'genotype': get_cell('Genotype'),
        'bloodPattern': get_cell('Blood Pattern'),
        'ascensionState': get_cell('Ascension State'),

        # Soul State Stats
        'soulState': {
            'cognition': get_int('Cognition'),
            'memory': get_int('Memory'),
            'emanation': get_int('Emanation'),
            'comprehension': get_int('Comprehension'),
            'stagnation': get_int('Stagnation'),
            'inversion': get_int('Inversion'),
            'dissonance': get_int('Dissonance'),
            'resonance': get_int('Resonance'),
        },

        # Main Stats
        'statistics': {
            'power': get_int('Power'),
            'agility': get_int('Agility'),
            'tenacity': get_int('Tenacity'),
            'discipline': get_int('Discipline'),
            'empathy': get_int('Empathy'),
            'presence': get_int('Presence'),
            'reasoning': get_int('Reasoning'),
            'intuition': get_int('Intuition'),
            'synchronicity': get_int('Synchronicity'),
        },

        # Alignments
        'emotionalMeridians': parse_alignment_list(get_cell('Emotional Meridians (Active)')),
        'conceptualAlignments': parse_alignment_list(get_cell('Conceptual Alignments (Active)')),
        'worldlineAffinities': parse_alignment_list(get_cell('Worldline Affinities (Active)')),

        # Other data
        'traits': [],  # Would need to parse from doc
        'powers': [{
            'name': get_cell('Base Powerset Name'),
            'description': ''
        }] if get_cell('Base Powerset Name') else [],
        'additionalRules': '',

        # Metadata
        'docUrl': get_cell('Doc URL'),
        'lastUpdated': get_cell('Last Updated'),
        'firstNameColor': get_cell('First Name Color'),
        'lastNameColor': get_cell('Last Name Color'),
    }

    return character


def fetch_characters(spreadsheet_id, sheet_name='Character Database'):
    """
    Fetch all characters from the Google Sheet
    """
    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=spreadsheet_id,
        range=f'{sheet_name}!A2:AK'  # Start from row 2 (skip header), go to column AK (37)
    ).execute()

    rows = result.get('values', [])

    if not rows:
        print('No data found.')
        return []

    characters = []
    for row in rows:
        if not row or not row[0]:  # Skip empty rows
            continue

        char = row_to_character(row)
        characters.append(char)
        print(f"Loaded: {char['characterName']}")

    return characters


def save_characters_json(characters, output_dir='characters'):
    """
    Save characters as individual JSON files
    """
    os.makedirs(output_dir, exist_ok=True)

    # Save individual character files
    for char in characters:
        filename = f"{char['id']}.json"
        filepath = os.path.join(output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(char, f, indent=2, ensure_ascii=False)

        print(f"Saved: {filepath}")

    # Save index file with all character names and IDs
    index = {
        'characters': [
            {
                'id': char['id'],
                'name': char['characterName'],
                'lastUpdated': char['lastUpdated']
            }
            for char in characters
        ]
    }

    index_path = os.path.join(output_dir, 'index.json')
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"\nSaved index: {index_path}")
    print(f"Total characters exported: {len(characters)}")


def main():
    """
    Main function
    """
    print("Sea of Stars Character Data Importer")
    print("=" * 50)

    # Get spreadsheet ID from user
    spreadsheet_id = input("\nEnter your Google Spreadsheet ID\n(from the URL: docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit):\n> ").strip()

    if not spreadsheet_id:
        print("Error: Spreadsheet ID is required")
        return

    # Optional: custom sheet name
    sheet_name = input("\nSheet name (default: 'Character Database'):\n> ").strip()
    if not sheet_name:
        sheet_name = 'Character Database'

    print(f"\nFetching data from '{sheet_name}'...")

    try:
        characters = fetch_characters(spreadsheet_id, sheet_name)

        if characters:
            print(f"\nFound {len(characters)} character(s)")
            save_characters_json(characters)
            print("\n✓ Export complete!")
        else:
            print("\nNo characters found in the database.")

    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
