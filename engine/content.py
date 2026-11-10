"""AI phrase generation with permanent no-repeat history."""

from __future__ import annotations

import json
import random
import time
from datetime import datetime

import requests

import config
from config import CATEGORIES, CATEGORIES_NATIVE, HISTORY_DIR, MAX_RECENT_CATEGORIES

PHRASE_HISTORY_FILE = HISTORY_DIR / "all_generated_phrases.json"
RECENT_CATEGORIES_FILE = HISTORY_DIR / "recent_categories.json"

PHRASE_KEY = config.LANGUAGE["history_key"]
LANGUAGE_NAME = config.LANGUAGE["name"]
NATIVE_NAME = config.LANGUAGE["native_name"]

# ==== FALLBACK PHRASES START ====
FALLBACK_PHRASES = [
    {"english": "Hello, nice to meet you.", "native": "Hallo, leuk je te ontmoeten.", "transliteration": "Hallo, leuk je te ontmoeten."},
    {"english": "Thank you very much.", "native": "Heel erg bedankt.", "transliteration": "Heel erg bedankt."},
    {"english": "Good morning, have a great day.", "native": "Goedemorgen, een fijne dag.", "transliteration": "Goedemorgen, een fijne dag."},
    {"english": "I love learning new languages.", "native": "Ik hou ervan om nieuwe talen te leren.", "transliteration": "Ik hou ervan om nieuwe talen te leren."},
    {"english": "Never give up on your dreams.", "native": "Geef nooit je dromen op.", "transliteration": "Geef nooit je dromen op."},
    {"english": "Every day is a fresh start.", "native": "Elke dag is een nieuwe start.", "transliteration": "Elke dag is een nieuwe start."},
    {"english": "Believe in yourself always.", "native": "Geloof altijd in jezelf.", "transliteration": "Geloof altijd in jezelf."},
    {"english": "Small steps lead to big changes.", "native": "Kleine stappen leiden tot grote veranderingen.", "transliteration": "Kleine stappen leiden tot grote veranderingen."},
    {"english": "You are stronger than you think.", "native": "Je bent sterker dan je denkt.", "transliteration": "Je bent sterker dan je denkt."},
    {"english": "Happiness is a choice, choose it.", "native": "Geluk is een keuze, kies ervoor.", "transliteration": "Geluk is een keuze, kies ervoor."},
    {"english": "What time is it please.", "native": "Hoe laat is het alstublieft.", "transliteration": "Hoe laat is het alstublieft."},
    {"english": "Where is the train station.", "native": "Waar is het treinstation.", "transliteration": "Waar is het treinstation."},
    {"english": "How much does this cost.", "native": "Hoeveel kost dit.", "transliteration": "Hoeveel kost dit."},
    {"english": "Can you help me please.", "native": "Kunt u mij alstublieft helpen.", "transliteration": "Kunt u mij alstublieft helpen."},
    {"english": "I would like a coffee please.", "native": "Ik wil graag een koffie alstublieft.", "transliteration": "Ik wil graag een koffie alstublieft."},
    {"english": "The food is delicious today.", "native": "Het eten is heerlijk vandaag.", "transliteration": "Het eten is heerlijk vandaag."},
    {"english": "Have a wonderful weekend.", "native": "Een fijn weekend.", "transliteration": "Een fijn weekend."},
    {"english": "Take care of yourself.", "native": "Zorg goed voor jezelf.", "transliteration": "Zorg goed voor jezelf."},
    {"english": "See you tomorrow my friend.", "native": "Tot morgen mijn vriend.", "transliteration": "Tot morgen mijn vriend."},
    {"english": "The weather is beautiful outside.", "native": "Het weer is prachtig buiten.", "transliteration": "Het weer is prachtig buiten."},
    {"english": "I am very happy today.", "native": "Ik ben erg blij vandaag.", "transliteration": "Ik ben erg blij vandaag."},
    {"english": "Learning a language opens new doors.", "native": "Een taal leren opent nieuwe deuren.", "transliteration": "Een taal leren opent nieuwe deuren."},
    {"english": "Keep practicing every single day.", "native": "Blijf elke dag oefenen.", "transliteration": "Blijf elke dag oefenen."},
    {"english": "You can achieve anything you want.", "native": "Je kunt alles bereiken wat je wilt.", "transliteration": "Je kunt alles bereiken wat je wilt."},
    {"english": "Rest when you are tired.", "native": "Rust als je moe bent.", "transliteration": "Rust als je moe bent."},
    {"english": "Focus on the positive things.", "native": "Focus op de positieve dingen.", "transliteration": "Focus op de positieve dingen."},
    {"english": "Learn from your mistakes.", "native": "Leer van je fouten.", "transliteration": "Leer van je fouten."},
    {"english": "Trust the process completely.", "native": "Vertrouw volledig op het proces.", "transliteration": "Vertrouw volledig op het proces."},
    {"english": "Breathe deeply and stay calm.", "native": "Haal diep adem en blijf kalm.", "transliteration": "Haal diep adem en blijf kalm."},
    {"english": "Enjoy the little moments in life.", "native": "Geniet van de kleine momenten in het leven.", "transliteration": "Geniet van de kleine momenten in het leven."},
    {"english": "Smile more, worry less.", "native": "Lach meer, maak je minder zorgen.", "transliteration": "Lach meer, maak je minder zorgen."},
    {"english": "Be kind to everyone you meet.", "native": "Wees vriendelijk tegen iedereen die je ontmoet.", "transliteration": "Wees vriendelijk tegen iedereen die je ontmoet."},
    {"english": "Help others without expecting anything back.", "native": "Help anderen zonder iets terug te verwachten.", "transliteration": "Help anderen zonder iets terug te verwachten."},
    {"english": "Forgive yourself and move forward.", "native": "Vergeef jezelf en ga verder.", "transliteration": "Vergeef jezelf en ga verder."},
    {"english": "Stay strong in difficult times.", "native": "Blijf sterk in moeilijke tijden.", "transliteration": "Blijf sterk in moeilijke tijden."},
    {"english": "Every moment is a new beginning.", "native": "Elk moment is een nieuw begin.", "transliteration": "Elk moment is een nieuw begin."},
    {"english": "Listen to your heart always.", "native": "Luister altijd naar je hart.", "transliteration": "Luister altijd naar je hart."},
    {"english": "Do what makes you happy.", "native": "Doe wat je gelukkig maakt.", "transliteration": "Doe wat je gelukkig maakt."},
    {"english": "Your potential is unlimited.", "native": "Je potentieel is onbeperkt.", "transliteration": "Je potentieel is onbeperkt."},
    {"english": "Be brave and take risks.", "native": "Wees moedig en neem risico's.", "transliteration": "Wees moedig en neem risico's."},
    {"english": "Celebrate your progress every day.", "native": "Vier je vooruitgang elke dag.", "transliteration": "Vier je vooruitgang elke dag."},
    {"english": "Surround yourself with good people.", "native": "Omring jezelf met goede mensen.", "transliteration": "Omring jezelf met goede mensen."},
    {"english": "Read books and grow your mind.", "native": "Lees boeken en ontwikkel je geest.", "transliteration": "Lees boeken en ontwikkel je geest."},
    {"english": "Travel and discover new places.", "native": "Reis en ontdek nieuwe plekken.", "transliteration": "Reis en ontdek nieuwe plekken."},
    {"english": "Appreciate what you already have.", "native": "Waardeer wat je al hebt.", "transliteration": "Waardeer wat je al hebt."},
    {"english": "Dance like nobody is watching.", "native": "Dans alsof niemand kijkt.", "transliteration": "Dans alsof niemand kijkt."},
    {"english": "Sing from your heart out loud.", "native": "Zing uit volle borst.", "transliteration": "Zing uit volle borst."},
    {"english": "Plant seeds of kindness everywhere.", "native": "Zaai overal zaadjes van vriendelijkheid.", "transliteration": "Zaai overal zaadjes van vriendelijkheid."},
    {"english": "Let go of what you cannot control.", "native": "Laat los wat je niet kunt beheersen.", "transliteration": "Laat los wat je niet kunt beheersen."},
    {"english": "Be present in the here and now.", "native": "Wees aanwezig in het hier en nu.", "transliteration": "Wees aanwezig in het hier en nu."},
]
# ==== FALLBACK PHRASES END ====


def _load_json(path, default):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_phrase_history():
    data = _load_json(PHRASE_HISTORY_FILE, {"phrases": [], "last_updated": None})
    data.setdefault("phrases", [])
    return data


def save_phrase_history(data):
    data["last_updated"] = datetime.now().isoformat()
    _save_json(PHRASE_HISTORY_FILE, data)


def is_phrase_used(english):
    english_lower = english.lower().strip()
    for p in load_phrase_history()["phrases"]:
        if p.get("english", "").lower().strip() == english_lower:
            return True
    return False


def _history_native(p):
    for key in (PHRASE_KEY, "vietnamese", "native", "translation", "target"):
        value = p.get(key)
        if value:
            return str(value)
    return ""


def add_phrases_to_history(phrases, category):
    history = load_phrase_history()
    for phrase in phrases:
        history["phrases"].append({
            "english": phrase["english"],
            PHRASE_KEY: phrase["native"],
            "transliteration": phrase.get("transliteration", ""),
            "category": category,
            "generated_at": datetime.now().isoformat(),
        })
    save_phrase_history(history)
    print(f"[content] Saved {len(phrases)} phrases (history total: {len(history['phrases'])})")


def get_available_category():
    data = _load_json(RECENT_CATEGORIES_FILE, {"recent_categories": [], "last_updated": None})
    recent = data.get("recent_categories", [])
    available = [c for c in CATEGORIES if c not in recent]
    if not available:
        recent = recent[-5:]
        available = [c for c in CATEGORIES if c not in recent]
        print("[rotation] Reset recent categories")
    selected = random.choice(available)
    recent.append(selected)
    data["recent_categories"] = recent[-MAX_RECENT_CATEGORIES:]
    data["last_updated"] = datetime.now().isoformat()
    _save_json(RECENT_CATEGORIES_FILE, data)
    print(f"[rotation] Category: {selected} ({len(available)} available)")
    return selected


def _normalize_phrase(item):
    if not isinstance(item, dict):
        return None
    english = str(item.get("english", "")).strip()
    native = str(
        item.get(PHRASE_KEY)
        or item.get("native")
        or item.get("vietnamese")
        or item.get("translation")
        or ""
    ).strip()
    translit = str(item.get("transliteration") or item.get("romanization") or item.get("romaji") or "").strip()
    if not english or not native:
        return None
    if len(english.split()) > 16:
        return None
    if "/" in native or "|" in native:
        native = native.split("/")[0].split("|")[0].strip()
    return {
        "english": english.replace("  ", " ").strip(),
        "native": native.strip(),
        "transliteration": translit.strip().strip("[]"),
    }


def _history_keys(history):
    used_en = set()
    used_nat = set()
    for p in history.get("phrases", []):
        en = str(p.get("english", "")).lower().strip()
        nat = _history_native(p).lower().strip()
        if en:
            used_en.add(en)
        if nat:
            used_nat.add(nat)
    return used_en, used_nat


def generate_phrases(category_english: str, num_phrases: int = 5) -> list:
    category_native = CATEGORIES_NATIVE[category_english]
    history = load_phrase_history()
    used_en, used_nat = _history_keys(history)
    recent_english = [
        p["english"] for p in history["phrases"] if p.get("category") == category_english
    ][-30:]

    models = [config.AI_MODEL]
    if "gemini-fast" not in models:
        models.append("gemini-fast")

    if config.POLLINATIONS_API_KEY:
        for attempt in range(5):
            model = models[0] if attempt < 3 else models[-1]
            try:
                phrases = _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model)
                unique = []
                for item in phrases:
                    p = _normalize_phrase(item)
                    if not p:
                        continue
                    key_en = p["english"].lower().strip()
                    key_nat = p["native"].lower().strip()
                    if key_en in used_en or key_nat in used_nat:
                        continue
                    if any(key_en == u["english"].lower().strip() for u in unique):
                        continue
                    used_en.add(key_en)
                    used_nat.add(key_nat)
                    unique.append(p)
                    if len(unique) >= num_phrases:
                        break
                if len(unique) >= num_phrases:
                    add_phrases_to_history(unique[:num_phrases], category_english)
                    return unique[:num_phrases]
                print(f"[content] Attempt {attempt + 1}: only {len(unique)} fresh phrases (need {num_phrases})")
            except Exception as exc:  # noqa: BLE001 - network boundary
                print(f"[content] Attempt {attempt + 1} failed ({model}): {exc}")
            time.sleep(1.5 * (attempt + 1))
    else:
        print("[content] No POLLINATIONS_API_KEY, using fallback phrases")

    fresh_fallback = []
    for p in FALLBACK_PHRASES:
        if p["english"].lower().strip() in used_en or p["native"].lower().strip() in used_nat:
            continue
        fresh_fallback.append(p)
    if not fresh_fallback:
        raise RuntimeError("Phrase API unavailable and no unused fallback phrases left; refusing to reuse phrases")
    chosen = fresh_fallback[:num_phrases]
    if len(chosen) < num_phrases:
        print(f"[content] Only {len(chosen)} fresh fallback phrases; building a shorter lesson")
    add_phrases_to_history(chosen, category_english)
    return chosen


def _request_phrases(category_english, category_native, recent_english, num_phrases, attempt, model=None):
    avoid = ""
    if recent_english:
        avoid = "\nDo NOT reuse any of these phrases:\n" + "\n".join(f"- {p}" for p in recent_english)

    prompt = f"""Create {num_phrases * 6} unique {category_english} phrases for English speakers learning {LANGUAGE_NAME}.
{avoid}

Rules:
1. Keep every phrase short and natural (4-11 words in English).
2. Use natural commas for TTS breathing pauses.
3. Each phrase must be speakable in 2-4 seconds.
4. Write clean {LANGUAGE_NAME} in {NATIVE_NAME} with correct accents and orthography. One translation only, no slashes.
5. Transliteration is a friendly Roman-script pronunciation guide for English speakers (not IPA).
6. Vary the sentence patterns and emotions. No duplicates.
7. Phrases must feel like real everyday language, not textbook filler.

Return ONLY a JSON array:
[{{"english": "...", "native": "...", "transliteration": "..."}}]"""

    response = requests.post(
        "https://gen.pollinations.ai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {config.POLLINATIONS_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model or config.AI_MODEL,
            "messages": [
                {"role": "system", "content": f"You are a {LANGUAGE_NAME} teacher creating short, natural, varied bilingual phrases. Reply with JSON only."},
                {"role": "user", "content": prompt},
            ],
            "temperature": min(0.95 + attempt * 0.02, 1.0),
        },
        timeout=90,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"].strip()

    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in content:
        content = content.split("```", 1)[1].split("```", 1)[0].strip()

    start = content.find("[")
    end = content.rfind("]")
    if start >= 0 and end > start:
        content = content[start:end + 1]

    data = json.loads(content)
    if not isinstance(data, list):
        raise ValueError("AI did not return a JSON array")
    return data
