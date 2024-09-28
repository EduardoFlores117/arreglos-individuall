import numpy as np
import os

# Función para limpiar la consola
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el menú principal con estilo
def mostrar_menu():
    clear_console()
    print("\033[1;36m" + "=" * 40)
    print("\033[1;33m" + "   BIENVENIDO A LA APLICACIÓN INTERACTIVA")
    print("\033[1;36m" + "=" * 40)
    print("\033[1;35m" + "1. Invertir un arreglo")
    print("2. Buscar en una matriz")
    print("3. Promedio de pesos")
    print("4. Promedio de notas por curso")
    print("5. Sueldo de empleados")
    print("6. Salir")
    print("\033[1;36m" + "=" * 40)
    return input("\033[1;32m" + "Seleccione una opción: ")

# Ejercicio 1: Invertir arreglo
def invertir_arreglo():
    clear_console()
    print("\033[1;33m" + "Ejercicio 1: Invertir un arreglo")
    while True:
        try:
            arreglo = input("Ingrese los elementos del arreglo separados por comas: ").split(',')
            if not arreglo:
                raise ValueError("El arreglo no puede estar vacío.")
            arreglo_invertido = arreglo[::-1]
            print("\033[1;32m" + f"Arreglo invertido: {arreglo_invertido}")
            break
        except ValueError as e:
            print("\033[1;31m" + f"Error: {e}")
    input("\033[1;34m" + "Presione Enter para volver al menú...")

# Ejercicio 2: Buscar en matriz 2D
def buscar_en_matriz():
    clear_console()
    print("\033[1;33m" + "Ejercicio 2: Buscar en una matriz 2D")
    matriz = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print("\033[1;32m" + "Matriz:")
    print(matriz)
    while True:
        try:
            valor = input("\033[1;36m" + "Ingrese el valor a buscar (número entero): ")
            if not valor.isdigit():
                raise ValueError("Debe ingresar un número entero.")
            valor = int(valor)
            existe = np.isin(valor, matriz)
            if existe:
                print("\033[1;32m" + f"El valor {valor} está en la matriz.")
            else:
                print("\033[1;31m" + f"El valor {valor} no está en la matriz.")
            break
        except ValueError as e:
            print("\033[1;31m" + f"Error: {e}")
    input("\033[1;34m" + "Presione Enter para volver al menú...")

# Ejercicio 3: Promedio de pesos
def promedio_pesos():
    clear_console()
    print("\033[1;33m" + "Ejercicio 3: Promedio de pesos")
    pesos = []
    for i in range(10):
        while True:
            try:
                peso = input(f"Ingrese el peso de la persona {i+1} (número decimal): ")
                if not peso.replace('.', '', 1).isdigit():
                    raise ValueError("Debe ingresar un número válido.")
                pesos.append(float(peso))
                break
            except ValueError as e:
                print("\033[1;31m" + f"Error: {e}")
    
    promedio = sum(pesos) / len(pesos)
    altos = len([p for p in pesos if p > promedio])
    bajos = len([p for p in pesos if p < promedio])
    
    print("\033[1;32m" + f"El promedio de los pesos es: {promedio:.2f}")
    print(f"Personas con peso superior al promedio: {altos}")
    print(f"Personas con peso inferior al promedio: {bajos}")
    
    input("\033[1;34m" + "Presione Enter para volver al menú...")

# Ejercicio 4: Promedio de notas por curso
def promedio_cursos():
    clear_console()
    print("\033[1;33m" + "Ejercicio 4: Promedio de notas por curso")
    cursos = {
        'Estructura de Datos': [85, 90, 88, 92, 78],
        'Desarrollo de Aplicaciones': [75, 80, 85, 88, 90],
        'Ingeniería de Software': [60, 70, 75, 85, 80],
        'Administración de BD': [80, 85, 90, 95, 100],
        'Inglés IV': [65, 70, 72, 80, 85]
    }
    
    try:
        promedios = {curso: sum(notas) / len(notas) for curso, notas in cursos.items()}
        mayor_promedio = max(promedios.values())
        
        print("\033[1;32m" + "Cursos con el mayor promedio:")
        for curso, promedio in promedios.items():
            if promedio == mayor_promedio:
                print(f"{curso}: {promedio:.2f}")
    except Exception as e:
        print("\033[1;31m" + f"Error inesperado: {e}")
    input("\033[1;34m" + "Presione Enter para volver al menú...")

# Ejercicio 5: Sueldo de empleados
def sueldo_empleados():
    clear_console()
    print("\033[1;33m" + "Ejercicio 5: Sueldo de empleados")
    empleados = {}
    
    for i in range(5):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        sueldos = []
        for j in range(5):
            while True:
                try:
                    sueldo = input(f"Ingrese el sueldo de la quincena {j+1} para {nombre} (número decimal): ")
                    if not sueldo.replace('.', '', 1).isdigit():
                        raise ValueError("Debe ingresar un número válido.")
                    sueldos.append(float(sueldo))
                    break
                except ValueError as e:
                    print("\033[1;31m" + f"Error: {e}")
        empleados[nombre] = sueldos
    
    # Paso 2: Generar un vector que contenga el ingreso acumulado en sueldos en los últimos 10 meses
    empleados_acumulado = {}
    for nombre, sueldos in empleados.items():
        sueldos_10_meses = sueldos * 2  # Duplicamos sueldos para simular 10 meses
        empleados_acumulado[nombre] = sueldos_10_meses

    # Paso 3: Mostrar el total pagado en sueldos a todos los empleados en los últimos 5 meses
    total_sueldos_5_meses = sum(sum(sueldos) for sueldos in empleados.values())
    print("\033[1;32m" + f"\nTotal pagado en sueldos a todos los empleados en los últimos 5 meses: {total_sueldos_5_meses:.2f}")

    # Paso 4: Obtener el nombre del empleado con mayor ingreso acumulado en los últimos 10 meses
    total_acumulado = {nombre: sum(sueldos) for nombre, sueldos in empleados_acumulado.items()}
    mayor_ingreso = max(total_acumulado.values())
    empleado_mayor_ingreso = [nombre for nombre, total in total_acumulado.items() if total == mayor_ingreso][0]

    print("\033[1;32m" + f"Empleado con mayor ingreso acumulado en 10 meses: {empleado_mayor_ingreso} con {mayor_ingreso:.2f}")

    input("\033[1;34m" + "Presione Enter para volver al menú...")

# Función principal
def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            invertir_arreglo()
        elif opcion == '2':
            buscar_en_matriz()
        elif opcion == '3':
            promedio_pesos()
        elif opcion == '4':
            promedio_cursos()
        elif opcion == '5':
            sueldo_empleados()
        elif opcion == '6':
            print("\033[1;32m" + "Gracias por usar el programa. ¡Hasta pronto!")
            break
        else:
            print("\033[1;31m" + "Opción no válida, intente nuevamente.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
