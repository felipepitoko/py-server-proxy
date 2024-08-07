#create an api with flask to receive a post and save its body into folder received as json
from flask import Flask, request, jsonify
import os, json
from datetime import datetime

app = Flask(__name__)

# Set the folder path where you want to save the JSON files
FOLDER_PATH = 'recebidas'

# Create the folder if it doesn't exist
if not os.path.exists(FOLDER_PATH):
    os.makedirs(FOLDER_PATH)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Testing api v 1.0'}), 200

@app.route('/api/received', methods=['GET'])
def list_received():
    lista_recebidos = os.listdir(FOLDER_PATH)
    return jsonify(lista_recebidos), 200

@app.route('/api/example-data', methods=['GET'])
def serve_example_data():
    example_data = [
        {
            "nome": "Neymar",
            "idade": "31"
        },
        {
            "nome": "Faustao",
            "idade": "72"
        },
        {
            "nome": "Selena gomez",
            "idade": "31"
        }
    ]
    return jsonify(example_data), 200

@app.route('/api/receive', methods=['POST'])
def receive_data():    
    data = request.get_json()
    if request.args:
        data["query_params"] = request.args

    filename = f"{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.json"
    file_path = os.path.join(FOLDER_PATH, filename)

    with open(file_path, 'w') as file:
        json.dump(data, file)

    return jsonify({'message': 'Data received and saved successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
