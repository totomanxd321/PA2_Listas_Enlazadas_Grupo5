"""Implementaciones enlazadas de pila LIFO y cola FIFO, O(1) en sus extremos."""
from dataclasses import dataclass
from typing import Generic, Iterator, Optional, TypeVar
T = TypeVar("T")

@dataclass
class _Nodo(Generic[T]):
    valor: T
    siguiente: Optional["_Nodo[T]"] = None

class Pila(Generic[T]):
    """El último en entrar es el primero en salir (LIFO)."""
    def __init__(self) -> None:
        self._tope: Optional[_Nodo[T]] = None
        self._cantidad = 0

    def apilar(self, elemento: T) -> None:
        self._tope = _Nodo(elemento, self._tope)
        self._cantidad += 1

    def desapilar(self) -> T:
        if self.esta_vacia():
            raise IndexError("No se puede desapilar: la pila está vacía")
        assert self._tope is not None
        elemento = self._tope.valor
        self._tope = self._tope.siguiente
        self._cantidad -= 1
        return elemento

    def ver_tope(self) -> T:
        if self.esta_vacia():
            raise IndexError("No hay tope: la pila está vacía")
        assert self._tope is not None
        return self._tope.valor

    def esta_vacia(self) -> bool:
        return self._tope is None

    def __len__(self) -> int:
        return self._cantidad

    def __iter__(self) -> Iterator[T]:
        actual = self._tope
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente

class Cola(Generic[T]):
    """El primero en entrar es el primero en salir (FIFO)."""
    def __init__(self) -> None:
        self._frente: Optional[_Nodo[T]] = None
        self._final: Optional[_Nodo[T]] = None
        self._cantidad = 0

    def encolar(self, elemento: T) -> None:
        nuevo = _Nodo(elemento)
        if self._final is None:
            self._frente = nuevo
        else:
            self._final.siguiente = nuevo
        self._final = nuevo
        self._cantidad += 1

    def desencolar(self) -> T:
        if self.esta_vacia():
            raise IndexError("No se puede desencolar: la cola está vacía")
        assert self._frente is not None
        elemento = self._frente.valor
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._cantidad -= 1
        return elemento

    def ver_frente(self) -> T:
        if self.esta_vacia():
            raise IndexError("No hay frente: la cola está vacía")
        assert self._frente is not None
        return self._frente.valor

    def esta_vacia(self) -> bool:
        return self._frente is None

    def __len__(self) -> int:
        return self._cantidad

    def __iter__(self) -> Iterator[T]:
        actual = self._frente
        while actual is not None:
            yield actual.valor
            actual = actual.siguiente
