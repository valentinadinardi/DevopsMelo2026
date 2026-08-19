import subprocess
import time
import webbrowser


def opcion1():
    print("🔍 Has elegido la Opción 1: Python Oficial")
    webbrowser.open("https://www.python.org")


def opcion2():
    print("🔍 Has elegido la Opción 2: Documentación de Python")
    webbrowser.open("https://docs.python.org/3/")


def opcion3():
    print("🔍 Has elegido la Opción 3: GitHub")
    webbrowser.open("https://github.com")


def opcion4():
    print("🔍 Has elegido la Opción 4: Stack Overflow")
    webbrowser.open("https://stackoverflow.com")


def opcion5():
    print("🔍 Has elegido la Opción 5: System monitor")
    subprocess.Popen(["python", "system_monitor.py"])
    time.sleep(1)  # esperar un segundo para que el servidor levante
    webbrowser.open("http://127.0.0.1:5000")


def opcion6():
    print("🔍 Has elegido la Opción 6: Aplicación de sistema de monitoreo")
    # arrancar el servidor Flask
    subprocess.Popen(["python", "system_check_flask.py"])
    time.sleep(1)  # esperar un segundo para que el servidor levante
    webbrowser.open("http://127.0.0.1:5000")


def mostrar_menu():
    print("\n----- 🔍 MENÚ CON ENLACES -----")
    print("1. Python Oficial")
    print("2. Documentación Python")
    print("3. GitHub")
    print("4. Stack Overflow")
    print("5. System Monitor")
    print("6. System Check")
    print("7. Salir")


def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nElige una opción (1-7): "))
            if opcion == 1:
                opcion1()
            elif opcion == 2:
                opcion2()
            elif opcion == 3:
                opcion3()
            elif opcion == 4:
                opcion4()
            elif opcion == 5:
                opcion5()
            elif opcion == 6:
                opcion6()
            elif opcion == 7:
                print("🔍 Saliendo del programa...")
                break
            else:
                print("❌ Error: Ingresa un número del 1 al 7.")
        except ValueError:
            print("❌ Error: Debes ingresar un número válido.")


if __name__ == "__main__":
    main()

#