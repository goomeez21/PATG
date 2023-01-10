from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.


#en este archivo contiene informacion que se nos representa en el admin


from .models import Post
@admin.register(Post)


class Post(OSMGeoAdmin):
    list_display = ('nombre', 'geometry')

from .models import Productos

@admin.register(Productos)
class Productos(admin.ModelAdmin):
    list_display = (['productos'])


from .models import precio
@admin.register(precio)
class precio(admin.ModelAdmin):
    list_display = ('local', 'precio','user','productos')