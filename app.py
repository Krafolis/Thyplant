import base64
import numpy as np
import io
from PIL import Image

from flask import request
from flask import jsonify
from flask import Flask
from keras.models import load_model

app = Flask(__name__) 

def get_apple_model():
    model = load_model('plant_model.h5')
    print("[+] model loaded")
    return model

def get_corn_model():
    model = load_model('plant_model.h5')
    print("[+] model loaded")
    return model

def get_grape_model():
    model = load_model('plant_model.h5')
    print("[+] model loaded")
    return model

def decode_request(req):
    encoded = req["image"]
    decoded = base64.b64decode(encoded)
    return decoded

def preprocess(decoded):
    pil_image = Image.open(io.BytesIO(decoded)).resize((150,150), Image.LANCZOS).convert("RGB") 
    image = np.asarray(pil_image)
    batch = np.expand_dims(image, axis=0)
    
    return batch

apple_model = get_apple_model()
corn_model = get_corn_model()
grape_model = get_grape_model()
 
@app.route("/applepredict", methods=["POST"])
def applepredict():

    print("[+] request received")

    req = request.get_json(force=True)

    image = decode_request(req)

    batch = preprocess(image)

    classes = apple_model.predict(batch)

    if classes[0,0]==1:
        apple_predict='Keropeng Apel'
    elif classes[0,1]==1:
        apple_predict='Busuk Hitam (Apel)'
    elif classes[0,2]==1:
        apple_predict='Karat Cedar Apel'
    elif classes[0,3]==1:
        apple_predict='Apel Sehat'
    elif classes[0,4]==1:
        apple_predict='Keropeng Apel'
    elif classes[0,5]==1:
        apple_predict='Busuk Hitam (Apel)'
    elif classes[0,6]==1:
        apple_predict='Karat Cedar Apel'
    elif classes[0,7]==1:
        apple_predict='Apel Sehat'
    elif classes[0,8]==1:
        apple_predict='Keropeng Apel'
    elif classes[0,9]==1:
        apple_predict='Busuk Hitam (Apel)'
    elif classes[0,10]==1:
        apple_predict='Karat Cedar Apel'
    elif classes[0,11]==1:
        apple_predict='Apel Sehat'

    print(apple_predict)

    response = {"prediction": apple_predict}

    print("[+] results {}".format(response))

    return jsonify(response)

@app.route("/cornpredict", methods=["POST"])
def cornpredict():

    print("[+] request received")

    req = request.get_json(force=True)

    image = decode_request(req)

    batch = preprocess(image)

    classes = corn_model.predict(batch)

    if classes[0,0]==1:
        corn_predict='Bercak Daun Cercospora'
    elif classes[0,1]==1:
        corn_predict='Karat Biasa'
    elif classes[0,2]==1:
        corn_predict='Hawar Daun Jagung Utara'
    elif classes[0,3]==1:
        corn_predict='Jagung Sehat'
    elif classes[0,4]==1:
        corn_predict='Bercak Daun Cercospora'
    elif classes[0,5]==1:
        corn_predict='Karat Biasa'
    elif classes[0,6]==1:
        corn_predict='Hawar Daun Jagung Utara'
    elif classes[0,7]==1:
        corn_predict='Jagung Sehat'
    elif classes[0,8]==1:
        corn_predict='Bercak Daun Cercospora'
    elif classes[0,9]==1:
        corn_predict='Karat Biasa'
    elif classes[0,10]==1:
        corn_predict='Hawar Daun Jagung Utara'
    elif classes[0,11]==1:
        corn_predict='Jagung Sehat'

    print(corn_predict)

    response = {"prediction": corn_predict}

    print("[+] results {}".format(response))

    return jsonify(response)

@app.route("/grapepredict", methods=["POST"])
def grapepredict():

    print("[+] request received")

    req = request.get_json(force=True)

    image = decode_request(req)

    batch = preprocess(image)

    classes = grape_model.predict(batch)

    if classes[0,0]==1:
        grape_predict='Busuk Hitam (Anggur)'
    elif classes[0,1]==1:
        grape_predict='Campak Hitam'
    elif classes[0,2]==1:
        grape_predict='Bercak Daun Isariopsis'
    elif classes[0,3]==1:
        grape_predict='Anggur Sehat'
    elif classes[0,4]==1:
        grape_predict='Busuk Hitam (Anggur)'
    elif classes[0,5]==1:
        grape_predict='Campak Hitam'
    elif classes[0,6]==1:
        grape_predict='Bercak Daun Isariopsis'
    elif classes[0,7]==1:
        grape_predict='Anggur Sehat'
    elif classes[0,8]==1:
        grape_predict='Busuk Hitam (Anggur)'
    elif classes[0,9]==1:
        grape_predict='Campak Hitam'
    elif classes[0,10]==1:
        grape_predict='Bercak Daun Isariopsis'
    elif classes[0,11]==1:
        grape_predict='Anggur Sehat'

    print(grape_predict)

    response = {"prediction": grape_predict}

    print("[+] results {}".format(response))

    return jsonify(response)