from googletrans import Translator

translator = Translator()

user_text = input('Type text to translate : ')
result = translator.translate(user_text)

print(f'\nThe source language: {result.src}'
      f'\nDestination/Output language: {result.dest}'
      f'\nOriginal text: {result.origin}'
      f'\nTranslated text: {result.text}')
