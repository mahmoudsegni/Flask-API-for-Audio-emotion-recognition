import numpy as np
from flask import Flask, request, render_template,redirect,jsonify
import joblib
from keras.models import model_from_json
import librosa 
from utils import *
import os
import json
import requests
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './Upload'

@app.route('/', methods=['GET', 'POST']) 


def index():
    y_pred = ""
    pred_list=[]
    confidence_list=[]
    
    file=True
    feature=request.get_json()
    

    if file:
        print(" Your file successfully uploaded")
            
        X = []
        #feature = get_features(wav_path)
        for ele in feature:
            X.append(ele)
        X = scaler.transform(X)
        data=np.expand_dims(X, axis=2) 
        pred_test = model.predict(data)
        print("***********",pred_test[0])
     
    data=[{"emotion": "angry","score": str(pred_test[0][0])},{"emotion": "calm","score": str(pred_test[0][1])},{"emotion": "disgust","score": str(pred_test[0][2])},
    {"emotion": "fear","score": str(pred_test[0][3])},{"emotion": "happy","score": str(pred_test[0][4])},{"emotion": "neutral","score": str(pred_test[0][5])},
    {"emotion": "sad","score": str(pred_test[0][6])},{"emotion": "surprise","score": str(pred_test[0][7])} ]
    
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # multiple requests at the same time for the file
