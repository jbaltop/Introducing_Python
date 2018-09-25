# linux only

import locale
from datetime import date

halloween = date(2015, 10, 31)
for lang_country in ["ko_kr", "en_us", "fr_fr", "de_de", "es_es", "is_is"]:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime("%A, %B %d")
