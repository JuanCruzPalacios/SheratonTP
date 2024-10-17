import tkinter
from ManejoDeDatos import *
import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True





fondo_iniciar_sesion = pygame.transform.scale(pygame.image.load("imagenes/iniciar_sesion.jpg"), (1280,720))
fondo_registrarse = pygame.transform.scale(pygame.image.load("imagenes/registrarse.jpg"),(1280,720))
fondo_estacionamiento = pygame.transform.scale(pygame.image.load("imagenes/estacionamiento.jpg"), (1280, 720))
fondo_habitacion = pygame.transform.scale(pygame.image.load("imagenes/habitacion.jpg"), (1280, 720))
fondo_pagar = pygame.transform.scale(pygame.image.load("imagenes/reserva_de_habitacion.jpg"), (1280, 720))


fondo_menu_amenities = pygame.transform.scale(pygame.image.load("imagenes/reserva_de_amenities.jpg"), (1280, 720))
fondo_menu_salones = pygame.transform.scale(pygame.image.load("imagenes/reserva_de_salon.jpg"), (1280, 720))
fondo_datos_usuario = pygame.transform.scale(pygame.image.load("imagenes/datos_usuario.jpg"), (1280, 720))
fondo_menu_mantenimiento = pygame.transform.scale(pygame.image.load("imagenes/menu_mantenimiento.jpg"), (1280, 720))

fondo_mantenimiento_stock = pygame.transform.scale(pygame.image.load("imagenes/stock_mantenimiento.jpg"), (1280, 720))
fondo_mantenimiento_notificaciones = pygame.transform.scale(pygame.image.load("imagenes/notificaciones_mantenimiento.jpg"), (1280, 720))
fondo_mantenimiento_notificaciones_archivadas = pygame.transform.scale(pygame.image.load("imagenes/mantenimiento_notificaciones_archivadas.jpg"), (1280, 720))

fondo_menu_recepcionista = pygame.transform.scale(pygame.image.load("imagenes/menu_recepcionista.jpg"), (1280, 720))
fondo_recepcionista_notificar = pygame.transform.scale(pygame.image.load("imagenes/recepcionista_notificar.jpg"), (1280, 720))
fondo_recepcinista_eventos = pygame.transform.scale(pygame.image.load("imagenes/recepcionista_eventos.jpg"), (1280, 720))
fondo_recepcinista_limpieza = pygame.transform.scale(pygame.image.load("imagenes/recepcionista_limpieza.jpg"), (1280, 720))

barra_arriba = pygame.image.load("imagenes/barra_arriba.jpg")

imagen_usuario = pygame.transform.scale(pygame.image.load("imagenes/usuario.png"), (321, 394))
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

habitaciones_libres = [0,1,2,3,4,5,6,7,8]


cambiar_nombre = []
temp =  []



fondo_actual = ["iniciar sesion", 0]
fondos = [
    fondo_iniciar_sesion,             # 0
    fondo_registrarse,                 # 1
    fondo_estacionamiento,             # 2
    fondo_habitacion,                  # 3
    "",
    fondo_pagar,                       # 5
    "",
    fondo_menu_amenities,              # 7
    fondo_menu_salones,                # 8
    fondo_datos_usuario,               # 9
    fondo_menu_mantenimiento,           # 10
    fondo_mantenimiento_stock,          # 11
    fondo_mantenimiento_notificaciones,  # 12
    fondo_mantenimiento_notificaciones_archivadas,  # 13
    fondo_menu_recepcionista,          # 14
    fondo_recepcionista_notificar,      # 15
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
    suite_estandar                     # 26
]



fuente = pygame.font.Font("fuentes/Averia_Libre/AveriaLibre-Regular.ttf", 31)
limite = 11

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

texto_seleccionado =  texto1 
texto_ingresado = ""




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
        

        else:

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 





    elif fondo_actual[0] == "reservar habitacion":

        if mouse_pos[0] < 687 and mouse_pos[0] > 400 and mouse_pos[1] < 300 and mouse_pos[1] > 253: #nombre y apellido        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM) 
        

        elif mouse_pos[0] < 332 and mouse_pos[0] > 223 and mouse_pos[1] < 383 and mouse_pos[1] > 225: #dia inicio        
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM) 


        elif mouse_pos[0] < 493 and mouse_pos[0] > 386 and mouse_pos[1] < 380 and mouse_pos[1] > 337: #dia fin      
                        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM) 
        

        elif mouse_pos[0] < 690 and mouse_pos[0] > 289 and mouse_pos[1] < 453 and mouse_pos[1] > 411: #direccion      
                        
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


        if mouse_pos[0] < 580 and mouse_pos[0] > 300 and mouse_pos[1] < 300 and mouse_pos[1] > 260: #cantidad asistentes

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 315 and mouse_pos[0] > 225 and mouse_pos[1] < 390 and mouse_pos[1] > 335: #inicia el horario

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 485 and mouse_pos[0] > 390 and mouse_pos[1] < 390 and mouse_pos[1] > 335: #termina el horario el horario

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 580 and mouse_pos[0] > 200 and mouse_pos[1] < 460 and mouse_pos[1] > 415: #dia del evento

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 590 and mouse_pos[0] > 310 and mouse_pos[1] < 527 and mouse_pos[1] > 490: #personal requerido

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 590 and mouse_pos[0] > 225 and mouse_pos[1] < 600 and mouse_pos[1] > 560: #mail

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 480 and mouse_pos[0] > 260 and mouse_pos[1] < 690 and mouse_pos[1] > 620: #reservar salon de eventos

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif  mouse_pos[0] < 1140 and mouse_pos[0] > 730 and mouse_pos[1] < 408 and mouse_pos[1] > 215: #especificaciones
            
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif  mouse_pos[0] < 920 and mouse_pos[0] > 865 and mouse_pos[1] < 580 and mouse_pos[1] > 530: #pago con efectivo
            
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif  mouse_pos[0] < 1105 and mouse_pos[0] > 1050 and mouse_pos[1] < 580 and mouse_pos[1] > 530: #pago con tarjeta
            
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif  mouse_pos[0] < 1005 and mouse_pos[0] > 950 and mouse_pos[1] < 650 and mouse_pos[1] > 600: #pago con mercado pago
            
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

        if mouse_pos[0] < 450 and mouse_pos[0] > 392 and mouse_pos[1] < 392 and mouse_pos[1] > 340: #spa

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 747 and mouse_pos[0] > 690 and mouse_pos[1] < 392 and mouse_pos[1] > 340: #piscina

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 1026 and mouse_pos[0] > 968 and mouse_pos[1] < 392 and mouse_pos[1] > 340: #gimnasio

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        

        elif mouse_pos[0] < 708 and mouse_pos[0] > 568 and mouse_pos[1] < 676 and mouse_pos[1] > 636: #reservar

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:

             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"]:
            if mouse_pos[0] < 1008 and mouse_pos[0] > 785 and mouse_pos[1] < 666 and mouse_pos[1] > 605:#reservar       
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)    
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar", "datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "reservar eventos", "ver datos", "reservar habitacion"]:



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
                # Al presionar Retroceso, eliminar el último carácter del texto
                texto_ingresado = texto_ingresado[:-1]
                barra = barra[:-1] 
                barra = barra[:-1] + "|"
                
                
    
            elif event.key == pygame.K_ESCAPE:
                #aleja la barra de escritura fuera de la pantalla
                texto_seleccionado = [(-10,-10),""]
                
            elif event.key == 13 :#enter
                if fondo_actual[0] == "iniciar sesion":
                        if ExisteUsuario(texto1[1]):

                            if VerificarContraseña(texto1[1],texto2[1]):

                                usuario = texto1[1]
                                fondo_actual[0] = "menu habitaciones"
                                fondo_actual[1] = 6
                                texto_ingresado = ""
                                texto1 = [(0,0),""]
                                texto2 = [(0,0),""]
                                texto3 = [(0,0),""]
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
                                texto_ingresado = ""
                                texto1 = [(0,0),""]
                                texto2 = [(0,0),""]  

                            else:                       
                                texto4[1] = chequeo_contraseña(texto3[1])    
                        else:
                            texto4[1] = "El usuario ingresado ya existe"
                    else:
                        texto4[1] = "usuario o mail muy cortos" 
                else:
                    texto_seleccionado[1] = ""
       
       
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
                        
                        
                        limite = 11

                    
            
                    elif mouse_pos[0] <= 819 and mouse_pos[0] >= 459 and mouse_pos[1] <= 630 and mouse_pos[1] >= 593:#-----> Contraseña                    
                        texto_ingresado = texto2[1]
                        texto_seleccionado = texto2 #Contraseña / iniciar sesion
                        
                        limite = 11



                    elif mouse_pos[0] <= 871 and mouse_pos[0] >= 830 and mouse_pos[1] <= 669 and mouse_pos[1] >= 634:#-----> Siguiente
                        

                        if ExisteUsuario(texto1[1]):

                            if VerificarContraseña(texto1[1],texto2[1]):

                                usuario = texto1[1]
                                fondo_actual[0] = "menu habitaciones"
                                fondo_actual[1] = 6
                                texto_ingresado = ""
                                texto_seleccionado = ""
                                reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                                
                            else:
                                texto3[1] = "Contraseña erronea"
                        else:
                            texto3[1] = "Usuario inexistente"



                    elif mouse_pos[0] <= 755 and mouse_pos[0] >= 522 and mouse_pos[1] <= 682 and mouse_pos[1] >= 669:#-----> Crear cuenta
                        fondo_actual[0] = "registrarse"
                        fondo_actual[1] = 1
                        texto_ingresado = ""
                        texto_seleccionado = ""
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                                      

    


                elif fondo_actual[0] == "registrarse" and alter_mouse == False:   
                    alter_mouse = True

                    if mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 505 and mouse_pos[1] >= 467: #-----> Usuario

                        texto_seleccionado = texto1 #usuario / registrarse
                        texto_ingresado = texto1[1]
                        limite = 11


                    elif mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 583 and mouse_pos[1] >= 544:#-----> Correo Electronico

                        texto_seleccionado = texto2 #mail / registrarse
                        texto_ingresado = texto2[1]
                        limite = 11


                    elif mouse_pos[0] <= 821 and mouse_pos[0] >= 460 and mouse_pos[1] <= 661 and mouse_pos[1] >= 621: #-----> Contraseña
    
                        texto_seleccionado = texto3 #contraseña / registrarse
                        texto_ingresado = texto3[1]
                        limite = 11



                    elif mouse_pos[0] <= 871 and mouse_pos[0] >= 832 and mouse_pos[1] <= 669 and mouse_pos[1] >= 633:#-----> Siguiente
                
                        if len(texto1[1]) > 3 and len(texto2[1]) > 3 :
                            if not(ExisteUsuario(texto1[1])) :

                                if chequeo_contraseña(texto3[1]) == "aprobado":

                                    CrearActualizarUsuario(texto1[1] , texto2[1] , "" , "" , "" , texto3[1] , "" , "" , "" , "" , "")
                                    fondo_actual[0] = "menu habitaciones"
                                    fondo_actual[1] = 6
                                    texto_ingresado = ""
                                    texto_seleccionado = ""
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
                        texto_seleccionado = ""
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                                       




                elif fondo_actual[0] == "menu habitaciones" and alter_mouse == False:
                    
                    

                    if mouse_pos[0] < 282 and mouse_pos[0] > 185 and mouse_pos[1] < 302 and mouse_pos[1] > 267:#personas        
                        texto_seleccionado = texto1
                        texto_ingresado = texto1[1]
                        barra = texto_ingresado + "|"
                        limite = 3
                        alter_mouse = True



                    elif mouse_pos[0] < 142 and mouse_pos[0] > 46 and mouse_pos[1] < 450 and mouse_pos[1] > 415:#precio "desde"
                        texto_seleccionado = texto2
                        texto_ingresado = texto2[1]
                        barra = texto_ingresado + "|"
                        limite = 3
                        alter_mouse = True



                    elif mouse_pos[0] < 284 and mouse_pos[0] > 185 and mouse_pos[1] < 450 and mouse_pos[1] > 416:#precio "hasta"
                        texto_seleccionado = texto3
                        texto_ingresado = texto3[1]
                        barra = texto_ingresado + "|"
                        limite = 3
                        alter_mouse = True



                    elif mouse_pos[0] < 253 and mouse_pos[0] > 76 and mouse_pos[1] < 561 and mouse_pos[1] > 525:#buscar
                        try:
                            habitaciones_libres = Filtros(int(texto1[1]),int(texto2[1]),int(texto3[1]))
                        except ValueError:
                            """"""
                        alter_mouse = True



                    elif mouse_pos[0] < 253 and mouse_pos[0] > 76 and mouse_pos[1] < 512 and mouse_pos[1] > 475:#restablecer
                        habitaciones_libres = [0,1,2,3,4,5,6,7,8]
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                        alter_mouse = True



                    if not(mouse_pos[0] < 1280 and mouse_pos[0] > 0 and mouse_pos[1] < 125 and mouse_pos[1] > 0): #-----> habitaciones
                        if not(mouse_pos[0] < 1275 and mouse_pos[0] > 962 and mouse_pos[1] < 519 and mouse_pos[1] > 131) or alter_usuario == False:
                            alter_mouse = True
                            if suite_balcon_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion balcon"
                                fondo_actual[1] = 18

                            elif habitacion_triple_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion triple"
                                fondo_actual[1] = 19

                            elif habitacion_doble_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion doble"
                                fondo_actual[1] = 20

                            elif habitacion_lujo_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion lujo"
                                fondo_actual[1] = 21

                            elif habitacion_cuadruple_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion cuadruple"
                                fondo_actual[1] = 22

                            elif suite_rio_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "suite rio"
                                fondo_actual[1] = 23

                            elif habitacion_individual_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "habitacion individual"
                                fondo_actual[1] = 24

                            elif suite_jacuzzi_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "suite jacuzzi"
                                fondo_actual[1] = 25

                            elif suite_estandar_rect[0].collidepoint(mouse_pos):
                                fondo_actual[0] = "suite estandar"
                                fondo_actual[1] = 26




                if alter_usuario:


                    if mouse_pos[0] < 1205  and mouse_pos[0] > 1030 and mouse_pos[1] < 478 and mouse_pos[1] > 431: #salir
                        fondo_actual[0] = "iniciar sesion"
                        fondo_actual[1] = 0
                        alter_usuario = not(alter_usuario)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        


                    elif mouse_pos[0] < 1245 and mouse_pos[0] > 992 and mouse_pos[1] < 310 and mouse_pos[1] > 261: #ver datos
                        fondo_actual[0] = "ver datos"
                        fondo_actual[1] = 9
                        alter_usuario = not(alter_usuario)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                                            


                    elif mouse_pos[0] < 1245 and mouse_pos[0] > 992 and mouse_pos[1] < 395 and mouse_pos[1] > 350: #reservar eventos
                        fondo_actual[0] = "reservar eventos"
                        fondo_actual[1] = 8
                        alter_usuario = not(alter_usuario)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        




                if fondo_actual[0] in ["reservar habitacion","habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar", "datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "reservar eventos", "ver datos"]:



                    if mouse_pos[0] < 410 and mouse_pos[0] > 290 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu habitaciones" : #Home 
                        fondo_actual[0] = "menu habitaciones"
                        fondo_actual[1] = 6
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                        



                    elif mouse_pos[0] < 560 and mouse_pos[0] > 435 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu parking" :#Parking
                        fondo_actual[0] = "menu parking"
                        fondo_actual[1] = 2
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        



                    elif mouse_pos[0] < 710 and mouse_pos[0] > 590 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu bedroom":#Bedroom
                        fondo_actual[0] = "menu bedroom"
                        fondo_actual[1] = 3
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        



                    elif mouse_pos[0] < 860 and mouse_pos[0] > 745 and mouse_pos[1] < 100 and mouse_pos[1] > 15 and fondo_actual != "menu amenities" :#Services
                        fondo_actual[0] = "menu amenities"
                        fondo_actual[1] = 7
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                    


                    elif mouse_pos[0] < 1220 and mouse_pos[0] > 1140 and mouse_pos[1] < 90 and mouse_pos[1] > 18:#boton usuario
                        alter_usuario = not(alter_usuario)
                        reset_textos(texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8) 
                        
                        

                if fondo_actual[0] in ["habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"] and alter_mouse == False:        
                    alter_mouse = True
                    if mouse_pos[0] < 1008 and mouse_pos[0] > 785 and mouse_pos[1] < 666 and mouse_pos[1] > 605:#reservar
                        fondo_actual[0] = "reservar habitacion"
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
            texto1[0] = ( 467 , 486 )
            texto2[0] = ( 467 , 592 )
            texto3[0] = ( 420 , 377 )
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))       
            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )
            screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )

        
        elif fondo_actual[0] == "registrarse":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0)) 
            texto1[0] = ( 467 , 465 )
            texto2[0] = ( 467 , 541 )    
            texto3[0] = ( 467 , 617 ) 
            texto4[0] = ( 415 , 375 )
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
            texto1[0] = ( 190 , 266 )
            texto2[0] = ( 47 , 411 )    
            texto3[0] = ( 190 , 411 )
            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )  
            screen.blit( fuente.render(texto3[1] , True , (0,0,0) ), texto3[0] )   
            screen.blit( fuente.render(barra , True , (0,0,0) ), texto_seleccionado[0] )

            


        elif fondo_actual[0] == "menu parking":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))
            texto1[0] = (365, 346)
            texto2[0] = (785, 346)
            reset_textos(texto1,texto2)
            try:
                for i in range(len(VerNumeroHabitacion(usuario))):
                    
                    if i < 3:
                        texto1[1] += str(VerNumeroHabitacion(usuario).pop( -1 - i ))
                        texto2[1] += str(VerNumeroEstacionamiento(usuario).pop(-1 - i))
                    if i < 2:
                        texto1[1] += ", "
                        texto2[1] += ", "
                
            except:
                """"""
            screen.blit( fuente.render(texto1[1] , True , (0,0,0) ), texto1[0] )
            screen.blit( fuente.render(texto2[1] , True , (0,0,0) ), texto2[0] )
            

        elif fondo_actual[0] == "menu bedroom":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))

            
        elif fondo_actual[0] == "menu amenities":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))


        elif fondo_actual[0] == "ver datos":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))


        elif fondo_actual[0] == "reservar eventos":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))


        elif fondo_actual[0] == "reservar habitacion":
            screen.blit (fondos[fondo_actual[1]] , (0 , 0))


        if fondo_actual[0] in ["datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "menu salon", "reservar habitacion"]:
            screen.blit (barra_arriba, (0,0))


        if fondo_actual[0] in [ "reservar eventos","ver datos","habitacion balcon", "habitacion triple", "habitacion doble", "habitacion lujo", "habitacion cuadruple", "suite rio", "habitacion individual", "suite jacuzzi", "suite estandar"]:
                screen.blit(fondos[fondo_actual[1]],(0,0))
                screen.blit(barra_arriba,(0,0))


        if alter_usuario:
            screen.blit (imagen_usuario , (958, 129))


    pygame.display.flip()



pygame.quit()
