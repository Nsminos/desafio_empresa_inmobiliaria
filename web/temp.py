from .models import Inmueble, Comuna


query = "SELECT * FROM web_inmueble"

inmuebles = Inmueble.objects.raw(query)

archi = open('comuna.txt', "a")
todas = Comuna.objects.all()
for c in todas:
    archi.write(c.nombre_comuna)
    archi.write('\n')
archi.close()