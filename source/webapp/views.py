from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.Cat import Cat

cat_instance = Cat()


def index(request):
    if request.method == 'POST':
        cat_instance.name = request.POST.get('catName', '')
        return HttpResponseRedirect('play')
    else:
        return render(request, 'index.html')


def play(request):
    cat_action = request.POST.get('catAction')
    return render(request, 'play.html', cat_instance.action(cat_action))
