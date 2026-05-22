class Producto:
    IVA: float = 0.19
    DESCUENTO_MAX: float = 40

    def __init__(self, nombre: str, precio: float) -> None:
        self._validar_precio(precio)
        self.nombre = nombre
        self.precio = precio
        self._descuento: float = 0

    def aplicar_descuento(self, descuento: float) -> None:
        self._validar_descuento(descuento)
        self._descuento = descuento

    @property
    def precio_con_descuento(self) -> float:
        return self.precio * (1 - self._descuento / 100)

    def calcular_precio_final(self) -> float:
        return self.precio_con_descuento * (1 + self.IVA)

    def __repr__(self) -> str:
        return f"Producto(nombre={self.nombre!r}, precio={self.precio})"

    @staticmethod
    def _validar_precio(precio: float) -> None:
        if precio <= 0:
            raise ValueError("el precio base debe ser mayor que cero")

    @staticmethod
    def _validar_descuento(descuento: float) -> None:
        if descuento < 0:
            raise ValueError("el descuento no puede ser negativo")
        if descuento > Producto.DESCUENTO_MAX:
            raise ValueError(f"el descuento no puede superar el {Producto.DESCUENTO_MAX}%")
