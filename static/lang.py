from babel.core import Locale

translations = {
    "be": {
        "greeting": "Вітаю!",
    },
    "en": {
        "greeting": "Hello!",
    },
}


def transalate(locale: Locale, line: str):
    translation: str = str(locale)

    # Fallback to English if no translation for given locale exists
    if not translation in translations:
        translation = "en"

    lang: dict = translations[translation]
    if line in lang:
        return lang[line]

    # Fallback to English if no translation for given line exists
    return translations["en"][line]
