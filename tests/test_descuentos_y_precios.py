import pytest
from pathlib import Path
from pytest_bdd import given, when, then, scenarios
from pytest_bdd import parsers
from libreria.producto import Producto

scenarios(Path(__file__).parent / "features" / "descuentos_y_precios.feature")


@pytest.fixture
def excepcion():
    return {}


@given(parsers.parse('un producto "{nombre}" con precio base {precio:d}'), target_fixture="producto")
def producto_fixture(nombre: str, precio: int) -> Producto:
    return Producto(nombre, float(precio))


@when(parsers.parse("aplico un descuento del {descuento:d}%"))
def aplico_descuento(producto: Producto, descuento: int) -> None:
    producto.aplicar_descuento(descuento)


@when(parsers.re(r"intento aplicar un descuento del (?P<descuento>-?\d+)%"))
def intento_aplicar_descuento(producto: Producto, descuento: str, excepcion: dict) -> None:
    try:
        producto.aplicar_descuento(int(descuento))
    except ValueError as e:
        excepcion["error"] = str(e)


@then(parsers.parse("el precio con descuento es {precio:f}"))
def verificar_precio_con_descuento(producto: Producto, precio: float) -> None:
    assert producto.precio_con_descuento == pytest.approx(precio)


@then("el sistema lanza un error de descuento invalido")
def verificar_error_descuento(excepcion: dict) -> None:
    assert "error" in excepcion


@then(parsers.parse("el precio final es {precio:f}"))
def verificar_precio_final(producto: Producto, precio: float) -> None:
    assert producto.calcular_precio_final() == pytest.approx(precio)
