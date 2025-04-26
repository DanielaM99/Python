print("Lista de productos disponibles")
productos_disponibles = ["mango", "chocolate", "azucar", "cafe", "pan"]
for producto in productos_disponibles:
  print(producto)

productos_con_precio = {}

while True:
    producto_seleccionado = input("Ingresa el nombre del producto que deseas: ").lower()

    if producto_seleccionado in productos_disponibles:
        while True:
            try:
                precio_unitario_str = input(f"Ingresa el precio de '{producto_seleccionado}': ")
                precio_unitario = float(precio_unitario_str)
                if precio_unitario >= 0:
                    break
                else:
                    print("Error: El precio debe ser un número positivo o cero. Inténtalo de nuevo.")
            except ValueError:
                print("Error: Por favor, ingresa un número válido para el precio.")

        while True:
            cantidad_str = input(f"Ingresa la cantidad de '{producto_seleccionado}': ")
            try:
                cantidad = float(cantidad_str)
                if cantidad > 0:
                    costo_sin_descuento = cantidad * precio_unitario

                    while True:
                        descuento_str = input("Ingresa el porcentaje de descuento (0-100): ")
                        try:
                            descuento_porcentaje = float(descuento_str)
                            if 0 <= descuento_porcentaje <= 100:
                                descuento_decimal = descuento_porcentaje / 100
                                monto_descuento = costo_sin_descuento * descuento_decimal
                                precio_final = costo_sin_descuento - monto_descuento

                                print(f"Precio unitario: ${precio_unitario:.2f}")
                                print(f"Cantidad: {cantidad:.2f}")
                                print(f"Precio original: ${costo_sin_descuento:.2f}")
                                print(f"Descuento aplicado: {descuento_porcentaje:.2f}%")
                                print(f"Monto del descuento: ${monto_descuento:.2f}")
                                print(f"Precio final: ${precio_final:.2f}")
                                break  # Sale del bucle de descuento
                            else:
                                print("Error: El porcentaje de descuento debe estar entre 0 y 100. Inténtalo de nuevo.")
                        except ValueError:
                            print("Error: Por favor, ingresa un número válido para el porcentaje de descuento.")
                    break  # Sale del bucle de cantidad
                else:
                    print("Error: La cantidad debe ser mayor que cero. Inténtalo de nuevo.")
            except ValueError:
                print("Error: Por favor, ingresa un número válido para la cantidad.")
    else:
        print(f"Error: El producto '{producto_seleccionado}' no se encuentra en la lista. Inténtalo de nuevo.")