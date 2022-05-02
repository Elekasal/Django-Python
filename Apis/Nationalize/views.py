from django.shortcuts import render
import requests
# Create your views here.
def homeNationalize (request):
    data=''
    if request.method=='POST':
        nombre=request.POST['Var']
        url=f'https://api.nationalize.io?name={nombre}' 
        data=requests.get(url)
        data=data.json()
    return render(request,'homeN.html',{'dataNombre':data})
