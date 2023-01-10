from django.contrib import admin
from django.urls import path,include
from .views import BlogListView,  BlogDetailView,precioCreateView,precio_listView

app_name="blog"
#creamos las url con los parametros que queramos pasar al metodo y seleccionamos el metodo que vamos a llamar en esa ruta y un nombre
urlpatterns=[
    path('<int:pag>', BlogListView.as_view(),name="home"),
    path('Details/<int:pk>',BlogDetailView.as_view(),name="details"),

    path('precio/',precioCreateView.as_view(),name="precio"),
    path('lista_precio/',precio_listView.as_view(),name="lista_precio")
    
    
]
