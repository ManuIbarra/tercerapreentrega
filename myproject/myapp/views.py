from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def simple_page(request):
    return render(request, 'myapp/simple_page.html')