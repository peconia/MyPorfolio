from django.shortcuts import render

def galleries(request):

    return render(request, 'gallery/galleries.html', {})
