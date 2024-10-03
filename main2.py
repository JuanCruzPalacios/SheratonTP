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

imagen_usuario = pygame.transform.scale(pygame.image.load("imagenes/usuario.png"), (321, 394))
alter_usuario = False


fondo_actual = ["iniciar sesion", 0]
fondos = [  fondo_iniciar_sesion, fondo_registrarse, 
            #0                    #1
            fondo_estacionamiento, fondo_habitacion,
            #2                     #3
            fondo_reservar, fondo_pagar , fondo_menu_habitaciones,
            #4              #5            #6
            fondo_menu_amenities, fondo_menu_salones, fondo_datos_usuario, fondo_menu_mantenimiento,
            #7                   #7                  #8                   #9
            fondo_mantenimiento_stock, fondo_mantenimiento_notificaciones, 
            #10                        #11
            fondo_mantenimiento_notificaciones_archivadas, fondo_menu_recepcionista, fondo_recepcionista_notificar,
            #12                                            #13                       #14
            fondo_recepcinista_eventos, fondo_recepcinista_limpieza]
            #15                         #16

fuente = pygame.font.Font("fuentes/Averia_Libre/AveriaLibre-Regular.ttf", 31)
limite = 13
texto1 = [(0,0), ""]
texto2 = [(0,0), ""]
texto3 = [(0,0), ""]
texto4 = [(0,0), ""]
texto5 = [(0,0), ""]
texto6 = [(0,0), ""]
texto7 = [(0,0), ""]
texto8 = [(0,0), ""]




texto_seleccionado =  texto1 
texto_ingresado = ""






def cursor(mouse_pos):
    


    if fondo_actual[0] == "iniciar sesion":


        if mouse_pos[0] <= 845 and mouse_pos[0] >= 439 and mouse_pos[1] <= 525 and mouse_pos[1] >= 484: #-----> Usuario
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        elif mouse_pos[0] <= 845 and mouse_pos[0] >= 439 and mouse_pos[1] <= 631 and mouse_pos[1] >= 587:#-----> Contraseña
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif mouse_pos[0] <= 900 and mouse_pos[0] >= 862 and mouse_pos[1] <= 660 and mouse_pos[1] >= 630:#-----> Siguiente
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_pos[0] <= 744 and mouse_pos[0] >= 539 and mouse_pos[1] <= 682 and mouse_pos[1] >= 673:#-----> Crear cuenta
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    elif fondo_actual[0] in ["datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "menu salon"]:


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

        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


    elif fondo_actual[0] == "registrarse":


        if mouse_pos[0] <= 844 and mouse_pos[0] >= 440 and mouse_pos[1] <= 500 and mouse_pos[1] >= 470: #-----> Usuario
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        elif mouse_pos[0] <= 844 and mouse_pos[0] >= 440 and mouse_pos[1] <= 581 and mouse_pos[1] >= 551:#-----> Correo Electronico
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

        elif mouse_pos[0] <= 844 and mouse_pos[0] >= 440 and mouse_pos[1] <= 653 and mouse_pos[1] >= 621: #-----> Contraseña
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)


        elif mouse_pos[0] <= 908 and mouse_pos[0] >= 852 and mouse_pos[1] <= 675 and mouse_pos[1] >= 630:#-----> Siguiente
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif mouse_pos[0] <= 748 and mouse_pos[0] >= 522 and mouse_pos[1] <= 683 and mouse_pos[1] >= 673:#-----> Crear cuenta
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)



    elif fondo_actual[0] == "menu habitaciones":



        if mouse_pos[0] < 295 and mouse_pos[0] > 195 and mouse_pos[1] < 290 and mouse_pos[1] > 260:#personas        
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 150 and mouse_pos[0] > 55 and mouse_pos[1] < 417 and mouse_pos[1] > 385:#precio "desde"
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 290 and mouse_pos[0] > 195 and mouse_pos[1] < 417 and mouse_pos[1] > 385:#precio "hasta"
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        elif mouse_pos[0] < 252 and mouse_pos[0] > 92 and mouse_pos[1] < 495 and mouse_pos[1] > 463:#buscar
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)






def chequeo_contraseña(conteraseña):
    if len(conteraseña) > 8:
        if  any( caracter in conteraseña for caracter in ["@", "#", "$", "*", "%", "&", "/", "!", "?", "-", "_"] ):
            if any( caracter in conteraseña for caracter in ["1","2","3","4","5","6","7","8","9","0"] ):
                return "aprobado"
            else:   
                return "Debe haber algun numero"
        else:
            return "Debe haber algun caracteres especiales"    
    else:
        return "La contraseña debe ser de al menos 8 caracteres"






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
                texto_seleccionado = ""
                
            else:                 
                if len(texto_ingresado) < limite:           
                    # Agregar caracteres al texto ingresado
                    texto_ingresado += event.unicode
            texto_seleccionado[1] = texto_ingresado
            
                

        if event.type == pygame.MOUSEBUTTONDOWN :


            print(mouse_pos)


            if fondo_actual[0] == "iniciar sesion":
               
                if mouse_pos[0] <= 845 and mouse_pos[0] >= 439 and mouse_pos[1] <= 525 and mouse_pos[1] >= 484: #-----> Usuario
                    texto_ingresado = texto1[1]
                    texto_seleccionado = texto1 #Usuario / iniciar sesion
                    limite = 13

                   
           
                elif mouse_pos[0] <= 845 and mouse_pos[0] >= 439 and mouse_pos[1] <= 631 and mouse_pos[1] >= 587: #-----> Contraseña                    
                    texto_ingresado = texto2[1]
                    texto_seleccionado = texto2 #Contraseña / iniciar sesion
                    limite = 13



                elif mouse_pos[0] <= 900 and mouse_pos[0] >= 862 and mouse_pos[1] <= 660 and mouse_pos[1] >= 630:#-----> Siguiente
                    

                    if ExisteUsuario(texto1[1]):

                        if VerificarContraseña(texto1[1],texto2[1]):

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



                elif mouse_pos[0] <= 744 and mouse_pos[0] >= 539 and mouse_pos[1] <= 682 and mouse_pos[1] >= 673:#-----> Crear cuenta
                    fondo_actual[0] = "registrarse"
                    fondo_actual[1] = 1
                    texto_ingresado = ""
                    texto1 = [(0,0),""]
                    texto2 = [(0,0),""]
                    texto3 = [(0,0),""]                

   


            elif fondo_actual[0] == "registrarse":   


                if mouse_pos[0] <= 844 and mouse_pos[0] >= 440 and mouse_pos[1] <= 500 and mouse_pos[1] >= 470: #-----> Usuario

                    texto_seleccionado = texto1 #usuario / registrarse
                    texto_ingresado = texto1[1]
                    limite = 13



                elif mouse_pos[0] <= 844 and mouse_pos[0] >= 440 and mouse_pos[1] <= 581 and mouse_pos[1] >= 551:#-----> Correo Electronico

                    texto_seleccionado = texto2 #mail / registrarse
                    texto_ingresado = texto2[1]
                    limite = 13



                elif mouse_pos[0] <= 844 and mouse_pos[0] >= 440 and mouse_pos[1] <= 653 and mouse_pos[1] >= 621: #-----> Contraseña
 
                    texto_seleccionado = texto3 #contraseña / registrarse
                    texto_ingresado = texto3[1]
                    limite = 13



                elif mouse_pos[0] <= 908 and mouse_pos[0] >= 852 and mouse_pos[1] <= 675 and mouse_pos[1] >= 630:#-----> Siguiente / Registrarse
            
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



                          
                elif mouse_pos[0] <= 748 and mouse_pos[0] >= 522 and mouse_pos[1] <= 683 and mouse_pos[1] >= 673:#-----> Iniciar Sesion
                    fondo_actual[0] = "iniciar sesion"
                    fondo_actual[1] = 0
                    texto_ingresado = ""
                    texto1 = [(0,0),""]
                    texto2 = [(0,0),""]               




            elif fondo_actual[0] in ["datos usuario", "menu parking", "menu bedroom", "menu habitaciones", "menu amenities", "menu salon"]:


                if mouse_pos[0] < 410 and mouse_pos[0] > 290 and mouse_pos[1] < 100 and mouse_pos[1] > 15: #Home 
                    fondo_actual[0] = "menu habitaciones"
                    fondo_actual[1] = 6



                elif mouse_pos[0] < 560 and mouse_pos[0] > 435 and mouse_pos[1] < 100 and mouse_pos[1] > 15:#Parking
                    fondo_actual[0] = "menu parking"
                    fondo_actual[1] = 2



                elif mouse_pos[0] < 710 and mouse_pos[0] > 590 and mouse_pos[1] < 100 and mouse_pos[1] > 15:#Bedroom
                    fondo_actual[0] = "menu bedroom"
                    fondo_actual[1] = 3



                elif mouse_pos[0] < 860 and mouse_pos[0] > 745 and mouse_pos[1] < 100 and mouse_pos[1] > 15:#Services
                    fondo_actual[0] = "menu amenities"
                    fondo_actual[1] = 7
                

                elif mouse_pos[0] < 1220 and mouse_pos[0] > 1140 and mouse_pos[1] < 90 and mouse_pos[1] > 18:#boton usuario
                    alter_usuario = not(alter_usuario)
                    print(alter_usuario)



            elif fondo_actual[0] == "menu habitaciones":


                if mouse_pos[0] < 295 and mouse_pos[0] > 195 and mouse_pos[1] < 290 and mouse_pos[1] > 260:#personas        
                    texto_seleccionado = texto1
                    texto_ingresado = texto1[1]
                    limite = 3



                elif mouse_pos[0] < 150 and mouse_pos[0] > 55 and mouse_pos[1] < 417 and mouse_pos[1] > 385:#precio "desde"
                    texto_seleccionado = texto2
                    texto_ingresado = texto2[1]
                    limite = 3



                elif mouse_pos[0] < 290 and mouse_pos[0] > 195 and mouse_pos[1] < 417 and mouse_pos[1] > 385:#precio "hasta"
                    texto_seleccionado = texto3
                    texto_ingresado = texto3[1]
                    limite = 3










        cursor(mouse_pos)

    #fondos :)

 


    if fondo_actual[0] == "iniciar sesion":
        texto1[0] = ( 445 , 484 )
        texto2[0] = ( 445 , 587 )
        texto3[0] = ( 350 , 375 )
        screen.blit (fondos[fondo_actual[1]] , (0 , 0))       
        screen.blit( fuente.render(texto1[1] , 0 , (0,0,0) ), texto1[0] )
        screen.blit( fuente.render(texto2[1] , 0 , (0,0,0) ), texto2[0] )
        screen.blit( fuente.render(texto3[1] , 0 , (0,0,0) ), texto3[0] )

    
    elif fondo_actual[0] == "registrarse":
        screen.blit (fondos[fondo_actual[1]] , (0 , 0)) 
        texto1[0] = ( 445 , 465 )
        texto2[0] = ( 445 , 545 )    
        texto3[0] = ( 445 , 615 ) 
        texto4[0] = ( 350 , 375 )
        screen.blit( fuente.render(texto1[1] , 0 , (0,0,0) ), texto1[0] )
        screen.blit( fuente.render(texto2[1] , 0 , (0,0,0) ), texto2[0] )  
        screen.blit( fuente.render(texto3[1] , 0 , (0,0,0) ), texto3[0] )
        screen.blit( fuente.render(texto4[1] , 0 , (0,0,0) ), texto4[0] )        


    elif fondo_actual[0] == "menu habitaciones":
        screen.blit (fondos[fondo_actual[1]] , (0 , 0))   
        texto1[0] = ( 200 , 255 )
        texto2[0] = ( 60  , 383 )    
        texto3[0] = ( 198 , 383 ) 
        screen.blit( fuente.render(texto1[1] , 0 , (0,0,0) ), texto1[0] )
        screen.blit( fuente.render(texto2[1] , 0 , (0,0,0) ), texto2[0] )  
        screen.blit( fuente.render(texto3[1] , 0 , (0,0,0) ), texto3[0] )   


    elif fondo_actual[0] == "menu parking":
        screen.blit (fondos[fondo_actual[1]] , (0 , 0))


    elif fondo_actual[0] == "menu bedroom":
        screen.blit (fondos[fondo_actual[1]] , (0 , 0))

        
    elif fondo_actual[0] == "menu amenities":
        screen.blit (fondos[fondo_actual[1]] , (0 , 0))


    if alter_usuario:
        screen.blit (imagen_usuario , (958, 111))  



    pygame.display.flip()



pygame.quit()
