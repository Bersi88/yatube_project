#posts views
from django.http import HttpResponse
from django.shortcuts import render


# Главная страница
#def index(request):
 #   return HttpResponse('Главная страница')

def index(request):
    template = 'posts/group_list.html'
    text = 'Главная страница'
    context = {
        'text': text,
    }
    return render(request, template, context)


# Страница со списком мороженого
def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'text': text,
    }
    return render(request, template, context)