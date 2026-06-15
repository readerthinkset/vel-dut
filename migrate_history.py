"""
Migrate phrase history to Dutch format
Converts legacy keys ('japanese', 'telugu', 'korean') -> 'dutch'
and 'romaji' -> 'transliteration'
"""

import json
from pathlib import Path

HISTORY_FILE = Path("output/history/all_generated_phrases.json")

LEGACY_KEYS = ["japanese", "telugu", "korean", "hindi", "slovak"]
TARGET_KEY = "dutch"

if HISTORY_FILE.exists():
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated_count = 0
    for phrase in data.get("phrases", []):
        for legacy_key in LEGACY_KEYS:
            if legacy_key in phrase:
                phrase[TARGET_KEY] = phrase.pop(legacy_key)
                phrase["is_legacy"] = True
                updated_count += 1
                break
        if "romanization" in phrase:
            phrase["transliteration"] = phrase.pop("romanization")

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Migrated {updated_count} phrases to Dutch format")
    if updated_count > 0:
        print(f"  Converted legacy keys to '{TARGET_KEY}'")
        print(f"  Converted 'romanization' -> 'transliteration'")
        print(f"  Legacy phrases marked with 'is_legacy: True'")
    print("Ready for new Dutch content generation")
else:
    print("No phrase history found to migrate")
