from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/transform', methods=['POST'])
def transform_text():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing "text" field'}), 400
    
    transformed_text = data['text'].upper()
    return jsonify({'transformed_text': transformed_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True) # allows Flask to accept connections from Docker and external users