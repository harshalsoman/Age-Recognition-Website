from django.shortcuts import render
from .forms import ImageForm
import glob
import os
from.models import Image
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model, save_model
import numpy as np
import scipy
# Create your views here.
from django.http import HttpResponse
global c
def home(request):
    form = ImageForm()
    return render(request,'home.html',{'form' :form})

def predict(request):

    if request.method == "POST":

        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    img_predict = Image.objects.all()
    c= len(img_predict)

    new_model = load_model('C:/Users/Dell/Desktop/Projects/Face Recognition/final_model3.h5')
    image = list(glob.glob('C:/Users/Dell/Desktop/Projects/Face Recognition/ML/media/myimage/*'))
    img = max(image, key=os.path.getctime)
    new_img = tf.keras.preprocessing.image.load_img(img)
    #pred_img = tf. keras.preprocessing.image.load_img(img[c-1])
    #predict_img = tf.keras.preprocessing.image.img_to_array(img)
    img_batch = np.expand_dims(new_img, axis=0)
    pred_generator = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255
    )


    pred_image = pred_generator.flow(
                 img_batch,
                 batch_size=1,
                 shuffle=False
    )
    age = int(new_model.predict(pred_image))

    print(new_model.summary())

    #img = max(image, key=os.path.getctime)


    return render(request,'predict.html',{'image':img_predict[c-1],'age': age})



