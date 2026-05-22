import pytest
from libreria.producto import Producto


def test_precio_final_aplica_descuento_e_iva_en_orden():
    p = Producto("Libro", 1000)
    p.aplicar_descuento(10)
    assert p.calcular_precio_final() == pytest.approx(1071.00)


def test_precio_final_sin_descuento_aplica_solo_iva():
    p = Producto("Libro", 1000)
    p.aplicar_descuento(0)
    assert p.calcular_precio_final() == pytest.approx(1190.00)
