import tkinter as tk
from tkinter import ttk, messagebox


# Clase principal

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda")
        self.root.geometry("450x400")

        # Frame principal
        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(pady=10)

        # TreeView (lista de eventos)
        self.tree = ttk.Treeview(self.frame_principal, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.pack()

        # Frame de entradas
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=10)

        # Labels y Entry
        tk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.fecha_entry = tk.Entry(self.frame_entrada)
        self.fecha_entry.grid(row=0, column=1)

        tk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(self.frame_entrada)
        self.hora_entry.grid(row=1, column=1)

        tk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(self.frame_entrada)
        self.desc_entry.grid(row=2, column=1)

        # Frame de botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        # Botones
        tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(self.frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        tk.Button(self.frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)


    # Método para agregar evento

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        desc = self.desc_entry.get()

        # Validación básica
        if fecha and hora and desc:
            self.tree.insert("", "end", values=(fecha, hora, desc))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")


    # Método para eliminar evento

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento?")
            if confirmacion:
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Error", "Seleccione un evento")


    # Limpiar campos

    def limpiar_campos(self):
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)


# Ejecución del programa

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()