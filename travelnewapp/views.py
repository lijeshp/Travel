from django.http import HttpResponse
from django.shortcuts import render
from . models import place, blog

# Create your views here.
def traveloo(request):
    obj = place.objects.all()
    obj1 = blog.objects.all()
    return render(request, 'index.html', {'outputs': obj, 'blog_outputs': obj1})


