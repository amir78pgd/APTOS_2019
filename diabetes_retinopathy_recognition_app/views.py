from __future__ import unicode_literals
from .models import Image
from .forms import UploadImageForm
import keras
from django.shortcuts import render
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import load_model
global graph,model

#initializing the graph
graph = tf.get_default_graph()

#loading our trained model
print("Keras model loading.......")
model = load_model('diabetes_retinopathy_recognition_app/model_169.h5')
print("Model loaded!!")

#creating a dictionary of classes
class_dict = {'No DR': 0,
            'Mild': 1,
            'Moderate': 2,
            'Severe': 3,
            'Proliferative': 4}

class_names = list(class_dict.keys())

def prediction(request):
    if request.method == 'POST' and request.FILES['myfile']:
        post = request.method == 'POST'
        myfile = request.FILES['myfile']

        # Preprocess image
        img = image.load_img(myfile, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        #img = img/255
        img = preprocess_input(img)


        # Prediction
        global graph
        with graph.as_default():
            #preds = decode_predictions(model.predict(img), top=3)[0]  # Get Top-3 Accuracy
            preds = model.predict(img)
        #preds = preds.flatten()
        preds = preds[0]
        print(preds)
        prob_dist = []
        for i in range(len(preds)):
            prob_dist.append([class_names[i], preds[i]*100])
            df = pd.DataFrame(prob_dist, columns=['Condition', 'Probability'])
            tables=[df.to_html(classes='data', header="true")]
            #titles=df.columns.values


        # Extract condition of disease and class
        classes = [name.title() for name in class_names]
        cond_name = classes[np.argmax(preds)]
        context = {
        'Condition': cond_name,
        #'Probability': 
        'tables': tables
        #'titles': titles        
        
        }

        #result = context
        return render(request, "diabetes_retinopathy_recognition_app/prediction.html", context)
        #return render(request, "diabetes_retinopathy_recognition_app/prediction.html", {
        #    'result': result})
    else:
        return render(request, "diabetes_retinopathy_recognition_app/prediction.html")


def image_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image(img=request.FILES['img'])
            image.save()
            return render(request, 'diabetes_retinopathy_recognition_app/prediction.html',
                          {'image' : image})
    else:
        form = UploadImageForm()
    return render(request, 'diabetes_retinopathy_recognition_app/prediction.html',
                  {'form': form })

#def predict(request):
    
    # Preprocess image
#    img_path = os.path.join(media_path, os.listdir(media_path)[0])
#    print(img_path)
#    img = image.load_img(img_path, target_size=(224, 224))
#    x = image.img_to_array(img)
#    x = np.expand_dims(x, axis=0)
#    x = preprocess_input(x)
#    print(x.shape)

    # Prediction
#    global graph
#    with graph.as_default():
#        preds = loaded_model.predict(x)

    # Extract name of dish and ingredients
#    classes = [name.title() for name in names]
#    dish_name = classes[np.argmax(preds)]
#    context = {
#        'dish_name': dish_name,
#        'ingredients': parse_ingredients(dish_name)
#    }

#    print(context)

#    return render(request, 'result.html', context)

def clean_up(request):
    # Delete image instance from model
    Classifier.objects.all().delete()

    # Delete image from media directory
 #   for img in os.listdir(media_path):
 #       os.remove(os.path.join(media_path, img))

 #   return HttpResponseRedirect('/')
    return render(request, "diabetes_retinopathy_recognition_app/prediction.html")
