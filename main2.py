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
fondo_reservar = pygame.transform.scale(pygame.image.load("imagenes/suite_parking.jpg"), (1280, 720))
fondo_pagar = pygame.transform.scale(pygame.image.load("imagenes/reserva_de_habitacion.jpg"), (1280, 720))

fondo_menu_habitaciones = pygame.transform.scale(pygame.image.load("imagenes/menu_habitaciones.jpg"), (1280, 720))
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





fondo_actual = ["iniciar sesion", 0]
fondos = [ fondo_iniciar_sesion, fondo_registrarse, 
           fondo_estacionamiento, fondo_habitacion, fondo_reservar,fondo_pagar, fondo_menu_habitaciones,
           fondo_menu_amenities, fondo_menu_salones, fondo_datos_usuario,fondo_menu_mantenimiento,
           fondo_mantenimiento_stock, fondo_mantenimiento_notificaciones, 
           fondo_mantenimiento_notificaciones_archivadas, fondo_menu_recepcionista, fondo_recepcionista_notificar,
           fondo_recepcinista_eventos, fondo_recepcinista_limpieza]

fuente = pygame.font.Font("fuentes/Averia_Libre/AveriaLibre-Regular.ttf", 31)

texto1 = [(0,0), ""]
texto2 = [(0,0), ""]
texto3 = [(0,0), ""]
texto4 = [(0,0), ""]
texto5 = [(0,0), ""]
texto6 = [(0,0), ""]
texto7 = [(0,0), ""]
texto8 = [(0,0), ""]


texto_seleccionado = ["", texto1 ]
texto_ingresado = ""














def cursor(mouse_pos):
    

    if fondo_actual[0] == "iniciar sesion":

        if mouse_pos[0] <= 845 and mouse_pos[0] >= 439 and mouse_pos[1] <= 525 and mouse_pos[1] >= 484:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        elif mouse_pos[0] <= 845 and mouse_pos[0] >= 439 and mouse_pos[1] <= 631 and mouse_pos[1] >= 587:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)






while running:


    for event in pygame.event.get():


        mouse_pos = pygame.mouse.get_pos()



        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.KEYDOWN:
                     
            if event.key == pygame.K_BACKSPACE:
                # Al presionar Retroceso, eliminar el último carácter del texto
                texto_ingresado = texto_ingresado[:-1]
                
    
            elif event.key == pygame.K_ESCAPE:
                texto_seleccionado[0] = ""
                
            else:                                    
            # Agregar caracteres al texto ingresado
                texto_ingresado += event.unicode
            texto_seleccionado[1][1] = texto_ingresado
            
                




        if event.type == pygame.MOUSEBUTTONDOWN :
            print(mouse_pos)
            if fondo_actual[0] == "iniciar sesion":
               
                if mouse_pos[0] <= 845 and mouse_pos[0] >= 439 and mouse_pos[1] <= 525 and mouse_pos[1] >= 484:
                    texto_ingresado = texto1[1]
                    texto_seleccionado[0] = "Usuario / iniciar sesion"
                    texto_seleccionado[1] = texto1
 
                   

                
                elif mouse_pos[0] <= 845 and mouse_pos[0] >= 439 and mouse_pos[1] <= 631 and mouse_pos[1] >= 587:
                    texto_ingresado = texto2[1]
                    texto_seleccionado[0] = "Contraseña / iniciar sesion"
                    texto_seleccionado[1] = texto2


            
        
        cursor(mouse_pos)

    #fondos :)
    if fondo_actual[0] == "iniciar sesion":
        texto1[0] = ( 439, 484 )
        texto2[0] = ( 439, 587 )
        screen.blit (fondos[fondo_actual[1]] , (0 , 0))       
        screen.blit( fuente.render(texto1[1] , 0 , (0,0,0) ), texto1[0] )
        screen.blit( fuente.render(texto2[1] , 0 , (0,0,0) ), texto2[0] )








    pygame.display.flip()



pygame.quit()
