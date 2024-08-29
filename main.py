import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Colores
color_fondo = "#FEF7E4"

# Estado de pantalla completa
pantalla_completa = True

def iniciar_sesion():
    correo = entrada_correo.get()
    contrasena = entrada_contrasena.get()
    print(f"Correo: {correo}")
    print(f"Contraseña: {contrasena}")
    # Aquí puedes añadir el código para manejar la autenticación.

def alternar_pantalla_completa(event=None):
    global pantalla_completa
    pantalla_completa = not pantalla_completa  # Cambia el estado
    ventana.attributes("-fullscreen", pantalla_completa)  # Aplica el estado
    if not pantalla_completa:
        ventana.geometry("1280x720")  # Tamaño cuando no está en pantalla completa

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.attributes("-fullscreen", pantalla_completa)
ventana.configure(bg=color_fondo)

# Asignar la tecla "F11" para alternar pantalla completa
ventana.bind("<F11>", alternar_pantalla_completa)

# Asignar la tecla "Esc" para salir del modo pantalla completa
ventana.bind("<Escape>", lambda event: ventana.attributes("-fullscreen", False))

# Cargar la imagen del logo
imagen_logo = Image.open("imagenes/logo.png")  # Ruta de la imagen
imagen_logo = imagen_logo.resize((450, 450), Image.LANCZOS)
logo = ImageTk.PhotoImage(imagen_logo)

# Crear widget de imagen
label_logo = tk.Label(ventana, image=logo, bg=color_fondo)
label_logo.pack(pady=10)

# Crear etiquetas y campos de entrada
label_correo = tk.Label(ventana, text="Correo electrónico", bg="#FAF0E6", font=("Arial", 12))
label_correo.pack(pady=(20, 5))
entrada_correo = tk.Entry(ventana, width=30)
entrada_correo.pack(pady=5)

label_contrasena = tk.Label(ventana, text="Contraseña", bg="#FAF0E6", font=("Arial", 12))
label_contrasena.pack(pady=5)
entrada_contrasena = tk.Entry(ventana, show="*", width=30)
entrada_contrasena.pack(pady=5)

# Crear botón de inicio de sesión
boton_iniciar = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
boton_iniciar.pack(pady=20)

# Iniciar la interfaz
ventana.mainloop()
