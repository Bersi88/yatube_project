#urls yatube

from django.contrib import admin
from django.urls import include, path

app_name = 'project'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('group/', include('posts.urls'))
]
