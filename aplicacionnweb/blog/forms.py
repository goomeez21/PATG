from django import forms

from .models import Post

from .models import precio
from .models import Productos
#creamos los froms y es el metodo que llamamos en clean_local de este modo podemos enviar errores a las paginas iniciales
class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('local',
    'barrio',
    'nombre',
    'descripcion',
    'direccion',
    'geometry')

    
class precioCreateForm(forms.Form):
    local=forms.CharField(max_length=250)
    precio=forms.FloatField()
    productos = forms.ModelChoiceField(queryset=Productos.objects)

    def clean_local(self):
        """
        validacion del form local 

        """
        localfiltro=self.data['local']
        localfiltro=localfiltro.split(",")[0]
        localfiltro=Post.objects.filter(local=localfiltro)[:]
        if len(localfiltro)!=1:
            #envia error si cumple con la condicion
            raise forms.ValidationError('el nombre del local no existe seleccione uno que exista')
        return localfiltro[0]


