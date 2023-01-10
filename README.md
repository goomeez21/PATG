# PATG
trabajo para patg. 
Para poder ejecutar este codigo correctamente deberemos tener descargado python , gdal y generar dos variables de entorno la de gdal y la de python. 
En python nos deberemos descargar django.
Despues de hacer las migraciones en la base de datos deberemos ejecutar un codigo python para rellenar la tabla de los restaurantes, ese codigo estara en la 
carpeta carga de datos y el proyecto en la carpeta aplicacionweb. En esa carpeta contiene todo lo necesario para ejecutar el codigo.
para ejecutar el codigo en django se necesitara usar el comando "python manage.py runserver" o en su defecto "py manage.py runserver",
el codigo de carga de datos contiene un notebook de jupyter para cargar los datos.
En todo el proyecto se utiliza la base de datos postgres por lo tanto si se va a utilizar otra base ded datos deberemos cambiar algunos lineas de la carga de datos y en la configuracion del proyecto.
tambien se utiliza un geoserver en localhost.


