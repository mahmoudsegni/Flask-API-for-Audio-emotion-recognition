import numpy as np
from flask import Flask, request, render_template,redirect,jsonify
import joblib
from keras.models import model_from_json
import librosa 
from utils import *
import os
import json

from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './Upload'

@app.route('/', methods=['GET', 'POST']) 


def index():
    y_pred = ""
    if request.method == "POST": 
        print("FORM DATA RECEIVED")
        if "file" not in request.files:  # no file uploaded
            print(" Cannot find file")
            return redirect(request.url)
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # if file exist, give that file
        if file.filename == "":  # if file is empty, return to the main page
            print(" Uploaded file is empty")
            return redirect(request.url)
        if file:
            print(" Your file successfully uploaded")
            
            X = []
            feature = get_features(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            for ele in feature:
                X.append(ele)
            X = scaler.transform(X)
            data=np.expand_dims(X, axis=2) 
            pred_test = model.predict(data)
            y_pred = encoder.inverse_transform(pred_test)
            print("***********",pred_test[0])
    #return (jsonify(y_pred[0][0])) 
    data=[{"emotion": "angry","score": str(pred_test[0][0])},{"emotion": "calm","score": str(pred_test[0][1])},{"emotion": "disgust","score": str(pred_test[0][2])},
    {"emotion": "fear","score": str(pred_test[0][3])},{"emotion": "happy","score": str(pred_test[0][4])},{"emotion": "neutral","score": str(pred_test[0][5])},
    {"emotion": "sad","score":str(pred_test[0][6])},{"emotion": "surprise","score":str(pred_test[0][7])} ]
    #return render_template('index.html', y_pred=y_pred)
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # multiple requests at the same time for the file
