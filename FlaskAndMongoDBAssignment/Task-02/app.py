from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

# Load environment variables from .env file
load_dotenv()

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI')

client = pymongo.MongoClient(mongo_uri) # type: ignore
db = client['Form'] # type: ignore
data_collection = db['Data'] # type: ignore

app = Flask(__name__)


@app.route('/form', methods=['GET', 'POST'])
def form():
    current_day = datetime.now().strftime("%A")
    current_time = datetime.now().strftime("%H:%M:%S")
    if request.method == 'GET':
        return render_template('form.html', current_day=current_day, current_time=current_time)
    else:
        data = request.form.to_dict()
        data['submission_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_collection.insert_one(data) # type: ignore
        return redirect(url_for('submit_form'))

@app.route('/submit')
def submit_form():
    return render_template('submit.html')

if __name__ == "__main__":
    app.run(debug=True)