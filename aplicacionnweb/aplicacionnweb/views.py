from django.views.generic import View
from django.shortcuts import render

#clase con solo el metodo get que no envia context para que nos muestre el home 

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request,'home.html',context)

        