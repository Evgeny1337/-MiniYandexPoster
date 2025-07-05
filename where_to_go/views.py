from django.shortcuts import render

def show_start(request):
    return render(request, 'start.html')