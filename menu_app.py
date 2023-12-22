def agregar_compra(compras):        #Función
    monto = int(input("Agregar $ de compra: "))     #Se muestra el mensaje en consola para ingreso del usuario

    compras.append(monto)

    print("¡Compra ingresada exitosamente!\n")      #Mensaje por consola mostrado tras el ingreso del monto

def mostrar_compras(compras):       #Función
    if not compras:
        print("No hay compras registradas :(\n")      #Si la lista está vacía, se muestra este mensaje x consola
    else:
        print("Compras realizadas:")                  #Mensaje x consola, se enumeran las compras
        for indice, monto in enumerate(compras, start=1):
            print(f"Compra {indice}: ${monto}\n")

def mostrar_total(compras):         #Función
    total = sum(compras)                              #Aquí se suman todas las compras para dar el total
    print(f"El total gastado es: ${int(total)}\n")    #Se imprime el total

