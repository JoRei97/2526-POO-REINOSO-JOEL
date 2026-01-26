
# Clase que representa un videojuego.

class Videojuego:

    def __init__(self, titulo, genero, plataforma):

        # Constructor:Se ejecuta al crear el objeto, inicializa los atributos del videojuego.

        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma
        print(f"Videojuego '{self.titulo}' cargado correctamente.")

    def iniciar_juego(self):
        """
        Método que simula iniciar el videojuego.
        """
        print(f"Iniciando '{self.titulo}' en {self.plataforma}...")

    def mostrar_informacion(self):
        """
        Método que muestra la información del videojuego.
        """
        print("Información del videojuego:")
        print(f"Título: {self.titulo}")
        print(f"Género: {self.genero}")
        print(f"Plataforma: {self.plataforma}")

    def __del__(self):

        # Destructor:Se ejecuta cuando el objeto es eliminado o cuando finaliza el programa, libera recursos .

        print(f"Videojuego '{self.titulo}' cerrado y recursos liberados.")


    # Programa principal
if __name__ == "__main__":
    juego1 = Videojuego("DOTA2", "Moba", "PC")
    juego1.iniciar_juego()
    juego1.mostrar_informacion()

    # El destructor se ejecuta automáticamente al finalizar el programa
