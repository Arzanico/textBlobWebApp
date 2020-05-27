from flask import Flask, request, render_template, redirect
from clases.analisisLib import BlobText
import os
from unicodedata import normalize


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/input/', methods=['POST'])
def input():
    if request.method == 'POST':
        usuario = request.form['usuario']
        tipoAnalisis = request.form['tipoAnalisis']
        
        if usuario == '':
            return render_template('index.html' , message = 'Ingrese nombre de usuario')

        return render_template('input.html' , usuario=usuario , tipoAnalisis=tipoAnalisis)


app.config["FILES_UPLOADS"] = "static/files"


tagDict = {
    'CC':'coordinating', #conjunction 	and
    'CD':'cardinal', #number 	1, third
    'DT':'determiner', 	#the
    'EX':'existential', #there 	there is
    'FW':'foreign word', #d’hoevre
    'IN':'preposition/subordinating', # conjunction 	in, of, like
    'JJ':'adjective', #big
    'JJR':'adjective/comparative', #bigger
    'JJS':'adjective/superlative', #biggest
    'LS':'list marker' , # 1)
    'MD':'modal', #could, will
    'NN':'noun singular',  #or mass 	door
    'NNS':'noun plural', #	doors
    'NNP':'proper noun, singular', #John
    'NNPS':'proper noun, plural', 	#Vikings
    'PDT':'predeterminer', 	#both the boys
    'POS':'possessive ending', 	#friend‘s
    'PRP':'personal pronoun', 	#I, he, it
    'PRPS':'possessive pronoun', 	#my, his
    'RB':'adverb', 	#however, usually, naturally, here, good
    'RBR':'adverb comparative',  	#better
    'RBS':'adverb superlative', 	#best
    'RP':'particle' ,#	give up
    'TO': 'to',# 	to go, to him
    'UH':'interjection',# 	uhhuhhuhh
    'VB': 'verb base form',# 	take
    'VBD':'verb past tense',# 	took
    'VBG':'verb gerund/present',# participle 	taking
    'VBN':'verb past participle' ,#	taken
    'VBP':'verb sing. present', #non-3d 	take
    'VBZ':'verb 3rd person',# sing. present 	takes
    'WDT':'wh-determiner',#	which
    'WP': 'wh-pronoun',#	who, what
    'WPS':'possessive',# wh-pronoun	whose
    'WRB':'wh-abverb'
}

@app.route('/proced/', methods=['POST'])
def proced():
    if request.method == 'POST':
        elecc = request.form['choise']

        def giveMeText(algo):
            choise = algo
            if choise == 'texto':
                text = request.form['texto']
                return text
            if choise == 'archivo':
                archivo = request.files['archivo']
                archivo.save(os.path.join(app.config["FILES_UPLOADS"] , archivo.filename))
                directorio = '{}/{}'.format(app.config["FILES_UPLOADS"], archivo.filename)
                with open(directorio, 'r') as textFile:
                    text = textFile.read()
                    text = normalize('NFC', text)
                return text
        # Uso giveMeText para simplificar la llamada a la libreria TextBlob
        texto = giveMeText(elecc)
        # Llamo a la mi clase donde imlemento la libreria TextBlob
        # en mi clase tengo los metodos de la libreria definidos como atributos del texto
        obText = BlobText(texto,2)
        tags = obText.tags
        gramas = obText.ngramas
        sentiment = obText.sentiment
        return render_template('results.html' , tags = tags , text = texto, gramas = gramas, tagDict = tagDict, sentiment = sentiment)


@app.route('/volver', methods=['POST'])
def vovler():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
