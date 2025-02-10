#posts views
from django.http import HttpResponse
from django.shortcuts import render


# Главная страница
#def index(request):
 #   return HttpResponse('Главная страница')

def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Страница со списком мороженого
def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    return HttpResponse(f'Мороженое номер {slug}')