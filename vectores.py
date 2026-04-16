"""
Tercera tarea de APA: Multiplicaciones de vectores y ortogonalidad

Nombre: Pol Ramírez Sánchez
"""

class Vector:
    """
    Clase para representar vectores y operar con ellos.
    """

    def __init__(self, iterable):
        """
        Inicializa el vector a partir de un iterable.
        """
        self._data = list(iterable)

    def __repr__(self):
        """
        Representación oficial del objeto.
        """
        return f"Vector({self._data})"

    def __str__(self):
        """
        Representación informal del vector.
        """
        return str(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    # ------------------ OPERACIONES ------------------

    def __add__(self, other):
        """
        Suma de vectores o suma con escalar.
        """
        if isinstance(other, (int, float, complex)):
            return Vector(x + other for x in self)
        return Vector(x + y for x, y in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        return Vector(-x for x in self)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        """
        Producto de Hadamard o multiplicación por escalar.

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * 2
        Vector([2, 4, 6])
        >>> v1 * v2
        Vector([4, 10, 18])
        """
        if isinstance(other, (int, float, complex)):
            return Vector(x * other for x in self)
        return Vector(x * y for x, y in zip(self, other))

    __rmul__ = __mul__

    def __matmul__(self, other):
        """
        Producto escalar entre dos vectores.

        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32
        """
        if not isinstance(other, Vector):
            raise TypeError("Se esperaba un Vector")
        return sum(x * y for x, y in zip(self, other))

    def __rmatmul__(self, other):
        if isinstance(other, Vector):
            return other @ self
        raise TypeError("Se esperaba un Vector")

    def __floordiv__(self, other):
        """
        Componente paralela de un vector respecto a otro.

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """
        if not isinstance(other, Vector):
            raise TypeError("Se esperaba un Vector")

        coef = (self @ other) / (other @ other)
        return Vector(coef * x for x in other)

    def __rfloordiv__(self, other):
        if isinstance(other, Vector):
            return self // other
        raise TypeError("Se esperaba un Vector")

    def __mod__(self, other):
        """
        Componente perpendicular de un vector respecto a otro.

        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        if not isinstance(other, Vector):
            raise TypeError("Se esperaba un Vector")

        proy = self // other
        return Vector(x - y for x, y in zip(self, proy))

    def __rmod__(self, other):
        if isinstance(other, Vector):
            return self % other
        raise TypeError("Se esperaba un Vector")


if __name__ == "__main__":
    import doctest
    doctest.testmod()