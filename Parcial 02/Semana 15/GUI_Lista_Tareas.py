import tkinter as tk
from tkinter import messagebox

# Clase principal
class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista donde se guardan las tareas
        self.tareas = []

        # Campo de entrada para escribir tareas
        self.entry = tk.Entry(root, width=60)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.agregar_tarea_evento)  # Enter agrega tarea

        # Lista visual donde se muestran las tareas
        self.listbox = tk.Listbox(root, width=70, height=10)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.marcar_completada_evento)  # Doble clic

        # Contenedor de botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        # Botón para añadir tarea
        self.btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        # Botón para marcar como completada
        self.btn_completar = tk.Button(frame_botones, text="Marcar o Desmarcar Tarea", command=self.marcar_completada)
        self.btn_completar.grid(row=0, column=1, padx=5)

        # Botón para eliminar tarea
        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

    # Agrega una nueva tarea a la lista
    def agregar_tarea(self):
        tarea = self.entry.get().strip()  # Obtener texto
        if tarea:
            # Guardar tarea con estado (no completada)
            self.tareas.append({"texto": tarea, "completada": False})
            self.actualizar_lista()
            self.entry.delete(0, tk.END)  # Limpiar entrada
        else:
            messagebox.showwarning("Advertencia", "Ingrese una tarea")

    # Evento al presionar Enter
    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    # Cambia el estado de la tarea seleccionada
    def marcar_completada(self):
        try:
            indice = self.listbox.curselection()[0]  # Obtener selección
            # Cambiar estado (True/False)
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea")

    # Evento doble clic
    def marcar_completada_evento(self, event):
        self.marcar_completada()

    # Elimina la tarea seleccionada
    def eliminar_tarea(self):
        try:
            indice = self.listbox.curselection()[0]
            del self.tareas[indice]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea")

    # Actualiza lo que se muestra en pantalla
    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)  # Limpiar lista visual
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto += " ✔"  # Indicador de completado
            self.listbox.insert(tk.END, texto)


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()