import tkinter
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

habitaciones_libres = Filtros("",0,1000)


cambiar_nombre = []
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
    fondo_registros                    # 27
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

barra = "|"

posicion = 150
alter_mouse = False

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
    




def cursor(mouse_pos):
    

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

        
        elif suite_balcon_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif habitacion_triple_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif habitacion_doble_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif habitacion_lujo_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif habitacion_cuadruple_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif suite_rio_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif habitacion_individual_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif suite_jacuzzi_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif suite_estandar_rect[0].collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
             


        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    elif fondo_actual[0] == "menu parking":


        if mouse_pos[0] < 490 and mouse_pos[0] > 260 and mouse_pos[1] < 656 and mouse_pos[1] > 579: #ver registros        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
                    

        elif mouse_pos[0] < 757 and mouse_pos[0] > 522 and mouse_pos[1] < 656 and mouse_pos[1] > 579:#notificar ingreso        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
                    

        elif mouse_pos[0] < 1018 and mouse_pos[0] > 784 and mouse_pos[1] < 656 and mouse_pos[1] > 579:#cancelar reserva de parking        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND) 
        

        elif mouse_pos[0] < 1225 and mouse_pos[0] > 1130 and mouse_pos[1] < 462 and mouse_pos[1] > 306:#flecha derecha   
            if len(VerNumeroEstacionamiento(usuario)) > 1 and texto2[1] != VerNumeroEstacionamiento(usuario).pop( 0 ):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 149 and mouse_pos[0] > 55 and mouse_pos[1] < 467 and mouse_pos[1] > 309:#flecha izquierda  
            if len(VerNumeroEstacionamiento(usuario)) > 1 and texto2[1] != VerNumeroEstacionamiento(usuario).pop( -1 ):    
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 



    elif fondo_actual[0] == "reservar habitacion":

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

        if mouse_pos[0] < 996 and mouse_pos[0] > 441 and mouse_pos[1] < 314 and mouse_pos[1] > 268: #Nombre del titular
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

        elif mouse_pos[0] < 996 and mouse_pos[0] > 441 and mouse_pos[1] < 379 and mouse_pos[1] > 335: #VOLVER
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)    

        elif mouse_pos[0] < 996 and mouse_pos[0] > 364 and mouse_pos[1] < 448 and mouse_pos[1] > 404: #Vencimiento
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)  

        elif mouse_pos[0] < 996 and mouse_pos[0] > 465 and mouse_pos[1] < 516 and mouse_pos[1] > 471: #Codigo de seguridad
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)  

        elif mouse_pos[0] < 996 and mouse_pos[0] > 486 and mouse_pos[1] < 584 and mouse_pos[1] > 542: #Documento
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)  

        elif mouse_pos[0] < 1128 and mouse_pos[0] > 906 and mouse_pos[1] < 665 and mouse_pos[1] > 605: #Pagar
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  

        else:
             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        
    if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"]:
            if mouse_pos[0] < 1008 and mouse_pos[0] > 785 and mouse_pos[1] < 666 and mouse_pos[1] > 605:#reservar       
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)    
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)




    if fondo_actual[0] in ["pagar mercado pago","pagar tarjeta","registros","habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar", "datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "reservar eventos", "ver datos", "reservar habitacion"]:



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
    if len(conteraseña) > 8:
        if  any( caracter in conteraseña for caracter in ["@", "#", "$", "*", "%", "&", "/", "!", "?", "-", "_"] ):
            if any( caracter in conteraseña for caracter in ["1","2","3","4","5","6","7","8","9","0"] ):
                return "aprobado"
            else:   
                return "Debe haber algun numero"
        else:
            return "Debe haber caracteres especiales"    
    else:
        return "Deben haber al menos 8 caracteres"






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

                                    



                            else:
                                texto3[1] = "Contraseña erronea"
                        else:
                            texto3[1] = "Usuario inexistente"
                elif fondo_actual[0] == "registrarse": 
                    if len(texto1[1]) > 3 and len(texto2[1]) > 3 :
                        if not(ExisteUsuario(texto1[1])) :

                            if chequeo_contraseña(texto3[1]) == "aprobado":

                                CrearActualizarUsuario(texto1[1] , texto2[1] , "" , "" , "" , texto3[1] , "" , "" , "" , "" , "")
                                fondo_actual[0] = "menu habitaciones"
                                fondo_actual[1] = 6
                                texto_seleccionado = [(-100,-100),""]
                                reset_textos(texto1,texto2,texto3,texto4)

                            else:
                                texto4[1] = chequeo_contraseña(texto3[1])    
                        else:
                            texto4[1] = "El usuario ingresado ya existe"
                    else:
                        texto4[1] = "usuario o mail muy cortos" 
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



                                
                            else:
                                texto3[1] = "Contraseña erronea"
                        else:
                            texto3[1] = "Usuario inexistente"





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
                            if not(ExisteUsuario(texto1[1])) :

                                if chequeo_contraseña(texto3[1]) == "aprobado":

                                    CrearActualizarUsuario(texto1[1] , texto2[1] , "" , "" , "" , texto3[1] , "" , "" , "" , "" , "")
                                    fondo_actual[0] = "menu habitaciones"
                                    fondo_actual[1] = 6
                                    texto_ingresado = ""
                                    texto_seleccionado = [(-100,-100),""]
                                    reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                                    

                                else:                       
                                    texto4[1] = chequeo_contraseña(texto3[1])    
                            else:
                                texto4[1] = "El usuario ingresado ya existe"
                        else:
                            texto4[1] = "usuario o mail muy cortos"

                          
                    elif mouse_pos[0] <= 748 and mouse_pos[0] >= 519 and mouse_pos[1] <= 682 and mouse_pos[1] >= 670:#-----> Iniciar Sesion
                        fondo_actual[0] = "iniciar sesion"
                        fondo_actual[1] = 0
                        texto_ingresado = ""
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                                       




                elif fondo_actual[0] == "menu habitaciones" and alter_mouse == False:
                    
                    

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
                            habitaciones_libres = Filtros(int(texto1[1]),int(texto2[1]),int(texto3[1]))
                        except ValueError:
                            """"""
                        alter_mouse = True



                    elif mouse_pos[0] < 253 and mouse_pos[0] > 76 and mouse_pos[1] < 512 and mouse_pos[1] > 475:#restablecer
                        habitaciones_libres = Filtros("",0,1000)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        print(texto1)
                        barra = texto_seleccionado[1] + "|"  
                        texto_ingresado = ""
                        print(barra)

                        ultimo_cambio_barra  = pygame.time.get_ticks()
                        alter_mouse = True



                    if not(mouse_pos[0] < 1280 and mouse_pos[0] > 0 and mouse_pos[1] < 125 and mouse_pos[1] > 0): #-----> habitaciones
                        if not(mouse_pos[0] < 1275 and mouse_pos[0] > 962 and mouse_pos[1] < 519 and mouse_pos[1] > 131) or alter_usuario == False:
                            alter_mouse = True
                            if suite_balcon_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion balcon"
                                fondo_actual[1] = 18
                                texto_seleccionado = [(-100,-100),""]

                            elif habitacion_triple_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion triple"
                                fondo_actual[1] = 19
                                texto_seleccionado = [(-100,-100),""]

                            elif habitacion_doble_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion doble"
                                fondo_actual[1] = 20
                                texto_seleccionado = [(-100,-100),""]

                            elif habitacion_lujo_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion lujo"
                                fondo_actual[1] = 21
                                texto_seleccionado = [(-100,-100),""]

                            elif habitacion_cuadruple_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion cuadruple"
                                fondo_actual[1] = 22
                                texto_seleccionado = [(-100,-100),""]

                            elif suite_rio_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "suite rio"
                                fondo_actual[1] = 23
                                texto_seleccionado = [(-100,-100),""]

                            elif habitacion_individual_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion individual"
                                fondo_actual[1] = 24
                                texto_seleccionado = [(-100,-100),""]

                            elif suite_jacuzzi_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "suite jacuzzi"
                                fondo_actual[1] = 25
                                texto_seleccionado = [(-100,-100),""]

                            elif suite_estandar_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "suite estandar"
                                fondo_actual[1] = 26
                                texto_seleccionado = [(-100,-100),""]




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

                        print("")
                        alter_mouse = True
                    

                    elif mouse_pos[0] < 752 and mouse_pos[0] > 516 and mouse_pos[1] < 655 and mouse_pos[1] > 576: #no molestar
                        if TieneHabitacion(usuario) != False:
                            CambiarEstadoHabitacion(VerNumeroHabitacion(usuario).pop( -1 - pagina ))
                        alter_mouse = True


                    elif mouse_pos[0] < 1018 and mouse_pos[0] > 785 and mouse_pos[1] < 655 and mouse_pos[1] > 576: #cancelar reserva
                        try:
                            CancelarReservaHabitaciones(usuario , VerNumeroHabitacion(usuario).pop( -1 - pagina ) )
                        except:
                            """"""
                        alter_mouse = True
                    
                        

                        

                elif fondo_actual[0] == "reservar habitacion":


                    if mouse_pos[0] < 690 and mouse_pos[0] > 255 and mouse_pos[1] < 300 and mouse_pos[1] > 250: #nombre        
                                    
                        texto_ingresado = texto1[1]
                        texto_seleccionado = texto1   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 22
        

                    elif mouse_pos[0] < 425 and mouse_pos[0] > 205 and mouse_pos[1] < 375 and mouse_pos[1] > 335: #dia inicio        

                        texto2[1]  = ""    
                        texto_ingresado = ""
                        texto_seleccionado = texto2   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 10
                        

                    elif mouse_pos[0] < 710 and mouse_pos[0] > 485 and mouse_pos[1] < 375 and mouse_pos[1] > 335: #dia fin       
                                    
                        texto3[1]  = ""
                        texto_ingresado = ""
                        texto_seleccionado = texto3
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 10 
                    

                    elif mouse_pos[0] < 690 and mouse_pos[0] > 289 and mouse_pos[1] < 453 and mouse_pos[1] > 411: #direccion      
                                    
                        texto_ingresado = texto4[1]
                        texto_seleccionado = texto4  
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 20

                    
                    elif mouse_pos[0] < 690 and mouse_pos[0] > 273 and mouse_pos[1] < 520 and mouse_pos[1] > 480: #telefono     
                                    
                        texto_ingresado = texto5[1]
                        texto_seleccionado = texto5   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 21
                    

                    elif mouse_pos[0] < 690 and mouse_pos[0] > 232 and mouse_pos[1] < 588 and mouse_pos[1] > 546: #mail   
                                    
                        texto_ingresado = texto6[1]
                        texto_seleccionado = texto6   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 23
                                        

                    elif mouse_pos[0] < 1107 and mouse_pos[0] > 896 and mouse_pos[1] < 223 and mouse_pos[1] > 178: #dni/cuit   
                                    
                        texto_ingresado = texto7[1]
                        texto_seleccionado = texto7   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 11 
                    

                    elif mouse_pos[0] < 1107 and mouse_pos[0] > 937 and mouse_pos[1] < 295 and mouse_pos[1] > 251: #codigo postal 
                                    
                        texto_ingresado = texto8[1]
                        texto_seleccionado = texto8   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 6 
                    

                    elif mouse_pos[0] < 925 and mouse_pos[0] > 870 and mouse_pos[1] < 460 and mouse_pos[1] > 405: #efectivo


                        posicion_cuadrado_reserva = ( 877, 413, 41 , 41  )
                

                    elif mouse_pos[0] < 1006 and mouse_pos[0] > 954 and mouse_pos[1] < 534 and mouse_pos[1] > 480: #mercado pago
                                    
                        
                        posicion_cuadrado_reserva = ( 960 , 490 , 41 , 41 )


                    elif mouse_pos[0] < 1108 and mouse_pos[0] > 1058 and mouse_pos[1] < 460 and mouse_pos[1] > 307: #tarjeta


                        posicion_cuadrado_reserva = ( 1062, 415, 41 , 41  ) 


                    elif mouse_pos[0] < 528 and mouse_pos[0] > 307 and mouse_pos[1] < 670 and mouse_pos[1] > 615: #pagar
                        
                        if ChequearDatosUsuario(usuario,texto1[1],texto2[1], texto3[1], texto4[1], texto5[1], texto6[1], texto7[1], texto8[1])[0] != False:
                            
                            if posicion_cuadrado_reserva == ( 877, 413, 41 , 41 ):                                
                                fondo_actual[0] = "menu habitaciones"
                                texto_seleccionado = [(-100,-100),""]
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                            elif posicion_cuadrado_reserva == ( 960 , 490 , 41 , 41 ):
                                fondo_actual[0] = "pagar mercado pago"
                                fondo_actual[1] = 4
                                texto_seleccionado = [(-100,-100),""]
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                            elif posicion_cuadrado_reserva == ( 1062, 415, 41 , 41  ):
                                fondo_actual[0] = "pagar tarjeta"
                                fondo_actual[1] = 6
                                texto_seleccionado = [(-100,-100),""]
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 






                elif fondo_actual[0] == "menu amenities":

                   
                    if mouse_pos[0] < 455 and mouse_pos[0] > 400 and mouse_pos[1] < 342 and mouse_pos[1] > 290 and posicion_cuadrado != (409,298, 41,41): #spa aparece
                   
                        posicion_cuadrado = (409,298, 41,41)
                    
                    elif mouse_pos[0] < 455 and mouse_pos[0] > 400 and mouse_pos[1] < 342 and mouse_pos[1] > 290 and posicion_cuadrado == (409,298, 41,41): #spa desaparece

                        posicion_cuadrado = (-100,-100,0,0)

                    elif mouse_pos[0] < 1005 and mouse_pos[0] > 948 and mouse_pos[1] < 345 and mouse_pos[1] > 290 and posicion_cuadrado_2 != (957,298, 41,41): #gimnasio aparece
                   
                        posicion_cuadrado_2 = (957,298, 41,41)

                    elif mouse_pos[0] < 1005 and mouse_pos[0] > 948 and mouse_pos[1] < 345 and mouse_pos[1] > 290 and posicion_cuadrado_2 == (957,298, 41,41): #gimnasio desaparece

                        posicion_cuadrado_2 = (-100,-100,0,0)

                    elif mouse_pos[0] < 740 and mouse_pos[0] > 688 and mouse_pos[1] < 345 and mouse_pos[1] > 290 and posicion_cuadrado_3 !=  (695,298, 41,41): #pileta aparece

                        posicion_cuadrado_3 = (695,298, 41,41)

                    elif  mouse_pos[0] < 740 and mouse_pos[0] > 688 and mouse_pos[1] < 345 and mouse_pos[1] > 290 and posicion_cuadrado_3 ==  (695,298, 41,41): #pileta desaparece

                        posicion_cuadrado_3 = (-100,-100,0,0)
                   
                    elif mouse_pos[0] < 708 and mouse_pos[0] > 568 and mouse_pos[1] < 676 and mouse_pos[1] > 636: #reservar
                        if posicion_cuadrado == (409,298, 41,41)  or posicion_cuadrado_2 == (957,298, 41,41) or posicion_cuadrado_3 == (695,298, 41,41):
                            fondo_actual[0] = "reservar habitacion"
                            fondo_actual[1] = 5
                            posicion_cuadrado = (0,0,0,0)
                            posicion_cuadrado_2 = (0,0,0,0)
                            posicion_cuadrado_3 = (0,0,0,0)
                        
                    
                    


                elif fondo_actual[0] == "reservar eventos":


                    

                    if mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 298 and mouse_pos[1] > 252: #Cantidad asistentes
                                    
                        texto_ingresado = texto1[1]
                        texto_seleccionado = texto1   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 3
        

                    elif  mouse_pos[0] < 332 and mouse_pos[0] > 214 and mouse_pos[1] < 382 and mouse_pos[1] > 340: #inicia el horario

                        texto2[1]  = ""    
                        texto_ingresado = ""
                        texto_seleccionado = texto2   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 5
                        


                    elif  mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 382 and mouse_pos[1] > 340: #termina el horario 
                                    
                        texto3[1]  = ""
                        texto_ingresado = ""
                        texto_seleccionado = texto3
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 5
                    

                    elif  mouse_pos[0] < 436 and mouse_pos[0] > 214 and mouse_pos[1] < 460 and mouse_pos[1] > 416: #dia del evento   
                                    
                        texto4[1]  = ""
                        texto_ingresado = ""
                        texto_seleccionado = texto4  
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 10

                    
                    elif  mouse_pos[0] < 560 and mouse_pos[0] > 445 and mouse_pos[1] < 524 and mouse_pos[1] > 474: #personal requerido  
                                    
                        texto_ingresado = texto5[1]
                        texto_seleccionado = texto5   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 3 
                    

                    elif  mouse_pos[0] < 684 and mouse_pos[0] > 212 and mouse_pos[1] < 605 and mouse_pos[1] > 565: #mail   
                                    
                        texto_ingresado = texto6[1]
                        texto_seleccionado = texto6   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 24

                                        

                    elif  mouse_pos[0] < 480 and mouse_pos[0] > 260 and mouse_pos[1] < 690 and mouse_pos[1] > 620: #reservar salon de eventos 

                        
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
        
                    elif mouse_pos[0] < 1225 and mouse_pos[0] > 1130 and mouse_pos[1] < 462 and mouse_pos[1] > 306 and alter_mouse == False:#flecha derecha   
                        if len(VerNumeroEstacionamiento(usuario)) > 1 and texto2[1] != VerNumeroEstacionamiento(usuario).pop( 0 ):
                            pagina += 1
                            alter_mouse = True


                    elif mouse_pos[0] < 149 and mouse_pos[0] > 55 and mouse_pos[1] < 467 and mouse_pos[1] > 309 and alter_mouse == False:#flecha izquierda  
                        if len(VerNumeroEstacionamiento(usuario)) > 1 and texto2[1] != VerNumeroEstacionamiento(usuario).pop( -1 ):    
                            pagina -= 1
                            alter_mouse = True

                
                elif fondo_actual[0] == "menu mantenimiento":
                    
                    if mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 342 and mouse_pos[1] > 285: #notificaciones

                        fondo_actual[0] = "mantenimiento notificaciones"
                        fondo_actual[1] = 12
                    

                    elif mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 440 and mouse_pos[1] > 378: #ver stcok

                        fondo_actual[0] = "mantenimiento stock"
                        fondo_actual[1] = 11
                    

                    elif mouse_pos[0] < 374 and mouse_pos[0] > 144 and mouse_pos[1] < 535 and mouse_pos[1] > 470: #salir

                        fondo_actual[0] = "iniciar sesion"
                        fondo_actual[1] = 0
                    

                elif fondo_actual[0] == "pagar mercado pago":
                    if mouse_pos[0] < 842 and mouse_pos[0] > 437 and mouse_pos[1] < 647 and mouse_pos[1] > 243: #QR

                        fondo_actual[0] = "menu habitaciones"
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 

                    elif mouse_pos[0] < 1127 and mouse_pos[0] > 907 and mouse_pos[1] < 662 and mouse_pos[1] > 599: #VOLVER
                        fondo_actual[0] = "reservar habitacion"
                        fondo_actual[1] = 5
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
            


                elif fondo_actual[0] == "pagar tarjeta":

                    if mouse_pos[0] < 996 and mouse_pos[0] > 441 and mouse_pos[1] < 314 and mouse_pos[1] > 268: #Nombre del titular
                        texto_ingresado = texto1[1]
                        texto_seleccionado = texto1 #Usuario / iniciar sesion   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 18

                    elif mouse_pos[0] < 996 and mouse_pos[0] > 441 and mouse_pos[1] < 379 and mouse_pos[1] > 335: #VOLVER
                        texto_ingresado = texto2[1]
                        texto_seleccionado = texto2 #Usuario / iniciar sesion   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 18   

                    elif mouse_pos[0] < 996 and mouse_pos[0] > 364 and mouse_pos[1] < 448 and mouse_pos[1] > 404: #Vencimiento
                        texto_ingresado = texto3[1]
                        texto_seleccionado = texto3 #Usuario / iniciar sesion   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 18 

                    elif mouse_pos[0] < 996 and mouse_pos[0] > 465 and mouse_pos[1] < 516 and mouse_pos[1] > 471: #Codigo de seguridad
                        texto_ingresado = texto4[1]
                        texto_seleccionado = texto4 #Usuario / iniciar sesion   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 18  

                    elif mouse_pos[0] < 996 and mouse_pos[0] > 486 and mouse_pos[1] < 584 and mouse_pos[1] > 542: #Documento
                        texto_ingresado = texto5[1]
                        texto_seleccionado = texto5 #Usuario / iniciar sesion   
                        barra = texto_seleccionado[1] + "|"  
                        ultimo_cambio_barra  = pygame.time.get_ticks()                   
                        limite = 18  

                    elif mouse_pos[0] < 1128 and mouse_pos[0] > 906 and mouse_pos[1] < 665 and mouse_pos[1] > 605: #Pagar
                        fondo_actual[0] = "menu habitaciones"
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 



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
                                            


                    elif mouse_pos[0] < 1245 and mouse_pos[0] > 992 and mouse_pos[1] < 395 and mouse_pos[1] > 350: #reservar eventos
                        
                        fondo_actual[0] = "reservar eventos"
                        fondo_actual[1] = 8
                        texto_seleccionado = [(-100,-100),""]
                        alter_usuario = not(alter_usuario)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        




                if fondo_actual[0] in ["pagar tarjeta","pagar mercado pago","registros","reservar habitacion","habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar", "datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "reservar eventos", "ver datos"]:



                    if mouse_pos[0] < 410 and mouse_pos[0] > 290 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu habitaciones" : #Home 
                        habitaciones_libres = Filtros((""),0,1000)
                        fondo_actual[0] = "menu habitaciones"
                        fondo_actual[1] = 6
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                        



                    elif mouse_pos[0] < 560 and mouse_pos[0] > 435 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu parking" :#Parking
                        fondo_actual[0] = "menu parking"
                        fondo_actual[1] = 2
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        pagina = 0
                        



                    elif mouse_pos[0] < 710 and mouse_pos[0] > 590 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu bedroom":#Bedroom
                        fondo_actual[0] = "menu bedroom"
                        fondo_actual[1] = 3
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        pagina = 0
                        



                    elif mouse_pos[0] < 860 and mouse_pos[0] > 745 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu amenities" :#Services
                        
                        fondo_actual[0] = "menu amenities"
                        fondo_actual[1] = 7
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                    


                    elif mouse_pos[0] < 1220 and mouse_pos[0] > 1140 and mouse_pos[1] < 90 and mouse_pos[1] > 18:#boton usuario
                        alter_usuario = not(alter_usuario)
                        
                        
                        



                if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"] and alter_mouse == False:        
                    alter_mouse = True
                    if mouse_pos[0] < 1008 and mouse_pos[0] > 785 and mouse_pos[1] < 666 and mouse_pos[1] > 605:#reservar
                        fondo_actual[0] = "reservar habitacion"
                        
                        texto_seleccionado = [(-100,-100),""]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                        fondo_actual[1] = 5




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
        
        
    cursor(mouse_pos)


    #fondos :)

    
    if True:

        if fondo_actual[0] == "iniciar sesion":
            texto1[0] = ( 467 , 487 )
            texto2[0] = ( 467 , 593 )
            texto3[0] = ( 420 , 377 )
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
            texto4[0] = ( 415 , 378 )
            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )  
            screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )
            screen.blit( fuente.render(texto4[1] , True , (0,0,0) ), texto4[0] )    
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )  


        elif fondo_actual[0] == "menu habitaciones":

            screen.fill((253,246,228))
            cont = 0
            cambiar_nombre = []

            for i in habitaciones_libres:   

                x = 316 * (cont  % 3 + 1) 
                y = posicion + 425 * (cont // 3)
                screen.blit(habitaciones[i], (x, y))
                cambiar_nombre.append((x,y))
                

                cont += 1
            
            for i in rects:
                
                if i[1] in habitaciones_libres:
                    
                    i[0][0] = cambiar_nombre[0][0] #posicion del rect en x
                    i[0][1] = cambiar_nombre[0][1] #posicion del rect en y
                    
                    cambiar_nombre.pop(0)
                
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


        elif fondo_actual[0] == "menu parking":
            screen.blit (fondos[fondo_actual[1]] , (0, 0))
            if VerNumeroEstacionamiento(usuario) != False:
                if len(VerNumeroEstacionamiento(usuario)) > 1 and texto2[1] != VerNumeroEstacionamiento(usuario).pop( 0 ):
                    screen.blit (flecha_derecha , (1130 , 308) )

                if len(VerNumeroEstacionamiento(usuario)) > 1 and texto2[1] != VerNumeroEstacionamiento(usuario).pop( -1 ):
                    screen.blit (flecha_izquierda , (55, 308) )

            texto1[0] = (345, 351)     
            texto2[0] = (822, 350) 
            texto3[0] = (535, 473)    
            reset_textos(texto1,texto2)
            
            try:

                for i in range(len(VerNumeroHabitacion(usuario))):
                    texto1[1] += str(VerNumeroHabitacion(usuario).pop(-1 - i))
                    if i != len(VerNumeroHabitacion(usuario) - 1):
                        texto1[1] += ","    
                
            except:
                """"""
            
            try:            
                
                texto2[1] = str(VerNumeroEstacionamiento(usuario).pop( -1 - pagina))
                texto3[1] = str(VencimientoEstacionamiento((VerNumeroEstacionamiento(usuario).pop( -1 - pagina))))
                
            except:
                """"""

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

            for i in range(1,4):
                if TieneServicio(usuario)[i-1][0]:
                    pygame.draw.rect(screen, (98,69,49) , ( 351 + 306 * ( i - 1 ) ,   496 , 41 , 41 )) #310

            try:       

                texto1[1] = str(VerNumeroHabitacion(usuario).pop( -1 - pagina))               
                texto3[1] = str(VerFechaFinal((VerNumeroHabitacion(usuario).pop( -1 - pagina))))
                
            except:
                reset_textos(texto1,texto3)

            

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


        elif fondo_actual[0] == "registros":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))


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


        elif fondo_actual[0] == "reservar habitacion":
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

        elif fondo_actual[0] == "mantenimiento stock":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))






        elif fondo_actual[0] == "pagar mercado pago":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))


        elif fondo_actual[0] == "pagar tarjeta":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))
            texto1[0] = (448, 271)
            texto2[0] = (448, 340)
            texto3[0] = (372, 409)
            texto4[0] = (471, 476)
            texto5[0] = (494, 544)
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )
            screen.blit(fuente.render(texto1[1], True, (0, 0, 0)), texto1[0])
            screen.blit(fuente.render(texto2[1], True, (0, 0, 0)), texto2[0])
            screen.blit(fuente.render(texto3[1], True, (0, 0, 0)), texto3[0])
            screen.blit(fuente.render(texto4[1], True, (0, 0, 0)), texto4[0])
            screen.blit(fuente.render(texto5[1], True, (0, 0, 0)), texto5[0])



        elif fondo_actual[0] == "menu recepcionista":

            screen.blit (fondos[fondo_actual[1]] , (0 , 0))  
            

        




        if fondo_actual[0] in ["pagar tarjeta","pagar mercado pago","registros","datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "menu salon", "reservar habitacion", "reservar eventos","ver datos"]:
            screen.blit (barra_arriba, (0,0))


        if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"]:
                screen.blit(fondos[fondo_actual[1]],(0,0))
                screen.blit(barra_arriba,(0,0))


        if alter_usuario:
            screen.blit (imagen_usuario , (958, 129))


    pygame.display.flip()



pygame.quit()
