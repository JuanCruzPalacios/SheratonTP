import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def iniciar_sesion():
    correo = entrada_correo.get()
    contrasena = entrada_contrasena.get()
    print(f"Correo: {correo}")
    print(f"Contraseña: {contrasena}")
    # Aquí puedes añadir el código para manejar la autenticación.

#Colores
color_fondo = "#FEF7E4"


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry("400x300")
ventana.configure(bg=color_fondo)

# Cargar la imagen del logo
imagen_logo = Image.open("imagenes/logo.png")  # Ruta de la imagen
imagen_logo = imagen_logo.resize((100, 100), Image.ANTIALIAS)
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
