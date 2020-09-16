def basic_ops(op_1, op_2, tipo):
    """
    Funcion que recibe dos numeros enteros, un parametro de operacion
    y retorna el resultado de dada operacion.
    Las operaciones se especifican mediante cadenas de texto
    y son 'suma', 'resta', 'and' y 'or'
    """

    # restricciones
    if isinstance(op_1, int) or isinstance(op_2, int):
        # si ambos operandos son numeros enteros
        if abs(op_1) > 127 or abs(op_2) > 127:
            # si se cumple que son enteros, revisar que
            # esten dentro del rango aceptable de [-127, 127]
            return 1001
            # codigo de error 1001 = fuera del rango aceptable

    else:
        return 1002
        # codigo de error 1002 = valor no entero

    if tipo.lower() == "suma":
        return op_1 + op_2
    elif tipo.lower() == "resta":
        return op_1 - op_2
    elif tipo.lower() == "and":
        return op_1 & op_2
    elif tipo.lower() == "or":
        return op_1 | op_2
    else:
        return 1003
        # codigo de error 1003 = operacion invalida


def array_ops(array_1, array_2, operacion):
    """
    Funcion que recibe dos arreglos de numeros enteros
    y les ejecuta la operacion de basic_ops especificada
    de manera paralela
    """

    op_validas = ["suma", "resta", "and", "or"]

    if operacion not in op_validas:
        return 1003
        # codigo de error 1003 = operacion invalida

    resultado = []

    lon = len(array_1)

    for i in range(lon):
        op_1 = array_1[i]
        op_2 = array_2[i]

        # revision de condiciones
        if isinstance(op_1, int) or isinstance(op_2, int):
            # si ambos operandos son numeros enteros
            if abs(op_1) > 127 or abs(op_2) > 127:
                # si se cumple que son enteros, revisar que
                # esten dentro del rango aceptable de [-127, 127]
                return 1001
                # codigo de error 1001 = fuera del rango aceptable
        else:
            return 1002
            # codigo de error 1002 = valor no entero

        # llamado a basic_ops, si no se levanto un error anteriormente
        resultado.append(basic_ops(op_1, op_2, operacion))

    return resultado
