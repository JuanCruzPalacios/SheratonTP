# Funciones requeridas : 

# Crear usuario 

# Crear notificacion

# Leer notificacion

# Eliminar/Agregar stock  
# Mostrar stock


import json
from datetime import datetime

def leer_json(archivo):
    """Lee un archivo JSON y devuelve su contenido como un diccionario."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
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

def actualizar_json(archivo, datos):
    """Actualiza un archivo JSON, borrando su contenido y escribiendo nuevos datos."""
    try:
        # Escribir el nuevo contenido en el archivo
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)
        print(f"Archivo {archivo} actualizado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al actualizar el archivo: {e}")

def ExisteUsuario(correo):  
    usuarios = leer_json("Usuario.json") 
    try:
        usuarios[correo] != None
        print("El usuario existe.")
        return True
    except:
        print("El usuario no existe.")
        return False

def VerificarContraseña(correo , contraseña): 
    usuarios = leer_json("Usuario.json")
    try:
        usuarios[correo] != None
        print("El usuario existe.")
        if usuarios[correo]["Contraseña"] == contraseña:
            print("La contraseña es correcta.")
        else:
            print("La contraseña es incorrecta.")
            return False

        return True

    except:
        print("El usuario no existe.")
        return False
    
def agregar_notificacion(texto):
    #Agrega una nueva notificación al archivo JSON.
    contenido_actual = leer_json("Notificaciones.json")
    
    # Generar una nueva clave para la notificación
    nueva_clave = str(len(contenido_actual))  # Usa la longitud actual como nueva clave

    # Obtener la fecha actual en formato dd/mm/yyyy
    fecha_enviada = datetime.now().strftime("%d/%m/%Y")

    # Crear la nueva notificación
    nueva_notificacion = {
        "Archivada": 0,
        "Fijada": 0,
        "Texto": texto,
        "FechaEnviada": fecha_enviada
    }

    # Agregar la nueva notificación al contenido
    contenido_actual[nueva_clave] = nueva_notificacion
    
    # Actualizar el archivo con el nuevo contenido
    actualizar_json("Notificaciones.json", contenido_actual)

def ver_notificacion(numero_de_notificacion):
    numero_de_notificacion = str(numero_de_notificacion) 
    Notificaciones = leer_json("Notificaciones.json")
    try:
        return Notificaciones[numero_de_notificacion]["Archivada"] , Notificaciones[numero_de_notificacion]["Fijada"] , Notificaciones[numero_de_notificacion]["Texto"] , Notificaciones[numero_de_notificacion]["FechaEnviada"]
    except: 
        print("No existe ninguna notificacion con ese numero.")
        return False




