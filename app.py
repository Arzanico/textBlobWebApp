from flask import Flask, request, render_template, redirect
from clases.analisisLib import BlobText
import os
from unicodedata import normalize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input', methods=['POST'])
def input():

    if request.method == 'POST':
        usuario = request.form['usuario']
        tipoAnalisis = request.form['tipoAnalisis']
        
        if usuario == '':
            return render_template('index.html' , message = 'Ingrese nombre de usuario')

        return render_template('input.html' , usuario=usuario , tipoAnalisis=tipoAnalisis)

app.config["FILES_UPLOADS"] = "static/files"

@app.route('/proced', methods=['POST'])
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

        #Uso a funcion para simplificar la llamada a la libreria TextBlob            
        texto = giveMeText(elecc)
        # Llamo a la mi clase donde imlemento la libreria TextBlob
        # en mi clase tengo los metodos de la libreria definidos como atributos del texto
        obText = BlobText(texto,2)
        tags = obText.tags
        gramas = obText.ngramas
        return render_template('results.html' , tags = tags , text = texto, gramas = gramas)


@app.route('/volver', methods=['POST'])
def vovler():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()