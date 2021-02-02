from django.shortcuts import render
import requests
from .models import Mess,Event

# Create your views here.

def home(request):
    return render(request, "baseapp/home.html")

def result(request, email):
    user_roll = int(email[0:6])
    print(user_roll)
    url = "https://nithp.herokuapp.com/api/result/student/{roll}"
    data = requests.get(url.format(roll=user_roll)).json()
    dictionary = {}
    for res in data['result']:
        if res['sem'] not in dictionary:
            dictionary[res['sem']] = []
        dictionary[res['sem']].append([res['grade'],res['sub_gp'],res['sub_point'],res['subject'],res['subject_code']]) 
    return render(request, "baseapp/result.html", {'data':dictionary, 'whole_data':data['summary']})

def mess(request, email):
    roll_first_two = int(email[0:2])
    mess_data = Mess.objects.get(roll_starts_with=roll_first_two)
    return render(request, 'baseapp/mess.html', {'mess_data':mess_data})

def CalendarView(request):
    return render(request, 'baseapp/calendar.html')