from .models import Articles
from django.forms import ModelForm,TextInput

class Articulesform(ModelForm):
    class Meta:
        model = Articles
        fields  = ['ekbid','card']

        widgets = {
            'ekbid':TextInput(attrs={
                'class':'btn btn-outline-info',
                'placeholder':'Поиск по ЕКБ ИД',
                'name':'id'
            }),
            'card': TextInput(attrs={
                'class': 'btn btn-outline-info',
                'placeholder': 'Поиск по Карте',
                'name':'cards'
            }),
        }
# import requests
# url = "https://deepmemo.a-bank.com.ua/prolog/conveyor/v0.2/siem_ccstat/siem_ccstat_search_all"
# responsesss = requests.post(url, json={'ekb_id':'1800847610','card':''})
# ccstat = responsesss.json()
# ccstat = ccstat["body"]["ccstat"][0]