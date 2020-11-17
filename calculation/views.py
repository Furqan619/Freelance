from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
      return render(request,'home.html',{ 'home':"furqan"})

def calculate(request):
      A = int(request.POST['valueA'])
      B = int(request.POST['valueB'])
      res =(A)+(B)
      return render(request, 'result.html',{'result':res})

