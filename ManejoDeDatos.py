# Funciones requeridas : 

import json
from datetime import datetime

def VerStock(): 
    Stock = LeerJson("Stock.json")
    lista_stock = []
    for clave  in Stock: 
        print (clave)
        lista_stock.append([clave , Stock[clave]["Cantidad"]])
        
    return lista_stock

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

def VerUsuario(usuario): 
    usuario_json = LeerJson("Usuario.json")
    return usuario_json[usuario]

def TieneServicio(usuario):
    contr = []
    n = 0
    usuarios_json = LeerJson("Usuario.json")
    contrataciones = usuarios_json[usuario]["Contrataciones"]
    try: 
        for i in range (0, len(contrataciones)):
            if contrataciones[i][0] == "GYM":
                contr.append([True , contrataciones[i][1]])
                n += 1
            
        if n == 0:
                contr.append([False])
            
        n = 0

        for i in range (0, len(contrataciones)):
            if contrataciones[i][0] == "SPA":
                contr.append([True , contrataciones[i][1]])
                n += 1
            
        if n == 0:
            contr.append([False])
            
        n = 0
        
        for i in range (0, len(contrataciones)):
            if contrataciones[i][0] == "PISCINA":
                contr.append([True , contrataciones[i][1]])
                n += 1
            
        if n == 0:
            contr.append([False])
            
        n = 0

    except:
        contr.append([False])
    
    return contr

def ExisteUsuario(Usuario):  

    usuarios = LeerJson("Usuario.json") 

    try:
        usuarios[Usuario] != None
        print("El usuario existe.")
        return True
    except:
        print("El usuario no existe.")
        return False

def VerFechaFinal(id_habitacion):
    try:
        habitaciones_data = LeerJson("habitaciones.json")
        for habitacion in habitaciones_data: 
            if habitaciones_data[habitacion]["ID"] == id_habitacion:
                habitacion_el = habitacion
                pass
        return(habitaciones_data[habitacion_el]["Fechas"][1])
    except:
        return None

def VerRolUsuario(usuario):
    contenido = LeerJson("Usuario.json")
    return contenido[usuario]["Tipo"]

def TieneHabitacion(usuario): 
    try:
        usuarios_json = LeerJson("Usuario.json")
        Estacionamiento = usuarios_json[usuario]["IdHabitacion"] 
        if len(Estacionamiento) >= 1: 
            return True , Estacionamiento
        else:
            return False , False
    except:
        print("El usuario no existe o hubo un error al hacer la operacion")
        return False , False

def CambiarEstadoAmenitie(id):
    contenido = LeerJson("Contrataciones.json")
    contenido2 = LeerJson("Usuario.json")
    contenido[id]["Estado"] = "Finalizado"
    contenido2[contenido[id]["Usuario"]]["Contrataciones"] = ""
    ActualizarJson("Contrataciones.json", contenido)
    ActualizarJson("Usuario.json", contenido2)

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

def VerNumeroHabitacion(cliente):

    contenido = LeerJson("Usuario.json")
    if contenido[cliente]["IdHabitacion"] == []:
        return False
    else:
        return contenido[cliente]["IdHabitacion"]

def TieneEstacionamiento(usuario): 
    try:
        usuarios_json = LeerJson("Usuario.json")
        Estacionamiento = usuarios_json[usuario]["IdEstacionamiento"] 
        if len(Estacionamiento) >= 1: 
            return True , Estacionamiento
        else:
            return False , False
    except:
        print("El usuario no existe o hubo un error al hacer la operacion")
        return False , False

def ActualizarJson(archivo, datos):
    """Actualiza un archivo JSON, borrando su contenido y escribiendo nuevos datos."""
    try:
        with open("jsons/" + archivo, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4)
        print(f"Archivo {archivo} actualizado correctamente.")
    except Exception as e:
        print(f"Ocurrió un error al actualizar el archivo: {e}")

def VerNumeroEstacionamiento(cliente):
    contenido = LeerJson("Usuario.json")
    return contenido[cliente]["IdEstacionamiento"]

def VerNotificacion(numero_de_notificacion):
    numero_de_notificacion = str(numero_de_notificacion) 
    Notificaciones = LeerJson("Notificaciones.json")
    try:
        return Notificaciones[numero_de_notificacion]["Archivada"] , Notificaciones[numero_de_notificacion]["Fijada"] , Notificaciones[numero_de_notificacion]["Texto"] , Notificaciones[numero_de_notificacion]["FechaEnviada"]
    except: 
        print("No existe ninguna notificacion con ese numero.")
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

def NotificarIngresoEgreso(id_estacionamiento):
    ahora = datetime.now()
    id_estacionamiento = str(id_estacionamiento)
    estacionamiento = LeerJson("Estacionamiento.json")
    if estacionamiento[id_estacionamiento]["EstadoActual"] == "Fuera":
        estacionamiento[id_estacionamiento]["EstadoActual"] = "Adentro"
        if len(estacionamiento[id_estacionamiento]["UltimoIngreso"]) < 5:
            estacionamiento[id_estacionamiento]["UltimoIngreso"].append([str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year), str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)])
        else:
            estacionamiento[id_estacionamiento]["UltimoIngreso"].pop(0)
            estacionamiento[id_estacionamiento]["UltimoIngreso"].append([str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year), str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)])
    else:
        estacionamiento[id_estacionamiento]["EstadoActual"] = "Fuera"
        if len(estacionamiento[id_estacionamiento]["UltimoEgreso"]) < 5:
            estacionamiento[id_estacionamiento]["UltimoEgreso"].append ([str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year), str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)])
        else:
            estacionamiento[id_estacionamiento]["UltimoEgreso"].pop(0)
            estacionamiento[id_estacionamiento]["UltimoEgreso"].append([str(ahora.day) + "/" + str(ahora.month) + "/" + str(ahora.year), str(ahora.hour) + ":" + str(ahora.minute) + ":" + str(ahora.second)])

    ActualizarJson("Estacionamiento.json", estacionamiento )

def Filtros(huespedes, precio_min, precio_max):
    filtro = LeerJson("habitaciones.json")
    habitacioneslist = ["suite_balcon","habitacion_triple","habitacion_doble","habitacion_lujo","habitacion_cuadruple","suite_rio","habitacion_individual","suite_jacuzzi","suite_estandar"]
    habitaciones_ocupado = []
    habitaciones_precio = []
    resultado_ocupado = []
    resultado_precio = []
    resultado_final = []
    if str(huespedes) != "" and str(precio_max) != "" and str(precio_min) != "":
        try:
            for habitacion in filtro: 
                if filtro[habitacion]["Ocupada"] == "No" :
                    resultado_ocupado.append(filtro[habitacion]["ID"])
                    habitaciones_ocupado.append(habitacion)
            for habitacion in habitaciones_ocupado:
                if int(filtro[habitacion]["Precio"]) >= int(precio_min) and int(filtro[habitacion]["Precio"]) <= int(precio_max) : 
                    resultado_precio.append(filtro[habitacion]["ID"])
                    habitaciones_precio.append(habitacion)
            for habitacion in habitaciones_precio:
                if int(filtro[habitacion]["RangoHuespedes"]) == int(huespedes): 
                    resultado_final.append(filtro[habitacion]["ID"])
            return resultado_final
        except ValueError:
            """"""
    
   
        try:
            for habitacion in filtro: 
                if filtro[habitacion]["Ocupada"] == "No" :
                    resultado_ocupado.append(filtro[habitacion]["ID"])
                    habitaciones_ocupado.append(habitacion)
            for habitacion in habitaciones_ocupado:
                if int(filtro[habitacion]["Precio"]) <= int(precio_max) : 
                    resultado_precio.append(filtro[habitacion]["ID"])
                    habitaciones_precio.append(habitacion)
            for habitacion in habitaciones_precio:
                if int(filtro[habitacion]["RangoHuespedes"]) == int(huespedes): 
                    resultado_final.append(filtro[habitacion]["ID"])
            return resultado_final
        except ValueError:
            """"""

    if str(huespedes) == "" and str(precio_max) != "" and str(precio_min) != "":
        try:
            for habitacion in filtro: 
                if filtro[habitacion]["Ocupada"] == "No" :
                    resultado_ocupado.append(filtro[habitacion]["ID"])
                    habitaciones_ocupado.append(filtro[habitacion]["ID"])
            for habitacion in habitacioneslist:
                if filtro[habitacion]["ID"] in habitaciones_ocupado:
                    if int(filtro[habitacion]["Precio"]) >= int(precio_min) and int(filtro[habitacion]["Precio"]) <= int(precio_max): 
                        resultado_precio.append(filtro[habitacion]["ID"])
                        habitaciones_precio.append(filtro[habitacion]["ID"])
            return habitaciones_precio
        except ValueError:
            """"""
    
def InformacionHabitacion (nombre_de_habitacion):
    habitaciones = LeerJson("habitaciones.json")
    try:
        return habitaciones[nombre_de_habitacion]
    except: 
        print("Esa habitacion no existe.")
        return None

def CancelarReservaEstacionamiento(usuario , id):
    id = str(id)
    data_usuario = LeerJson("Usuario.json")
    data_parking = LeerJson("Estacionamiento.json")
    try:
        parking = data_usuario[usuario]["IdEstacionamiento"]
        if id in parking: 
            data_parking[id]["Ocupado"] = 0
            data_parking[id]["Ocupante"] = "Nadie"
            parking.remove(id)
            data_usuario[usuario]["IdEstacionamiento"] = parking
            ActualizarJson("Usuario.json" , data_usuario)
            ActualizarJson("Estacionamiento.json" , data_parking)
            print("Reserva de estacionamiento cancelada con exito.")
        else:
            print("El usuario no posee ese estacionamiento.")
    except: 
        print("El usuario o el estacionamiento ingresado no existe.")

def CambiarEstadoHabitacion(id_habitacion):
    habitacion_data = LeerJson("habitaciones.json")
    id_habitacion = int(id_habitacion)
    try:
        for habitacion in habitacion_data: 
                if habitacion_data[habitacion]["ID"] == id_habitacion:
                    nombre_de_habitacion = habitacion
                    pass
        if habitacion_data[nombre_de_habitacion]["Estado"] == "Ninguno":
            habitacion_data[nombre_de_habitacion]["Estado"] = "No molestar"
        else:
            habitacion_data[nombre_de_habitacion]["Estado"] = "Ninguno"
    
        ActualizarJson("habitaciones.json" , habitacion_data)
    except:
        print ("Error en la habitacion")

def FijarDesfijarNotificaciones (id_notificacion):
    contenido = LeerJson("Notificaciones.json")
    if contenido[id_notificacion]["Fijada"] == 0:
        contenido[id_notificacion]["Fijada"] = 1
    else:
        contenido[id_notificacion]["Fijada"] = 0
    ActualizarJson("Notificaciones.json", contenido)

def VencimientoEstacionamiento(id_estacionamiento):
    contenido = LeerJson("Estacionamiento.json")
    return(contenido[id_estacionamiento]["Vencimiento"])

def AgregarEliminarStock (nombre_stock , cantidad) : 
    Stock = LeerJson("Stock.json")
    try: 
        cantidad_actual = Stock[nombre_stock]["Cantidad"] 
        Stock[nombre_stock]["Cantidad"] = int(cantidad_actual) + int(cantidad) 
        ActualizarJson("Stock.json" , Stock)
        print (nombre_stock , "añadio" , cantidad , " de stock.")
        return True
    except:
        print ("Hubo un error al agregar o eliminar el stock, verifique que el stock ingresado exista.")
        return False

def ContratarAmenities(usuario,amenitie,fecha,precio):
    contenido = LeerJson("Contrataciones.json")
    contenido2 = LeerJson("Usuario.json")
    nueva_clave = str(len(contenido))
    contenido[nueva_clave]["ServiciosContratados"] = amenitie
    contenido[nueva_clave]["FechaContratada"] = fecha
    contenido[nueva_clave]["Estado"] = "No vencido"
    contenido[nueva_clave]["Precio"] = precio
    contenido[nueva_clave]["Usuario"] = usuario
    contenido2[usuario]["Contrataciones"] = amenitie
    ActualizarJson("Contrataciones.json", contenido)
    ActualizarJson("Usuario.json", contenido2)

def CancelarReservaHabitaciones(usuario,id_habitacion):
    usuario_data = LeerJson("Usuario.json")
    habitaciones_data = LeerJson("habitaciones.json")
    try: 
        for habitacion in habitaciones_data: 
            if habitaciones_data[habitacion]["ID"] == id_habitacion:
                nombre_habitacion = habitacion
                pass
        usuario_data[usuario]["IdHabitacion"].remove(id_habitacion)
        habitaciones_data[nombre_habitacion]["IdClienteOcupante"] = ""
        habitaciones_data[nombre_habitacion]["Ocupada"] = "No"
        habitaciones_data[nombre_habitacion]["Fechas"] = [""]
        habitaciones_data[nombre_habitacion]["ServiciosIncluidos"] = [""]
        habitaciones_data[nombre_habitacion]["EstadoActual"] = [""]
        ActualizarJson("Usuario.json", usuario_data)
        ActualizarJson("Habitaciones.json", habitaciones_data)
    except: 
        print("Error al cancelar la reserva de habitacion")

def ArchivarDesarchivarNotificaciones (id_notificacion):
    contenido = LeerJson("Notificaciones.json")
    if contenido[id_notificacion]["Archivada"] == 0:
        contenido[id_notificacion]["Archivada"] = 1
    else:
        contenido[id_notificacion]["Archivada"] = 0
    ActualizarJson("Notificaciones.json", contenido)

def MarcarReservacionHabitacion(usuario,habitacion,fecha_inicio, fecha_final):
    contenido = LeerJson("Usuario.json")
    contenido2 = LeerJson("habitacion.json")
    contenido[usuario]["IdHabitacion"].append(contenido2[habitacion]["ID"])
    contenido2[habitacion]["Ocupada"] = "Si"
    contenido2[habitacion]["IdClienteOcupante"] = contenido[usuario]["NumeroDeCliente"]
    contenido2[habitacion]["Fechas"] = [[fecha_inicio],[fecha_final]]
    ActualizarJson("habitaciones.json",contenido2)
    ActualizarJson("Usuario.json", contenido)

def ReservarEvento(precio,cliente,salon,asistentes,hora,dia,cantidad_personal,mail,especificaciones):
    contenido = LeerJson("ContratacionEventos")
    nueva_clave = str(len(contenido))
    contenido[nueva_clave]["IdSalon"] = salon
    contenido[nueva_clave]["FechaContratada"] = dia
    contenido[nueva_clave]["Hora"] = hora
    contenido[nueva_clave]["Estado"] = "No realizado"
    contenido[nueva_clave]["Mail"] = mail
    contenido[nueva_clave]["Especificaciones"] = especificaciones
    contenido[nueva_clave]["Precio"] = precio
    contenido[nueva_clave]["Personal"] = cantidad_personal
    contenido[nueva_clave]["Asistentes"] = asistentes
    contenido[nueva_clave]["Usuario"] = cliente
    ActualizarJson("ContratacionEventos.json", contenido)

def CrearActualizarUsuario(Usuario, Correo , Tipo , Nombre , Apellido , Contraseña , DNI , NumeroTelefono , CodigoPostal , IdContrataciones , IdHabitacion):    
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

def CancelarReservaEstacionamiento(usuario , id):
    id = str(id)
    data_usuario = LeerJson("Usuario.json")
    data_parking = LeerJson("Estacionamiento.json")
    try:
        parking = data_usuario[usuario]["IdEstacionamiento"]
        if id in parking: 
            data_parking[id]["Ocupado"] = 0
            data_parking[id]["Ocupante"] = "Nadie"
            data_parking[id]["EstadoActual"] = "Afuera"
            data_parking[id]["UltimoIngreso"] = []
            data_parking[id]["UltimoEgreso"] = []
            parking.remove(id)
            data_usuario[usuario]["IdEstacionamiento"] = parking
            ActualizarJson("Usuario.json" , data_usuario)
            ActualizarJson("Estacionamiento.json" , data_parking)
            print("Reserva de estacionamiento cancelada con exito.")
        else:
            print("El usuario no posee ese estacionamiento.")
    except: 
        print("El usuario o el estacionamiento ingresado no existe.")

def diferencia_dias(fecha1_str, fecha2_str):
    fecha1 = datetime.strptime(fecha1_str, '%d/%m/%Y')
    fecha2 = datetime.strptime(fecha2_str, '%d/%m/%Y')
    
    diferencia = abs((fecha2 - fecha1).days)
    return int(diferencia)
  
def CalcularPrecioHabitacion(habitacion, dia_inicio, dia_final):
    contenido = LeerJson("Habitaciones.json")
    precio = contenido[habitacion]["Precio"]
    return precio*diferencia_dias(dia_inicio,dia_final)

def CalcularPrecioAmenities(dia_inicio,dia_final,cantidad_amenities):
    return ((50*cantidad_amenities)*diferencia_dias(dia_inicio,dia_final))

def CalcularPrecioEstacionamiento(dia_final):
    dia_inicio = datetime.now()
    return 4*diferencia_dias(dia_inicio,dia_final)

def ReservarEstacionamiento(usuario , dia_final):
    contenido = LeerJson("Estacionamiento.json")
    data_usuario = LeerJson("Usuario.json")
    parking = data_usuario[usuario]["IdEstacionamiento"]

    pase = False
    for i in contenido: 
        if contenido[i]["Ocupado"] == 0:
            contenido[i]["Ocupado"] = 1 
            contenido[i]["Ocupante"] = usuario 
            contenido[i]["Vencimiento"] = dia_final
            pase = True
            parking.append(i)
            data_usuario[usuario]["IdEstacionamiento"] = parking
            print("Se reservo un estacionamiento existente de forma exitosa.")
            ActualizarJson("Estacionamiento.json" , contenido)
            ActualizarJson("Usuario.json" , data_usuario)
            return True
            break
    if not pase :
        print("No hay estacionamiento disponible.") 
        return False

def ChequearDatosUsuario(usuario,Nombre, dia1, dia2, direccion, telefono, mail, dni, codigo_postal):
    contenido = LeerJson("Usuario.json")
    chequeadormaximo = []
    
    if contenido[usuario]["Nombre"] == "":
        contenido[usuario]["Nombre"] = Nombre
    elif Nombre != contenido[usuario]["Nombre"]:
         return False , "El nombre del usuario es incorrecto"
    else:
        chequeadormaximo.append(1)
    
    if contenido[usuario]["Direccion"] == "":
        contenido[usuario]["Direccion"] = direccion
    elif direccion != contenido[usuario]["Direccion"]:
         return False , "La direccion del usuario es incorrecto"
    else:
        chequeadormaximo.append(1)
    
    
    if contenido[usuario]["Correo"] == "":
        contenido[usuario]["Correo"] = mail    
    elif mail != contenido[usuario]["Correo"]:
         return False , "El correo del usuario es incorrecto"
    else:
        chequeadormaximo.append(1)
    
    if contenido[usuario]["DNI"] == "":
        contenido[usuario]["DNI"] = dni 
    elif dni != contenido[usuario]["DNI"]:
         return False , "El dni ingresado es incorrecto"
    else:
        chequeadormaximo.append(1)
     
    if contenido[usuario]["CodigoPostal"] == "":
        contenido[usuario]["CodigoPostal"] = codigo_postal 
    elif codigo_postal != contenido[usuario]["CodigoPostal"]:
         return False , "El codigo postal ingresado es incorrecto"
    else:
        chequeadormaximo.append(1)
     
    if contenido[usuario]["NumeroTelefono"] == "":
        contenido[usuario]["NumeroTelefono"] = telefono
        
    elif direccion != contenido[usuario]["NumeroTelefono"]:
         return False , "El numero ingresado es incorrecto"
    else:
        chequeadormaximo.append(1)
     
    try: 
        if diferencia_dias(dia1,dia2) >= 1:
            chequeadormaximo.append(1)
        else:
            return False, "El periodo ingresado es invalido"
    except:
        return False, "El formato de dias esta mal enviado"

    if chequeadormaximo == [1,1,1,1,1,1,1]:
        return True
                
        
def ChequearDatosReservaEventos(usuario,mail, hora1, hora2 , asistentes , personal , fecha):
    contenido = LeerJson("Usuario.json")
    hora1_str = hora1  
    hora2_str = hora2  

    try:
        

        hora1 = datetime.strptime(hora1_str, "%H:%M")
        hora2 = datetime.strptime(hora2_str, "%H:%M")
    
    except:
        
        return False

    if hora2 > hora1:
        pass
    else:
        
        return False

    try:
        if asistentes != "":
            int(asistentes)     
        else:
            return False
    except: 
        
        return False

    try:
        if personal != "":
            int(personal)     
        else:
            return False
    except: 
        
        return False
    
    
    try:
        fecha_actual = datetime.now()
        fecha_ingresada = datetime.strptime(fecha, "%d/%m/%Y")

        if fecha_ingresada < fecha_actual:
            
            return False

    except:
        
        return False



    if contenido[usuario]["Correo"] == "":
        contenido[usuario]["Correo"] = mail    
    elif mail != contenido[usuario]["Correo"]:
        return False , "El correo del usuario es incorrecto"

    

    return True
     
def VerRegistrosEstacionamiento(id_estacionamiento):
    id_estacionamiento = str(id_estacionamiento)
    contenido = LeerJson("Estacionamiento.json")
    return contenido[id_estacionamiento]["UltimoIngreso"], contenido[id_estacionamiento]["UltimoEgreso"]

print(ChequearDatosUsuario("pepe","Pepe",))