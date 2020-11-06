from googletrans import Translator

trans = Translator()

t = trans.translate('history')

print(t.text)