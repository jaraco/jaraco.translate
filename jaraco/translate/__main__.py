import sys
import os

from . import google

lang = sys.argv[1]
text = ' '.join(sys.argv[2:])

google.translate.API_key = os.environ['GOOGLE_TRANSLATE_API_KEY']
print(google.translate(text, target_lang=lang))
