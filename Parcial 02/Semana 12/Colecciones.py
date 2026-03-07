# CLASE LIBRO

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla porque titulo y autor no cambiarán
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

# CLASE USUARIO

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []   # Lista de libros prestados

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

# CLASE BIBLIOTECA


class Biblioteca:
    def __init__(self):
        self.libros = {}   # Diccionario ISBN -> Libro
        self.usuarios = {} # Diccionario ID -> Usuario
        self.ids = set()   # Conjunto para evitar IDs repetidos

    # Añadir libro
    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro agregado correctamente")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids.add(usuario.id_usuario)
            print("Usuario registrado")
        else:
            print("ID de usuario ya existe")

    # Eliminar usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids.remove(id_usuario)
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]

            if libro.disponible:
                usuario = self.usuarios[id_usuario]
                usuario.prestar_libro(libro)
                libro.disponible = False
                print("Libro prestado")
            else:
                print("El libro no está disponible")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            usuario.devolver_libro(libro)
            libro.disponible = True
            print("Libro devuelto")

    # Buscar libros
    def buscar_libro(self, texto):
        print("\nResultados de búsqueda:")
        for libro in self.libros.values():
            if (texto.lower() in libro.info[0].lower() or
                texto.lower() in libro.info[1].lower() or
                texto.lower() in libro.categoria.lower()):
                print(libro.info[0], "-", libro.info[1], "-", libro.categoria)

    # Listar libros prestados
    def listar_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            print("\nLibros prestados a", usuario.nombre)

            if not usuario.libros_prestados:
                print("No tiene libros prestados")

            for libro in usuario.libros_prestados:
                print("-", libro.info[0])

# MENÚ

biblioteca = Biblioteca()

while True:

    print("\n===== BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    # Agregar libro
    if opcion == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")

        libro = Libro(titulo, autor, categoria, isbn)
        biblioteca.agregar_libro(libro)

    # Quitar libro
    elif opcion == "2":
        isbn = input("ISBN del libro a eliminar: ")
        biblioteca.quitar_libro(isbn)

    # Registrar usuario
    elif opcion == "3":
        nombre = input("Nombre del usuario: ")
        id_usuario = input("ID del usuario: ")

        usuario = Usuario(nombre, id_usuario)
        biblioteca.registrar_usuario(usuario)

    # Eliminar usuario
    elif opcion == "4":
        id_usuario = input("ID del usuario a eliminar: ")
        biblioteca.eliminar_usuario(id_usuario)

    # Prestar libro
    elif opcion == "5":
        isbn = input("ISBN del libro: ")
        id_usuario = input("ID del usuario: ")

        biblioteca.prestar_libro(isbn, id_usuario)

    # Devolver libro
    elif opcion == "6":
        isbn = input("ISBN del libro: ")
        id_usuario = input("ID del usuario: ")

        biblioteca.devolver_libro(isbn, id_usuario)

    # Buscar libro
    elif opcion == "7":
        texto = input("Buscar por título, autor o categoría: ")
        biblioteca.buscar_libro(texto)

    # Listar libros prestados
    elif opcion == "8":
        id_usuario = input("ID del usuario: ")
        biblioteca.listar_prestados(id_usuario)

    # Salir
    elif opcion == "9":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")