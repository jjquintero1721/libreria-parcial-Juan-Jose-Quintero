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
