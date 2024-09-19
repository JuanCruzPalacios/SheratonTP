import tkinter

import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True



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




    screen.fill("purple")


    pygame.display.flip()



pygame.quit()
