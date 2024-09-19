import tkinter

import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True



fondo_iniciar_sesion = pygame.image.load("imagenes/iniciar_sesion.jpg")
fondo_registrarse = pygame.image.load("imagenes/registrarse.jpg")
fondo_estacionamiento = pygame.image.load("imagenes/estacionamiento.jpg")
fondo_habitacion = pygame.image.load("imagenes/Sheraton_page-0004.jpg")
fondo_reservar = pygame.image.load("imagenes/Sheraton_page-0005.jpg")
fondo_pagar = pygame.image.load("imagenes/Sheraton_page-0006.jpg")

fondo_menu_habitaciones = pygame.image.load("imagenes/Sheraton_page-0007.jpg")
fondo_menu_amenities = pygame.image.load("imagenes/Sheraton_page-0008.jpg")
fondo_menu_salones = pygame.image.load("imagenes/Sheraton_page-0009.jpg")
fondo_datos_usuario = pygame.image.load("imagenes/Sheraton_page-0010.jpg")
fondo_menu_mantenimiento = pygame.image.load("imagenes/Sheraton_page-0011.jpg")

fondo_mantenimiento_stock = pygame.image.load("imagenes/Sheraton_page-0012.jpg")
fondo_mantenimiento_notificaciones = pygame.image.load("imagenes/Sheraton_page-0015.jpg")
fondo_mantenimiento_notificaciones_archivadas = pygame.image.load("imagenes/Sheraton_page-0018.jpg")

fondo_menu_recepcionista = pygame.image.load("imagenes/Sheraton_page-0013.jpg")
fondo_recepcionista_notificar = pygame.image.load("imagenes/Sheraton_page-0014.jpg")
fondo_recepcinista_eventos = pygame.image.load("imagenes/Sheraton_page-0016.jpg")
fondo_recepcinista_limpieza = pygame.image.load("imagenes/Sheraton_page-0017.jpg")




fondo_actual = ["iniciar sesion", 0]
fondos = [ fondo_iniciar_sesion, fondo_registrarse, 
           fondo_estacionamiento, fondo_habitacion, fondo_reservar,fondo_pagar, fondo_menu_habitaciones,
           fondo_menu_amenities, fondo_menu_salones, fondo_datos_usuario,fondo_menu_mantenimiento,
           fondo_mantenimiento_stock, fondo_mantenimiento_notificaciones, 
           fondo_mantenimiento_notificaciones_archivadas, fondo_menu_recepcionista, fondo_recepcionista_notificar,
           fondo_recepcinista_eventos, fondo_recepcinista_limpieza]





while running:


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
          
            if event.key == pygame.K_RETURN:
                # Al presionar Enter, guardar el texto ingresado y limpiar el campo
                texto_entrado = texto_ingresado
                enter = True
                texto_ingresado = ""
                campo_activo = False

                
            elif event.key == pygame.K_BACKSPACE:
                # Al presionar Retroceso, eliminar el último carácter del texto
                texto_ingresado = texto_ingresado[:-1]
                
    
            elif event.key == pygame.K_ESCAPE:
                creando = False
                agregando = False
                modificando = False
                campo_activo = False
                enter = False
                una_vez = 0
                contador = 0

                
            else:                                    
            # Agregar caracteres al texto ingresado
                texto_ingresado += event.unicode






    if fondo_actual[0] == "iniciar sesion": 
        


    pygame.display.flip()



pygame.quit()
