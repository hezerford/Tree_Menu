from django.shortcuts import render

def home(request):
    current_url = request.path
    context = {'current_url': current_url}  
    return render(request, 'menu/home.html', context)