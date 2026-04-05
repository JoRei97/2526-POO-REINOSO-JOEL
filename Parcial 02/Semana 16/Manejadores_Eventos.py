import tkinter as tk
from tkinter import messagebox

class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Lista de tareas: [texto, estado]
        self.tareas = []

        # ====== INTERFAZ ======
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # Entrada de texto
        self.entry = tk.Entry(self.frame, width=40)
        self.entry.grid(row=0, column=0, columnspan=3, pady=5)

        # Lista de tareas
        self.lista = tk.Listbox(self.frame, width=50, height=10)
        self.lista.grid(row=1, column=0, columnspan=3, pady=5)

        # Botones
        tk.Button(self.frame, text="Agregar", command=self.agregar_tarea).grid(row=2, column=0)
        tk.Button(self.frame, text="Completar / Desmarcar", command=self.toggle_tarea).grid(row=2, column=1)
        tk.Button(self.frame, text="Eliminar", command=self.eliminar_tarea).grid(row=2, column=2)

        # ====== ATAJOS ======
        self.root.bind("<Return>", lambda e: self.agregar_tarea())      # Enter
        self.root.bind("c", lambda e: self.completar_tarea())           # completar
        self.root.bind("d", lambda e: self.desmarcar_tarea())           # desmarcar
        self.root.bind("<Delete>", lambda e: self.eliminar_tarea())     # eliminar
        self.root.bind("<Escape>", lambda e: self.root.quit())          # cerrar programa

    # Agregar tarea
    def agregar_tarea(self):
        texto = self.entry.get().strip()
        if texto:
            self.tareas.append([texto, False])  # False = pendiente
            self.actualizar_lista()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Escribe una tarea")

    # Alternar estado (botón)
    def toggle_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index][1] = not self.tareas[index][1]
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    #  marcar como completada (tecla C)
    def completar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index][1] = True
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    # desmarcar (tecla D)
    def desmarcar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index][1] = False
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    # Eliminar tarea
    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            del self.tareas[index]
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    # Actualizar lista visual
    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea, estado in self.tareas:
            if estado:
                self.lista.insert(tk.END, f"✔ {tarea}")
                self.lista.itemconfig(tk.END, fg="gray")
            else:
                self.lista.insert(tk.END, f"✘ {tarea}")
                self.lista.itemconfig(tk.END, fg="black")


# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()