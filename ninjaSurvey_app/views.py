from django.shortcuts import render, HttpResponse

def index(request):
    print('index view method:', request.method)
    return render(request, 'index.html')

def result(request):
    #return render(request, 'show.html')
    if request.method == "POST":
        ninja_name = request.POST['ninja_name']
        location = request.POST['location']
        languages = request.POST['languages']
        comments = request.POST['comments']
        context = {
            "ninja_name": ninja_name,
            "location" : location,
            "languages" : languages,
            "comments" : comments
    }
    return render(request, 'show.html', context)

