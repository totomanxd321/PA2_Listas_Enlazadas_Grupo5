"""Estructuras enlazadas implementadas sin listas de Python como almacenamiento.
Caso académico: gestión dinámica de solicitudes de atención (curso 30710).
"""
from dataclasses import dataclass
from typing import Optional, Iterator


@dataclass
class Solicitud:
    codigo: str
    asunto: str
    estado: str = "Pendiente"

    def __post_init__(self):
        if not self.codigo.strip():
            raise ValueError("El código de la solicitud no puede estar vacío")


class NodoSimple:
    def __init__(self, dato: Solicitud):
        self.dato = dato
        self.siguiente: Optional["NodoSimple"] = None


class ListaSimple:
    """Lista simple con punteros a cabeza y cola; códigos únicos."""

    def __init__(self):
        self.cabeza: Optional[NodoSimple] = None
        self.cola: Optional[NodoSimple] = None
        self.tamano = 0

    def __iter__(self) -> Iterator[Solicitud]:
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def codigos(self) -> list[str]:
        return [solicitud.codigo for solicitud in self]

    def buscar(self, codigo: str) -> Optional[NodoSimple]:
        actual = self.cabeza
        while actual is not None:
            if actual.dato.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def _comprobar_unico(self, codigo: str) -> None:
        if self.buscar(codigo) is not None:
            raise ValueError(f"El código {codigo} ya existe")

    def insertar_inicio(self, dato: Solicitud) -> None:
        self._comprobar_unico(dato.codigo)
        nuevo = NodoSimple(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        if self.cola is None:
            self.cola = nuevo
        self.tamano += 1

    def insertar_final(self, dato: Solicitud) -> None:
        self._comprobar_unico(dato.codigo)
        nuevo = NodoSimple(dato)
        if self.cola is None:
            self.cabeza = nuevo
        else:
            self.cola.siguiente = nuevo
        self.cola = nuevo
        self.tamano += 1

    def insertar_despues(self, codigo_previo: str, dato: Solicitud) -> bool:
        """Devuelve False si no existe el nodo previo."""
        self._comprobar_unico(dato.codigo)
        previo = self.buscar(codigo_previo)
        if previo is None:
            return False
        nuevo = NodoSimple(dato)
        nuevo.siguiente = previo.siguiente
        previo.siguiente = nuevo
        if self.cola is previo:
            self.cola = nuevo
        self.tamano += 1
        return True

    def modificar(self, codigo: str, *, asunto: Optional[str] = None,
                  estado: Optional[str] = None) -> bool:
        nodo = self.buscar(codigo)
        if nodo is None:
            return False
        if asunto is not None:
            nodo.dato.asunto = asunto
        if estado is not None:
            nodo.dato.estado = estado
        return True

    def eliminar(self, codigo: str) -> bool:
        anterior = None
        actual = self.cabeza
        while actual is not None and actual.dato.codigo != codigo:
            anterior, actual = actual, actual.siguiente
        if actual is None:
            return False
        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente
        if self.cola is actual:
            self.cola = anterior
        self.tamano -= 1
        actual.siguiente = None
        return True

    def reubicar_despues(self, codigo: str, codigo_destino: str) -> bool:
        """Mueve un nodo existente después de otro. No crea un registro duplicado."""
        if codigo == codigo_destino:
            return False
        anterior = None
        nodo = self.cabeza
        while nodo is not None and nodo.dato.codigo != codigo:
            anterior, nodo = nodo, nodo.siguiente
        destino = self.buscar(codigo_destino)
        if nodo is None or destino is None:
            return False
        if nodo is destino.siguiente:
            return True  # Ya está en la posición deseada.
        # Separar el nodo del enlace actual.
        if anterior is None:
            self.cabeza = nodo.siguiente
        else:
            anterior.siguiente = nodo.siguiente
        if self.cola is nodo:
            self.cola = anterior
        # Reconectar tras el destino.
        nodo.siguiente = destino.siguiente
        destino.siguiente = nodo
        if self.cola is destino:
            self.cola = nodo
        return True


class NodoDoble:
    def __init__(self, dato: Solicitud):
        self.dato = dato
        self.anterior: Optional["NodoDoble"] = None
        self.siguiente: Optional["NodoDoble"] = None


class ListaDoble:
    """Historial para navegar por solicitudes hacia adelante y atrás."""

    def __init__(self):
        self.cabeza: Optional[NodoDoble] = None
        self.cola: Optional[NodoDoble] = None
        self.tamano = 0

    def insertar_final(self, dato: Solicitud) -> None:
        nuevo = NodoDoble(dato)
        nuevo.anterior = self.cola
        if self.cola is None:
            self.cabeza = nuevo
        else:
            self.cola.siguiente = nuevo
        self.cola = nuevo
        self.tamano += 1

    def recorrer_adelante(self) -> list[str]:
        salida = []
        actual = self.cabeza
        while actual is not None:
            salida.append(actual.dato.codigo)
            actual = actual.siguiente
        return salida

    def recorrer_atras(self) -> list[str]:
        salida = []
        actual = self.cola
        while actual is not None:
            salida.append(actual.dato.codigo)
            actual = actual.anterior
        return salida


class NodoCircular:
    def __init__(self, dato: Solicitud):
        self.dato = dato
        self.siguiente: Optional["NodoCircular"] = None


class ListaCircular:
    """Ronda continua de revisión; la cola apunta de nuevo a la cabeza."""

    def __init__(self):
        self.cola: Optional[NodoCircular] = None
        self.tamano = 0
        self.turno: Optional[NodoCircular] = None

    def insertar_final(self, dato: Solicitud) -> None:
        nuevo = NodoCircular(dato)
        if self.cola is None:
            nuevo.siguiente = nuevo
            self.cola = nuevo
            self.turno = nuevo
        else:
            nuevo.siguiente = self.cola.siguiente
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.tamano += 1

    def una_vuelta(self) -> list[str]:
        """Visita exactamente tamano nodos y termina: evita un bucle infinito."""
        if self.cola is None:
            return []
        actual = self.cola.siguiente
        resultado = []
        for _ in range(self.tamano):
            resultado.append(actual.dato.codigo)
            actual = actual.siguiente
        return resultado

    def siguiente_revision(self) -> Optional[str]:
        """Devuelve el turno actual y avanza el cursor para la siguiente consulta."""
        if self.turno is None:
            return None
        codigo = self.turno.dato.codigo
        self.turno = self.turno.siguiente
        return codigo
