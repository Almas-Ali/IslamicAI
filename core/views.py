from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')


def search(request, query=None):
    if request.method == 'POST':
        query = request.POST.get('query')
        return render(request, 'core/search.html', {'query': query})

    return render(request, 'core/search.html')
