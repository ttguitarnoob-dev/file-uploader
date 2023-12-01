from flask import Flask, request
from flask_cors import CORS
import os

#INIT
app = Flask(__name__)
CORS(app)

#Home Route
@app.route('/')
def home():
    return "Welcome Home, by Coheed"

#Photo upload
@app.route('/photos', methods=["POST"])
def upload_photos():
    poo = request.get_data()
    print("gdata", request.files)
    file = request.files
    # print('getting data?', file)
    # for i in poo:
    #     print("iii", i)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], "smells"))
    return "poo happened"

#Run app

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=3005, debug=True)