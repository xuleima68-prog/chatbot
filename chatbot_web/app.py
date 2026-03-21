from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import chatbot_response 
print("--- EL SERVIDOR ESTÁ INTENTANDO ARRANCAR ---")
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "Servidor del Chatbot AD activo."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    
    if not data or 'message' not in data:
        return jsonify({"error": "Mensaje vacío"}), 400
    
    user_message = data['message']
    
    # Aquí llamamos a tu lógica real de chatbot.py
    respuesta = chatbot_response(user_message)
    
    return jsonify({
        "status": "success",
        "reply": respuesta
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)