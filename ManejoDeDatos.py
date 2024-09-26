# Funciones requeridas : 

import json

def leer_json(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = json.load(f)
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
    

    


