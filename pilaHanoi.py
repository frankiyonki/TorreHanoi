class NodoPila:
    """
    Clase para representar un nodo de una pila.

    Atributos:
        dato: Dato almacenado en el nodo.
        siguiente: Puntero al nodo siguiente.
    """

    def __init__(self, dato, siguiente=None):
        """
        Inicializa un nuevo nodo de pila.

        Args:
            dato: Dato almacenado en el nodo.
            siguiente: Puntero al nodo siguiente.
        """
        self.dato = dato
        self.siguiente = siguiente

    def __str__(self):
        """
        Devuelve una representación del nodo en forma de cadena de texto.

        Returns:
            Cadena de texto con el contenido del nodo.
        """
        return str(self.dato)


class Pila:
    """
    Clase para representar una pila.

    Atributos:
        tope: Puntero al nodo que está en la cima de la pila.
    """

    def __init__(self):
        """
        Inicializa una nueva pila vacía.
        """
        self.tope = None

    def push(self, dato):
        """
        Añade un elemento a la pila.

        Args:
            dato: Dato a añadir a la pila.
        """
        nuevo_nodo = NodoPila(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        """
        Elimina el elemento de la cima de la pila.

        Returns:
            Dato del elemento eliminado.
        """
        if self.tope is None:
            raise IndexError("La pila está vacía.")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def __str__(self):
        """
        Devuelve una representación de la pila en forma de cadena de texto.

        Returns:
            Cadena de texto con el contenido de la pila.
        """
        if self.tope is None:
            return "[]"
        cadena = "["
        nodo = self.tope
        while nodo is not None:
            cadena += str(nodo) + ", "
            nodo = nodo.siguiente
        cadena = cadena[:-2] + "]"
        return cadena

