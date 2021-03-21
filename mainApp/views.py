from django.shortcuts import render


def index(request):
    return render(request, "mainApp/homepage.html")

def contact(request):
    return render(request, "mainApp/basic.html",{'values':['Если у вас остались вопросы задавайт', '380638974416']})