import tensorflow as tf
import cv2
import numpy as np
from PIL import Image,ImageOps

def load_model():
    model = tf.keras.models.load_model("assets/car_bike_classifier.h5",compile=False)
    model.compile(loss='categorical_crossentropy',
                  optimizer="adam",
                  metrics=['acc'])
    return model

def import_and_predict(image_data,model):
    size =  (75,75)
    image = ImageOps.fit(image_data,size,Image.LANCZOS)
    img=np.asarray(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_reshape=gray[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction

def test_prediction():
    model = load_model()
    image = Image.open("assets/test_image_bike.jpg")
    result = import_and_predict(image,model)
    print(result)
    assert np.argmax(result) == 0