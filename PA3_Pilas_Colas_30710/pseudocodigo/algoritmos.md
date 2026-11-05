# Algoritmos en pseudocódigo — PA3

## Pila LIFO: tope ← NULO, cantidad ← 0

```text
PROCEDIMIENTO APILAR(valor)
    nuevo ← Nodo(valor)
    nuevo.siguiente ← tope
    tope ← nuevo
    cantidad ← cantidad + 1
FIN

FUNCIÓN DESAPILAR()
    SI ESTA_VACIA_PILA() ENTONCES ERROR "Pila vacía"
    valor ← tope.valor
    tope ← tope.siguiente
    cantidad ← cantidad - 1
    DEVOLVER valor
FIN

FUNCIÓN VER_TOPE()
    SI ESTA_VACIA_PILA() ENTONCES ERROR "Pila vacía"
    DEVOLVER tope.valor
FIN

FUNCIÓN ESTA_VACIA_PILA()
    DEVOLVER tope = NULO
FIN
```

## Cola FIFO: frente ← NULO, final ← NULO, cantidad ← 0

```text
PROCEDIMIENTO ENCOLAR(valor)
    nuevo ← Nodo(valor)
    SI final = NULO ENTONCES
        frente ← nuevo
    SINO
        final.siguiente ← nuevo
    FIN SI
    final ← nuevo
    cantidad ← cantidad + 1
FIN

FUNCIÓN DESENCOLAR()
    SI ESTA_VACIA_COLA() ENTONCES ERROR "Cola vacía"
    valor ← frente.valor
    frente ← frente.siguiente
    SI frente = NULO ENTONCES final ← NULO
    cantidad ← cantidad - 1
    DEVOLVER valor
FIN

FUNCIÓN VER_FRENTE()
    SI ESTA_VACIA_COLA() ENTONCES ERROR "Cola vacía"
    DEVOLVER frente.valor
FIN

FUNCIÓN ESTA_VACIA_COLA()
    DEVOLVER frente = NULO
FIN
```

## Aplicación al caso

```text
PROCEDIMIENTO REGISTRAR_CAMBIO(campo, nuevo)
    SI campo NO EXISTE EN ficha ENTONCES ERROR "Campo inexistente"
    anterior ← ficha[campo]
    SI anterior = nuevo ENTONCES DEVOLVER FALSO
    ficha[campo] ← nuevo
    APILAR(Cambio(campo, anterior, nuevo))
    DEVOLVER VERDADERO
FIN

FUNCIÓN DESHACER_CAMBIO()
    cambio ← DESAPILAR()
    ficha[cambio.campo] ← cambio.valor_anterior
    DEVOLVER cambio
FIN

PROCEDIMIENTO RECIBIR_SOLICITUD(codigo, asunto)
    VALIDAR codigo Y asunto Y AUSENCIA DE DUPLICADOS
    ENCOLAR(Solicitud(codigo, asunto))
FIN

FUNCIÓN ATENDER_SIGUIENTE()
    solicitud ← DESENCOLAR()
    REGISTRAR COMO ATENDIDA solicitud
    DEVOLVER solicitud
FIN
```

**Complejidad:** apilar, desapilar, ver tope, comprobar pila vacía, encolar, desencolar, ver frente y comprobar cola vacía toman O(1) con nodos y punteros de extremos. Las validaciones de códigos del caso usan un conjunto hash y tienen O(1) promedio. Recorrer n elementos requiere O(n).
