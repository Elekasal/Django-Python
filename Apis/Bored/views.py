from django.shortcuts import render
import requests
# Create your views here.
def home (request):
    url='https://www.boredapi.com/api/activity'
    data=requests.get(url)
    data=data.json()
    return render(request,'Bored/home.html',{'data':data,'url':url})