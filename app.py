#!/home/nico/Documents/proyectoFlask/v2/env/bin py

from flask import Flask, request, render_template, redirect
from textblob import TextBlob
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
        #Instancia de la clase TextBlob
        txBlob = TextBlob(texto)
        #La clase aun no funciona con el español, pero lo que hace el metodo es identificar funcion liguistica
        resultados = txBlob.tags

        return render_template('results.html' , resultados = resultados)


@app.route('/volver', methods=['POST'])
def vovler():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()