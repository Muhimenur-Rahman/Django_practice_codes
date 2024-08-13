from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    diction = {'list_1' : [1,2,3,4],
               'list_2' : ['Bangladesh','Nepal','China','Thiland'],
               'digit' : 10,
               'name' : 'Anonymous Person',
               'birthday' : datetime.datetime.now(),
               'firends' : [
                            {'name': 'Liam', 'age': 25},
                            {'name': 'Emma', 'age': 28},
                            {'name': 'Noah', 'age': 34},
                           ],
               }
    return render(request,"first_app/home.html",diction)
