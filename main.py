from menu_app import agregar_compra, mostrar_compras, mostrar_total

def main():
    compras = []        #Aquí almacenaremos todos los montos de las compras
    total_gastado = 0   #Esta variable mantiene el registro del total

    while True:
        print("Menú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_compra(compras)
            total_gastado = sum(compras)                        #Actualiza el total de las compras
        elif opcion == '2':
            mostrar_compras(compras)
        elif opcion == '3':
            print(f"El total gastado es: ${total_gastado}")     #Utiliza la variable total_gastado
        elif opcion == '4':
            print("¡Gracias y adiós!")
            break                                               #Sale del bucle y termina el programa con un mensaje
        else:                                                   #por consola
            print("¡Inténtalo de nuevo!\n")

main()
