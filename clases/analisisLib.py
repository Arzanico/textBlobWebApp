from textblob import TextBlob
# Ej de funciones que voy a usar : text.tags ; text.noun_phrases ; text.sentiment ; sentiment.polarity
# words ; sentences ; word_counts['word'] ; .translate(to='es') ; .detect_language()
# .ngrams(n=3) ;


class BlobText:
    # Los atributos los deribo de la clase TextBlob
    def __init__(self, texto, ng=None):
        self.texto = texto
        self.blob = TextBlob(self.texto)
        blob_es = self.blob
        blob_en = self.blob.translate(to='en')
        #La libreria aun no esta funcionando bien en español, si quisieramos usarla directo en español
        # tendriamos que entrenar los algoritmos, en cambio, vamos a necesitar traducir el texto al ingles
        # para aplicar las funciones de manera directa, luego volvemos a traducir al español.
        self.text = blob_en
        self.tags = blob_en.tags
        self.words = blob_es.words
        self.ngramas = blob_es.ngrams(ng)
        self.sentiment = blob_en.sentiment
        self.polarity = self.sentiment.polarity

        