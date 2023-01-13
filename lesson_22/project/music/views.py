from django.shortcuts import render
# Create your views here.
from datetime import datetime

def index(request):
    user_name = request.GET.get('user', None)
    year = request.GET.get('year')
    date = datetime.now()
    context = {'user': user_name, "year": year, "date": date}
    return render(request, 'music/home.html', context)

def contacts(request):
    return render(request, 'music/contacts.html')