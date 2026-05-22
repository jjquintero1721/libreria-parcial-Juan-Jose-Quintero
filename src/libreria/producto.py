class Producto:
    def __init__(self, nombre, precio):
        if precio <= 0:
            raise ValueError("el precio base debe ser mayor que cero")
        self.nombre = nombre
        self.precio = precio
        self._descuento = 0

    def aplicar_descuento(self, descuento):
        if descuento < 0:
            raise ValueError("el descuento no puede ser negativo")
        if descuento > 40:
            raise ValueError("el descuento no puede superar el 40%")
        self._descuento = descuento

    @property
    def precio_con_descuento(self):
        return self.precio * (1 - self._descuento / 100)

    def calcular_precio_final(self):
        return self.precio_con_descuento * 1.19
