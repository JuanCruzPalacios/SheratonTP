import tkinter as tk
from PIL import Image, ImageTk, ImageFont, ImageDraw

# Colores
color_fondo = "#FEF7E4"
color_recuadro = "#F2E6C6"
marron = "#6A4D52"
color_texto = marron  # Color del texto de las etiquetas

# Ruta del archivo de la fuente
ruta_fuente = "fuentes/Averia_Libre/AveriaLibre-Regular.ttf"

# Estado de pantalla completa
pantalla_completa = True

def iniciar_sesion():
    correo = entrada_correo.get()
    contrasena = entrada_contrasena.get()
    print(f"Correo: {correo}")
    print(f"Contraseña: {contrasena}")
    # Aquí puedes añadir el código para manejar la autenticación.
    cambiar_pagina()

def alternar_pantalla_completa(event=None):
    global pantalla_completa
    pantalla_completa = not pantalla_completa  # Cambia el estado
    ventana.attributes("-fullscreen", pantalla_completa)  # Aplica el estado
    if not pantalla_completa:
        ventana.geometry("1280x720")  # Tamaño cuando no está en pantalla completa
    ventana.resizable(False, False)

def dibujar_recuadro_redondeado(canvas, x, y, ancho, alto, radio, color):
    canvas.create_oval(x, y, x + radio * 2, y + radio * 2, fill=color, outline=color)
    canvas.create_oval(x + ancho - radio * 2, y, x + ancho, y + radio * 2, fill=color, outline=color)
    canvas.create_oval(x + ancho - radio * 2, y + alto - radio * 2, x + ancho, y + alto, fill=color, outline=color)
    canvas.create_oval(x, y + alto - radio * 2, x + radio * 2, y + alto, fill=color, outline=color)
    canvas.create_rectangle(x + radio, y, x + ancho - radio, y + alto, fill=color, outline=color)
    canvas.create_rectangle(x, y + radio, x + ancho, y + alto - radio, fill=color, outline=color)

def crear_imagen_con_texto(texto, fuente, tamaño, color, ancho , alto):
    # Crear una imagen en blanco
    imagen = Image.new('RGBA', (ancho, alto), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(imagen)
    
    # Cargar la fuente
    font = ImageFont.truetype(fuente, tamaño)
    
    # Calcular el tamaño del texto y la posición
    texto_width, texto_height = draw.textsize(texto, font=font)
    posicion = ((imagen.width - texto_width) // 2, (imagen.height - texto_height) // 2)
    
    # Dibujar el texto
    draw.text(posicion, texto, font=font, fill=color)
    
    return imagen

def cambiar_pagina():
    # Destruir todos los widgets de la ventana actual para simular un cambio de página
    for widget in ventana.winfo_children():
        widget.destroy()

    # Aquí puedes añadir el contenido de la nueva "página"
    nuevo_label = tk.Label(ventana, text="Bienvenido a la siguiente página", font=("Helvetica", 24), bg=color_fondo)
    nuevo_label.pack(pady=20)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.attributes("-fullscreen", pantalla_completa)
ventana.configure(bg=color_fondo)

# Asignar la tecla "F11" para alternar pantalla completa
ventana.bind("<F11>", alternar_pantalla_completa)

# Cargar la imagen del logo
imagen_logo = Image.open("imagenes/logo.png")  # Ruta de la imagen
imagen_logo = imagen_logo.resize((450, 450), Image.LANCZOS)
logo = ImageTk.PhotoImage(imagen_logo)

# Crear widget de imagen
label_logo = tk.Label(ventana, image=logo, bg=color_fondo)
label_logo.pack(pady=10)

# Crear un Canvas para dibujar el recuadro con bordes redondeados
canvas_recuadro = tk.Canvas(ventana, width=600, height=400, bg=color_fondo, bd=0, highlightthickness=0)
canvas_recuadro.place(relx=0.5, rely=0.85, anchor="center")

# Dibujar el recuadro redondeado
dibujar_recuadro_redondeado(canvas_recuadro, 75, 0, 450, 250, 20, color_recuadro)

# Crear campos de entrada directamente en el Canvas para que se alineen correctamente
entrada_correo = tk.Entry(ventana, bg=color_fondo, bd=0, highlightthickness=2, highlightbackground=marron, relief="solid", font=("Helvetica", 14), width=35)
entrada_correo.place(relx=0.5, rely=0.70, anchor="center")

entrada_contrasena = tk.Entry(ventana, bg=color_fondo, bd=0, highlightthickness=2, highlightbackground=marron, relief="solid", show="*", font=("Helvetica", 14), width=35)
entrada_contrasena.place(relx=0.5, rely=0.83, anchor="center")

# Crear imágenes para las etiquetas
imagen_correo = ImageTk.PhotoImage(crear_imagen_con_texto("Correo electrónico", ruta_fuente, 32, marron, 300, 30))
imagen_contrasena = ImageTk.PhotoImage(crear_imagen_con_texto("Contraseña", ruta_fuente, 32, marron, 300, 30))

# Crear etiquetas con las imágenes
label_correo = tk.Label(ventana, image=imagen_correo, bg=color_recuadro)
label_correo.place(relx=0.5, rely=0.65, anchor="center")

label_contrasena = tk.Label(ventana, image=imagen_contrasena, bg=color_recuadro)
label_contrasena.place(relx=0.5, rely=0.78, anchor="center")

# Cargar la imagen para el botón "Enter"
imagen_boton_enter = Image.open("imagenes/enter.png")  # Ruta de la imagen de botón
imagen_boton_enter = imagen_boton_enter.resize((44 , 44), Image.LANCZOS)
boton_enter_img = ImageTk.PhotoImage(imagen_boton_enter)

# Crear el botón "Enter"
boton_enter = tk.Button(ventana, image=boton_enter_img, bg=color_recuadro, bd=0, command=iniciar_sesion)
boton_enter.place(relx=0.64, rely=0.88, anchor="center")

# Iniciar la interfaz
ventana.mainloop()
