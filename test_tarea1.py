import tarea1


def test_errores():
    """
    Se llaman los metodos para probar las funciones basic_ops
    y array_ops.
    Ambas son identicas pero la de array envía arreglos
    """
    test_basic_ops()

    test_array_ops()


def test_basic_ops():
    """
    Tester de basic_ops. Primero, se evalúa que cada una
    de las operaciones retorne el valor esperado, y luego
    que cada uno de los posibles casos de error retorne el
    código de error esperado
    """

    # se revisa que sume 1 + 2 = 3
    assert tarea1.basic_ops(1, 2, 'suma') == 3

    # resta 1 - 2 = -1
    assert tarea1.basic_ops(1, 2, 'resta') == -1

    # and 1 & 2 = 01 & 10 = 0
    assert tarea1.basic_ops(1, 2, 'and') == 0

    # or 1 | 2 = 11 = 3
    assert tarea1.basic_ops(1, 2, 'or') == 3

    # valor no entero
    assert tarea1.basic_ops(0.6, 'foo', 'suma') == 1002

    # numero mayor a 127
    assert tarea1.basic_ops(255, 1023, 'resta') == 1001

    # operacion no soportada
    assert tarea1.basic_ops(4, 5, 'jaja') == 1003


def test_array_ops():
    """
    Tester de array_ops. Igual que la función anterior,
    se evalúa que cada una de las operaciones retorne
    el valor esperado para ciertos arreglos de entrada,
    y despues cada uno de los casos de error
    """

    # se revisa la suma para los arreglos, [0] 1 + 2 = 3
    # [1] 2 + 3 = 5
    assert tarea1.array_ops([1, 2], [2, 3], 'suma') == [3, 5]

    # resta con los mismos arreglos de entrada
    assert tarea1.array_ops([1, 2], [2, 3], 'resta') == [-1, -1]

    # and
    assert tarea1.array_ops([1, 2], [2, 3], 'and') == [0, 2]

    # or
    assert tarea1.array_ops([1, 2], [2, 3], 'or') == [3, 3]

    # valor no entero
    assert tarea1.array_ops([0.6, 1], 'foo', 'suma') == 1002

    # numero mayor a 127
    assert tarea1.array_ops([255, 11], [1023, 2], 'resta') == 1001

    # operacion no soportada
    assert tarea1.array_ops([4, 5], [5, 6], 'jaja') == 1003
