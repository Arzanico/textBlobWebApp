from clases.analisisLib import BlobText

p = 'Esto es un texto de prueba'

# Instancia
obText = BlobText(p,3)
# Aqui tengo que llamar a la funcion pasandole el metodo de la libreria TextBlob que que quiero usar
# Ej : text.tags ; noun_phrases ; sentiment ; sentiment.polarity
# words ; sentences ; word_counts['word'] ; .translate(to='es') ; .detect_language()
# .ngrams(n=3) ; 
print(obText.text)

