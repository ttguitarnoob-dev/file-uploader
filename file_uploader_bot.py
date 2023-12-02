from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/home/travis/frontend/fireweed-guitars/build/static/media'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return "Hello home"

@app.route('/photos', methods=['POST'])
def photo_upload():
    
    
    # Check if the POST request has a file part
    if 'file' not in request.files:
        
        return jsonify({'error': 'No file part'})
    

    file = request.files['file']
    

    # If the user does not select a file, the browser sends an empty file without a filename
    if file.filename == '':
        
        return jsonify({'error': 'No selected file'})

    # Check if the file is allowed
    if file and allowed_file(file.filename):
        print('smellyourassbro', file.filename)
        filename = file.filename  # Set the desired filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print('file saved? supposedly')
        return jsonify({'success': 'File uploaded successfully'})

    return jsonify({'error': 'File type not allowed'})

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port=3005, debug=True)
