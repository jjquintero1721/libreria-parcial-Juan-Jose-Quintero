import pytest
from libreria.producto import Producto


def test_crear_producto_con_precio_valido():
    p = Producto("Libro Python", 25000)
    assert p.precio == 25000


def test_rechazar_precio_cero():
    with pytest.raises(ValueError):
        Producto("Libro", 0)


def test_rechazar_precio_negativo():
    with pytest.raises(ValueError):
        Producto("Libro", -100)


def test_aceptar_precio_minimo_valido():
    p = Producto("Libro", 0.01)
    assert p.precio == 0.01
