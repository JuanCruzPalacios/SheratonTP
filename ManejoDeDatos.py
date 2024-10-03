# Funciones requeridas : 

# Crear usuario 

# Crear notificacion

# Leer notificacion

# Eliminar/Agregar stock  
# Mostrar stock


import json
from datetime import datetime

def LeerJson(archivo):
    #Lee un archivo JSON y devuelve su contenido como un diccionario.
    try:
        with open("jsons/" + archivo, 'r', encoding='utf-8') as f:
            contenido = json.load(f)
            if contenido is None: 
                contenido = {}
        return contenido
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo {archivo}. Asegúrate de que tenga un formato JSON válido.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

def ActualizarJson(archivo, datos):
    """Actualiza un archivo JSON, borrando su contenido y escribiendo nuevos datos."""
    try:
        with open("jsons/" + archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)
        print(f"Archivo {archivo} actualizado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al actualizar el archivo: {e}")

def ExisteUsuario(Usuario):  

    usuarios = LeerJson("Usuario.json") 

    try:
        usuarios[Usuario] != None
        print("El usuario existe.")
        return True
    except:
        print("El usuario no existe.")
        return False

def VerificarContraseña(Usuario , contraseña): 

    usuarios = LeerJson("Usuario.json")


    try:
        usuarios[Usuario] != None
        print("El usuario existe.")
        if usuarios[Usuario]["Password"] == contraseña:
            print("La contraseña es correcta.")
        else:
            print("La contraseña es incorrecta.")
            return False

        return True

    except:
        print("El usuario no existe.")
        return False
    
def AgregarNotificacion(texto):
   
    contenido_actual = LeerJson("Notificaciones.json")
    
    nueva_clave = str(len(contenido_actual))  

    fecha_enviada = datetime.now().strftime("%d/%m/%Y")

    nueva_notificacion = {
        "Archivada": 0,
        "Fijada": 0,
        "Texto": texto,
        "FechaEnviada": fecha_enviada
    }

    contenido_actual[nueva_clave] = nueva_notificacion

    ActualizarJson("Notificaciones.json", contenido_actual)

def VerNotificacion(numero_de_notificacion):
    numero_de_notificacion = str(numero_de_notificacion) 
    Notificaciones = LeerJson("Notificaciones.json")
    try:
        return Notificaciones[numero_de_notificacion]["Archivada"] , Notificaciones[numero_de_notificacion]["Fijada"] , Notificaciones[numero_de_notificacion]["Texto"] , Notificaciones[numero_de_notificacion]["FechaEnviada"]
    except: 
        print("No existe ninguna notificacion con ese numero.")
        return False

def CrearActualizarUsuario(Usuario, Correo , Tipo , Nombre , Apellido , Contraseña , DNI , NumeroTelefono , CodigoPostal , IdContrataciones , IdHabitacion):


    #Agrega una nueva notificación al archivo JSON.


    
    contenido_actual = LeerJson("Usuario.json")

    try: 
        nueva_clave = contenido_actual[Usuario]["NumeroDeCliente"]
    except:
        nueva_clave = str(len(contenido_actual)) 

    nuevo_usuario = {
        "Correo" : Correo , 
        "Tipo" : Tipo,  
        "Nombre" : Nombre ,
        "Apellido" : Apellido , 
        "Password" : Contraseña , 
        "DNI" : DNI , 
        "NumeroTelefono" : NumeroTelefono , 
        "NumeroDeCliente": nueva_clave , 
        "CodigoPostal" : CodigoPostal ,
        "IdContrataciones": IdContrataciones, 
        "IdHabitacion" : IdHabitacion
    }

    contenido_actual[Usuario] = nuevo_usuario


    ActualizarJson("Usuario.json", contenido_actual)

def VerStock(): 
    Stock = LeerJson("Stock.json")
    lista_stock = []
    for clave  in Stock: 
        print (clave)
        lista_stock.append([clave , Stock[clave]["Cantidad"]])
        
    return lista_stock

def AgregarEliminarStock (nombre_stock , cantidad) : 
    Stock = LeerJson("Stock.json")
    try: 
        cantidad_actual = Stock[nombre_stock]["Cantidad"] 
        Stock[nombre_stock]["Cantidad"] = int(cantidad_actual) + int(cantidad) 
        ActualizarJson("Stock.json" , Stock)
        print (nombre_stock , "sumo " , cantidad , " de stock.")
        return True
    except:
        print ("Hubo un error al agregar o eliminar el stock, verifique que el stock ingresado exista.")
        return False

def InformacionHabitacion (numero_de_habitacion):
    habitaciones = LeerJson("habitaciones.json")
    try:
        return habitaciones[str(numero_de_habitacion)]
    except: 
        print("Esa habitacion no existe.")
        return None

def NotificarIngresoEgreso(id_estacionamiento):
    ahora = datetime.now()
    estacionamiento = LeerJson("Estacionamiento.json")
    if estacionamiento[id_estacionamiento]["Ocupado"] == 0:
        estacionamiento[id_estacionamiento]["Ocupado"] = 1
        estacionamiento[id_estacionamiento]["UltimoIngreso"] = [str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year), str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)]
    else:
        estacionamiento[id_estacionamiento]["Ocupado"] = 0
        estacionamiento[id_estacionamiento]["UltimoEgreso"] = [str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year), str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)]
    ActualizarJson("Estacionamiento.json", estacionamiento )

NotificarIngresoEgreso("-1")

def Filtros(huespedes, precio_min, precio_max):
    filtro = LeerJson("habitaciones.json")
    if precio_min
    

