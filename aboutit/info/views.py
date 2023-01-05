from django.shortcuts import render
def home(request):
    return render(request,'info/index.html')
# Create your views here.
