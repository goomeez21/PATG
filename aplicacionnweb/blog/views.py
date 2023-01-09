from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .forms import precioCreateForm
from .models import Post
from .models import precio
from django.urls import reverse_lazy
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis.utils import LayerMapping
from django.contrib import auth
from datetime import datetime

from django.db.models import OuterRef
from django.db.models import Max

from django.contrib.auth.models import User

# Create your views here.
# clase en el el que muestra una lista de los restaurantes
class BlogListView(View):
    #metodo get se pasa un parametro que sera la pagina para no sobrecargar la pagina con todos los restaurantes
    def get(self, request, pag ,*args, **kwargs):
        x=10
        posts = Post.objects.all()[(pag-1)*x:pag*x]
        max=Post.objects.count()
        if int(max) % x == 0:
            pagm=max // x
        else:
            pagm=(max // x)+1
            
#categories_list = Category.objects.annotate(posts_count=Count('post'))
#print(categories_list.values())

        if pag > (pagm-3):
            x=pagm-3
            y=pagm-2
            z=pagm-1
        else:
            x=pag+1
            y=pag
            z=pag-1
        context={
            'posts':posts,
            'max':max,
            'pag1':z,
            'pag':y,
            'pag2':x,
            'pagm':pagm
        }
        return render(request,'blogs_list.html',context)




#clase detalles para mostrar los detalles de los restaurantes
class BlogDetailView(View):
    #metodo get en el que envia la informacion detallada del restaurante con los precios
    def get(self, request, pk , *args, **kwargs):
        post=get_object_or_404(Post,pk=pk)
        precio1= precio.objects.raw('select id, precio, a.productos_id, a.local_id, dia from (select productos_id, max(dia)as mdia, local_id from blog_precio where local_id='+str(pk)+' group by productos_id, local_id ) a inner join blog_precio  b on a.local_id=b.local_id and b.dia=a.mdia and a.productos_id=b.productos_id ')
        lon=len(precio1)
        context={
                "post":post,
                "precios":precio1,
                "lon":lon
            }
        return render(request,'blogs_details.html',context)

#clase crear precio
from allauth.account.decorators import login_required 
class precioCreateView(View):
    #crear seguridad
    #metodo get en el que envia solo el formulario y una lista con los locales
    
    #@login_required
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            
            form=precioCreateForm();
            local=Post.objects.all();
            context={
              'form':form,
              'local':local,
            }
        
            return render(request,'precio_Post.html',context)
        else:
            return redirect('home')
        
    #metodo post para guardar los datos del formulario en la base de datos pero primero se confirma que estan bien todos los datos si no te devuelve a la misma pagina
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form=precioCreateForm(request.POST)
            
            
            if form.is_valid():
                local= form.cleaned_data.get('local')
                precios= form.cleaned_data.get('precio')
                productos= form.cleaned_data.get('productos')
                dia= datetime.now().date()
                user= request.user
                p, created = precio.objects.get_or_create(local=local,precio=precios,user=user,dia=dia,productos=productos)
                p.save()
                return redirect('home')


        local=Post.objects.all();
        context={
          'form':form,
          'local':local,
        }
        return render(request,'precio_Post.html',context)
#clase que solo te muestra una lista con los precios que el usuario a subido 
class precio_listView(View):
    #metodo get que solo te muestra los precios qye ha subido el usuario  con el que te has logueado 
    #meter seguridad
    def get(self, request, *args, **kwargs):
        context={
          'precios':precio.objects.filter(user=request.user)
        }
        
        return render(request,'precio_list.html',context)
    
#class contactoView(View):
#    def get(self, request, pk , *args, **kwargs):
#        post=get_object_or_404(Post,pk=pk)
#        return render(request,'contactanos.html')
