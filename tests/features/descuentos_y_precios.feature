Feature: Descuentos y precio final de productos
  Como administrador de la Librería del Centro
  Quiero aplicar descuentos a los productos y calcular su precio final con IVA
  Para que los clientes vean el precio correcto en caja

  Background:
    Given un producto "Libro Python" con precio base 1000

  @regla2 @borde
  Scenario: Descuento del 0% no modifica el precio base
    When aplico un descuento del 0%
    Then el precio con descuento es 1000.0

  @regla2 @borde
  Scenario: Descuento del 40% aplica la rebaja maxima permitida
    When aplico un descuento del 40%
    Then el precio con descuento es 600.0

  @regla2 @error
  Scenario: Descuento mayor al 40% es rechazado
    When intento aplicar un descuento del 41%
    Then el sistema lanza un error de descuento invalido

  @regla2 @error
  Scenario: Descuento negativo es rechazado
    When intento aplicar un descuento del -5%
    Then el sistema lanza un error de descuento invalido

  @regla2 @outline
  Scenario Outline: Descuentos validos calculan el precio con descuento correcto
    When aplico un descuento del <descuento>%
    Then el precio con descuento es <precio_esperado>

    Examples:
      | descuento | precio_esperado |
      | 10        | 900.0           |
      | 25        | 750.0           |
      | 40        | 600.0           |

  @regla3 @positivo
  Scenario: Precio final aplica descuento e IVA en el orden correcto
    When aplico un descuento del 10%
    Then el precio final es 1071.0

  @regla3 @positivo
  Scenario: Precio final sin descuento aplica solo el IVA del 19%
    When aplico un descuento del 0%
    Then el precio final es 1190.0
