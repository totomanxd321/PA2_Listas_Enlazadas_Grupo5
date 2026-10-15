# Pseudocódigo de la PA2

**Modelo:** `Nodo(dato, siguiente)`, con `dato = Solicitud(codigo, asunto, estado)`. La lista simple conserva `cabeza` y `cola`. En una lista vacía ambos son `NULO`. Se considera que los códigos se verifican como únicos antes de insertar.

## Recorrido completo

```text
PROCEDIMIENTO Recorrer(cabeza)
    actual ← cabeza
    MIENTRAS actual ≠ NULO HACER
        MOSTRAR actual.dato
        actual ← actual.siguiente
    FIN MIENTRAS
FIN PROCEDIMIENTO
```

## Insertar al inicio

```text
PROCEDIMIENTO InsertarInicio(dato)
    nuevo ← Nodo(dato)
    nuevo.siguiente ← cabeza
    cabeza ← nuevo
    SI cola = NULO ENTONCES
        cola ← nuevo
    FIN SI
FIN PROCEDIMIENTO
```

**Efecto:** el nuevo nodo pasa a ser la cabeza. Si la lista estaba vacía, también es la cola.

## Insertar al final

```text
PROCEDIMIENTO InsertarFinal(dato)
    nuevo ← Nodo(dato)
    nuevo.siguiente ← NULO
    SI cabeza = NULO ENTONCES
        cabeza ← nuevo
    SINO
        cola.siguiente ← nuevo
    FIN SI
    cola ← nuevo
FIN PROCEDIMIENTO
```

**Efecto:** la antigua cola apunta al nuevo nodo y la cola se actualiza.

## Insertar después de un código

```text
FUNCIÓN InsertarDespues(codigo_previo, dato)
    previo ← Buscar(codigo_previo)
    SI previo = NULO ENTONCES DEVOLVER FALSO
    nuevo ← Nodo(dato)
    nuevo.siguiente ← previo.siguiente
    previo.siguiente ← nuevo
    SI cola = previo ENTONCES cola ← nuevo
    DEVOLVER VERDADERO
FIN FUNCIÓN
```

**Orden obligatorio de enlaces:** conectar `nuevo.siguiente` con el sucesor antiguo antes de conectar `previo.siguiente` con `nuevo`.

## Buscar por código

```text
FUNCIÓN Buscar(codigo)
    actual ← cabeza
    MIENTRAS actual ≠ NULO HACER
        SI actual.dato.codigo = codigo ENTONCES DEVOLVER actual
        actual ← actual.siguiente
    FIN MIENTRAS
    DEVOLVER NULO
FIN FUNCIÓN
```

## Modificar una solicitud

```text
FUNCIÓN Modificar(codigo, nuevo_asunto, nuevo_estado)
    nodo ← Buscar(codigo)
    SI nodo = NULO ENTONCES DEVOLVER FALSO
    SI nuevo_asunto está indicado ENTONCES nodo.dato.asunto ← nuevo_asunto
    SI nuevo_estado está indicado ENTONCES nodo.dato.estado ← nuevo_estado
    DEVOLVER VERDADERO
FIN FUNCIÓN
```

**Efecto:** cambian los datos, no los enlaces. No se modifica el código identificador.

## Eliminar una solicitud

```text
FUNCIÓN Eliminar(codigo)
    anterior ← NULO
    actual ← cabeza
    MIENTRAS actual ≠ NULO Y actual.dato.codigo ≠ codigo HACER
        anterior ← actual
        actual ← actual.siguiente
    FIN MIENTRAS
    SI actual = NULO ENTONCES DEVOLVER FALSO
    SI anterior = NULO ENTONCES
        cabeza ← actual.siguiente
    SINO
        anterior.siguiente ← actual.siguiente
    FIN SI
    SI cola = actual ENTONCES cola ← anterior
    actual.siguiente ← NULO
    DEVOLVER VERDADERO
FIN FUNCIÓN
```

**Casos:** eliminar cabeza (cambia `cabeza`), interior (el anterior salta al sucesor) y cola (se actualiza `cola`). Al borrar el último nodo ambos punteros quedan `NULO`.

## Reubicar un nodo después de otro

```text
FUNCIÓN ReubicarDespues(codigo, destino)
    SI codigo = destino ENTONCES DEVOLVER FALSO
    LOCALIZAR nodo Y su anterior
    LOCALIZAR nodo_destino
    SI alguno no existe ENTONCES DEVOLVER FALSO
    SI nodo_destino.siguiente = nodo ENTONCES DEVOLVER VERDADERO
    DESENLAZAR nodo (ajustar cabeza y cola cuando corresponda)
    nodo.siguiente ← nodo_destino.siguiente
    nodo_destino.siguiente ← nodo
    SI cola = nodo_destino ENTONCES cola ← nodo
    DEVOLVER VERDADERO
FIN FUNCIÓN
```

**Efecto:** se conserva la misma solicitud; solo cambia su posición y los enlaces. Es una operación adicional para atender el requisito del caso de mover expedientes.

## Lista doble: insertar y recorrer en ambos sentidos

```text
PROCEDIMIENTO InsertarFinalDoble(dato)
    nuevo ← NodoDoble(dato)
    nuevo.anterior ← cola
    nuevo.siguiente ← NULO
    SI cola = NULO ENTONCES cabeza ← nuevo
    SINO cola.siguiente ← nuevo
    cola ← nuevo
FIN PROCEDIMIENTO

PROCEDIMIENTO RecorrerHaciaAtras()
    actual ← cola
    MIENTRAS actual ≠ NULO HACER
        MOSTRAR actual.dato
        actual ← actual.anterior
    FIN MIENTRAS
FIN PROCEDIMIENTO
```

## Lista circular: agregar y revisar una vuelta

```text
PROCEDIMIENTO InsertarFinalCircular(dato)
    nuevo ← NodoCircular(dato)
    SI cola = NULO ENTONCES
        nuevo.siguiente ← nuevo
        cola ← nuevo
    SINO
        nuevo.siguiente ← cola.siguiente
        cola.siguiente ← nuevo
        cola ← nuevo
    FIN SI
FIN PROCEDIMIENTO

PROCEDIMIENTO UnaVueltaCircular()
    SI cola = NULO ENTONCES TERMINAR
    actual ← cola.siguiente
    REPETIR tamaño VECES
        MOSTRAR actual.dato
        actual ← actual.siguiente
    FIN REPETIR
FIN PROCEDIMIENTO
```

**Precaución:** una lista circular no termina en `NULO`. El recorrido necesita un límite explícito de `tamaño` nodos o detenerse al volver al inicio.
