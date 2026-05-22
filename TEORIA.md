---

## SECCIÓN TEÓRICA — 2.0 puntos
### Archivo: `TEORIA.md` en el repositorio

---

**PREGUNTAS DE SELECCIÓN MÚLTIPLE**
*Escribe el ID de la respuesta correcta y explica en una línea por qué las otras son incorrectas.*

**SM-1 (0.3 puntos)**

Un equipo de desarrollo termina de escribir toda la funcionalidad de un módulo y luego le pide al QA que diseñe las pruebas. Según lo visto en clase, ¿cómo se llama este enfoque y cuál es su principal problema?

A. Shift-left testing. El problema es que las pruebas se vuelven demasiado técnicas para que el cliente las entienda.

B. Shift-right testing. El problema es que las pruebas solo se pueden ejecutar en producción.

C. Desarrollo tradicional con pruebas al final. El problema es que los defectos se detectan tarde, cuando corregirlos cuesta hasta 100 veces más que si se hubieran encontrado en etapas tempranas.

D. Integración continua. El problema es que requiere un pipeline de CI/CD que el equipo no tiene configurado.

RESPUESTA: C - esta es la correcta ya que habla de como se diseña las pruebas al final de diseñar un modulo y Shift-left testing es lo contrario el Shift-right testing era hacer las pruebas en ambientes de produccion pero segun el enunciado las pruebas se hacen cada que finalizar un modulo y la d es lo contrario al enunciado por que son pruebas de codigo automaticas.

---

**SM-2 (0.3 puntos)**

Un desarrollador escribe el siguiente ciclo: primero implementa la función `calcular_descuento()` completa con todos los casos que se le ocurren, luego escribe los tests para verificar que funciona. ¿Qué regla de TDD está violando?

A. La regla del refactor, porque debería mejorar el código antes de escribir tests.

B. La primera regla de Uncle Bob: no escribir código de producción sin que exista primero un test que falle. El código fue escrito antes de que ningún test lo requiriera.

C. La regla del Green, porque el código debería ser mínimo y no cubrir todos los casos desde el inicio.

D. No está violando ninguna regla. TDD permite escribir el código primero siempre que los tests se escriban inmediatamente después.

RESPUESTA: B - ya que habla de como esta implementando funcionalidades antes de implementar los test minimos, por lo que la a no es ya que el refactor ya hay tanto codigo como test en el c lo mismo en el enunciado dice que se implemento codigo antes del test y en el green ya se implemento el codigo de los test y la d no puede ser ya que el tdd habla de como se implementan los test minimos antes de implementar codigo

---

**PREGUNTAS ABIERTAS**
*Responde con tus propias palabras. La extensión ideal es entre 5 y 8 líneas por pregunta. No se piden definiciones de diccionario: se pide que demuestres que entendiste el concepto.*

**PA-1 (0.3 puntos)**

Durante la semana 4 implementamos el carrito de compras con TDD y en el primer ciclo, el paso GREEN consistió en escribir el código más simple posible aunque fuera "feo". Explica por qué TDD obliga a hacer esto en el GREEN y qué pasaría con el proceso si el desarrollador aprovecha ese paso para escribir código "limpio y completo" desde el inicio.

RESPUESTA: por que en la fase green la idea es que se realize el codigo minimo para  pasar los test que se diseñaron en la fase red entonces si se aprovecha la fase green para hacer codigo limpio y mas completo puede pasar que alguna de las funcionalidades que implemento supuestamente "completo" no sea tomado en cuenta en los test entonces si hay un bug en una funcionalidad puede pasar que no haya un test que valide ese bug

---

**PA-2 (0.3 puntos)**

Explica con tus propias palabras la diferencia entre TDD y BDD. No es suficiente decir que uno usa código y el otro usa Gherkin. Explica qué problema resuelve cada uno, a quién está dirigido y por qué se complementan en lugar de reemplazarse.

RESPUESTA:pues para mi es como que uno esta mas enfocado a que la parte tecnica del desarrollo funcione y seea confiable y solida con sus test (tdd) y el bdd es mas como para asegurarse que funcione bien el comportamiento del sistema desde la vista como del negocio o usuario, entonces el tdd resuelve problemas tecnicos y el bdd resuelve problemas de como lo ve y entiende un usuario externo para que sea mas entendible, el tdd esta dirigido mas que todo a los desarrolladores y el bdd a todo el equipo de l proyecto incluyendo ahi a los clientes o usuarios del negocio
y por eso se complementan por que si solo se usa tdd se asegura un sistema solido con buenos test pero a nivel de entendimiento o comportamiento del sistema quedara flojo y viseversa en caso de que se use solo el bdd

---

**PA-3 (0.3 puntos)**

Un compañero te muestra su suite de pruebas y dice: "Tengo 95% de cobertura de código, así que mi sistema no tiene bugs." Explica por qué esa afirmación es incorrecta. Usa un ejemplo concreto que demuestre que cobertura alta no garantiza ausencia de defectos.

RESPUESTA: es incorrecta por que la cobertura de codigo solo mide el codigo ejecutado mas no si el codigo ejuctado dio un resultado correcto por ejemplo yo tengo una calculadora y la prueba es que multiplique 4 por 3 y con la prueba se ejecuta bien entonces esto hace que aumente la cobertura de codigo pero no esta validando si el resultado que dio fue correcto entonces no garantiza que no tenga bugs.

---

**PA-4 (0.2 puntos)**

En el contexto de la Regla 2 del examen (descuento entre 0% y 40%), un compañero dice que basta con probar el descuento del 20% porque "si funciona con ese valor, funciona con todos". Explica por qué esa lógica es incorrecta y qué valores concretos deberías probar tú y por qué.

RESPUESTA: es incorrecto porque un solo valor no garantiza que el sistema maneje correctamente los límites y casos inválidos. Muchas veces los errores aparecen precisamente en los valores extremos o fuera del rango permitido.
Los valores que yo probaría serían:

0% - porque es el límite inferior y además la regla dice que es válido.
40% - porque es el límite máximo permitido y debe aceptarse.
20% - un valor válido dentro del rango para comprobar el funcionamiento normal.
-1% - para verificar que el sistema rechace descuentos negativos.
41% - para comprobar que el sistema rechace valores mayores al máximo permitido.

---

**PA-5 (0.3 puntos)**

Mirando el planeador de la asignatura, las semanas 3 y 4 cubren pruebas ágiles, TDD y BDD. Explica cómo estas prácticas se conectan con el concepto de CI/CD que veremos en la semana 6. ¿Qué pasaría con un pipeline de CI/CD si el equipo no tiene una suite de tests automatizados sólida?

RESPUESTA: Por que en un pipeline de CI/CD cada vez que un desarrollador sube cambios al repositorio el sistema ejecuta automáticamente compilaciones pruebas y validaciones antes de permitir el despliegue. Gracias a tdd y bdd el pipeline puede detectar errores rápidamente sin depender de pruebas manuales

si el equipo no tiene una suite de tests automatizados sólida, el pipeline pierde gran parte de su utilidad. El sistema podría compilar correctamente pero aun así contener bugs graves, errores de negocio o funcionalidades dañadas. Eso provocaría despliegues inseguros, fallos en producción y más tiempo corrigiendo problemas después de publicar el software. Además, el equipo perdería confianza en el pipeline y probablemente tendría que volver a revisar muchas cosas manualmente, haciendo más lento el desarrollo.