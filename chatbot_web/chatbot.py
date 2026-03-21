#importo todas las librerias necesarias
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

#lemmatizer lo que hace es convertir palabras en la raiz de la palabra (ejemplo: leimos -> leer)
lemmatizer = WordNetLemmatizer()

# abro el archivo json con utf-8 (contiene casi todos los caracteres del mundo), lo guardo en formato json y lo meto en la variable intentos
# .read() lo que hace es extraer todo el contenido de un fichero y lo lee como una string

intentos = json.loads(open(r'data/intentos.json', encoding = "utf-8").read())

#metemos en la variable palabras todo lo que sale del fichero palabras.pkl y lo leemos en binario
#pickle lo que hace es guardar algo en un archivo.pkl para que no lo tengas que crear 2 veces, hace un volcado de datos. Asique se guarda en unos y ceros, por eso lo leemos en binario
palabras = pickle.load(open("palabras.pkl", rb))
etiquetas = pickle.load(open("etiquetas.pkl", rb))