import pytest
from libreria.producto import Producto


def test_aceptar_descuento_cero():
    p = Producto("Libro", 1000)
    p.aplicar_descuento(0)
    assert p.precio_con_descuento == 1000


def test_aceptar_descuento_cuarenta():
    p = Producto("Libro", 1000)
    p.aplicar_descuento(40)
    assert p.precio_con_descuento == 600


def test_rechazar_descuento_cuarenta_y_uno():
    p = Producto("Libro", 1000)
    with pytest.raises(ValueError):
        p.aplicar_descuento(41)


def test_rechazar_descuento_negativo():
    p = Producto("Libro", 1000)
    with pytest.raises(ValueError):
        p.aplicar_descuento(-5)
