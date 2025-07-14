from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    try:
        file = 'C:\\Users\\albert\\code\\DevOps-TuteDude\\FlaskAndMongoDBAssignment\\Task-01\\data.json'
        # Open and read the JSON file
        with open(file, 'r') as f:
            data = json.load(f)
        f.close()
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "data.json not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in file"}), 400

if __name__ == "__main__":
    app.run(debug=True)
