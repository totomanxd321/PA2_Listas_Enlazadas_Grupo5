# Pseudocódigo

## Pila (LIFO)
```
APILAR(pila, x):
    si pila.tope == capacidad - 1 -> error "desbordamiento"
    pila.tope <- pila.tope + 1
    pila.datos[pila.tope] <- x

DESAPILAR(pila):
    si VACIA(pila) -> error "subdesbordamiento"
    x <- pila.datos[pila.tope]
    pila.tope <- pila.tope - 1
    retornar x

VER_TOPE(pila):
    si VACIA(pila) -> error
    retornar pila.datos[pila.tope]

VACIA(pila):
    retornar pila.tope == -1
```

## Cola (FIFO, circular)
```
ENCOLAR(cola, x):
    si cola.cantidad == capacidad -> error "cola llena"
    cola.final <- (cola.final + 1) mod capacidad
    cola.datos[cola.final] <- x
    cola.cantidad <- cola.cantidad + 1

DESENCOLAR(cola):
    si VACIA(cola) -> error
    x <- cola.datos[cola.frente]
    cola.frente <- (cola.frente + 1) mod capacidad
    cola.cantidad <- cola.cantidad - 1
    retornar x

VER_FRENTE(cola):
    si VACIA(cola) -> error
    retornar cola.datos[cola.frente]

VACIA(cola):
    retornar cola.cantidad == 0
```

Todas las operaciones son O(1).
