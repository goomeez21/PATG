from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
#clase con solo el metodo get que no envia context para que nos muestre el home 
from django.conf import settings
from django.core.mail import send_mail
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request,'home.html',context)

class inicioView(View):
    def get(self, request, *args, **kwargs):
        context={

        }
        return render(request,'inicio.html',context)

class contactanosView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form': form}
        return render(request,'contactanos.html',context)
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form=ContactForm(request.POST)
            
            
            if form.is_valid():
                email = form.cleaned_data.get('email')
                subject = form.cleaned_data.get('subject')
                message = form.cleaned_data.get('message')
                
                send_mail(
                subject,
                message+' recibido de:'+email,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER,email],
                fail_silently=False
                )
                return redirect('home')
        
        form = ContactForm()
        context = {'form': form}
        return render(request,'contactanos.html',context)
