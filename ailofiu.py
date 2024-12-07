import random
import tkinter as tk
from tkinter import Toplevel

import pygame
from PIL import Image, ImageTk

# Inicializar pygame.mixer para la música
pygame.mixer.init()
pygame.mixer.music.load(
    "Music/MILO J - M.A.I.mp3")  # Asegúrate de que el archivo esté en la misma carpeta o ajusta la ruta
pygame.mixer.music.play(-1)  # Reproduce en bucle

# Lista de mensajes de amor (50 mensajes)
messages = [
    "¡Feliz 3 meses, mi amor! uwu",
    "Eres la razón de mi sonrisa todos los días :3",
    "No puedo imaginar mi vida sin ti <3",
    "Gracias por ser mi refugio en todo momento, wiuu",
    "Cada instante contigo es un regalo :>",
    "Eres la melodía que da vida a mi corazón uwu",
    "Amo cómo iluminas mis días grises wiii",
    "Eres mi primer pensamiento al despertar :3",
    "Tus abrazos son mi lugar favorito wiuu",
    "No hay nadie en el mundo como tú uwu",
    "Amo tu risa más que nada wiii",
    "Contigo, cada día es una aventura :>",
    "Gracias por entenderme incluso en silencio uwu",
    "Eres mi mayor bendición <3",
    "Tu amor me hace fuerte wiuu",
    "Siempre encuentro paz en tus ojos :3",
    "Tu felicidad es mi prioridad uwu",
    "Eres la persona más especial que he conocido wiii",
    "Tus palabras siempre me llenan de alegría wiuu",
    "Te amo más que las estrellas al cielo :>",
    "Gracias por ser tú mismo/a siempre uwu",
    "Mi corazón late más fuerte cuando estás cerca <3",
    "Nunca pensé que el amor podría ser tan increíble wiii",
    "Eres mi razón para creer en la magia :3",
    "Amo compartir mi mundo contigo wiuu",
    "Tu ternura es única uwu",
    "Gracias por confiar en mí siempre wiii",
    "Eres mi lugar seguro <3",
    "Te admiro más cada día :>",
    "Tu amor me inspira a ser mejor uwu",
    "Eres el sueño que nunca quiero despertar wiuu",
    "Gracias por ser mi mejor amigo/a y mi amor wiii",
    "Tu risa ilumina todo a tu alrededor :3",
    "Eres mi motivo de orgullo uwu",
    "No importa el lugar, contigo estoy en casa <3",
    "Gracias por cada pequeño detalle de amor wiuu",
    "Tus besos son mi tesoro más preciado wiii",
    "Amo cómo me haces sentir amado/a uwu",
    "Eres mi poema favorito :3",
    "Te amo con cada latido de mi corazón wiuu",
    "Tu existencia hace el mundo más hermoso uwu",
    "Gracias por traer felicidad a mi vida wiii",
    "Eres mi luz en la oscuridad :>",
    "Tus palabras siempre tocan mi alma uwu",
    "Eres todo lo que soñé y más wiuu",
    "Tu amor me hace brillar wiii",
    "Eres mi cielo y mi tierra <3",
    "Nunca olvidaré lo especial que eres para mí uwu",
    "Te amo hoy y siempre lo haré wiuu"
]

# Lista de imágenes para las 4 ventanas adicionales
images = [
    "nwn.jpeg",  # Imagen 1
    "uwu.jpeg",  # Imagen 2
    "wiu.jpeg",  # Imagen 3
    "7w7.jpeg"  # Imagen 4
]


# Función para mostrar una ventana con mensaje
def show_window(message):
    # Obtener las dimensiones de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Crear la ventana emergente
    new_window = Toplevel(root)
    new_window.title("Mensaje Especial uwu")
    new_window.geometry("300x150")  # Ajusta el tamaño de la ventana

    # Generar coordenadas aleatorias para la ventana
    x = random.randint(0, screen_width - 300)
    y = random.randint(0, screen_height - 150)
    new_window.geometry(f"300x150+{x}+{y}")

    # Mostrar el mensaje
    label_message = tk.Label(new_window, text=message, font=("Arial", 12), wraplength=250, padx=10, pady=10)
    label_message.pack(pady=10)

    # Botón para cerrar la ventana
    close_button = tk.Button(new_window, text="Cerrar wiii", command=new_window.destroy, bg="lightblue")
    close_button.pack(pady=10)


# Función para mostrar una ventana con mensaje e imagen
def show_image_window(message, image_path):
    # Obtener las dimensiones de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Crear la ventana emergente
    new_window = Toplevel(root)
    new_window.title("Mensaje Especial uwu")
    new_window.geometry("400x400")  # Ajusta el tamaño de la ventana

    # Generar coordenadas aleatorias para la ventana
    x = random.randint(0, screen_width - 400)
    y = random.randint(0, screen_height - 400)
    new_window.geometry(f"400x400+{x}+{y}")

    # Cargar la imagen
    try:
        image = Image.open(image_path)
        image = image.resize((300, 200))  # Redimensiona la imagen
        photo = ImageTk.PhotoImage(image)

        # Mostrar la imagen
        label_image = tk.Label(new_window, image=photo)
        label_image.image = photo  # Mantener una referencia de la imagen
        label_image.pack(pady=10)
    except Exception as e:
        print(f"Error al cargar la imagen {image_path}: {e}")
        label_image = tk.Label(new_window, text="Imagen no encontrada", font=("Arial", 12))
        label_image.pack(pady=10)

    # Mostrar el mensaje
    label_message = tk.Label(new_window, text=message, font=("Arial", 12), wraplength=350, padx=10, pady=10)
    label_message.pack(pady=10)

    # Botón para cerrar la ventana
    close_button = tk.Button(new_window, text="Cerrar wiii", command=new_window.destroy, bg="lightblue")
    close_button.pack(pady=10)


# Función para mostrar todas las ventanas (50 con mensaje y 4 con imagen)
def show_all_windows():
    # Mostrar las 50 ventanas con solo mensajes
    for message in messages:
        show_window(message)

    # Mostrar las 4 ventanas adicionales con imágenes y mensajes
    for i in range(4):
        show_image_window(messages[i], images[i])


# Configuración de la ventana principal
root = tk.Tk()
root.title("Feliz 3 Meses <3")
root.geometry("400x200")

# Texto inicial
label = tk.Label(
    root,
    text="¡Bienvenida, mi cielito! <3\nHaz clic para la sorpresa wiii.",
    font=("Arial", 14),
    pady=20,
)
label.pack()

# Botón para mostrar todas las ventanas
start_button = tk.Button(
    root,
    text="Mostrar Mensajes 💖",
    font=("Arial", 14),
    bg="pink",
    command=show_all_windows,
)
start_button.pack(pady=20)

# Iniciar la interfaz
root.mainloop()

# Detener la música cuando se cierre la ventana principal
pygame.mixer.music.stop()
