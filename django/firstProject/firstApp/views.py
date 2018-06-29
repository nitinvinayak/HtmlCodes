from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.
def index(Request):
    my_dict={"insert_me":"Hello I am from firstApp/index.html"}
    return render(Request,os.path.join('firstApp','index.html'),context=my_dict)
