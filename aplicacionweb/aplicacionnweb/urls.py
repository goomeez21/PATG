
from django.contrib import admin
from django.urls import path
from django.urls.conf import include



from .views import HomeView

#url y los metodos que llama al usar esa url
#este archivo contiene a las url padres del resto de url
urlpatterns = [
    path('admin/', admin.site.urls),
    #incluye los urls que estan dentro del archivo blog.urls
    path('blog/', include('blog.urls',namespace='home'),name='lista'),
    #incluye los urls que estan dentro del archivo allauth.urls este archivo es el que tiene todo el tema de los usuarios
    path('accounts/', include('allauth.urls')),
    path('', HomeView.as_view(),name='home')

]
