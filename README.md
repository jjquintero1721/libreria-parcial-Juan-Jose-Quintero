# Librería del Centro — Módulo de Precios

Módulo para calcular el precio final de productos aplicando descuentos e IVA.

**Stack:** Python 3.11+ · uv · pytest · pytest-bdd · pytest-cov

---

## Parte 1 — Análisis previo

### Regla 1 — Particiones de equivalencia: precio base

| Partición | Descripción | Valor representativo | Resultado esperado |
|-----------|-------------|---------------------|--------------------|
| Válida | Precio estrictamente mayor que cero | 10 000 | Producto creado correctamente |
| Inválida | Precio igual a cero | 0 | Error: el precio base debe ser mayor que cero |
| Inválida | Precio negativo | -500 | Error: el precio base debe ser mayor que cero |

---

### Regla 2 — Particiones de equivalencia: descuento porcentual

| Partición | Descripción | Valor representativo | Resultado esperado |
|-----------|-------------|---------------------|--------------------|
| Válida | Descuento dentro del rango (0 % – 40 %) | 20 % | Descuento aplicado |
| Válida borde inferior | Descuento exactamente en 0 % | 0 % | Descuento aplicado (precio sin rebaja) |
| Válida borde superior | Descuento exactamente en 40 % | 40 % | Descuento aplicado al máximo permitido |
| Inválida | Descuento mayor al 40 % | 55 % | Error: el descuento no puede superar el 40 % |
| Inválida | Descuento negativo | -10 % | Error: el descuento no puede ser negativo |

---

### Regla 2 — Análisis de valores límite: rango 0 % – 40 %

| Valor límite | Tipo | Resultado esperado |
|-------------|------|-------------------|
| -1 % | Justo por debajo del mínimo | Rechazado |
| 0 % | Mínimo válido | Aceptado |
| 1 % | Justo por encima del mínimo | Aceptado |
| 39 % | Justo por debajo del máximo | Aceptado |
| 40 % | Máximo válido | Aceptado |
| 41 % | Justo por encima del máximo | Rechazado |

---

### Regla 3 — Pregunta al administrador

**Pregunta:** ¿El precio final debe redondearse a dos cifras decimales (como aparece en una factura) o el sistema debe conservar la precisión completa de punto flotante?

**Justificación:** La multiplicación sucesiva de descuento e IVA produce con frecuencia valores con muchos decimales ej. precio 999, descuento 15 % = 999 × 0,85 × 1,19 = 1 010,8815; sin una regla de redondeo  no es posible definir el resultado esperado exacto en los tests.

---

## Parte 2 — Casos de prueba

| ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|----|-------|-------------|--------------|-----------------|-------|--------------------|------|
| TC-01 | R1 | Crear producto con precio válido | Ninguna | nombre="Libro Python", precio=25000 | Instanciar Producto | Objeto creado con precio=25000 | Positivo |
| TC-02 | R1 | Rechazar precio igual a cero | Ninguna | nombre="Libro", precio=0 | Instanciar Producto | ValueError: precio debe ser mayor que cero | Negativo |
| TC-03 | R1 | Rechazar precio negativo | Ninguna | nombre="Libro", precio=-100 | Instanciar Producto | ValueError: precio debe ser mayor que cero | Negativo |
| TC-04 | R1 | Aceptar el menor precio válido posible | Ninguna | nombre="Libro", precio=0.01 | Instanciar Producto | Objeto creado con precio=0.01 | Borde |
| TC-05 | R2 | Aceptar descuento del 0 % | Producto con precio=1000 | descuento=0 | Llamar aplicar_descuento(0) | Descuento aplicado; precio_con_descuento=1000 | Borde |
| TC-06 | R2 | Aceptar descuento del 40 % | Producto con precio=1000 | descuento=40 | Llamar aplicar_descuento(40) | Descuento aplicado; precio_con_descuento=600 | Borde |
| TC-07 | R2 | Rechazar descuento del 41 % | Producto con precio=1000 | descuento=41 | Llamar aplicar_descuento(41) | ValueError: descuento no puede superar el 40 % | Borde |
| TC-08 | R2 | Rechazar descuento negativo | Producto con precio=1000 | descuento=-5 | Llamar aplicar_descuento(-5) | ValueError: descuento no puede ser negativo | Negativo |
| TC-09 | R3 | Precio final aplica descuento e IVA en orden correcto | Producto precio=1000, descuento=10 % aplicado | Ninguno adicional | Llamar calcular_precio_final() | (1000 × 0.90) × 1.19 = 1071.00 | Positivo |
| TC-10 | R3 | Sin descuento el precio final es solo precio base más IVA | Producto precio=1000, descuento=0 % aplicado | Ninguno adicional | Llamar calcular_precio_final() | 1000 × 1.19 = 1190.00 | Positivo |

