from django.shortcuts import render,redirect
from .models import Articles
from .form import Articulesform
import requests
from django.http import HttpResponseRedirect



def index(request):
    return render(request, "mainApp/homepage.html")

def ccstat(request):
    error = ''
    info = ''
    form = Articulesform()
    url = "https://deepmemo.a-bank.com.ua/prolog/conveyor/v0.2/siem_ccstat/siem_ccstat_search_all"
    if request.method == 'POST':
        form = Articulesform(request.POST)
        if form.is_valid():
            id = form.cleaned_data['ekbid']
            responsesss = requests.post(url, json={'ekb_id': id, 'card': ''})
            ccstat = responsesss.json()
            ccstat = ccstat["body"]["ccstat"][0]

            info = ccstat
        else:
            error = 'Форма была не верная'


    date = {
        'form':form,
        'error': error,
        'info':info
    }
    return render(request, "mainApp/ccstat.html",date)

def contact(request):
    return render(request, "mainApp/basic.html",{'values':['Если у вас остались вопросы задавайт', '380638974416']})