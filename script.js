// Sea of Stars Character Sheet JavaScript

class CharacterSheet {
    constructor() {
        this.currentCharacterId = null;
        this.characters = this.loadCharacters();
        this.autoSaveInterval = null;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.setupDynamicSections();
        this.loadLastCharacter();
        this.startAutoSave();
    }

    setupEventListeners() {
        // Button controls
        document.getElementById('newCharacter').addEventListener('click', () => this.newCharacter());
        document.getElementById('saveCharacter').addEventListener('click', () => this.saveCurrentCharacter());
        document.getElementById('loadCharacter').addEventListener('click', () => this.showLoadDialog());
        document.getElementById('importFromDoc').addEventListener('click', () => this.showImportModal());
        document.getElementById('exportCharacter').addEventListener('click', () => this.exportCharacter());
        document.getElementById('importCharacter').addEventListener('click', () => this.importCharacter());
        document.getElementById('printSheet').addEventListener('click', () => window.print());

        // Dynamic section buttons
        document.getElementById('addTrait').addEventListener('click', () => this.addTrait());
        document.getElementById('addPower').addEventListener('click', () => this.addPower());

        // Modal controls
        document.getElementById('closeModal').addEventListener('click', () => this.hideImportModal());
        document.getElementById('cancelImport').addEventListener('click', () => this.hideImportModal());
        document.getElementById('parseImport').addEventListener('click', () => this.parseDocText());
    }

    setupDynamicSections() {
        // Setup remove buttons for traits
        this.setupRemoveButtons('traitsContainer', '.trait-block');
        this.setupRemoveButtons('powersetContainer', '.power-block');
    }

    setupRemoveButtons(containerId, selector) {
        const container = document.getElementById(containerId);
        container.addEventListener('click', (e) => {
            if (e.target.classList.contains('btn-remove')) {
                const block = e.target.closest(selector);
                if (block) {
                    block.remove();
                }
            }
        });
    }

    addTrait(title = '', description = '') {
        const container = document.getElementById('traitsContainer');
        const traitBlock = document.createElement('div');
        traitBlock.className = 'trait-block';
        traitBlock.innerHTML = `
            <input type="text" class="trait-title" placeholder="Trait Name" value="${this.escapeHtml(title)}">
            <textarea class="trait-description" rows="6" placeholder="Trait description...">${this.escapeHtml(description)}</textarea>
            <button class="btn-small btn-remove">Remove</button>
        `;
        container.appendChild(traitBlock);
    }

    addPower(name = '', description = '') {
        const container = document.getElementById('powersetContainer');
        const powerBlock = document.createElement('div');
        powerBlock.className = 'power-block';
        powerBlock.innerHTML = `
            <input type="text" class="power-name" placeholder="Power Name" value="${this.escapeHtml(name)}">
            <textarea class="power-description" rows="6" placeholder="Power description...">${this.escapeHtml(description)}</textarea>
            <button class="btn-small btn-remove">Remove</button>
        `;
        container.appendChild(powerBlock);
    }

    gatherCharacterData() {
        const data = {
            id: this.currentCharacterId || this.generateId(),
            lastModified: new Date().toISOString(),

            // Identity
            characterName: document.getElementById('characterName').value,
            characterQuote: document.getElementById('characterQuote').value,
            theme: document.getElementById('theme').value,
            sponsor: document.getElementById('sponsor').value,
            sephiraState: document.getElementById('sephiraState').value,
            rank: document.getElementById('rank').value,
            role: document.getElementById('role').value,
            originNode: document.getElementById('originNode').value,
            potential: document.getElementById('potential').value,
            grudgeLevel: document.getElementById('grudgeLevel').value,
            genotype: document.getElementById('genotype').value,
            bloodPattern: document.getElementById('bloodPattern').value,
            ascensionState: document.getElementById('ascensionState').value,

            // Alignments
            emotionalMeridians: this.getCheckboxValues('emotional'),
            conceptualAlignments: this.getCheckboxValues('conceptual'),
            worldlineAffinities: this.getCheckboxValues('worldline'),

            // Stats
            soulState: {
                cognition: document.getElementById('cognition').value,
                memory: document.getElementById('memory').value,
                emanation: document.getElementById('emanation').value,
                comprehension: document.getElementById('comprehension').value,
                stagnation: document.getElementById('stagnation').value,
                inversion: document.getElementById('inversion').value,
                dissonance: document.getElementById('dissonance').value,
                resonance: document.getElementById('resonance').value
            },

            statistics: {
                power: document.getElementById('power').value,
                agility: document.getElementById('agility').value,
                tenacity: document.getElementById('tenacity').value,
                discipline: document.getElementById('discipline').value,
                empathy: document.getElementById('empathy').value,
                presence: document.getElementById('presence').value,
                reasoning: document.getElementById('reasoning').value,
                intuition: document.getElementById('intuition').value,
                synchronicity: document.getElementById('synchronicity').value
            },

            // Narrative sections
            traits: this.getTraits(),
            powers: this.getPowers(),
            additionalRules: document.getElementById('additionalRules').value
        };

        return data;
    }

    getCheckboxValues(category) {
        const checkboxes = document.querySelectorAll(`input[type="checkbox"][data-category="${category}"]`);
        const values = [];
        checkboxes.forEach(cb => {
            if (cb.checked) {
                values.push(cb.id);
            }
        });
        return values;
    }

    getTraits() {
        const traits = [];
        const traitBlocks = document.querySelectorAll('#traitsContainer .trait-block');
        traitBlocks.forEach(block => {
            const title = block.querySelector('.trait-title').value;
            const description = block.querySelector('.trait-description').value;
            if (title || description) {
                traits.push({ title, description });
            }
        });
        return traits;
    }

    getPowers() {
        const powers = [];
        const powerBlocks = document.querySelectorAll('#powersetContainer .power-block');
        powerBlocks.forEach(block => {
            const name = block.querySelector('.power-name').value;
            const description = block.querySelector('.power-description').value;
            if (name || description) {
                powers.push({ name, description });
            }
        });
        return powers;
    }

    loadCharacterData(data) {
        if (!data) return;

        this.currentCharacterId = data.id;

        // Identity
        this.setValueById('characterName', data.characterName);
        this.setValueById('characterQuote', data.characterQuote);
        this.setValueById('theme', data.theme);
        this.setValueById('sponsor', data.sponsor);
        this.setValueById('sephiraState', data.sephiraState);
        this.setValueById('rank', data.rank);
        this.setValueById('role', data.role);
        this.setValueById('originNode', data.originNode);
        this.setValueById('potential', data.potential);
        this.setValueById('grudgeLevel', data.grudgeLevel);
        this.setValueById('genotype', data.genotype);
        this.setValueById('bloodPattern', data.bloodPattern);
        this.setValueById('ascensionState', data.ascensionState);

        // Alignments
        this.setCheckboxValues(data.emotionalMeridians || []);
        this.setCheckboxValues(data.conceptualAlignments || []);
        this.setCheckboxValues(data.worldlineAffinities || []);

        // Stats
        if (data.soulState) {
            Object.entries(data.soulState).forEach(([key, value]) => {
                this.setValueById(key, value);
            });
        }

        if (data.statistics) {
            Object.entries(data.statistics).forEach(([key, value]) => {
                this.setValueById(key, value);
            });
        }

        // Clear existing traits and powers
        document.getElementById('traitsContainer').innerHTML = '';
        document.getElementById('powersetContainer').innerHTML = '';

        // Load traits
        if (data.traits && data.traits.length > 0) {
            data.traits.forEach(trait => {
                this.addTrait(trait.title, trait.description);
            });
        } else {
            this.addTrait(); // Add one empty trait
        }

        // Load powers
        if (data.powers && data.powers.length > 0) {
            data.powers.forEach(power => {
                this.addPower(power.name, power.description);
            });
        } else {
            this.addPower(); // Add one empty power
        }

        // Additional rules
        this.setValueById('additionalRules', data.additionalRules);
    }

    setValueById(id, value) {
        const element = document.getElementById(id);
        if (element) {
            element.value = value || '';
        }
    }

    setCheckboxValues(checkedIds) {
        // Uncheck all first
        document.querySelectorAll('input[type="checkbox"]').forEach(cb => {
            cb.checked = false;
        });
        // Check the specified ones
        checkedIds.forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.checked = true;
            }
        });
    }

    newCharacter() {
        if (confirm('Create a new character? Any unsaved changes will be lost.')) {
            this.currentCharacterId = null;
            this.loadCharacterData(this.getEmptyCharacter());
            this.saveCurrentCharacter();
        }
    }

    getEmptyCharacter() {
        return {
            id: this.generateId(),
            characterName: 'New Character',
            traits: [],
            powers: []
        };
    }

    saveCurrentCharacter() {
        const data = this.gatherCharacterData();
        this.characters[data.id] = data;
        this.currentCharacterId = data.id;
        this.saveCharacters();
        this.showNotification('Character saved!');
    }

    showLoadDialog() {
        const characterList = Object.values(this.characters);

        if (characterList.length === 0) {
            alert('No saved characters found.');
            return;
        }

        let listHtml = 'Select a character to load:\n\n';
        characterList.forEach((char, index) => {
            const name = char.characterName || 'Unnamed Character';
            const modified = new Date(char.lastModified).toLocaleString();
            listHtml += `${index + 1}. ${name} (Modified: ${modified})\n`;
        });

        const selection = prompt(listHtml + '\nEnter the number of the character to load:');

        if (selection) {
            const index = parseInt(selection) - 1;
            if (index >= 0 && index < characterList.length) {
                this.loadCharacterData(characterList[index]);
                this.showNotification('Character loaded!');
            } else {
                alert('Invalid selection.');
            }
        }
    }

    exportCharacter() {
        const data = this.gatherCharacterData();
        const jsonStr = JSON.stringify(data, null, 2);
        const blob = new Blob([jsonStr], { type: 'application/json' });
        const url = URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = `${data.characterName || 'character'}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        this.showNotification('Character exported!');
    }

    importCharacter() {
        const input = document.getElementById('importFileInput');
        input.onchange = (e) => {
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = (event) => {
                try {
                    const data = JSON.parse(event.target.result);
                    this.loadCharacterData(data);
                    this.saveCurrentCharacter();
                    this.showNotification('Character imported!');
                } catch (error) {
                    alert('Error importing character: Invalid JSON file');
                }
            };
            reader.readAsText(file);
        };
        input.click();
    }

    loadCharacters() {
        const stored = localStorage.getItem('seaOfStarsCharacters');
        return stored ? JSON.parse(stored) : {};
    }

    saveCharacters() {
        localStorage.setItem('seaOfStarsCharacters', JSON.stringify(this.characters));
        localStorage.setItem('lastCharacterId', this.currentCharacterId);
    }

    loadLastCharacter() {
        const lastId = localStorage.getItem('lastCharacterId');
        if (lastId && this.characters[lastId]) {
            this.loadCharacterData(this.characters[lastId]);
        } else {
            // Load empty character with one trait and one power
            this.addTrait();
            this.addPower();
        }
    }

    startAutoSave() {
        // Auto-save every 30 seconds
        this.autoSaveInterval = setInterval(() => {
            if (this.currentCharacterId) {
                this.saveCurrentCharacter();
            }
        }, 30000);
    }

    generateId() {
        return 'char_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    showImportModal() {
        document.getElementById('importModal').style.display = 'flex';
        document.getElementById('docTextInput').value = '';
        document.getElementById('docTextInput').focus();
    }

    hideImportModal() {
        document.getElementById('importModal').style.display = 'none';
    }

    parseDocText() {
        const text = document.getElementById('docTextInput').value;
        if (!text.trim()) {
            alert('Please paste some text first.');
            return;
        }

        try {
            const characterData = this.parseGoogleDocFormat(text);
            this.loadCharacterData(characterData);
            this.saveCurrentCharacter();
            this.hideImportModal();
            this.showNotification('Character imported from doc!');
        } catch (error) {
            alert('Error parsing character sheet: ' + error.message);
        }
    }

    parseGoogleDocFormat(text) {
        const lines = text.split('\n').map(line => line.trim()).filter(line => line);
        const data = {
            id: this.generateId(),
            emotionalMeridians: [],
            conceptualAlignments: [],
            worldlineAffinities: [],
            soulState: {},
            statistics: {},
            traits: [],
            powers: []
        };

        let currentSection = null;
        let currentTrait = null;
        let currentPower = null;
        let traitDescription = [];
        let powerDescription = [];

        // Extract character name (first line)
        if (lines.length > 0) {
            data.characterName = lines[0];
        }

        for (let i = 1; i < lines.length; i++) {
            const line = lines[i];

            // Extract quote (text in quotes)
            if (line.startsWith('"') && line.endsWith('"')) {
                data.characterQuote = line.substring(1, line.length - 1);
                continue;
            }

            // Check for section headers
            if (line === 'Emotional Meridians') {
                currentSection = 'emotional';
                continue;
            }
            if (line === 'Conceptual Alignments') {
                currentSection = 'conceptual';
                continue;
            }
            if (line === 'Worldline Affinities') {
                currentSection = 'worldline';
                continue;
            }
            if (line === 'Soul-State Status') {
                currentSection = 'soulState';
                continue;
            }
            if (line === 'Statistic Makeup') {
                currentSection = 'statistics';
                continue;
            }
            if (line === 'Traits') {
                // Save previous trait if exists
                if (currentTrait) {
                    data.traits.push({
                        title: currentTrait,
                        description: traitDescription.join('\n')
                    });
                }
                currentSection = 'traits';
                currentTrait = null;
                traitDescription = [];
                continue;
            }
            if (line === 'Base Powerset') {
                // Save previous trait if exists
                if (currentTrait) {
                    data.traits.push({
                        title: currentTrait,
                        description: traitDescription.join('\n')
                    });
                }
                currentSection = 'powers';
                currentTrait = null;
                currentPower = null;
                traitDescription = [];
                powerDescription = [];
                continue;
            }
            if (line === 'Additional Rules' || line === 'END') {
                // Save previous power if exists
                if (currentPower) {
                    data.powers.push({
                        name: currentPower,
                        description: powerDescription.join('\n')
                    });
                }
                currentSection = 'additionalRules';
                currentPower = null;
                powerDescription = [];
                continue;
            }

            // Parse field: value pairs
            const colonIndex = line.indexOf(':');
            if (colonIndex > -1 && colonIndex < 50) {
                const field = line.substring(0, colonIndex).trim();
                const value = line.substring(colonIndex + 1).trim();

                // Map fields to data properties
                const fieldMap = {
                    'Theme': 'theme',
                    'Sponsor': 'sponsor',
                    'True Sephira State': 'sephiraState',
                    'Sea of Stars Rank': 'rank',
                    'Sea of Stars Role': 'role',
                    'Origin Node': 'originNode',
                    'Potential': 'potential',
                    'Grudge Level': 'grudgeLevel',
                    'Genotype': 'genotype',
                    'Blood Pattern': 'bloodPattern',
                    'Ascension State': 'ascensionState'
                };

                if (fieldMap[field]) {
                    data[fieldMap[field]] = value;
                    continue;
                }
            }

            // Parse alignment sections (lists separated by /)
            if (currentSection === 'emotional' || currentSection === 'conceptual' || currentSection === 'worldline') {
                const items = line.split('/').map(item => item.trim()).filter(item => item);
                items.forEach(item => {
                    const normalized = item.toLowerCase().replace(/\s+/g, '-');
                    const id = `${currentSection === 'emotional' ? 'em' : currentSection === 'conceptual' ? 'ca' : 'wa'}-${normalized}`;

                    if (currentSection === 'emotional') {
                        data.emotionalMeridians.push(id);
                    } else if (currentSection === 'conceptual') {
                        data.conceptualAlignments.push(id);
                    } else if (currentSection === 'worldline') {
                        data.worldlineAffinities.push(id);
                    }
                });
                continue;
            }

            // Parse stats (label followed by number on same or next line)
            if (currentSection === 'soulState' || currentSection === 'statistics') {
                // Try to split by whitespace to get stat name and value
                const parts = line.split(/\s+/);
                if (parts.length >= 2) {
                    const lastPart = parts[parts.length - 1];
                    if (!isNaN(lastPart)) {
                        const statName = parts.slice(0, -1).join(' ').toLowerCase();
                        const value = lastPart;

                        // Map stat names
                        const statMap = {
                            'cognition': 'cognition',
                            'memory': 'memory',
                            'emanation': 'emanation',
                            'comprehension': 'comprehension',
                            'stagnation': 'stagnation',
                            'inversion': 'inversion',
                            'dissonance': 'dissonance',
                            'resonance': 'resonance',
                            'power': 'power',
                            'agility': 'agility',
                            'tenacity': 'tenacity',
                            'discipline': 'discipline',
                            'empathy': 'empathy',
                            'presence': 'presence',
                            'reasoning': 'reasoning',
                            'intuition': 'intuition',
                            'synchronicity': 'synchronicity'
                        };

                        if (statMap[statName]) {
                            if (currentSection === 'soulState') {
                                data.soulState[statMap[statName]] = value;
                            } else {
                                data.statistics[statMap[statName]] = value;
                            }
                        }
                    }
                }
                continue;
            }

            // Parse traits section
            if (currentSection === 'traits') {
                // If this line looks like a title (short, not starting with lowercase)
                if (line.length < 100 && !line.match(/^[a-z]/)) {
                    // Save previous trait
                    if (currentTrait) {
                        data.traits.push({
                            title: currentTrait,
                            description: traitDescription.join('\n')
                        });
                    }
                    currentTrait = line;
                    traitDescription = [];
                } else if (currentTrait) {
                    traitDescription.push(line);
                }
                continue;
            }

            // Parse powers section
            if (currentSection === 'powers') {
                // If this line looks like a title (short, not starting with lowercase)
                if (line.length < 100 && !line.match(/^[a-z]/)) {
                    // Save previous power
                    if (currentPower) {
                        data.powers.push({
                            name: currentPower,
                            description: powerDescription.join('\n')
                        });
                    }
                    currentPower = line;
                    powerDescription = [];
                } else if (currentPower) {
                    powerDescription.push(line);
                }
                continue;
            }

            // Additional rules section
            if (currentSection === 'additionalRules') {
                if (!data.additionalRules) {
                    data.additionalRules = line;
                } else {
                    data.additionalRules += '\n' + line;
                }
            }
        }

        // Save final trait or power if exists
        if (currentTrait) {
            data.traits.push({
                title: currentTrait,
                description: traitDescription.join('\n')
            });
        }
        if (currentPower) {
            data.powers.push({
                name: currentPower,
                description: powerDescription.join('\n')
            });
        }

        return data;
    }

    showNotification(message) {
        // Simple notification - could be enhanced with a toast system
        const originalTitle = document.title;
        document.title = message;
        setTimeout(() => {
            document.title = originalTitle;
        }, 2000);
    }
}

// Initialize the character sheet when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.characterSheet = new CharacterSheet();
});
