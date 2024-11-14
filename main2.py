from ManejoDeDatos import *
import pygame



pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Sheraton")
pygame.display.set_icon(pygame.image.load("imagenes/logo.png"))
running = True





fondo_iniciar_sesion = pygame.image.load("imagenes/iniciar_sesion.jpg")
fondo_registrarse = pygame.image.load("imagenes/registrarse.jpg")
fondo_estacionamiento = pygame.image.load("imagenes/estacionamiento.jpg")
fondo_registros = pygame.image.load("imagenes/registros.jpg")
fondo_habitacion = pygame.image.load("imagenes/habitacion.jpg")
fondo_pagar = pygame.image.load("imagenes/reserva_de_habitacion.jpg")
fondo_pagar_con_mercado = pygame.image.load("imagenes/pagar_con_mercado.jpg")
fondo_pagar_con_tarjeta = pygame.image.load("imagenes/pagar_con_tarjeta.jpg")
fondo_estacionamiento_final = pygame.image.load("imagenes/estacionamiento_final.jpg")


fondo_menu_amenities = pygame.image.load("imagenes/reserva_de_amenities.jpg")
fondo_menu_salones = pygame.image.load("imagenes/reserva_de_salon.jpg")
fondo_datos_usuario = pygame.image.load("imagenes/datos_usuario.jpg")
fondo_menu_mantenimiento = pygame.image.load("imagenes/menu_mantenimiento.jpg")

fondo_mantenimiento_stock = pygame.image.load("imagenes/stock_mantenimiento.jpg")
fondo_mantenimiento_notificaciones = pygame.image.load("imagenes/notificaciones_mantenimiento.jpg")
fondo_mantenimiento_notificaciones_archivadas = pygame.image.load("imagenes/mantenimiento_notificaciones_archivadas.jpg")

fondo_menu_recepcionista = pygame.image.load("imagenes/menu_recepcionista.jpg")
fondo_recepcionista_notificar = pygame.image.load("imagenes/recepcionista_notificar.jpg")
fondo_recepcinista_eventos = pygame.image.load("imagenes/recepcionista_eventos.jpg")
fondo_recepcinista_limpieza = pygame.image.load("imagenes/recepcionista_limpieza.jpg")

barra_arriba = pygame.image.load("imagenes/barra_arriba.jpg")

imagen_usuario = pygame.image.load("imagenes/usuario.png")
imagen_filtro = pygame.image.load("imagenes/NICOLAS.png")
alter_usuario = False


suite_balcon = pygame.image.load("imagenes/habitaciones_sheraton/1.jpg")
habitacion_triple = pygame.image.load("imagenes/habitaciones_sheraton/2.jpg")
habitacion_doble = pygame.image.load("imagenes/habitaciones_sheraton/3.jpg")
habitacion_lujo = pygame.image.load("imagenes/habitaciones_sheraton/4.jpg")
habitacion_cuadruple = pygame.image.load("imagenes/habitaciones_sheraton/5.jpg")
suite_rio = pygame.image.load("imagenes/habitaciones_sheraton/6.jpg")
habitacion_individual = pygame.image.load("imagenes/habitaciones_sheraton/7.jpg")
suite_jacuzzi = pygame.image.load("imagenes/habitaciones_sheraton/8.jpg")
suite_estandar = pygame.image.load("imagenes/habitaciones_sheraton/9.jpg")

suite_balcon_sola = pygame.image.load("imagenes/habitaciones_solas/1.jpg")
habitacion_triple_sola = pygame.image.load("imagenes/habitaciones_solas/2.jpg")
habitacion_doble_sola = pygame.image.load("imagenes/habitaciones_solas/3.jpg")
habitacion_lujo_sola = pygame.image.load("imagenes/habitaciones_solas/4.jpg")
habitacion_cuadruple_sola = pygame.image.load("imagenes/habitaciones_solas/5.jpg")
suite_rio_sola = pygame.image.load("imagenes/habitaciones_solas/6.jpg")
habitacion_individual_sola = pygame.image.load("imagenes/habitaciones_solas/7.jpg")
suite_jacuzzi_sola = pygame.image.load("imagenes/habitaciones_solas/8.jpg")
suite_estandar_sola = pygame.image.load("imagenes/habitaciones_solas/9.jpg")

flecha_derecha = pygame.image.load("imagenes/flecha_adelante.png")
flecha_izquierda = pygame.transform.flip ( flecha_derecha , True , False ) 

notificiaciones_mantenimiento = pygame.image.load("imagenes/notificacion_mantenimiento.jpg")
fondo_gracias = pygame.image.load("imagenes/gracias.png")

suite_balcon_rect = [suite_balcon_sola.get_rect(topleft=(316, 150)), 0]
habitacion_triple_rect = [habitacion_triple_sola.get_rect(topleft=(632, 150)), 1]
habitacion_doble_rect = [habitacion_doble_sola.get_rect(topleft=(948, 150)), 2]
habitacion_lujo_rect = [habitacion_lujo_sola.get_rect(topleft=(316, 575)), 3]
habitacion_cuadruple_rect = [habitacion_cuadruple_sola.get_rect(topleft=(632, 575)), 4]
suite_rio_rect = [suite_rio_sola.get_rect(topleft=(948, 575)), 5]
habitacion_individual_rect = [habitacion_individual_sola.get_rect(topleft=(316, 1000)), 6]
suite_jacuzzi_rect = [suite_jacuzzi_sola.get_rect(topleft=(632, 1000)), 7]
suite_estandar_rect = [suite_estandar_sola.get_rect(topleft=(948, 1000)), 8]


rects = [suite_balcon_rect,habitacion_triple_rect,habitacion_doble_rect,
        habitacion_lujo_rect,habitacion_cuadruple_rect,suite_rio_rect,
        habitacion_individual_rect,suite_jacuzzi_rect,suite_estandar_rect]

habitaciones = [suite_balcon_sola, habitacion_triple_sola, habitacion_doble_sola,
                habitacion_lujo_sola, habitacion_cuadruple_sola, suite_rio_sola,
                habitacion_individual_sola, suite_jacuzzi_sola, suite_estandar_sola]

habitaciones_libres = Filtros("",0,99999999999)


posiciones_rects = []
temp =  []



fondo_actual = ["iniciar sesion", 0]
fondos = [
    fondo_iniciar_sesion,               # 0
    fondo_registrarse,                  # 1
    fondo_estacionamiento,              # 2
    fondo_habitacion,                   # 3
    fondo_pagar_con_mercado,            # 4
    fondo_pagar,                        # 5
    fondo_pagar_con_tarjeta,            # 6
    fondo_menu_amenities,               # 7
    fondo_menu_salones,                 # 8
    fondo_datos_usuario,                # 9
    fondo_menu_mantenimiento,           # 10
    fondo_mantenimiento_stock,          # 11
    fondo_mantenimiento_notificaciones, # 12
    fondo_mantenimiento_notificaciones_archivadas,  # 13
    fondo_menu_recepcionista,          # 14
    fondo_recepcionista_notificar,     # 15
    fondo_recepcinista_eventos,        # 16
    fondo_recepcinista_limpieza,       # 17
    suite_balcon,                      # 18
    habitacion_triple,                 # 19
    habitacion_doble,                  # 20
    habitacion_lujo,                   # 21
    habitacion_cuadruple,              # 22
    suite_rio,                         # 23
    habitacion_individual,             # 24
    suite_jacuzzi,                     # 25
    suite_estandar,                    # 26
    fondo_registros,                   # 27
    fondo_estacionamiento_final        # 28
]





fuente = pygame.font.Font("fuentes/Fuente_sheraton_mono.ttf", 31)


limite = 18

usuario = ""

texto1 = [(0,0), ""]
texto2 = [(0,0), ""]
texto3 = [(0,0), ""]
texto4 = [(0,0), ""]
texto5 = [(0,0), ""]
texto6 = [(0,0), ""]
texto7 = [(0,0), ""]
texto8 = [(0,0), ""]

gracias = False

barra = "|"

posicion = 150
alter_mouse = False

servicio_pagar = ""

alter_barra = True
ultimo_cambio_barra = pygame.time.get_ticks()

posicion_cuadrado_reserva = (-100 , -100 , 10 , 10)
posicion_cuadrado_salon = (-100 , -100 , 10 , 10)
posicion_cuadrado = (-100 , -100 , 10 , 10)
posicion_cuadrado_2 = (-100 , -100 , 10 , 10)
posicion_cuadrado_3 = (-100 , -100 , 10 , 10)

texto_seleccionado =  texto1 
texto_ingresado = ""

pagina = 0


def reset_textos(*textos):
    for texto in textos:
        texto[1] = ""
    




def cursor(mouse_pos,alter_usuario , gracias):
    

    if fondo_actual[0] == "iniciar sesion":


        if mouse_pos[0] <= 819 and mouse_pos[0] >= 459 and mouse_pos[1] <= 525 and mouse_pos[1] >= 488: #-----> Usuario
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        elif mouse_pos[0] <= 819 and mouse_pos[0] >= 459 and mouse_pos[1] <= 630 and mouse_pos[1] >= 593:#-----> Contraseña
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif mouse_pos[0] <= 871 and mouse_pos[0] >= 830 and mouse_pos[1] <= 669 and mouse_pos[1] >= 634:#-----> Siguiente
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_pos[0] <= 755 and mouse_pos[0] >= 522 and mouse_pos[1] <= 682 and mouse_pos[1] >= 669:#-----> Crear cuenta
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    elif fondo_actual[0] == "registrarse":


        if mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 505 and mouse_pos[1] >= 467: #-----> Usuario
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        elif mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 583 and mouse_pos[1] >= 544:#-----> Correo Electronico
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

        elif mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 661 and mouse_pos[1] >= 621: #-----> Contraseña
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif mouse_pos[0] <= 871 and mouse_pos[0] >= 832 and mouse_pos[1] <= 669 and mouse_pos[1] >= 633:#-----> Siguiente
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_pos[0] <= 748 and mouse_pos[0] >= 519 and mouse_pos[1] <= 682 and mouse_pos[1] >= 670:#-----> Iniciar Sesion
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    elif fondo_actual[0] == "menu habitaciones":

        if gracias == False:

            if mouse_pos[0] < 282 and mouse_pos[0] > 185 and mouse_pos[1] < 302 and mouse_pos[1] > 267:#personas        
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


            elif mouse_pos[0] < 142 and mouse_pos[0] > 46 and mouse_pos[1] < 450 and mouse_pos[1] > 415:#precio "desde"
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


            elif mouse_pos[0] < 284 and mouse_pos[0] > 185 and mouse_pos[1] < 450 and mouse_pos[1] > 416:#precio "hasta"
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


            elif mouse_pos[0] < 253 and mouse_pos[0] > 76 and mouse_pos[1] < 561 and mouse_pos[1] > 525:#buscar
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


            elif mouse_pos[0] < 253 and mouse_pos[0] > 76 and mouse_pos[1] < 512 and mouse_pos[1] > 475:#restablecer
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            

            for i in rects:
                if i[0].collidepoint(mouse_pos):
                    if not(mouse_pos[0] < 1280 and mouse_pos[0] > 0 and mouse_pos[1] < 125 and mouse_pos[1] > 0): #-----> habitaciones
                        if not(mouse_pos[0] < 1275 and mouse_pos[0] > 962 and mouse_pos[1] < 519 and mouse_pos[1] > 131) or alter_usuario == False:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        else:


            if mouse_pos[0] < 1130 and mouse_pos[0] > 898 and mouse_pos[1] < 664 and mouse_pos[1] > 598:#continuar
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



        
        
       
        
             


        



    elif fondo_actual[0] == "menu parking":

        if mouse_pos[0] < 757 and mouse_pos[0] > 522 and mouse_pos[1] < 656 and mouse_pos[1] > 579 and len(VerNumeroEstacionamiento(usuario)) == pagina:#Reservar        
                            
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 

        if mouse_pos[0] < 490 and mouse_pos[0] > 260 and mouse_pos[1] < 656 and mouse_pos[1] > 579: #ver registros        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
                

        elif mouse_pos[0] < 757 and mouse_pos[0] > 522 and mouse_pos[1] < 656 and mouse_pos[1] > 579:#notificar ingreso        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
                    

        elif mouse_pos[0] < 1018 and mouse_pos[0] > 784 and mouse_pos[1] < 656 and mouse_pos[1] > 579:#cancelar reserva de parking        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
        
        
       
            

        elif mouse_pos[0] < 1225 and mouse_pos[0] > 1130 and mouse_pos[1] < 462 and mouse_pos[1] > 306:#flecha derecha   
            if len(VerNumeroEstacionamiento(usuario)) > 0: 
                    if texto2[1] != (VerNumeroEstacionamiento(usuario).pop( 0 )) or pagina != (len(VerNumeroEstacionamiento(usuario))):
                        if pagina != (len(VerNumeroEstacionamiento(usuario))):
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 149 and mouse_pos[0] > 55 and mouse_pos[1] < 467 and mouse_pos[1] > 309:#flecha izquierda  
            if len(VerNumeroEstacionamiento(usuario)) > 0 and texto2[1] != VerNumeroEstacionamiento(usuario).pop( -1 ):    
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 



    elif fondo_actual[0] == "pagar servicio":

        if mouse_pos[0] < 690 and mouse_pos[0] > 255 and mouse_pos[1] < 300 and mouse_pos[1] > 250: #nombre       
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM) 
        

        elif mouse_pos[0] < 425 and mouse_pos[0] > 205 and mouse_pos[1] < 375 and mouse_pos[1] > 335: #dia inicio        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM) 


        elif mouse_pos[0] < 710 and mouse_pos[0] > 485 and mouse_pos[1] < 375 and mouse_pos[1] > 335: #dia fin      
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM) 
        

        elif mouse_pos[0] < 690 and mouse_pos[0] > 290 and mouse_pos[1] < 453 and mouse_pos[1] > 411: #direccion      
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM) 

        
        elif mouse_pos[0] < 690 and mouse_pos[0] > 273 and mouse_pos[1] < 520 and mouse_pos[1] > 480: #telefono     
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        

        elif mouse_pos[0] < 690 and mouse_pos[0] > 232 and mouse_pos[1] < 588 and mouse_pos[1] > 546: #mail   
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        

        elif mouse_pos[0] < 528 and mouse_pos[0] > 307 and mouse_pos[1] < 670 and mouse_pos[1] > 615: #pagar    
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 1107 and mouse_pos[0] > 896 and mouse_pos[1] < 223 and mouse_pos[1] > 178: #dni/cuit   
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        

        elif mouse_pos[0] < 1107 and mouse_pos[0] > 937 and mouse_pos[1] < 295 and mouse_pos[1] > 251: #codigo postal 
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        

        elif mouse_pos[0] < 925 and mouse_pos[0] > 870 and mouse_pos[1] < 460 and mouse_pos[1] > 405: #efectivo
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 1006 and mouse_pos[0] > 954 and mouse_pos[1] < 534 and mouse_pos[1] > 480: #mercado pago
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 1108 and mouse_pos[0] > 1058 and mouse_pos[1] < 460 and mouse_pos[1] > 307: #tarjeta
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 



    elif fondo_actual[0] == "ver datos":

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    elif fondo_actual[0] == "reservar eventos":


        if mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 298 and mouse_pos[1] > 252: #cantidad asistentes

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 332 and mouse_pos[0] > 214 and mouse_pos[1] < 382 and mouse_pos[1] > 340: #inicia el horario

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 382 and mouse_pos[1] > 340: #termina el horario

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 436 and mouse_pos[0] > 214 and mouse_pos[1] < 460 and mouse_pos[1] > 416: #dia del evento

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 524 and mouse_pos[1] > 474: #personal requerido

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 684 and mouse_pos[0] > 212 and mouse_pos[1] < 605 and mouse_pos[1] > 565: #mail

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 480 and mouse_pos[0] > 260 and mouse_pos[1] < 690 and mouse_pos[1] > 620: #reservar salon de eventos

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif  mouse_pos[0] < 1140 and mouse_pos[0] > 730 and mouse_pos[1] < 294 and mouse_pos[1] > 215: #especificaciones
            
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 920 and mouse_pos[0] > 865 and mouse_pos[1] < 468 and mouse_pos[1] > 410: #pago con efectivo
            
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif  mouse_pos[0] < 1105 and mouse_pos[0] > 1050 and mouse_pos[1] < 468 and mouse_pos[1] > 410: #pago con tarjeta
            
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif  mouse_pos[0] < 1005 and mouse_pos[0] > 950 and mouse_pos[1] < 540 and mouse_pos[1] > 484: #pago con mercado pago
            
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)



        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 



    elif fondo_actual[0] == "menu bedroom":

        if mouse_pos[0] < 481 and mouse_pos[0] > 250 and mouse_pos[1] < 655 and mouse_pos[1] > 576: #pedir limpieza

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 752 and mouse_pos[0] > 516 and mouse_pos[1] < 655 and mouse_pos[1] > 576: #no molestar

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 1018 and mouse_pos[0] > 785 and mouse_pos[1] < 655 and mouse_pos[1] > 576: #cancelar reserva

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    elif fondo_actual[0] == "menu amenities":

        if mouse_pos[0] < 455 and mouse_pos[0] > 400 and mouse_pos[1] < 342 and mouse_pos[1] > 290: #spa

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 740 and mouse_pos[0] > 688 and mouse_pos[1] < 345 and mouse_pos[1] > 290: #piscina

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 1005 and mouse_pos[0] > 948 and mouse_pos[1] < 345 and mouse_pos[1] > 290: #gimnasio

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 708 and mouse_pos[0] > 568 and mouse_pos[1] < 676 and mouse_pos[1] > 636: #reservar

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:

             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    elif fondo_actual[0] == "pagar mercado pago":

        if mouse_pos[0] < 842 and mouse_pos[0] > 437 and mouse_pos[1] < 647 and mouse_pos[1] > 243: #QR
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_pos[0] < 1127 and mouse_pos[0] > 907 and mouse_pos[1] < 662 and mouse_pos[1] > 599: #VOLVER
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)    

        else:
             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    
    
    elif fondo_actual[0] == "pagar tarjeta":

        if mouse_pos[0] < 1022 and mouse_pos[0] > 485 and mouse_pos[1] < 305 and mouse_pos[1] > 270: #Nombre del titular
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

        elif mouse_pos[0] < 1022 and mouse_pos[0] > 485 and mouse_pos[1] < 375 and mouse_pos[1] > 335: #Numero de tarjeta
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)    

        elif mouse_pos[0] < 1018 and mouse_pos[0] > 485 and mouse_pos[1] < 445 and mouse_pos[1] > 405: #Documento
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)  

        elif mouse_pos[0] < 737 and mouse_pos[0] > 485 and mouse_pos[1] < 515 and mouse_pos[1] > 475: #Vencimiento
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)  

        elif mouse_pos[0] < 740 and mouse_pos[0] > 483 and mouse_pos[1] < 584 and mouse_pos[1] > 542: #Codigo de seguridad
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)  

        elif mouse_pos[0] < 1128 and mouse_pos[0] > 906 and mouse_pos[1] < 665 and mouse_pos[1] > 605: #Pagar
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  

        else:
             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    elif fondo_actual[0] == "menu mantenimiento":
        if mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 342 and mouse_pos[1] > 285: #notificaciones
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 440 and mouse_pos[1] > 378: #ver stcok
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 535 and mouse_pos[1] > 470: #salir
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    elif fondo_actual[0] == "mantenimiento notificaciones":

        if mouse_pos[0] < 400 and mouse_pos[0] > 170 and mouse_pos[1] < 630 and mouse_pos[1] > 575: #volver
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        
        elif len(VerNotificacion()) > 0 and mouse_pos[0] < 1105 and mouse_pos[0] > 1066 and mouse_pos[1] < 192 and mouse_pos[1] > 155: #boton 1
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        elif len(VerNotificacion()) > 1 and mouse_pos[0] < 1105 and mouse_pos[0] > 1066 and mouse_pos[1] < 338 and mouse_pos[1] > 296: #boton 2
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        elif len(VerNotificacion()) > 2 and mouse_pos[0] < 1105 and mouse_pos[0] > 1066 and mouse_pos[1] < 480 and mouse_pos[1] > 442: #boton 3
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        elif len(VerNotificacion()) > 3 and mouse_pos[0] < 1105 and mouse_pos[0] > 1066 and mouse_pos[1] < 626 and mouse_pos[1] > 586: #boton 4
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            


        

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
       
        

    elif fondo_actual[0] == "menu recepcionista":

        if mouse_pos[0] < 378 and mouse_pos[0] > 145 and mouse_pos[1] < 294 and mouse_pos[1] > 229: # notificar

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        elif mouse_pos[0] < 378 and mouse_pos[0] > 145 and mouse_pos[1] < 373 and mouse_pos[1] > 312: # ver eventos

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 378 and mouse_pos[0] > 145 and mouse_pos[1] < 455 and mouse_pos[1] > 398: # enviar limpieza

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 378 and mouse_pos[0] > 145 and mouse_pos[1] < 548 and mouse_pos[1] > 482: # salir

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    elif fondo_actual[0] == "recepcionista notificar":

        
        if mouse_pos[0] < 1250 and mouse_pos[0] > 1189 and mouse_pos[1] < 702 and mouse_pos[1] > 645: # salir

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            
        

        elif mouse_pos[0] < 514 and mouse_pos[0] > 264 and mouse_pos[1] < 578 and mouse_pos[1] > 515: # enviar notificacion
        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 630 and mouse_pos[0] > 148 and mouse_pos[1] < 318 and mouse_pos[1] > 264: # objeto a reponer

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        

        elif mouse_pos[0] < 334 and mouse_pos[0] > 120 and mouse_pos[1] < 425 and mouse_pos[1] > 370: # Cantidad

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        

        elif mouse_pos[0] < 657 and mouse_pos[0] > 450 and mouse_pos[1] < 425 and mouse_pos[1] > 374: # Habitacion

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            

        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    
    elif fondo_actual[0] == "recepcionista eventos":



        if mouse_pos[0] < 314 and mouse_pos[0] > 78 and mouse_pos[1] < 664 and mouse_pos[1] > 606: # volver

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    elif fondo_actual[0] == "recepcionista limpieza":



        if mouse_pos[0] < 1253 and mouse_pos[0] > 1194 and mouse_pos[1] < 698 and mouse_pos[1] > 647: # salir

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 500 and mouse_pos[0] > 332 and mouse_pos[1] < 660 and mouse_pos[1] > 612: # enviar limpieza

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)    
        
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        
    elif fondo_actual[0] == "mantenimiento stock":
        if mouse_pos[0] < 465 and mouse_pos[0] > 330 and mouse_pos[1] < 665 and mouse_pos[1] > 625: #añadir
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        elif mouse_pos[0] < 1245 and mouse_pos[0] > 1185 and mouse_pos[1] < 695 and mouse_pos[1] > 640: #volver
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    elif fondo_actual[0] == "registros":

        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    


    if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"]:
            if mouse_pos[0] < 1008 and mouse_pos[0] > 785 and mouse_pos[1] < 666 and mouse_pos[1] > 605:#reservar       
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)    
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)




    if fondo_actual[0] in ["pagar mercado pago","pagar tarjeta","registros","habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar", "datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "reservar eventos", "ver datos", "pagar servicio"]:



            if mouse_pos[0] < 410 and mouse_pos[0] > 290 and mouse_pos[1] < 100 and mouse_pos[1] > 15: #Home
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


            elif mouse_pos[0] < 560 and mouse_pos[0] > 435 and mouse_pos[1] < 100 and mouse_pos[1] > 15:#parking
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


            elif mouse_pos[0] < 710 and mouse_pos[0] > 590 and mouse_pos[1] < 100 and mouse_pos[1] > 15:#bedroom
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


            elif mouse_pos[0] < 860 and mouse_pos[0] > 745 and mouse_pos[1] < 100 and mouse_pos[1] > 15:#services
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


            elif mouse_pos[0] < 1220 and mouse_pos[0] > 1140 and mouse_pos[1] < 90 and mouse_pos[1] > 18:#boton usuario
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
  



    if alter_usuario:

        if mouse_pos[0] < 1245 and mouse_pos[0] > 992 and mouse_pos[1] < 310 and mouse_pos[1] > 261: #ver datos 
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 1245 and mouse_pos[0] > 992 and mouse_pos[1] < 395 and mouse_pos[1] > 350: #reservar eventos
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 1205  and mouse_pos[0] > 1030 and mouse_pos[1] < 478 and mouse_pos[1] > 431: #salir
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    




def chequeo_contraseña(conteraseña):
    if len(conteraseña) >= 8:
        if  any( caracter in conteraseña for caracter in ["@", "#", "$", "*", "%", "&", "/", "!", "?", "-", "_"] ):
            if any( caracter in conteraseña for caracter in ["1","2","3","4","5","6","7","8","9","0"] ):
                return "aprobado"
            else:   
                return "    La contraseña debe tener numeros."
        else:
            return "La contraseña debe tener caracteres especiales."    
    else:
        return "La contraseña debe tener al menos 8 caracteres."





while running:


    for event in pygame.event.get():


        mouse_pos = pygame.mouse.get_pos()



        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
                     
            if event.key == pygame.K_BACKSPACE:

                
                if fondo_actual[0] == "reservar eventos" and texto_seleccionado == texto8 and texto_ingresado == "":
                    

                    texto_seleccionado = texto7
                    texto_aux = texto7[1]

                    for i in range (0 , (len(texto_aux) - 1)) :

                        texto_ingresado += texto_aux[i]




                # Al presionar Retroceso, eliminar el último carácter del texto
                texto_ingresado = texto_ingresado[:-1]
                barra = barra[:-1] 
                barra = barra[:-1] + "|"


                


                
                
    
            elif event.key == pygame.K_ESCAPE:
                #aleja la barra de escritura fuera de la pantalla
                texto_seleccionado = [(-100,-100),""]
                
            elif event.key == 13 :#enter
                if fondo_actual[0] == "iniciar sesion":
                        if ExisteUsuario(texto1[1]):

                            if VerificarContraseña(texto1[1],texto2[1]):


                                if VerRolUsuario(texto1[1]).lower() == "cliente":

                                    usuario = texto1[1]
                                    fondo_actual[0] = "menu habitaciones"
                                    fondo_actual[1] = 6
                                    texto_ingresado = ""
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1,texto2,texto3,texto4)
                                

                                elif VerRolUsuario(texto1[1]).lower() == "mantenimiento":

                                    usuario = texto1[1]
                                    fondo_actual[0] = "menu mantenimiento"
                                    fondo_actual[1] = 10
                                    texto_ingresado = ""
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1,texto2,texto3,texto4)


                                elif VerRolUsuario(texto1[1]).lower() == "recepcionista":

                                    usuario = texto1[1]
                                    fondo_actual[0] = "menu recepcionista"
                                    fondo_actual[1] = 14
                                    texto_ingresado = ""
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1,texto2,texto3,texto4)
                                

                                datos_usuario = VerUsuario(usuario)

                                    



                            else:
                                texto3[1] = "Contraseña incorrecta."
                        else:
                            texto3[1] = "Usuario no encontrado."
                elif fondo_actual[0] == "registrarse": 
                    if len(texto1[1]) > 3 and len(texto2[1]) > 3 :
                        if "@" in texto2[1]:
                            if not(ExisteUsuario(texto1[1])) :

                                if chequeo_contraseña(texto3[1]) == "aprobado":

                                    usuario = texto1[1]
                                    CrearActualizarUsuario(texto1[1] , texto2[1] , texto3[1] , " " , " " , " " ," " )
                                    fondo_actual[0] = "menu habitaciones"
                                    fondo_actual[1] = 6
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1,texto2,texto3,texto4)

                                else:
                                    texto4[1] = chequeo_contraseña(texto3[1])    
                            else:
                                texto4[1] = "         El usuario ingresado ya existe."
                        else:
                            texto4[1] = "            Falta @ en el mail."
                    else:
                        texto4[1] = "El usuario/mail ingresado es demasiado corto." 
                else:
                    texto_seleccionado[1] = ""
       
       
            else:                 
                
                if fondo_actual[0] == "reservar eventos" and texto_seleccionado == texto7:
                
                    if len(texto_ingresado) < limite - 1:    

                        if event.unicode .isprintable():
                            
                            texto_ingresado += event.unicode
                        
                    else:

                        texto_seleccionado[1] += "-"


                        texto_seleccionado = texto8
                        texto_ingresado = texto8[1]

                        if event.unicode .isprintable():
                            
                            texto_ingresado += event.unicode

                elif fondo_actual[0] == "pagar servicio" and (texto_seleccionado == texto2 or texto_seleccionado == texto3):

                    if len(texto_ingresado) == 1 or len(texto_ingresado) == 4:


                        if event.unicode .isprintable():
                                
                            texto_ingresado += event.unicode
                            texto_ingresado += "/"
                    
                    else:

                        if len(texto_ingresado) < limite:           
                        # Agregar caracteres al texto ingresado

                            if event.unicode .isprintable():
                                
                                texto_ingresado += event.unicode


                elif fondo_actual[0] == "reservar eventos" and ( texto_seleccionado == texto2 or texto_seleccionado == texto3 or texto_seleccionado == texto4):

                    if texto_seleccionado == texto2 or texto_seleccionado == texto3:


                        if len(texto_ingresado) == 1:


                            if event.unicode .isprintable():
                                    
                                texto_ingresado += event.unicode
                                texto_ingresado += ":"
                        
                        else:

                            if len(texto_ingresado) < limite:           
                            # Agregar caracteres al texto ingresado

                                if event.unicode .isprintable():
                                    
                                    texto_ingresado += event.unicode
                    
                    elif texto_seleccionado == texto4:


                        if len(texto_ingresado) == 1 or len(texto_ingresado) == 4:


                            if event.unicode .isprintable():
                                    
                                texto_ingresado += event.unicode
                                texto_ingresado += "/"
                        
                        else:

                            if len(texto_ingresado) < limite:           
                            # Agregar caracteres al texto ingresado

                                if event.unicode .isprintable():
                                    
                                    texto_ingresado += event.unicode

                elif fondo_actual[0] == "pagar tarjeta" and (texto_seleccionado ==  texto4):
                    
                        if len(texto_ingresado) == 1 :

                            if event.unicode .isprintable():      
                                texto_ingresado += event.unicode
                                texto_ingresado += "-"
                        else:
                            if len(texto_ingresado) < limite:           
                            # Agregar caracteres al texto ingresado

                                if event.unicode .isprintable():
                                    
                                    texto_ingresado += event.unicode







                else:

                    if len(texto_ingresado) < limite:           
                        # Agregar caracteres al texto ingresado

                        if event.unicode .isprintable():
                            
                            texto_ingresado += event.unicode
                
                
            

            texto_seleccionado[1] = texto_ingresado
            barra = texto_seleccionado[1] + "|" 
            
            
        




        if event.type == pygame.MOUSEBUTTONUP :        
        
            if event.button == 1:
                alter_mouse = False




        if event.type == pygame.MOUSEBUTTONDOWN :

            if event.button == 4:  # Rueda hacia arriba   
                
                    if posicion <= 125:
                        posicion += 25


            elif event.button == 5:  # Rueda hacia abajo
                if len(habitaciones_libres) > 6:
                    if posicion >= -550:
                        posicion -= 25
                else:
                    if posicion >= -100:
                        posicion -= 25


            if event.button == 1:
                
                print(mouse_pos)   


                if fondo_actual[0] == "iniciar sesion" and alter_mouse == False:

                    alter_mouse = True

                    if mouse_pos[0] <= 819 and mouse_pos[0] >= 459 and mouse_pos[1] <= 525 and mouse_pos[1] >= 488: #-----> Usuario
                        texto_ingresado = texto1[1]
                        texto_seleccionado = texto1 #Usuario / iniciar sesion   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 18

                    
            
                    elif mouse_pos[0] <= 819 and mouse_pos[0] >= 459 and mouse_pos[1] <= 630 and mouse_pos[1] >= 593:#-----> Contraseña                    
                        texto_ingresado = texto2[1]
                        texto_seleccionado = texto2 #Contraseña / iniciar sesion
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()   
                        
                        limite = 18



                    elif mouse_pos[0] <= 871 and mouse_pos[0] >= 830 and mouse_pos[1] <= 669 and mouse_pos[1] >= 634:#-----> Siguiente
                        
                        print(VerRolUsuario(texto1[1]))
                        if ExisteUsuario(texto1[1]):

                            if VerificarContraseña(texto1[1],texto2[1]):


                                if VerRolUsuario(texto1[1]).lower() == "cliente":

                                    usuario = texto1[1]
                                    fondo_actual[0] = "menu habitaciones"
                                    fondo_actual[1] = 6
                                    texto_ingresado = ""
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1,texto2,texto3,texto4)
                                

                                elif VerRolUsuario(texto1[1]).lower() == "mantenimiento":

                                    usuario = texto1[1]
                                    fondo_actual[0] = "menu mantenimiento"
                                    fondo_actual[1] = 10
                                    texto_ingresado = ""
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1,texto2,texto3,texto4)


                                elif VerRolUsuario(texto1[1]).lower() == "recepcionista":

                                    usuario = texto1[1]
                                    fondo_actual[0] = "menu recepcionista"
                                    fondo_actual[1] = 14
                                    texto_ingresado = ""
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1,texto2,texto3,texto4)


                                datos_usuario = VerUsuario(usuario)



                                
                            else:
                                texto3[1] = "Contraseña incorrecta."
                        else:
                            texto3[1] = "Usuario no encontrado."





                    elif mouse_pos[0] <= 755 and mouse_pos[0] >= 522 and mouse_pos[1] <= 682 and mouse_pos[1] >= 669:#-----> Crear cuenta
                        fondo_actual[0] = "registrarse"
                        fondo_actual[1] = 1
                        texto_ingresado = ""
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                                      

    


                elif fondo_actual[0] == "registrarse" and alter_mouse == False:   
                    alter_mouse = True

                    if mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 505 and mouse_pos[1] >= 467: #-----> Usuario

                        texto_seleccionado = texto1 #usuario / registrarse
                        texto_ingresado = texto1[1]
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()   
                        limite = 18


                    elif mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 583 and mouse_pos[1] >= 544:#-----> Correo Electronico

                        texto_seleccionado = texto2 #mail / registrarse
                        texto_ingresado = texto2[1]
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()   
                        limite = 18


                    elif mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 661 and mouse_pos[1] >= 621: #-----> Contraseña
    
                        texto_seleccionado = texto3 #contraseña / registrarse
                        texto_ingresado = texto3[1]
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()   
                        limite = 18


                    elif mouse_pos[0] <= 871 and mouse_pos[0] >= 832 and mouse_pos[1] <= 669 and mouse_pos[1] >= 633:#-----> Siguiente
                
                        if len(texto1[1]) > 3 and len(texto2[1]) > 3 :
                            if "@" in texto2[1]:
                                if not(ExisteUsuario(texto1[1])) :

                                    if chequeo_contraseña(texto3[1]) == "aprobado":

                                        CrearActualizarUsuario(texto1[1] , texto2[1]  , texto3[1], " " , " " , " " , " " )
                                        usuario = texto1[1]
                                        fondo_actual[0] = "menu habitaciones"
                                        fondo_actual[1] = 6
                                        texto_ingresado = ""
                                        texto_seleccionado = [(-100,-100),""]
                                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                                        datos_usuario = VerUsuario(usuario)

                                        
                                        

                                    else:                       
                                        texto4[1] = chequeo_contraseña(texto3[1])    
                                else:
                                    texto4[1] = "El usuario ingresado ya existe."
                            else:

                                texto4[1] = "            Falta @ en el mail."

                        else:
                            texto4[1] = "El usuario/mail ingresado es demasiado corto."

                        

                          
                    elif mouse_pos[0] <= 748 and mouse_pos[0] >= 519 and mouse_pos[1] <= 682 and mouse_pos[1] >= 670:#-----> Iniciar Sesion
                        fondo_actual[0] = "iniciar sesion"
                        fondo_actual[1] = 0
                        texto_ingresado = ""
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                                       




                elif fondo_actual[0] == "menu habitaciones" and alter_mouse == False and gracias == False:
                    
                    

                    if mouse_pos[0] < 282 and mouse_pos[0] > 185 and mouse_pos[1] < 302 and mouse_pos[1] > 267:#personas        
                        texto_seleccionado = texto1
                        texto_ingresado = texto1[1]
                        barra = texto_ingresado + "|" 
                        ultimo_cambio_barra  = pygame.time.get_ticks()   
                        limite = 3
                        alter_mouse = True



                    elif mouse_pos[0] < 142 and mouse_pos[0] > 46 and mouse_pos[1] < 450 and mouse_pos[1] > 415:#precio "desde"
                        texto_seleccionado = texto2
                        texto_ingresado = texto2[1]
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()   
                        limite = 3
                        alter_mouse = True



                    elif mouse_pos[0] < 284 and mouse_pos[0] > 185 and mouse_pos[1] < 450 and mouse_pos[1] > 416:#precio "hasta"
                        texto_seleccionado = texto3
                        texto_ingresado = texto3[1]
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()   
                        limite = 3
                        alter_mouse = True



                    elif mouse_pos[0] < 253 and mouse_pos[0] > 76 and mouse_pos[1] < 561 and mouse_pos[1] > 525:#buscar
                        try:
                            habitaciones_libres = Filtros(texto1[1],texto2[1],texto3[1])
                        except:
                            print("Error al filtrar")
                        alter_mouse = True



                    elif mouse_pos[0] < 253 and mouse_pos[0] > 76 and mouse_pos[1] < 512 and mouse_pos[1] > 475:#restablecer
                        habitaciones_libres = Filtros("",0,999999999)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        print(texto1)
                        barra = texto_seleccionado[1] + "|"  
                        texto_ingresado = ""
                        print(barra)

                        ultimo_cambio_barra  = pygame.time.get_ticks()
                        alter_mouse = True



                    if not(mouse_pos[0] < 1280 and mouse_pos[0] > 0 and mouse_pos[1] < 125 and mouse_pos[1] > 0): #-----> habitaciones
                        if not(mouse_pos[0] < 1275 and mouse_pos[0] > 962 and mouse_pos[1] < 519 and mouse_pos[1] > 131) or alter_usuario == False:
                            

                            for i in rects:
                                if i[0].collidepoint(mouse_pos):
                                    alter_mouse = True
                                    fondo_actual[1] = i[1] + 18
                                    fondo_actual[0] = "habitacion balcon"
                                    texto_seleccionado = [(-100,-100),""]
                                    servicio_pagar = i[1]

                            




                elif fondo_actual[0] == "menu bedroom" and alter_mouse == False:

                    if mouse_pos[0] < 1225 and mouse_pos[0] > 1130 and mouse_pos[1] < 462 and mouse_pos[1] > 306:#flecha derecha   
                        if len(VerNumeroHabitacion(usuario)) > 1 and texto1[1] != str(VerNumeroHabitacion(usuario).pop( 0 )):
                            pagina += 1
                            alter_mouse = True


                    elif mouse_pos[0] < 149 and mouse_pos[0] > 55 and mouse_pos[1] < 467 and mouse_pos[1] > 309:#flecha izquierda  
                        if len(VerNumeroHabitacion(usuario)) > 1 and texto1[1] != str(VerNumeroHabitacion(usuario).pop( -1 )):    
                            pagina -= 1
                            alter_mouse = True

                        
                    if mouse_pos[0] < 481 and mouse_pos[0] > 250 and mouse_pos[1] < 655 and mouse_pos[1] > 576: #pedir limpieza

                        print("Limpieza pedida.")
                        alter_mouse = True
                    

                    elif mouse_pos[0] < 752 and mouse_pos[0] > 516 and mouse_pos[1] < 655 and mouse_pos[1] > 576: #no molestar
                        if TieneHabitacion(usuario)[0] != False:
                            CambiarEstadoHabitacion(VerNumeroHabitacion(usuario).pop( -1 - pagina ))
                        else: 
                            print("El usuario no tiene habitacion en la cual cambiar el estado.")
                        alter_mouse = True


                    elif mouse_pos[0] < 1018 and mouse_pos[0] > 785 and mouse_pos[1] < 655 and mouse_pos[1] > 576: #cancelar reserva
                        if TieneHabitacion(usuario)[0]:
                            CancelarReservaHabitaciones(usuario , VerNumeroHabitacion(usuario).pop( -1 - pagina ) )
                        else:
                            print("El usuario no tiene habitacion de la cual cancelar la reserva.")
                        alter_mouse = True
                    
                        

                        

                elif fondo_actual[0] == "pagar servicio" and alter_mouse == False:


                    if mouse_pos[0] < 690 and mouse_pos[0] > 255 and mouse_pos[1] < 300 and mouse_pos[1] > 250: #nombre        
                                    
                        texto_ingresado = texto1[1]
                        texto_seleccionado = texto1   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 22
                        alter_mouse = True
        

                    elif mouse_pos[0] < 425 and mouse_pos[0] > 205 and mouse_pos[1] < 375 and mouse_pos[1] > 335: #dia inicio        

                        texto2[1]  = ""    
                        texto_ingresado = ""
                        texto_seleccionado = texto2   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 10
                        alter_mouse = True
                        

                    elif mouse_pos[0] < 710 and mouse_pos[0] > 485 and mouse_pos[1] < 375 and mouse_pos[1] > 335: #dia fin       
                                    
                        texto3[1]  = ""
                        texto_ingresado = ""
                        texto_seleccionado = texto3
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 10 
                        alter_mouse = True
                    

                    elif mouse_pos[0] < 690 and mouse_pos[0] > 289 and mouse_pos[1] < 453 and mouse_pos[1] > 411: #direccion      
                                    
                        texto_ingresado = texto4[1]
                        texto_seleccionado = texto4  
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 20
                        alter_mouse = True

                    
                    elif mouse_pos[0] < 690 and mouse_pos[0] > 273 and mouse_pos[1] < 520 and mouse_pos[1] > 480: #telefono     
                                    
                        texto_ingresado = texto5[1]
                        texto_seleccionado = texto5   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 21
                        alter_mouse = True
                    

                    elif mouse_pos[0] < 690 and mouse_pos[0] > 232 and mouse_pos[1] < 588 and mouse_pos[1] > 546: #mail   
                                    
                        texto_ingresado = texto6[1]
                        texto_seleccionado = texto6   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 23
                        alter_mouse = True
                                        

                    elif mouse_pos[0] < 1107 and mouse_pos[0] > 896 and mouse_pos[1] < 223 and mouse_pos[1] > 178: #dni/cuit   
                                    
                        texto_ingresado = texto7[1]
                        texto_seleccionado = texto7   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 11 
                        alter_mouse = True


                    elif mouse_pos[0] < 1107 and mouse_pos[0] > 937 and mouse_pos[1] < 295 and mouse_pos[1] > 251: #codigo postal 
                                    
                        texto_ingresado = texto8[1]
                        texto_seleccionado = texto8   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 6 
                        alter_mouse = True
                    

                    elif mouse_pos[0] < 925 and mouse_pos[0] > 870 and mouse_pos[1] < 460 and mouse_pos[1] > 405: #efectivo

                        alter_mouse = True
                        posicion_cuadrado_reserva = ( 877, 413, 41 , 41  )
                

                    elif mouse_pos[0] < 1006 and mouse_pos[0] > 954 and mouse_pos[1] < 534 and mouse_pos[1] > 480: #mercado pago
                                    
                        alter_mouse = True
                        posicion_cuadrado_reserva = ( 960 , 490 , 41 , 41 )


                    elif mouse_pos[0] < 1108 and mouse_pos[0] > 1058 and mouse_pos[1] < 460 and mouse_pos[1] > 307: #tarjeta

                        alter_mouse = True
                        posicion_cuadrado_reserva = ( 1062, 415, 41 , 41  ) 


                    elif mouse_pos[0] < 528 and mouse_pos[0] > 307 and mouse_pos[1] < 670 and mouse_pos[1] > 615: #pagar


                        if ChequearDatosUsuario(usuario,texto1[1],texto2[1], texto3[1], texto4[1], texto5[1], texto6[1], texto7[1], texto8[1]):
                            
                            
                            if servicio_pagar != "" and servicio_pagar != "Estacionamiento":
                                print("reservando habitacion")
                                if posicion_cuadrado_reserva == ( 877, 413, 41 , 41 ):      

                                    alter_mouse = True                         
                                    fondo_actual[0] = "menu habitaciones"
                                    gracias = True
                                    texto_seleccionado = [(-100,-100),""]
                                    MarcarReservacionHabitacion(usuario, servicio_pagar , texto2[1] , texto3[1])
                                    reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                                elif posicion_cuadrado_reserva == ( 960 , 490 , 41 , 41 ):
                                    alter_mouse = True
                                    fondo_actual[0] = "pagar mercado pago"
                                    fondo_actual[1] = 4
                                    texto_seleccionado = [(-100,-100),""]
                                    texto1[1] = "total: " + str(CalcularPrecioHabitacion(servicio_pagar, texto2[1],texto3[1]))
                                    

                                elif posicion_cuadrado_reserva == ( 1062, 415, 41 , 41  ):
                                    alter_mouse = True
                                    fondo_actual[0] = "pagar tarjeta"
                                    fondo_actual[1] = 6
                                    texto_seleccionado = [(-100,-100),""]
                                    texto6[1] = "total: " + str(CalcularPrecioHabitacion(servicio_pagar, texto2[1],texto3[1]))
                                    
                                    reset_textos(texto1, texto2, texto3, texto4, texto5, texto7, texto8) 

                            elif servicio_pagar == "Estacionamiento" :
                                print("reservando estacionamiento")
                                if posicion_cuadrado_reserva == ( 877, 413, 41 , 41 ):       
                                    alter_mouse = True                         
                                    fondo_actual[0] = "menu parking"
                                    ReservarEstacionamiento(usuario, texto3[1])
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                                elif posicion_cuadrado_reserva == ( 960 , 490 , 41 , 41 ):
                                    alter_mouse = True
                                    fondo_actual[0] = "pagar mercado pago"
                                    fondo_actual[1] = 4
                                    texto_seleccionado = [(-100,-100),""]
                                    texto1[1] = "total: " + str(CalcularPrecioEstacionamiento(texto2[1] , texto3[1]))
                                    servicio_pagar = "Estacionamiento"
                                        

                                elif posicion_cuadrado_reserva == ( 1062, 415, 41 , 41  ):
                                    alter_mouse = True
                                    fondo_actual[0] = "pagar tarjeta"
                                    fondo_actual[1] = 6
                                    texto_seleccionado = [(-100,-100),""]
                                    texto6[1] = "total: " + str(CalcularPrecioEstacionamiento(texto2[1],texto3[1]))
                                    servicio_pagar = "Estacionamiento"
                                    reset_textos(texto1, texto2, texto3, texto4, texto5, texto7, texto8) 

                            else:
                                print("reservando amenities")
                                if posicion_cuadrado_reserva == ( 877, 413, 41 , 41 ):       
                                    alter_mouse = True                         
                                    fondo_actual[0] = "menu habitaciones"
                                    gracias = True
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                                elif posicion_cuadrado_reserva == ( 960 , 490 , 41 , 41 ):
                                    alter_mouse = True
                                    fondo_actual[0] = "pagar mercado pago"
                                    fondo_actual[1] = 4
                                    texto_seleccionado = [(-100,-100),""]
                                    servicio_pagar = 0
                                    print(posicion_cuadrado_3)
                                    if posicion_cuadrado[1] == 298:
                                        servicio_pagar += 1
                                    if posicion_cuadrado_2[1] == 298:
                                        servicio_pagar += 1
                                    if posicion_cuadrado_3[1] == 298:
                                        servicio_pagar += 1
                                    texto1[1] = "total: " + str(CalcularPrecioAmenities(texto2[1],texto3[1],servicio_pagar))
                                    servicio_pagar = ""
                                        

                                elif posicion_cuadrado_reserva == ( 1062, 415, 41 , 41  ): 
                                    alter_mouse = True
                                    fondo_actual[0] = "pagar tarjeta"
                                    fondo_actual[1] = 6
                                    texto_seleccionado = [(-100,-100),""]
                                    servicio_pagar = 0 
                                    if posicion_cuadrado[1] == 298:
                                        servicio_pagar += 1
                                    if posicion_cuadrado_2[1] == 298:
                                        servicio_pagar += 1
                                    if posicion_cuadrado_3[1] == 298:
                                        servicio_pagar += 1
                                    texto6[1] = "total: " + str(CalcularPrecioAmenities(texto2[1],texto3[1],servicio_pagar))
                                    servicio_pagar = ""
                                    reset_textos(texto1, texto2, texto3, texto4, texto5, texto7, texto8)





                elif fondo_actual[0] == "menu amenities" and alter_mouse == False:

                   
                    if mouse_pos[0] < 455 and mouse_pos[0] > 400 and mouse_pos[1] < 342 and mouse_pos[1] > 290 and posicion_cuadrado != (409,298, 41,41): #spa aparece
                        alter_mouse = True
                        posicion_cuadrado = (409,298, 41,41)
                    
                    elif mouse_pos[0] < 455 and mouse_pos[0] > 400 and mouse_pos[1] < 342 and mouse_pos[1] > 290 and posicion_cuadrado == (409,298, 41,41): #spa desaparece
                        alter_mouse = True
                        posicion_cuadrado = (-100,-100,0,0)

                    elif mouse_pos[0] < 1005 and mouse_pos[0] > 948 and mouse_pos[1] < 345 and mouse_pos[1] > 290 and posicion_cuadrado_2 != (957,298, 41,41): #gimnasio aparece
                        alter_mouse = True
                        posicion_cuadrado_2 = (957,298, 41,41)

                    elif mouse_pos[0] < 1005 and mouse_pos[0] > 948 and mouse_pos[1] < 345 and mouse_pos[1] > 290 and posicion_cuadrado_2 == (957,298, 41,41): #gimnasio desaparece
                        alter_mouse = True
                        posicion_cuadrado_2 = (-100,-100,0,0)

                    elif mouse_pos[0] < 740 and mouse_pos[0] > 688 and mouse_pos[1] < 345 and mouse_pos[1] > 290 and posicion_cuadrado_3 !=  (695,298, 41,41): #pileta aparece
                        alter_mouse = True
                        posicion_cuadrado_3 = (695,298, 41,41)

                    elif  mouse_pos[0] < 740 and mouse_pos[0] > 688 and mouse_pos[1] < 345 and mouse_pos[1] > 290 and posicion_cuadrado_3 ==  (695,298, 41,41): #pileta desaparece
                        alter_mouse = True
                        posicion_cuadrado_3 = (-100,-100,0,0)
                   
                    elif mouse_pos[0] < 708 and mouse_pos[0] > 568 and mouse_pos[1] < 676 and mouse_pos[1] > 636: #reservar
                        if posicion_cuadrado == (409,298, 41,41)  or posicion_cuadrado_2 == (957,298, 41,41) or posicion_cuadrado_3 == (695,298, 41,41):
                            servicio_pagar = ""
                            fondo_actual[0] = "pagar servicio"
                            fondo_actual[1] = 5
                            
                        
                    
                    


                elif fondo_actual[0] == "reservar eventos" and alter_mouse == False:


                    

                    if mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 298 and mouse_pos[1] > 252: #Cantidad asistentes
                        alter_mouse = True            
                        texto_ingresado = texto1[1]
                        texto_seleccionado = texto1   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 3
        

                    elif  mouse_pos[0] < 332 and mouse_pos[0] > 214 and mouse_pos[1] < 382 and mouse_pos[1] > 340: #inicia el horario
                        alter_mouse = True
                        texto2[1]  = ""    
                        texto_ingresado = ""
                        texto_seleccionado = texto2   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 5
                        


                    elif  mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 382 and mouse_pos[1] > 340: #termina el horario 
                        alter_mouse = True           
                        texto3[1]  = ""
                        texto_ingresado = ""
                        texto_seleccionado = texto3
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 5
                    

                    elif  mouse_pos[0] < 436 and mouse_pos[0] > 214 and mouse_pos[1] < 460 and mouse_pos[1] > 416: #dia del evento   
                        alter_mouse = True         
                        texto4[1]  = ""
                        texto_ingresado = ""
                        texto_seleccionado = texto4  
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 10

                    
                    elif  mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 524 and mouse_pos[1] > 474: #personal requerido  
                        alter_mouse = True            
                        texto_ingresado = texto5[1]
                        texto_seleccionado = texto5   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 3 
                    

                    elif  mouse_pos[0] < 684 and mouse_pos[0] > 212 and mouse_pos[1] < 605 and mouse_pos[1] > 565: #mail   
                        alter_mouse = True           
                        texto_ingresado = texto6[1]
                        texto_seleccionado = texto6   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 24

                                        
                    elif  mouse_pos[0] < 480 and mouse_pos[0] > 260 and mouse_pos[1] < 690 and mouse_pos[1] > 620: #reservar salon de eventos 

                        alter_mouse = True
                        if ChequearDatosReservaEventos(usuario , texto6[1] , texto2[1] , texto3[1] , texto1[1] , texto5[1] , texto4[1]) == True:

                            if posicion_cuadrado_salon == ( 956, 494, 41 , 41  ):

                                fondo_actual[0] = "pagar mercado pago"
                                fondo_actual[1] = 4
                                texto_seleccionado = [(-100,-100),""]
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8)
                            
                            elif posicion_cuadrado_salon == ( 1058 , 421 , 41 , 41 ):

                                fondo_actual[0] = "pagar tarjeta"
                                fondo_actual[1] = 6
                                texto_seleccionado = [(-100,-100),""]
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8)


                    elif  mouse_pos[0] < 1140 and mouse_pos[0] > 730 and mouse_pos[1] < 408 and mouse_pos[1] > 215: #especificaciones

                        alter_mouse = True           
                        texto_ingresado = texto7[1]
                        texto_seleccionado = texto7   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 20
                    

                    
                    

                    elif  mouse_pos[0] < 920 and mouse_pos[0] > 865 and mouse_pos[1] < 468 and mouse_pos[1] > 410: #pago con efectivo
                                    
                        posicion_cuadrado_salon = ( 873, 421, 41 , 41  )
                        


                    elif  mouse_pos[0] < 1105 and mouse_pos[0] > 1050 and mouse_pos[1] < 468 and mouse_pos[1] > 410: #pago con tarjeta
                                    
                        
                        posicion_cuadrado_salon = ( 1058 , 421 , 41 , 41 )


                    elif  mouse_pos[0] < 1005 and mouse_pos[0] > 950 and mouse_pos[1] < 540 and mouse_pos[1] > 484: #pago con mercado pago


                        posicion_cuadrado_salon = ( 956, 494, 41 , 41  ) 





                elif fondo_actual[0] == "menu parking":

                    if len(VerNumeroEstacionamiento(usuario) ) != pagina:   

                        if mouse_pos[0] < 490 and mouse_pos[0] > 260 and mouse_pos[1] < 656 and mouse_pos[1] > 579 and alter_mouse == False: #ver registros        
                            
                            fondo_actual[0] = "registros"
                            fondo_actual[1] = 27
                            texto_seleccionado = [(-100,-100),""]
                            reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                            alter_mouse = True
                                    

                        elif mouse_pos[0] < 757 and mouse_pos[0] > 522 and mouse_pos[1] < 656 and mouse_pos[1] > 579 and alter_mouse == False:#notificar ingreso
                                        
                            NotificarIngresoEgreso(VerNumeroEstacionamiento(usuario).pop( -1 - pagina )) 
                            alter_mouse = True

                            
                                    

                        elif mouse_pos[0] < 1018 and mouse_pos[0] > 784 and mouse_pos[1] < 656 and mouse_pos[1] > 579 and alter_mouse == False:#cancelar reserva de parking                 
                            CancelarReservaEstacionamiento( usuario , VerNumeroEstacionamiento(usuario).pop( -1 - pagina ) )
                            alter_mouse = True
            
                       
                    else:            
                        if mouse_pos[0] < 757 and mouse_pos[0] > 522 and mouse_pos[1] < 656 and mouse_pos[1] > 579 and alter_mouse == False: #ReservarEstacionamiento(usuario)
                            print ("Reservar estacionamiento")
                            servicio_pagar = "Estacionamiento" 
                            reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                            fondo_actual[0] = "pagar servicio"
                            fondo_actual[1] = 5
                            alter_mouse = True


                    if mouse_pos[0] < 1225 and mouse_pos[0] > 1130 and mouse_pos[1] < 462 and mouse_pos[1] > 306 and alter_mouse == False:#flecha derecha   
                        if len(VerNumeroEstacionamiento(usuario)) > 0: 
                            if texto2[1] != (VerNumeroEstacionamiento(usuario).pop( 0 )) or pagina != (len(VerNumeroEstacionamiento(usuario))):
                                if pagina != (len(VerNumeroEstacionamiento(usuario))):
                                    pagina += 1
                                    alter_mouse = True


                    if mouse_pos[0] < 149 and mouse_pos[0] > 55 and mouse_pos[1] < 467 and mouse_pos[1] > 309 and alter_mouse == False:#flecha izquierda  
                        if len(VerNumeroEstacionamiento(usuario)) > 0 and texto2[1] != VerNumeroEstacionamiento(usuario).pop( -1 ):    
                            pagina -= 1
                            alter_mouse = True
                    

                
                elif fondo_actual[0] == "menu mantenimiento" and alter_mouse == False:
                    
                    if mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 342 and mouse_pos[1] > 285: #notificaciones

                        alter_mouse = True
                        fondo_actual[0] = "mantenimiento notificaciones"
                        fondo_actual[1] = 12
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                    

                    elif mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 440 and mouse_pos[1] > 378: #ver stcok

                        alter_mouse = True
                        fondo_actual[0] = "mantenimiento stock"
                        fondo_actual[1] = 11
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                    

                    elif mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 535 and mouse_pos[1] > 470: #salir

                        alter_mouse = True
                        fondo_actual[0] = "iniciar sesion"
                        fondo_actual[1] = 0
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                

                elif fondo_actual[0] == "mantenimiento notificaciones":

                    if mouse_pos[0] < 400 and mouse_pos[0] > 170 and mouse_pos[1] < 630 and mouse_pos[1] > 575: #volver

                        fondo_actual[0] = "menu mantenimiento"
                        fondo_actual[1] = 10
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                    

                    elif len(VerNotificacion()) > 0 and mouse_pos[0] < 1105 and mouse_pos[0] > 1066 and mouse_pos[1] < 192 and mouse_pos[1] > 155: #boton 1
                        ArchivarDesarchivarNotificaciones(VerNotificacion()[0][2])
                    
                    elif len(VerNotificacion()) > 1 and mouse_pos[0] < 1105 and mouse_pos[0] > 1066 and mouse_pos[1] < 338 and mouse_pos[1] > 296: #boton 2
                        ArchivarDesarchivarNotificaciones(VerNotificacion()[1][2])
                    
                    elif len(VerNotificacion()) > 2 and mouse_pos[0] < 1105 and mouse_pos[0] > 1066 and mouse_pos[1] < 480 and mouse_pos[1] > 442: #boton 3
                        ArchivarDesarchivarNotificaciones(VerNotificacion()[2][2])
                    
                    elif len(VerNotificacion()) > 3 and mouse_pos[0] < 1105 and mouse_pos[0] > 1066 and mouse_pos[1] < 626 and mouse_pos[1] > 586: #boton 4
                        ArchivarDesarchivarNotificaciones(VerNotificacion()[3][2])





                elif fondo_actual[0] == "mantenimiento stock":
                    if mouse_pos[0] < 1245 and mouse_pos[0] > 1185 and mouse_pos[1] < 695 and mouse_pos[1] > 640: #volver

                        fondo_actual[0] = "menu mantenimiento"
                        fondo_actual[1] = 10
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 


                elif fondo_actual[0] == "pagar mercado pago" and alter_mouse == False:

                    if mouse_pos[0] < 842 and mouse_pos[0] > 437 and mouse_pos[1] < 647 and mouse_pos[1] > 243: #QR
                        if servicio_pagar != "" and servicio_pagar != "Estacionamiento":

                            print ("Pago habitacion con mercado pago")
                            alter_mouse = True
                            fondo_actual[0] = "menu habitaciones"
                            gracias = True
                            texto_seleccionado = [(-100,-100),""]
                            MarcarReservacionHabitacion(usuario, servicio_pagar , texto2[1] , texto3[1])
                            habitaciones_libres = Filtros((""),0,9999999999)
                            reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                        elif servicio_pagar == "Estacionamiento": 

                            print ("Pago estacionamiento con mercado pago")
                            alter_mouse = True
                            fondo_actual[0] = "menu parking"
                            fondo_actual[1] = 2
                            ReservarEstacionamiento(usuario , texto3[1])
                            texto_seleccionado = [(-100,-100),""]
                            reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8)

                        else:

                            print("Pago un amenitie con mercado pago")
                            alter_mouse = True
                            fondo_actual[0] = "menu habitaciones"
                            gracias = True
                            texto_seleccionado = [(-100,-100),""]
                            

                            if posicion_cuadrado[1] == 298:
                                print("SPA reservado")
                                ContratarAmenities(usuario, "SPA", (texto2[1],texto3[1]),texto1[1])

                            if posicion_cuadrado_3[1] == 298:
                                print("Piscina reservado")
                                ContratarAmenities(usuario, "PISCINA", (texto2[1],texto3[1]),texto1[1])
                            
                            if posicion_cuadrado_2[1] == 298:
                                print("Gimnasio reservado")
                                ContratarAmenities(usuario, "GYM", (texto2[1],texto3[1]),texto1[1])

                            habitaciones_libres = Filtros((""),0,9999999999)
                            reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 


                    elif mouse_pos[0] < 1127 and mouse_pos[0] > 907 and mouse_pos[1] < 662 and mouse_pos[1] > 599: #VOLVER

                        alter_mouse = True
                        fondo_actual[0] = "pagar servicio"
                        fondo_actual[1] = 5
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
            


                elif fondo_actual[0] == "pagar tarjeta" and alter_mouse == False:



                    if mouse_pos[0] < 1022 and mouse_pos[0] > 485 and mouse_pos[1] < 305 and mouse_pos[1] > 270: #Nombre del titular
                        alter_mouse = True
                        texto_ingresado = texto1[1]
                        texto_seleccionado = texto1 
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 27

                    elif mouse_pos[0] < 1022 and mouse_pos[0] > 485 and mouse_pos[1] < 375 and mouse_pos[1] > 335: #Numero de tarjeta
                        alter_mouse = True
                        texto_ingresado = texto2[1]
                        texto_seleccionado = texto2   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 20 

                
                    elif mouse_pos[0] < 1018 and mouse_pos[0] > 485 and mouse_pos[1] < 445 and mouse_pos[1] > 405: #Documento
                        alter_mouse = True
                        texto_ingresado = texto3[1]
                        texto_seleccionado = texto3   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 8

                    
                    elif mouse_pos[0] < 737 and mouse_pos[0] > 485 and mouse_pos[1] < 515 and mouse_pos[1] > 475: #Vencimiento
                        alter_mouse = True
                        texto4[1] = ""
                        texto_ingresado = texto4[1]
                        texto_seleccionado = texto4  
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 8 

                    elif mouse_pos[0] < 740 and mouse_pos[0] > 483 and mouse_pos[1] < 584 and mouse_pos[1] > 542: #Codigo de seguridad
                        alter_mouse = True
                        texto_ingresado = texto5[1]
                        texto_seleccionado = texto5 
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 3 

                    elif mouse_pos[0] < 1128 and mouse_pos[0] > 906 and mouse_pos[1] < 665 and mouse_pos[1] > 605: #Pagar   
                        alter_mouse = True
                        print(ChequearDatosTarjeta (texto2[1],texto4[1],texto5[1]))
                        if ChequearDatosTarjeta (texto2[1],texto4[1],texto5[1])[0] :
                        
                            if servicio_pagar != "" and servicio_pagar != "Estacionamiento":

                                print ("Pago habitacion con tarjeta")
                                alter_mouse = True
                                fondo_actual[0] = "menu habitaciones"
                                gracias = True
                                texto_seleccionado = [(-100,-100),""]
                                MarcarReservacionHabitacion(usuario, servicio_pagar , texto2[1] , texto3[1])
                                habitaciones_libres = Filtros((""),0,9999999999)
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                            elif servicio_pagar == "Estacionamiento": 

                                print ("Pago estacionamiento con tarjeta")
                                alter_mouse = True
                                fondo_actual[0] = "menu parking"
                                fondo_actual[1] = 2
                                ReservarEstacionamiento(usuario , texto3[1])
                                texto_seleccionado = [(-100,-100),""]
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8)

                            else:

                                print("Pago un amenitie con tarjeta")
                                alter_mouse = True
                                fondo_actual[0] = "menu habitaciones"
                                gracias = True
                                texto_seleccionado = [(-100,-100),""]
                                

                                if posicion_cuadrado[1] == 298:
                                    print("SPA reservado")
                                    ContratarAmenities(usuario, "SPA", (texto2[1],texto3[1]),texto1[1])

                                if posicion_cuadrado_3[1] == 298:
                                    print("Piscina reservado")
                                    ContratarAmenities(usuario, "PISCINA", (texto2[1],texto3[1]),texto1[1])
                                
                                if posicion_cuadrado_2[1] == 298:
                                    print("Gimnasio reservado")
                                    ContratarAmenities(usuario, "GYM", (texto2[1],texto3[1]),texto1[1])

                                habitaciones_libres = Filtros((""),0,9999999999)
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 


                        

                elif fondo_actual[0] == "menu recepcionista":

                    if mouse_pos[0] < 378 and mouse_pos[0] > 145 and mouse_pos[1] < 294 and mouse_pos[1] > 229: # notificar
                        
                        fondo_actual[0] = "recepcionista notificar"
                        fondo_actual[1] = 15
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                    
                    elif mouse_pos[0] < 378 and mouse_pos[0] > 145 and mouse_pos[1] < 373 and mouse_pos[1] > 312: # ver eventos
                                             
                        fondo_actual[0] = "recepcionista eventos"
                        fondo_actual[1] = 16
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8)
                        
                    

                    elif mouse_pos[0] < 378 and mouse_pos[0] > 145 and mouse_pos[1] < 455 and mouse_pos[1] > 398: # enviar limpieza

                        fondo_actual[0] = "recepcionista limpieza"
                        fondo_actual[1] = 17
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                    

                    elif mouse_pos[0] < 378 and mouse_pos[0] > 145 and mouse_pos[1] < 548 and mouse_pos[1] > 482: # salir

                        fondo_actual[0] = "iniciar sesion"
                        fondo_actual[1] = 0
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 





                elif fondo_actual[0] == "recepcionista notificar":

        
                    if mouse_pos[0] < 1250 and mouse_pos[0] > 1189 and mouse_pos[1] < 702 and mouse_pos[1] > 645: # salir

                        fondo_actual[0] = "menu recepcionista"
                        fondo_actual[1] = 14
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                    

                    elif mouse_pos[0] < 514 and mouse_pos[0] > 264 and mouse_pos[1] < 578 and mouse_pos[1] > 515: # enviar notificacion
                    
                        
                        AgregarNotificacion(texto1[1] , texto2[1] , texto3[1])


                    elif mouse_pos[0] < 630 and mouse_pos[0] > 148 and mouse_pos[1] < 318 and mouse_pos[1] > 264: # objeto a reponer

                        alter_mouse = True           
                        texto_ingresado = texto1[1]
                        texto_seleccionado = texto1  
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 24
                    

                    elif mouse_pos[0] < 334 and mouse_pos[0] > 120 and mouse_pos[1] < 425 and mouse_pos[1] > 370: # Cantidad

                        alter_mouse = True           
                        texto_ingresado = texto2[1]
                        texto_seleccionado = texto2   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 3
                    

                    elif mouse_pos[0] < 657 and mouse_pos[0] > 450 and mouse_pos[1] < 425 and mouse_pos[1] > 374: # Habitacion

                        alter_mouse = True           
                        texto_ingresado = texto3[1]
                        texto_seleccionado = texto3  
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 2
                        
                    

                
                elif fondo_actual[0] == "recepcionista eventos":


                    if mouse_pos[0] < 314 and mouse_pos[0] > 78 and mouse_pos[1] < 664 and mouse_pos[1] > 606: # volver

                        fondo_actual[0] = "menu recepcionista"
                        fondo_actual[1] = 14
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 


                
                elif fondo_actual[0] == "recepcionista limpieza":



                    if mouse_pos[0] < 1253 and mouse_pos[0] > 1194 and mouse_pos[1] < 698 and mouse_pos[1] > 647: # salir

                        fondo_actual[0] = "menu recepcionista"
                        fondo_actual[1] = 14
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                    


                    elif mouse_pos[0] < 500 and mouse_pos[0] > 332 and mouse_pos[1] < 660 and mouse_pos[1] > 612: # enviar limpieza

                        pass



                if alter_usuario:


                    if mouse_pos[0] < 1205  and mouse_pos[0] > 1030 and mouse_pos[1] < 478 and mouse_pos[1] > 431: #salir
                        fondo_actual[0] = "iniciar sesion"
                        fondo_actual[1] = 0
                        texto_seleccionado = [(-100,-100),""]
                        alter_usuario = not(alter_usuario)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        


                    elif mouse_pos[0] < 1245 and mouse_pos[0] > 992 and mouse_pos[1] < 310 and mouse_pos[1] > 261: #ver datos
                        fondo_actual[0] = "ver datos"
                        fondo_actual[1] = 9
                        texto_seleccionado = [(-100,-100),""]
                        alter_usuario = not(alter_usuario)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        

                        try:
                            texto1[1] = datos_usuario["Nombre"]
                            texto2[1] = datos_usuario["Direccion"]
                            texto3[1] = datos_usuario["NumeroTelefono"]
                            texto4[1] = datos_usuario["Correo"]
                            texto5[1] = datos_usuario["CodigoPostal"]
                            texto6[1] = datos_usuario["DNI"]
                        except:
                            """"""


                    elif mouse_pos[0] < 1245 and mouse_pos[0] > 992 and mouse_pos[1] < 395 and mouse_pos[1] > 350: #reservar eventos
                        
                        fondo_actual[0] = "reservar eventos"
                        fondo_actual[1] = 8
                        texto_seleccionado = [(-100,-100),""]
                        alter_usuario = not(alter_usuario)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        

                if gracias == True and alter_mouse == False:

                    if mouse_pos[0] < 1130 and mouse_pos[0] > 898 and mouse_pos[1] < 664 and mouse_pos[1] > 598:#continuar
                        gracias = False
                        alter_mouuse = True

        

                if fondo_actual[0] in ["pagar tarjeta","pagar mercado pago","registros","pagar servicio","habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar", "datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "reservar eventos", "ver datos"]:



                    if mouse_pos[0] < 410 and mouse_pos[0] > 290 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu habitaciones" : #Home 
                        habitaciones_libres = Filtros((""),0,9999999999)
                        fondo_actual[0] = "menu habitaciones"
                        fondo_actual[1] = 6
                        texto_seleccionado = [(-100,-100),""]
                        gracias = False
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                        



                    elif mouse_pos[0] < 560 and mouse_pos[0] > 435 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu parking" :#Parking
                        print(len(VerNumeroEstacionamiento(usuario)) == 0)
                        if len(VerNumeroEstacionamiento(usuario)) != 0:

                            fondo_actual[0] = "menu parking"
                            fondo_actual[1] = 2
                            texto_seleccionado = [(-100,-100),""]
                            gracias = False
                            reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                            pagina = 0

                        else:

                            
                            fondo_actual[0] = "menu parking"
                            fondo_actual[1] = 28
                            texto_seleccionado = [(-100,-100),""]
                            gracias = False
                            reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                            pagina = 0



                    elif mouse_pos[0] < 710 and mouse_pos[0] > 590 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu bedroom":#Bedroom
                        fondo_actual[0] = "menu bedroom"
                        fondo_actual[1] = 3
                        texto_seleccionado = [(-100,-100),""]
                        gracias = False
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        pagina = 0
                        



                    elif mouse_pos[0] < 860 and mouse_pos[0] > 745 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu amenities" :#Services
                        
                        fondo_actual[0] = "menu amenities"
                        fondo_actual[1] = 7
                        texto_seleccionado = [(-100,-100),""]
                        gracias = False
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                    


                    elif mouse_pos[0] < 1220 and mouse_pos[0] > 1140 and mouse_pos[1] < 90 and mouse_pos[1] > 18:#boton usuario
                        alter_usuario = not(alter_usuario)
                        gracias = False
                        
                        
                        



                if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"] and alter_mouse == False:        
                    alter_mouse = True
                    if mouse_pos[0] < 1008 and mouse_pos[0] > 785 and mouse_pos[1] < 666 and mouse_pos[1] > 605:#reservar
                        fondo_actual[0] = "pagar servicio"
                        fondo_actual[1] = 5
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                        




    tiempo_actual = pygame.time.get_ticks()
    
    
    if (tiempo_actual - ultimo_cambio_barra) >= 650 :

        alter_barra = not(alter_barra)
        
        if alter_barra:
                       
            ultimo_cambio_barra  = pygame.time.get_ticks()
            if texto_seleccionado != "":
                barra = texto_seleccionado[1] + "|" 

        else:
                   
            ultimo_cambio_barra  = pygame.time.get_ticks()
            if texto_seleccionado != "":
                barra = texto_seleccionado[1]
        
        
    cursor(mouse_pos,alter_usuario , gracias)


    #fondos :)

    
    if True:

        if fondo_actual[0] == "iniciar sesion":
            texto1[0] = ( 467 , 487 )
            texto2[0] = ( 467 , 593 )
            texto3[0] = ( 420 , 375 )
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))       
            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )
            screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )

            

        
        elif fondo_actual[0] == "registrarse":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0)) 
            texto1[0] = ( 467 , 466 )
            texto2[0] = ( 467 , 543 )    
            texto3[0] = ( 467 , 620 ) 
            texto4[0] = ( 250 , 375 )
            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )  
            screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )
            screen.blit( fuente.render(texto4[1] , True , (0,0,0) ), texto4[0] )    
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )  


        elif fondo_actual[0] == "menu habitaciones":

            screen.fill((253,246,228))
            cont = 0
            posiciones_rects = []

            for i in habitaciones_libres:   

                x = 316 * (cont  % 3 + 1) 
                y = posicion + 425 * (cont // 3)
                screen.blit(habitaciones[i], (x, y))
                posiciones_rects.append((x,y))
                

                cont += 1
            
            for i in rects:
                
                if i[1] in habitaciones_libres:
                    
                    i[0][0] = posiciones_rects[0][0] #posicion del rect en x
                    i[0][1] = posiciones_rects[0][1] #posicion del rect en y
                    
                    posiciones_rects.pop(0)
                
                else:
                    i[0][0] = 1000 #posicion del rect en x
                    i[0][1] = 1000 #posicion del rect en y
                

            screen.blit (imagen_filtro , ( 30, 160 ))        
            texto1[0] = ( 192 , 265 )
            texto2[0] = ( 52 , 412 )    
            texto3[0] = ( 192 , 412 )
            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )  
            screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )   
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )


            if gracias == True:

                screen.blit(fondo_gracias , ( 0 , 0))


        elif fondo_actual[0] == "menu parking":
           
            if pagina == len(VerNumeroEstacionamiento(usuario)):               
                fondo_actual[1] = 28
            else:
                fondo_actual[1] = 2

            screen.blit (fondos[fondo_actual[1]] , (0, 0))

            if VerNumeroEstacionamiento(usuario) != False:
                if len(VerNumeroEstacionamiento(usuario)) > 0: 
                    if texto2[1] != (VerNumeroEstacionamiento(usuario).pop( 0 )) or pagina != (len(VerNumeroEstacionamiento(usuario))):
                        if pagina != (len(VerNumeroEstacionamiento(usuario))):
                            screen.blit (flecha_derecha , (1130 , 308) )

                if len(VerNumeroEstacionamiento(usuario)) > 0 and texto2[1] != (VerNumeroEstacionamiento(usuario).pop( -1 )):
                    screen.blit (flecha_izquierda , (55, 308) )

            
            texto1[0] = (375, 351)  
            texto2[0] = (822, 350) 
            texto3[0] = (535, 473)    
            reset_textos(texto1,texto2)
            
            try:
                
                for i in range(len(VerNumeroHabitacion(usuario))):
                    texto1[1] += str(VerNumeroHabitacion(usuario).pop(-1 - i))
                    if i != (len(VerNumeroHabitacion(usuario)) -1):
                        texto1[1] += ","    
                
            except:
                texto1[1] = " -"
                
            
            try:       

                texto2[1] = str(VerNumeroEstacionamiento(usuario).pop( -1 - pagina))
                texto3[1] = str(VencimientoEstacionamiento((VerNumeroEstacionamiento(usuario).pop( -1 - pagina))))
                  
                

            except:

                texto2[1] = "-"
                texto3[1] = "    ---"                
              

            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )
            screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )
            reset_textos(texto1)
            

        elif fondo_actual[0] == "menu bedroom":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))
            texto1[0] = (408, 305)
            texto2[0] = (767, 305)
            texto3[0] = (538, 369)

            if VerNumeroHabitacion(usuario) != False:
                if len(VerNumeroHabitacion(usuario)) > 1 and texto1[1] != str(VerNumeroHabitacion(usuario).pop( 0 )):
                    screen.blit (flecha_derecha , (1130 , 308) )

                if len(VerNumeroHabitacion(usuario)) > 1 and texto1[1] != str(VerNumeroHabitacion(usuario).pop( -1 )):
                    screen.blit (flecha_izquierda , (55, 308) )


        
            for i in range(len(VerNumeroEstacionamiento(usuario))):
                texto2[1] += str(VerNumeroEstacionamiento(usuario).pop(-1 - i))
                if i != len(VerNumeroEstacionamiento(usuario) ) - 1:
                    texto2[1] += ","
            if len(VerNumeroEstacionamiento(usuario)) == 0:
                texto2[1] = "  -"
            

            for i in range(1,4):
                print(TieneServicio(usuario))
                if TieneServicio(usuario)[i-1][0]:
                    pygame.draw.rect(screen, (98,69,49) , ( 351 + 306 * ( i - 1 ) ,   496 , 41 , 41 )) #310

            try:       

                texto1[1] = str(VerNumeroHabitacion(usuario).pop( -1 - pagina))               
                texto3[1] = str(VerFechaFinal((VerNumeroHabitacion(usuario).pop( -1 - pagina)))[0])
                
            except:
                texto1[1] = "-"
                texto3[1] = "    ---"
            

            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )
            screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )
            reset_textos(texto2)


        elif fondo_actual[0] == "menu amenities":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))
            pygame.draw.rect(screen, (98,69,49) , posicion_cuadrado)
            pygame.draw.rect(screen, (98,69,49) , posicion_cuadrado_2)
            pygame.draw.rect(screen, (98,69,49) , posicion_cuadrado_3)
            

        elif fondo_actual[0] == "ver datos":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))

            texto1[0] = (420, 260) #Nombre y apellido
            texto2[0] = (302, 320) #direccion
            texto3[0] = (302, 382) #telefono
            texto4[0] = (233, 447) #mail
            texto5[0] = (358, 516) #codigo postal
            texto6[0] = (308, 576) #dni


            screen.blit(fuente.render(texto1[1], True, (0, 0, 0)), texto1[0])
            screen.blit(fuente.render(texto2[1], True, (0, 0, 0)), texto2[0])
            screen.blit(fuente.render(texto3[1], True, (0, 0, 0)), texto3[0])
            screen.blit(fuente.render(texto4[1], True, (0, 0, 0)), texto4[0])
            screen.blit(fuente.render(texto5[1], True, (0, 0, 0)), texto5[0])
            screen.blit(fuente.render(texto6[1], True, (0, 0, 0)), texto6[0])



        elif fondo_actual[0] == "registros":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))

            texto1[0] = (200 , 325)
            texto2[0] = (200 , 400)
            texto3[0] = (200 , 470)
            texto4[0] = (200 , 540)
            texto5[0] = (200 , 610)

            texto1[1] = "         ---                      ---"
            texto2[1] = "         ---                      ---"
            texto3[1] = "         ---                      ---"
            texto4[1] = "         ---                      ---"
            texto5[1] = "         ---                      ---"
  

            try:
                          
                texto1[1] = str (VerRegistrosEstacionamiento (usuario , pagina) [0] [0] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [0] [0] [1]) + "    " +str ( VerRegistrosEstacionamiento (usuario , pagina) [1] [0] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [1] [0] [1] )
                
                texto2[1] = str (VerRegistrosEstacionamiento (usuario , pagina) [0] [1] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [0] [1] [1] + "    " +str ( VerRegistrosEstacionamiento (usuario , pagina) [1] [1] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [1] [1] [1] ))
                
                texto3[1] = str (VerRegistrosEstacionamiento (usuario , pagina) [0] [2] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [0] [2] [1] + "    " +str ( VerRegistrosEstacionamiento (usuario , pagina) [1] [2] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [1] [2] [1] ))
          
                texto4[1] = str (VerRegistrosEstacionamiento (usuario , pagina) [0] [3] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [0] [3] [1]) + "    " +str ( VerRegistrosEstacionamiento (usuario , pagina) [1] [3] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [1] [3] [1] )
            
                texto5[1] = str (VerRegistrosEstacionamiento (usuario , pagina) [0] [4] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [0] [4] [1]) + "    " +str ( VerRegistrosEstacionamiento (usuario , pagina) [1] [4] [0] + " - " + VerRegistrosEstacionamiento (usuario , pagina) [1] [4] [1] )

            except:
                """"""
                

            screen.blit(fuente.render(texto1[1], True, (0, 0, 0)), texto1[0])
            screen.blit(fuente.render(texto2[1], True, (0, 0, 0)), texto2[0])
            screen.blit(fuente.render(texto3[1], True, (0, 0, 0)), texto3[0])
            screen.blit(fuente.render(texto4[1], True, (0, 0, 0)), texto4[0])
            screen.blit(fuente.render(texto5[1], True, (0, 0, 0)), texto5[0])
            screen.blit(fuente.render(texto6[1], True, (0, 0, 0)), texto6[0])
            screen.blit(fuente.render(texto7[1], True, (0, 0, 0)), texto7[0])
            screen.blit(fuente.render(texto8[1], True, (0, 0, 0)), texto8[0])







           






        elif fondo_actual[0] == "reservar eventos":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))  
            
            
            texto1[0] = (456, 251) #Cantidad asistentes
            texto2[0] = (226, 340) #Hora1
            texto3[0] = (454, 340) #Hora2
            texto4[0] = (222, 418) #Dia
            texto5[0] = (456, 474) #Personal requerido
            texto6[0] = (222, 560) #Mail
            texto7[0] = (734, 215) #especificaciones
            texto8[0] = (734, 250) #especificaciones

            
            if texto_seleccionado != texto4 :
                if texto4[1] == "" or texto4[1] == "DD/MM/AAAA" :
                    texto4[1] = "DD/MM/AAAA"
            else:
                texto4[1] = texto_seleccionado[1]
                barra = texto4[1] + "|"
                ultimo_cambio_barra = pygame.time.get_ticks()



            if texto_seleccionado != texto2 :
                if texto2[1] == "" or texto2[1] == "HH:MM" :
                    texto2[1] = "HH:MM"
            else:
                texto2[1] = texto_seleccionado[1]
                barra = texto2[1] + "|"
                ultimo_cambio_barra = pygame.time.get_ticks()



            if texto_seleccionado != texto3 :
                if texto3[1] == "" or texto3[1] == "HH:MM" :
                    texto3[1] = "HH:MM"
            else:
                texto3[1] = texto_seleccionado[1]
                barra = texto3[1] + "|"
                ultimo_cambio_barra = pygame.time.get_ticks()            

            

          
        

   
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )
            screen.blit(fuente.render(texto1[1], True, (0, 0, 0)), texto1[0])
            screen.blit(fuente.render(texto2[1], True, (0, 0, 0)), texto2[0])
            screen.blit(fuente.render(texto3[1], True, (0, 0, 0)), texto3[0])
            screen.blit(fuente.render(texto4[1], True, (0, 0, 0)), texto4[0])
            screen.blit(fuente.render(texto5[1], True, (0, 0, 0)), texto5[0])
            screen.blit(fuente.render(texto6[1], True, (0, 0, 0)), texto6[0])
            screen.blit(fuente.render(texto7[1], True, (0, 0, 0)), texto7[0])
            screen.blit(fuente.render(texto8[1], True, (0, 0, 0)), texto8[0])
            pygame.draw.rect(screen, (98,69,49) , posicion_cuadrado_salon)


        elif fondo_actual[0] == "pagar servicio":
            texto1[0] = (265, 255) #Nombre
            texto2[0] = (213, 333) #Dia1
            texto3[0] = (495, 333) #Dia2
            texto4[0] = (300, 413) #Direccion
            texto5[0] = (284, 480) #Telefono
            texto6[0] = (246, 548) #Mail
            texto7[0] = (906, 180) #DNI
            texto8[0] = (944, 255) #codigo postal

            if texto_seleccionado != texto2 :
                if texto2[1] == "" or texto2[1] == "DD/MM/AAAA" :
                    texto2[1] = "DD/MM/AAAA"
            else:
                texto2[1] = texto_seleccionado[1]
                barra = texto2[1] + "|"
                ultimo_cambio_barra = pygame.time.get_ticks()

            if texto_seleccionado != texto3 :
                if texto3[1] == "" or texto3[1] == "DD/MM/AAAA":
                    texto3[1] = "DD/MM/AAAA"
            else:
                texto3[1] = texto_seleccionado[1]
                barra = texto3[1] + "|"
                ultimo_cambio_barra = pygame.time.get_ticks()


            
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )
            screen.blit(fuente.render(texto1[1], True, (0, 0, 0)), texto1[0])
            screen.blit(fuente.render(texto2[1], True, (0, 0, 0)), texto2[0])
            screen.blit(fuente.render(texto3[1], True, (0, 0, 0)), texto3[0])
            screen.blit(fuente.render(texto4[1], True, (0, 0, 0)), texto4[0])
            screen.blit(fuente.render(texto5[1], True, (0, 0, 0)), texto5[0])
            screen.blit(fuente.render(texto6[1], True, (0, 0, 0)), texto6[0])
            screen.blit(fuente.render(texto7[1], True, (0, 0, 0)), texto7[0])
            screen.blit(fuente.render(texto8[1], True, (0, 0, 0)), texto8[0])
            pygame.draw.rect(screen, (98,69,49) , posicion_cuadrado_reserva)
        


        elif fondo_actual[0] == "menu mantenimiento":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))


        elif fondo_actual[0] == "mantenimiento notificaciones":
            

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))

            
            for i in range (1 , 5):

                if i <= len (VerNotificacion()):

                    screen.blit (notificiaciones_mantenimiento , (562 , 145 * i))



        
            try:

                texto1[0] = (578 , 152)
                texto1[1] = VerNotificacion() [0][0]

                texto2[0] = (986 , 152)
                texto2[1] = VerNotificacion() [0][1]



                texto3[0] = (578 , 297)
                texto3[1] = VerNotificacion() [1][0]

                texto4[0] = (986 , 297)
                texto4[1] = VerNotificacion() [1][1]
            

                texto5[0] = (578 , 442)
                texto5[1] = VerNotificacion() [2][0]

                texto6[0] = (986 , 442)
                texto6[1] = VerNotificacion() [2][1]
            


                texto7[0] = (578 , 587)
                texto7[1] = VerNotificacion() [3][0]

                texto8[0] = (986 , 587)
                texto8[1] = VerNotificacion() [3][1]
            

            except:
                """"""



            if len(VerNotificacion()) > 0:

                screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
                screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )
            
            if len(VerNotificacion()) > 1:
                screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )
                screen.blit( fuente.render(texto4[1] , True , (0,0,0) ), texto4[0] )
            
            if len(VerNotificacion()) > 2:
                screen.blit( fuente.render(texto5[1] , True , (0,0,0) ), texto5[0] )
                screen.blit( fuente.render(texto6[1] , True , (0,0,0) ), texto6[0] )
            
            if len(VerNotificacion()) > 3:
                screen.blit( fuente.render(texto7[1] , True , (0,0,0) ), texto7[0] )
                screen.blit( fuente.render(texto8[1] , True , (0,0,0) ), texto8[0] )






        elif fondo_actual[0] == "mantenimiento stock":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))






        elif fondo_actual[0] == "pagar mercado pago":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))
            texto1[0] = (164, 612)    
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )
            screen.blit( fuente.render(texto1[1], True, (0, 0, 0)), texto1[0])


        elif fondo_actual[0] == "pagar tarjeta":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))
            texto1[0] = (489, 271)
            texto2[0] = (489, 340)
            texto3[0] = (489, 409)
            texto4[0] = (489, 476)
            texto5[0] = (489, 544)
            texto6[0] = (164,612)

            if texto_seleccionado != texto4 :
                if texto4[1] == "" or texto4[1] == "MM-AAAA" :
                    texto4[1] = "MM-AAAA"
            else:
                texto4[1] = texto_seleccionado[1]
                barra = texto4[1] + "|"
                ultimo_cambio_barra = pygame.time.get_ticks()

            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )
            screen.blit(fuente.render(texto1[1], True, (0, 0, 0)), texto1[0])
            screen.blit(fuente.render(texto2[1], True, (0, 0, 0)), texto2[0])
            screen.blit(fuente.render(texto3[1], True, (0, 0, 0)), texto3[0])
            screen.blit(fuente.render(texto4[1], True, (0, 0, 0)), texto4[0])
            screen.blit(fuente.render(texto5[1], True, (0, 0, 0)), texto5[0])
            screen.blit(fuente.render(texto6[1], True, (0, 0, 0)), texto6[0])




        elif fondo_actual[0] == "menu recepcionista":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))  
        
        elif fondo_actual[0] == "recepcionista notificar":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))  

            texto1[0] = (162, 270) #objeto a reponer
            texto2[0] = (185, 378) #cantidad
            texto3[0] = (535, 378) #habitacion


            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )
            screen.blit(fuente.render(texto1[1], True, (0, 0, 0)), texto1[0])
            screen.blit(fuente.render(texto2[1], True, (0, 0, 0)), texto2[0])
            screen.blit(fuente.render(texto3[1], True, (0, 0, 0)), texto3[0])

        
        elif fondo_actual[0] == "recepcionista eventos":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))  

        elif fondo_actual[0] == "recepcionista limpieza":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))  

        
            

        




        if fondo_actual[0] in ["pagar tarjeta","pagar mercado pago","registros","datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "menu salon", "pagar servicio", "reservar eventos","ver datos"]:
            screen.blit (barra_arriba, (0,0))


        if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"]:
            screen.blit(fondos[fondo_actual[1]],(0,0))
            screen.blit(barra_arriba,(0,0))


        if alter_usuario:
            screen.blit (imagen_usuario , (958, 129))


    pygame.display.flip()



pygame.quit()