import os
import sys
import subprocess

# Busca carpetas que contengan "parcial" en el directorio base
def encontrar_unidades(base):
    try:
        return sorted([d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)) and 'parcial' in d.lower()])
    except Exception:
        return []

# Lista subcarpetas dentro de una ruta dada
def listar_subcarpetas(ruta):
    try:
        return sorted([d for d in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, d))])
    except Exception:
        return []

# Lista archivos .py dentro de una carpeta
def listar_scripts(ruta):
    try:
        return sorted([f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f)) and f.lower().endswith('.py')])
    except Exception:
        return []

# Muestra el contenido del archivo en la consola
def mostrar_codigo(ruta):
    try:
        # Abrir con utf-8 y reemplazar errores de codificación
        with open(ruta, 'r', encoding='utf-8', errors='replace') as f:
            print("\n--- Contenido de", ruta, "---\n")
            print(f.read())
    except Exception as e:
        print("Error al leer el archivo:", e)

# Ejecuta el script en una nueva consola en Windows o en segundo plano en Unix
def ejecutar_script(ruta):
    ruta_abs = os.path.abspath(ruta)
    if not os.path.exists(ruta_abs):
        print("Archivo no encontrado:", ruta_abs)
        return
    # Ejecutar en el directorio del script para que rutas relativas funcionen
    cwd = os.path.dirname(ruta_abs) or None
    try:
        if os.name == 'nt':
            # En Windows: usar cmd /k para mantener la consola abierta al terminar
            cmd = ['cmd', '/k', sys.executable, ruta_abs]
            if hasattr(subprocess, 'CREATE_NEW_CONSOLE'):
                subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE, cwd=cwd)
            else:
                subprocess.Popen(cmd, cwd=cwd)
        else:
            # En Unix: lanzar el intérprete directamente (no abre nueva terminal)
            subprocess.Popen([sys.executable, ruta_abs], cwd=cwd)
        print("Script lanzado:", ruta_abs)
    except Exception as e:
        print("Error al ejecutar el script:", e)

# Menú principal: muestra unidades encontradas
def menu_principal(base):
    unidades = encontrar_unidades(base)
    if not unidades:
        print("No se encontraron carpetas con 'parcial' en", base)
        return

    while True:
        print("\nUnidades disponibles:")
        for i, u in enumerate(unidades, 1):
            print(f"{i}) {u}")
        print("0) Salir")
        elec = input("Elige unidad: ").strip()
        if elec == '0':
            break
        try:
            idx = int(elec) - 1
            if 0 <= idx < len(unidades):
                submenu_unidad(os.path.join(base, unidades[idx]))
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida.")

# Submenú: lista subcarpetas de la unidad seleccionada
def submenu_unidad(ruta_unidad):
    sub = listar_subcarpetas(ruta_unidad)
    if not sub:
        print("No hay subcarpetas en", ruta_unidad)
        return
    while True:
        print(f"\nSubcarpetas en `{ruta_unidad}`:")
        for i, s in enumerate(sub, 1):
            print(f"{i}) {s}")
        print("0) Volver")
        elec = input("Elige subcarpeta: ").strip()
        if elec == '0':
            break
        try:
            idx = int(elec) - 1
            if 0 <= idx < len(sub):
                submenu_scripts(os.path.join(ruta_unidad, sub[idx]))
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida.")

# Submenú de scripts: muestra, permite ver y ejecutar un script .py
def submenu_scripts(ruta_carpeta):
    scripts = listar_scripts(ruta_carpeta)
    if not scripts:
        print("No hay scripts .py en", ruta_carpeta)
        return
    while True:
        print(f"\nScripts en `{ruta_carpeta}`:")
        for i, s in enumerate(scripts, 1):
            print(f"{i}) {s}")
        print("0) Volver")
        elec = input("Elige script: ").strip()
        if elec == '0':
            break
        try:
            idx = int(elec) - 1
            if 0 <= idx < len(scripts):
                ruta = os.path.join(ruta_carpeta, scripts[idx])
                mostrar_codigo(ruta)  # Mostrar contenido antes de ejecutar
                run = input("Ejecutar script? (s/n): ").strip().lower()
                if run == 's':
                    ejecutar_script(ruta)
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida.")

# Punto de entrada: determina el directorio base y lanza el menú
if __name__ == '__main__':
    base = os.path.abspath(os.path.dirname(__file__)) if '__file__' in globals() else os.getcwd()
    menu_principal(base)
