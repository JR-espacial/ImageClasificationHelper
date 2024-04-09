import os
import shutil
from tkinter import Tk, Label, Button, Checkbutton, IntVar
from PIL import Image, ImageTk

class ImageClassifier:
    def __init__(self, master):
        self.master = master
        master.title("Image Classifier")  # Título de la ventana

        # Etiqueta para mostrar la imagen
        self.label = Label(master)
        self.label.pack()

        # Botones para cada categoría
        self.vaca_var = IntVar()
        self.vaca_checkbox = Checkbutton(master, text="Vaca", variable=self.vaca_var)
        self.vaca_checkbox.pack()

        self.no_vaca_var = IntVar()
        self.no_vaca_checkbox = Checkbutton(master, text="No Vaca", variable=self.no_vaca_var)
        self.no_vaca_checkbox.pack()

        self.dia_var = IntVar()
        self.dia_checkbox = Checkbutton(master, text="Dia", variable=self.dia_var)
        self.dia_checkbox.pack()

        self.noche_var = IntVar()
        self.noche_checkbox = Checkbutton(master, text="Noche", variable=self.noche_var)
        self.noche_checkbox.pack()

        self.parda_var = IntVar()
        self.parda_checkbox = Checkbutton(master, text="Parda", variable=self.parda_var)
        self.parda_checkbox.pack()

        self.sentada_var = IntVar()
        self.sentada_checkbox = Checkbutton(master, text="Sentada", variable=self.sentada_var)
        self.sentada_checkbox.pack()

        self.ruido_var = IntVar()
        self.ruido_checkbox = Checkbutton(master, text="Ruido", variable=self.ruido_var)
        self.ruido_checkbox.pack()

        # Botón para copiar la imagen
        self.copy_button = Button(master, text="Siguiente", command=self.copy_image)
        self.copy_button.pack()

        # Inicialización de variables
        self.image_index = 0
        self.images = self.load_images("./batch")

        # Mostrar la primera imagen
        self.show_image()

    def load_images(self, directory):
        """Cargar la lista de imágenes desde el directorio especificado"""
        return [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith(('.jpg', '.jpeg', '.png'))]

    def show_image(self):
        """Mostrar la imagen actual en la interfaz gráfica"""
        if self.image_index < len(self.images):
            image_path = self.images[self.image_index]
            image = Image.open(image_path)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.label.config(image=photo)
            self.label.image = photo
        else:
            self.label.config(text="No hay más imágenes para clasificar.")

    def copy_image(self):
        """Crear copias de la imagen actual en las carpetas correspondientes a las categorías seleccionadas"""
        image_path = self.images[self.image_index]
        
        # Obtener las categorías seleccionadas
        categories = []
        if self.vaca_var.get():
            categories.append("vaca")
        if self.no_vaca_var.get():
            categories.append("no_vaca")
        if self.dia_var.get():
            categories.append("dia")
        if self.noche_var.get():
            categories.append("noche")
        if self.parda_var.get():
            categories.append("parda")
        if self.sentada_var.get():
            categories.append("sentada")
        if self.ruido_var.get():
            categories.append("ruido")

        # Crear copias de la imagen en las carpetas correspondientes
        for category in categories:
            new_directory = f"./{category}"
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
            shutil.copy2(image_path, new_directory)
        
        self.image_index += 1
        self.show_image()

if __name__ == "__main__":
    # Crear la ventana de la interfaz gráfica
    root = Tk()
    my_gui = ImageClassifier(root)
    root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica
