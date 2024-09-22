from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    
    d={'author':'rahim','age':'23','lst':["python","is","best"],'birthday':datetime.datetime.now(),
       "val":'me'}
    return render(request,'home.html',d)