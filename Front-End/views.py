import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .models import User
from django.http import HttpResponse
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf


# Create your models here.
def prepare_image(filepath, img_size):
    img_array = plt.imread(filepath)
    img_resize = cv2.resize(img_array, (img_size, img_size))
    return img_resize.reshape(-1, img_size, img_size, 3)


def accidentDetectionPred(img_path, img_size):
    image = prepare_image(img_path, img_size)
    model = tf.keras.models.load_model('C:/Users/assem/ModelD_CNN_94%.h5')
    pred = model.predict(image)
    return pred


def logout(request):
    # context= {'myUser':None}
    if 'myUserFn' and 'myUserLn' in request.session:
        request.session.pop('myUserFn')
        request.session.pop('myUserLn')
    return render(request, 'AccidentWebAPP/home.html')


def plot_image(filepath):
    img_array = plt.imread(filepath)
    plt.imshow(img_array)
    plt.axis('off')
    plt.savefig('AccidentWebAPP/static/AccidentWebAPP/uploaded_File/plot.jpg', bbox_inches='tight', pad_inches=0)


def get_image(request):
    cat = ['an Accident', 'not an Accident']
    context = {}
    if request.method == 'POST':
        if request.FILES != 0:
            uploaded_file = request.FILES['photo']
            fs = FileSystemStorage(location='AccidentWebAPP/static/AccidentWebAPP/uploaded_File')
            name = fs.save(uploaded_file.name, uploaded_file)
            path = fs.path(name)
            context['path'] = path
            plot_image(path)
            ndx = accidentDetectionPred(path, 300)
            result = cat[int(ndx[0])]
            context['result'] = result
            os.remove(path)
    return render(request, 'AccidentWebAPP/results.html', context)


def login(request):
    if request.method == 'POST':
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        try:
            user = User.objects.get(uname=uname, password=pwd)
        except Exception as ds:
            print(ds)
            context = {'correct': 'Your email or password is not correct'}
            return render(request, 'AccidentWebAPP/login.html', context)
        # context= {'myUser':user}
        request.session['myUserFn'] = user.last_name
        request.session['myUserLn'] = user.first_name
        return render(request, 'AccidentWebAPP/home.html')


def sign(request):
    if request.method == 'POST':
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]
        uname = request.POST["uname"]
        password = request.POST["pwd"]
        try:
            user = User(first_name=first_name, last_name=last_name, email=email, uname=uname, password=password)
            user.save()
            worked = 'Your account has been created successfully!!'
            context = {'worked': worked}
        except ValueError as ve:
            print(ve)
            worked = 'Your account has not been created!!'
            context = {'worked': worked}
            render(request, 'AccidentWebAPP/sign.html', context)
        print('worked')
    return render(request, 'AccidentWebAPP/sign.html', context)


def home(request):
    return render(request, 'AccidentWebAPP/home.html')


def accidentDetection(request):
    return render(request, 'AccidentWebAPP/accidentDetection.html')


def predResults(request):
    return render(request, 'AccidentWebAPP/results.html')


def loginPage(request):
    return render(request, 'AccidentWebAPP/login.html')


def signPage(request):
    return render(request, 'AccidentWebAPP/sign.html')
