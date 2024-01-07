from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def djform(request):
    NFO=Form1()
    d={'NFO':NFO}
    if request.method=='POST':
        NDO=Form1(request.POST)
        if NDO.is_valid():
            return HttpResponse(NDO.cleaned_data['Sname'])
        else:
            return HttpResponse('INvalid Data')
    return render(request,'djform.html',d)