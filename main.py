text_menu = """
#####################
# Control de Stock: #
#####################

1. Lista de Productos

2. Agregar Producto

3. Modificar Producto

4. Quitar Producto

5. Salir

Elija una opcion: """
respuesta_opcion_menu = input(text_menu)

if respuesta_opcion_menu.isnumeric():
    respuesta_opcion_menu = int(respuesta_opcion_menu)
    while respuesta_opcion_menu < 1 or respuesta_opcion_menu > 5:
        respuesta_opcion_menu = input("Elija una opcion valida: ")
        if respuesta_opcion_menu.isnumeric():
            respuesta_opcion_menu = int(respuesta_opcion_menu)
            
    if respuesta_opcion_menu == 1:
        pass
    elif respuesta_opcion_menu == 2:
        pass
    elif respuesta_opcion_menu == 3:
        pass
    elif respuesta_opcion_menu == 4:
        pass
    else:
        print(
            """
            #####################
            # Gracias por usar  #
            # el programa de    #
            # stock             #
            #####################
            """
        )
        exit()