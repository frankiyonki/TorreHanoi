from pilaHanoi import Pila

def solve(tablero, n, origen, auxiliar, destino):
    """
    Resuelve el problema de las Torres de Hanoi.

    Args:
        tablero: Tupla con las tres pilas en su estado inicial.
        n: Número de discos en juego.
        origen: Pila de origen.
        auxiliar: Pila auxiliar.
        destino: Pila de destino.

    Returns:
        Lista de movimientos para la solución óptima.
    """

    if n == 0:
        return []

    movimientos = []

    # Mover la torre de n - 1 discos de la pila de origen a la pila auxiliar,
    # usando la pila de destino como auxiliar.

    movimientos += solve(tablero, n - 1, origen, destino, auxiliar)

    # Mover el disco más grande de la pila de origen a la pila de destino.

    movimientos.append("D{} from {} to {}".format(n, origen, destino))

    # Mover la torre de n - 1 discos de la pila auxiliar a la pila de destino,
    # usando la pila de origen como auxiliar.

    movimientos += solve(tablero, n - 1, auxiliar, origen, destino)

    return movimientos



def getTablero(n):
    """
    Devuelve una tupla con las tres pilas en su estado inicial.

    Args:
        n: Número de discos en juego.

    Returns:
        Tupla con las tres pilas en su estado inicial.
    """

    tablero = tuple([Pila() for _ in range(3)])
    for i in range(n):
        tablero[0].push(i + 1)
    return tablero


def main():
    n = int(input("Introduce el número de discos: "))

    # Inicializa el tablero en su estado inicial.

    tablero = getTablero(n)

    # Imprime el tablero inicial.

    print("Tablero inicial:")
    for pila in tablero:
        print(pila)

    # Resuelve el problema de las Torres de Hanoi.

    movimientos = solve(tablero, n, 0, 1, 2)

    # Imprime la solución.

    print("Solución:")
    for movimiento in movimientos:
        print(movimiento)

    # Imprime el tablero final.

    print("Tablero final:")
    for pila in tablero:
        print(pila)


if __name__ == "__main__":
    main()
