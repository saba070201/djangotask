from django.shortcuts import render, get_object_or_404
from .models import* 
def home(request):
    return render(request,'info/index.html')
def article(request,item_id):
    bigitem=get_object_or_404(FullItem,pk=item_id)
    smallitem=Item.objects.filter(parentid=item_id)
    return render(request,'info/article.html',{'bigitem':bigitem,'smallitem':smallitem})
# Create your views here.
