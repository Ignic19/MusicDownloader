import tkinter as tk
from pytube import YouTube

# Función para descargar video o música según la selección del usuario
def descargar_contenido():
    # Obtén el enlace de YouTube desde la entrada
    enlace = enlace_entry.get()
    
    try:
        # Crea una instancia de YouTube
        yt = YouTube(enlace)
        
        if seleccion.get() == 1:
            # Descargar el video con la mejor calidad disponible
            stream = yt.streams.get_highest_resolution()
            stream.download()
            mensaje_label.config(text="Descarga de video completa")
        elif seleccion.get() == 2:
            # Descargar el audio del video con la mejor calidad disponible
            stream = yt.streams.filter(only_audio=True).first()
            stream.download()
            mensaje_label.config(text="Descarga de música completa")
        else:
            mensaje_label.config(text="Selecciona una opción")
    except Exception as e:
        mensaje_label.config(text="Error: " + str(e))

# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Descargador de Contenido de YouTube")

# Etiqueta de instrucciones
instrucciones_label = tk.Label(ventana, text="Pegue el enlace de YouTube:")
instrucciones_label.pack(pady=10)

# Campo de entrada para el enlace de YouTube
enlace_entry = tk.Entry(ventana, width=40)
enlace_entry.pack()

# Etiqueta para seleccionar el tipo de contenido
seleccion_label = tk.Label(ventana, text="Selecciona el tipo de contenido:")
seleccion_label.pack()

# Variable para almacenar la selección del usuario
seleccion = tk.IntVar()

# Botones de selección: Video y Música
video_radio = tk.Radiobutton(ventana, text="Video", variable=seleccion, value=1)
video_radio.pack()
musica_radio = tk.Radiobutton(ventana, text="Música", variable=seleccion, value=2)
musica_radio.pack()

# Botón de descarga
descargar_button = tk.Button(ventana, text="Descargar Contenido", command=descargar_contenido)
descargar_button.pack(pady=10)

# Etiqueta para mostrar mensajes
mensaje_label = tk.Label(ventana, text="")
mensaje_label.pack()

ventana.mainloop()