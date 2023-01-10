from django.contrib.gis.db import models

from django.contrib.auth.models import User

# creamos el modelo cada clase es una tabla y el nombre de la clase es el nombre de la tabla cada 
#atributo es una columna de la tabla. Creamos tambien indices para acelerar las consultas y el ___str___ es un metodo con el que 
#al immprimir el objeto imprimimos lo que devuelve el metodo
class Post(models.Model):
    local=models.IntegerField(primary_key=True)
    barrio=models.CharField(max_length=250)
    nombre=models.CharField(max_length=250)
    descripcion=models.CharField(max_length=250)
    direccion=models.CharField(max_length=250)
    geometry=models.PointField(srid=25830)
    index_together = [
    ["nombre"],
    ]
    def __str__(self):
        return str(self.local)+', '+self.nombre+', '+self.direccion
    def strlon(self):
        list=[str(self.geometry[0]),str(self.geometry[1])]

        return list


class Productos(models.Model):
    productos=models.CharField(max_length=15,primary_key=True)
    def __str__(self):
        return str(self.productos)
#creamos una clase con unique_together es para que no se repita dos veces el mismo registro.
class precio(models.Model):
    local=models.ForeignKey(to=Post, on_delete=models.CASCADE)
    precio=models.FloatField()
    user=models.ForeignKey(to=User, on_delete=models.CASCADE)
    dia=models.DateField()
    productos=models.ForeignKey(to=Productos, on_delete=models.CASCADE)
    unique_together = [['local', 'user','dia','productos']]
    index_together = [
    ["local", "dia",'productos'],["local",'productos'],
]


    
