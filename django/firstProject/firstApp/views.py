from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(Request):
    my_dict={"insert_me":"Hello I am from index.html"}
    return render(Request,'index.html',context=my_dict)
