
# APLICACIÓN GUI BÁSICA

import tkinter as tk
from tkinter import messagebox


# Clase que contiene la aplicacion
class AplicacionGUI:

    # Constructor inicializa la ventana y los componentes
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Aplicación GUI Básica")
        self.ventana.geometry("400x400")

        # Etiqueta
        self.label = tk.Label(ventana, text="Ingrese un dato:")
        self.label.pack(pady=5)

        # Campo de texto
        self.entrada = tk.Entry(ventana, width=30)
        self.entrada.pack(pady=5)

        # Boton  para agregar datos
        self.boton_agregar = tk.Button(
            ventana, text="Agregar", command=self.agregar_dato
        )
        self.boton_agregar.pack(pady=5)

        # Lista de datos ingresados
        self.lista = tk.Listbox(ventana, width=40, height=10)
        self.lista.pack(pady=10)

        # Boton para limpiar o eliminar datos de la lista
        self.boton_limpiar = tk.Button(
            ventana, text="Limpiar", command=self.limpiar_dato
        )
        self.boton_limpiar.pack(pady=5)

    # Metodo que agrega el dato ingresado a la lista
    def agregar_dato(self):
        dato = self.entrada.get()  # Obtener texto del campo

        if dato != "":
            self.lista.insert(tk.END, dato)  # Insertar en la lista
            self.entrada.delete(0, tk.END)   # Limpiar el campo de texto
        else:
            # Muestra un mensaje si el campo está vacío
            messagebox.showwarning("Aviso", "Ingrese un dato")

    # Método que elimina el elemento seleccionado o limpia toda la lista
    def limpiar_dato(self):
        seleccion = self.lista.curselection()

        if seleccion:
            self.lista.delete(seleccion)  # Elimina el elemento seleccionado
        else:
            self.lista.delete(0, tk.END)  # Si no hay selección, borra toda la lista


# Punto de inicio del programa
if __name__ == "__main__":
    ventana = tk.Tk()              # Crear ventana principal
    app = AplicacionGUI(ventana)   # Crear objeto de la aplicación
    ventana.mainloop()             # Ejecutar la interfaz gráfica