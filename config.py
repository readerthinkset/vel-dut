"""VELOCITY DUTCH - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY DUTCH"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "DUTCH"
HANDLE = "@velocitydutch"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "nl",
    "name": "Dutch",
    "native_name": "Nederlands",
    "history_key": "dutch",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "nl-NL-MaartenNeural",
    "native_fallback_voice": "nl-NL-ColetteNeural",
    "native_engine": "edge",
    "native_lang_code": "nl",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "NEDERLANDS",
    "translit_label": "SAY IT LIKE",
    "greeting": "Hallo!",
    "encouragement": "Geweldig!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Groeten", "hand", "#1CB0F6"),
    ("Basic Phrases", "Basisuitdrukkingen", "chat", "#58CC02"),
    ("Common Expressions", "Veelvoorkomende Uitdrukkingen", "chat", "#1CB0F6"),
    ("Travel", "Reizen", "plane", "#1CB0F6"),
    ("Restaurant", "Restaurant", "fork", "#FF7A00"),
    ("Shopping", "Winkelen", "bag", "#E056A0"),
    ("Emergency", "Noodgevallen", "siren", "#FF4B4B"),
    ("Family Terms", "Familietermen", "heart", "#E056A0"),
    ("Numbers", "Nummers", "hash", "#A560E8"),
    ("Time", "Tijd", "clock", "#00A889"),
    ("Motivation", "Motivatie", "rocket", "#A560E8"),
    ("Love", "Liefde", "heart", "#FF4B4B"),
    ("Success", "Succes", "trophy", "#F5A700"),
    ("Wisdom", "Wijsheid", "book", "#A560E8"),
    ("Happiness", "Geluk", "smile", "#F5A700"),
    ("Self Improvement", "Zelfverbetering", "leaf", "#58CC02"),
    ("Gratitude", "Dankbaarheid", "heart", "#FF7A00"),
    ("Friendship", "Vriendschap", "users", "#00A889"),
    ("Hope", "Hoop", "sun", "#FF7A00"),
    ("Creativity", "Creativiteit", "palette", "#E056A0"),
    ("Inner Peace", "Innerlijke Rust", "lotus", "#00A889"),
    ("Confidence", "Vertrouwen", "shield", "#1CB0F6"),
    ("Perseverance", "Doorzettingsvermogen", "mountain", "#FF7A00"),
    ("Inspiration", "Inspiratie", "sparkles", "#A560E8"),
    ("Positive Life", "Positief Leven", "sun", "#58CC02"),
    ("Courage", "Moed", "shield", "#FF4B4B"),
    ("Kindness", "Vriendelijkheid", "heart", "#E056A0"),
    ("Patience", "Geduld", "hourglass", "#00A889"),
    ("Forgiveness", "Vergeving", "hands", "#FF7A00"),
    ("Strength", "Kracht", "dumbbell", "#FF4B4B"),
    ("Joy", "Vreugde", "smile", "#F5A700"),
    ("Balance", "Balans", "scale", "#00A889"),
    ("Growth", "Groei", "sprout", "#58CC02"),
    ("Purpose", "Doel", "target", "#A560E8"),
    ("Mindfulness", "Mindfulness", "lotus", "#00A889"),
    ("Daily Routine", "Dagelijkse routine", "calendar", "#1CB0F6"),
    ("Weather", "Weer", "cloud", "#1CB0F6"),
    ("Feelings", "Gevoelens", "smile", "#E056A0"),
    ("Food", "Eten", "fork", "#FF7A00"),
    ("Health", "Gezondheid", "heart", "#58CC02"),
    ("Work", "Werk", "briefcase", "#1CB0F6"),
    ("Technology", "Technologie", "chip", "#A560E8"),
    ("Nature", "Natuur", "leaf", "#58CC02"),
    ("Animals", "Dieren", "paw", "#FF7A00"),
    ("Colors", "Kleuren", "palette", "#E056A0"),
    ("Directions", "Richtingen", "compass", "#1CB0F6"),
    ("Body Parts", "Lichaamsdelen", "hand", "#00A889"),
    ("Clothes", "Kleding", "shirt", "#E056A0"),
    ("Music", "Muziek", "music", "#A560E8"),
    ("Sports", "Sport", "ball", "#FF7A00"),
    ("Holidays", "Feestdagen", "gift", "#FF4B4B"),
    ("Education", "Onderwijs", "book", "#1CB0F6"),
    ("Culture", "Cultuur", "globe", "#00A889"),
    ("Finance", "Financiën", "coin", "#58CC02"),
    ("Relationships", "Relaties", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learndutch",
    "#dutchlessons",
    "#dutchforbeginners",
    "#languagelearning",
    "#dutchvocabulary",
    "#velocitydutch",
    "#dailydutch",
    "#dutch",
    "#learnlanguages",
    "#speakdutch",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
