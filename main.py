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

@app.route('/api/receive', methods=['POST'])
def receive_data():
    # Get the request data
    data = request.get_json()
    #create an str as dd-MM-yyyy hh-mm with current time


    filename = f"{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.json"
    file_path = os.path.join(FOLDER_PATH, filename)

    # Save the data to a JSON file
    with open(file_path, 'w') as file:
        json.dump(data, file)

    return jsonify({'message': 'Data received and saved successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)
