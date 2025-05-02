#En este bloque se define y se le pide al usuario la calificación 
def calificacion():
    try:
        calificacion_str = input("Ingrese la calificación (de 0 a 100): ")
        calificacion = float(calificacion_str)
        if 0 <= calificacion <= 100:
            return calificacion, True
        else:
            print("La calificación debe estar entre 0 y 100")
            return None, False
    except ValueError:
        print("Inválido, por favor ingrese un número")
        return None, False

#En este bloque se define si aprueba
def aprobacion(calificacion):
    if calificacion is not None:
        if calificacion >= 60:
            print("Aprobado")
        else:
            print("Reprobado")

#En este bloque se define la lista de calificaciones
def lista_calificaciones():
    try:
        calificaciones_str = input("Ingrese la lista de calificaciones separadas por comas: ")
        lista_calificaciones = [float(calif.strip()) for calif in calificaciones_str.split(',')]
        if not lista_calificaciones:
            print("La lista de calificaciones está vacía")
            return [], False
        return lista_calificaciones, True
    except ValueError:
        print("Inválido, por favor ingrese los números separados por comas")

#Este bloque calcula el promedio
def calcular_promedio(lista_calificaciones):
    if lista_calificaciones:
        return sum(lista_calificaciones) / len(lista_calificaciones)
    return None

#Este bloque compara en la lista el valor ingresado 
def valor_comparacion():
    try:
        valor_especifico_str = input("Ingrese el valor a comparar: ")
        valor_especifico = float(valor_especifico_str)
        return valor_especifico, True
    except ValueError:
        print("Inválido, por favor ingrese un número")
        return None, False

#Este bloque compara el valor ingresado con los elementos de la lista y muestra la cantidad de números mayores al mismo
def calificaciones_mayores(lista_calificaciones, valor_especifico):
    if lista_calificaciones is not None and valor_especifico is not None:
        contador = 0
        for calificacion in lista_calificaciones:
            if calificacion > valor_especifico:
                contador += 1
        print(f"Hay {contador} calificaciones mayores que {valor_especifico}")

#Este bloque es para ingresar una calificación específica de la lista
def calificacion_especifica():
    try:
        calificacion_especifica_str = input("Ingrese la calificación que desea verificar: ")
        calificacion_especifica = float(calificacion_especifica_str)
        return calificacion_especifica, True
    except ValueError:
        print("Inválido, por favor ingrese un número")
        return None, False

#Este bloque es para contar cuántas veces está el valor ingresado en la lista
def contar_calificacion_especifica(lista_calificaciones, calificacion_especifica):
    if lista_calificaciones is not None and calificacion_especifica is not None:
        contador = 0
        encontrada = False
        for calificacion in lista_calificaciones:
            if calificacion == calificacion_especifica:
                contador += 1
                encontrada = True
                continue
            if contador > 0 and not encontrada:
                break

        if encontrada:
            print(f"{calificacion_especifica} está en la lista y aparece {contador} veces")
        else:
            print(f"{calificacion_especifica} no se encontró en la lista")

def mostrar_menu_y_obtener_opcion():
    print("1. Verificar aprobación")
    print("2. Calcular promedio")
    print("3. Contar calificaciones mayores")
    print("4. Contar calificación específica")
    print("5. Salir")
    return input("Seleccione una opción: ")

# Ejecución 
opcion = mostrar_menu_y_obtener_opcion()

if opcion == '1':
    calif, valido = calificacion()
    if valido:
        aprobacion(calif)
elif opcion == '2':  
    lista_calif, valido = lista_calificaciones()
    if valido:
        promedio = calcular_promedio(lista_calif)
        if promedio is not None:
            print(f"El promedio es: {promedio:.2f}")
            nota_aprobatoria = 60
            if promedio >= nota_aprobatoria:
                print("El estudiante aprobó")
            else:
                print("El estudiante reprobó")
    else:
        print("No se obtuvieron las calificaciones")
elif opcion == '3':
    lista_calif, valido_lista = lista_calificaciones()
    if valido_lista:
        valor_comp, valido_valor = valor_comparacion()
        if valido_valor:
            calificaciones_mayores(lista_calif, valor_comp)
elif opcion == '4':
    lista_calif, valido_lista = lista_calificaciones()
    if valido_lista:
        calif_especifica, valido_calif = calificacion_especifica()
        if valido_calif:
            contar_calificacion_especifica(lista_calif, calif_especifica)
elif opcion == '5':
    print("Hasta luego")
else:
    print("Opción inválida")