# chatbot_library

chatbot_venv es la libreria que contiene las funciones o programas para que funcione lo que vamos a crear.

## data

en data tenemos el fichero intents.json que sirve para almacenar preguntas de (clave:valor)

## Requeriments.txt

Hay que poner "pip install -r requirements.txt" en la terminal para que se instalen todos los paquetes necesarios sin tener que ir uno por uno

## implementacion del chatbot en wordpress

Hay que unir el chatbot con wordpress, para ello lo que se hara es: descargar flask y ngrok. ngrok es el tunel entre python y wordpress y por otro lado flask es el tradctor entre python y la web, para que flask se pueda conectar a ngrok hay qe hacer un api rest.

## app.py 
Es el fichero que contiene Flask. Por lo tanto hay que hacer un api rest con los metodos de http GET y POST para que envie y reciba mensajes (formato json) con el servidor web.