from web.models import Usuario, Inmueble,Region, Comuna,Tipo_usuario,Tipo_inmueble, Perfil
from django.contrib.auth.models import User

def obtener_inmuebles():
    inmuebles = Inmueble.objects.all()#obtenemos una lista de todos los inmueble creados
    for inmueble in inmuebles:
        print(inmueble)
    

def crear_inmueble(id_tipo_inmueble,id_usuario,id_comuna,
    id_region,nombre_inmueble,direccion,descripcion,m2_construidos,
    m2_totales,cant_de_estac,cant_de_hab,cant_de_banos,precio_mensual_de_arriendo,estado):
    #primero obtenemos los datos para crear el inmueble
    user = User.objects.get(id =id_usuario)
    tipo_inmueble = Tipo_inmueble.objects.get(id =id_tipo_inmueble)
    comuna = Comuna.objects.get(id =id_comuna)
    region = Region.objects.get(id =id_region)

    inmueble = Inmueble(
        id_tipo_inmueble =tipo_inmueble,
        id_usuario = user,
        id_comuna = comuna,
        id_region = region,
        nombre_inmueble = nombre_inmueble,
        direccion = direccion,
        descripcion = descripcion,
        m2_construidos = m2_construidos, 
        m2_totales = m2_totales,
        cant_de_estac =cant_de_estac,
        cant_de_hab = cant_de_hab,
        cant_de_banos =  cant_de_banos,
        precio_mensual_de_arriendo = precio_mensual_de_arriendo,
        estado = estado, 
    )

    inmueble.save()
    return inmueble
    

def actualizar_inmueble(id_inmueble,nombre_inmueble,m2_construido,numero_banos,numero_hab,direccion,estado):
    inmueble = Inmueble.objects.get(id=id_inmueble) #obtener el id del inmueble
    #campos que puedo modificar
    inmueble.nombre_inmueble = nombre_inmueble
    inmueble.m2_construido = m2_construido
    inmueble.numero_banos = numero_banos
    inmueble.numero_hab = numero_hab
    inmueble.direccion = direccion
    estado =estado

    inmueble.save()
    return inmueble

    

def borrar_inmueble(id_inmueble):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    inmueble.delete()
    return obtener_inmuebles()



def obtener_inmuebles_por_comuna(comuna):
    select = f"""
            SELECT web_inmueble.id, web_inmueble.nombre_inmueble, web_inmueble.descripcion, web_comuna.nombre_comuna 
            FROM web_inmueble 
            INNER JOIN web_comuna 
            ON web_inmueble.id_comuna_id = web_comuna.id 
            WHERE web_comuna.nombre_comuna like '{comuna}';
            """
    query = Inmueble.objects.raw(select)
    archivo1=open("inmuebles_por_comuna.txt","a",encoding='utf-8')
    for i in query:
        archivo1.write(f" Inmueble: {i.nombre_inmueble}")
        archivo1.write("\n")
        archivo1.write(f" Descripcion: {i.descripcion}")
        archivo1.write("\n")
        archivo1.write(f" Comuna: {i.nombre_comuna}" )
        archivo1.write("\n")
    archivo1.close()

def obtener_inmuebles_por_region(region):
    select = f"""
            SELECT web_inmueble.id, web_inmueble.nombre_inmueble, web_inmueble.descripcion, web_region.nombre_region 
            FROM web_inmueble 
            INNER JOIN web_region 
            ON web_inmueble.id_region_id = web_region.id 
            WHERE web_region.nombre_region like '{region}';
            """
    query = Inmueble.objects.raw(select)
    archivo1=open("inmuebles_por_region.txt","a",encoding='utf-8')
    for i in query:
        archivo1.write(f" Inmueble: {i.nombre_inmueble}")
        archivo1.write("\n")
        archivo1.write(f" Descripcion: {i.descripcion}")
        archivo1.write("\n")
        archivo1.write(f" Region: {i.nombre_region}" )
        archivo1.write("\n")
    archivo1.close()