from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'title': 'Home'})


def index1(request):
    return render(request, 'page1.html', {'title': 'Page 1', 'userName': 'Harsh'})


def index2(request):
    return render(request, 'page2.html', {'title': 'Page 2'})


def index3(request):
    return render(request, 'page3.html', {'title': 'Page 3'})


def index4(request):
    return render(request, 'page4.html', {'title': 'Page 4'})

