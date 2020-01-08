from textblob import TextBlob
# Ej de funciones que voy a usar : text.tags ; text.noun_phrases ; text.sentiment ; sentiment.polarity
# words ; sentences ; word_counts['word'] ; .translate(to='es') ; .detect_language()
# .ngrams(n=3) ;

#Descripcion de los tags que nos devuelve la libreria TextBlob cuando aplicamos el metodo .tags
# tagDict = {
#     'CC':'coordinating', #conjunction 	and
#     'CD':'cardinal', #number 	1, third
#     'DT':'determiner', 	#the
#     'EX':'existential', #there 	there is
#     'FW':'foreign word', #d’hoevre
#     'IN':'preposition/subordinating', # conjunction 	in, of, like
#     'JJ':'adjective', #big
#     'JJR':'adjective/comparative', #bigger
#     'JJS':'adjective/superlative', #biggest
#     'LS':'list marker' , # 1)
#     'MD':'modal', #could, will
#     'NN':'noun singular',  #or mass 	door
#     'NNS':'noun plural', #	doors
#     'NNP':'proper noun, singular', #John
#     'NNPS':'proper noun, plural', 	#Vikings
#     'PDT':'predeterminer', 	#both the boys
#     'POS':'possessive ending', 	#friend‘s
#     'PRP':'personal pronoun', 	#I, he, it
#     'PRPS':'possessive pronoun', 	#my, his
#     'RB':'adverb', 	#however, usually, naturally, here, good
#     'RBR':'adverb comparative',  	#better
#     'RBS':'adverb superlative', 	#best
#     'RP':'particle' ,#	give up
#     'TO': 'to',# 	to go, to him
#     'UH':'interjection',# 	uhhuhhuhh
#     'VB': 'verb base form',# 	take
#     'VBD':'verb past tense',# 	took
#     'VBG':'verb gerund/present',# participle 	taking
#     'VBN':'verb past participle' ,#	taken
#     'VBP':'verb sing. present', #non-3d 	take
#     'VBZ':'verb 3rd person',# sing. present 	takes
#     'WDT':'wh-determiner',#	which
#     'WP': 'wh-pronoun',#	who, what
#     'WPS':'possessive',# wh-pronoun	whose
#     'WRB':'wh-abverb'
# }

# def translateTag(t):
#     return tagDict[t]

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

