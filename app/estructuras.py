
from dataclasses import dataclass


@dataclass
class Solicitud:
    codigo: str
    asunto: str
    estado: str = "pendiente"

    def __str__(self):
        return f"{self.codigo}"


@dataclass
class Accion:
    descripcion: str

    def __str__(self):
        return self.descripcion


class PilaVaciaError(Exception):
    """Subdesbordamiento: se intentó desapilar o ver el tope de una pila vacía."""


class PilaLlenaError(Exception):
    """Desbordamiento: se intentó apilar en una pila llena."""


class ColaVaciaError(Exception):
    """Se intentó desencolar o ver el frente de una cola vacía."""


class ColaLlenaError(Exception):
    """Se intentó encolar en una cola llena."""


class Pila:
    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.tope = -1

    def esta_vacia(self):
        return self.tope == -1

    def esta_llena(self):
        return self.tope == self.capacidad - 1

    def apilar(self, elemento):
        if self.esta_llena():
            raise PilaLlenaError("La pila está llena")
        self.tope += 1
        self.datos[self.tope] = elemento

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        elemento = self.datos[self.tope]
        self.datos[self.tope] = None
        self.tope -= 1
        return elemento

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")
        return self.datos[self.tope]

    def tamano(self):
        return self.tope + 1

    def __str__(self):
        if self.esta_vacia():
            return "Pila: [vacía]"
        elementos = [str(self.datos[i]) for i in range(self.tope, -1, -1)]
        return "Pila (tope primero): " + " | ".join(elementos)


class Cola:
    """Cola circular: frente y final avanzan con módulo de la capacidad."""

    def __init__(self, capacidad=10):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.frente = 0
        self.final = -1
        self.cantidad = 0

    def esta_vacia(self):
        return self.cantidad == 0

    def esta_llena(self):
        return self.cantidad == self.capacidad

    def encolar(self, elemento):
        if self.esta_llena():
            raise ColaLlenaError("La cola está llena")
        self.final = (self.final + 1) % self.capacidad
        self.datos[self.final] = elemento
        self.cantidad += 1

    def desencolar(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        elemento = self.datos[self.frente]
        self.datos[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.cantidad -= 1
        return elemento

    def ver_frente(self):
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía")
        return self.datos[self.frente]

    def tamano(self):
        return self.cantidad

    def __str__(self):
        if self.esta_vacia():
            return "Cola: [vacía]"
        elementos = [str(self.datos[(self.frente + i) % self.capacidad])
                     for i in range(self.cantidad)]
        return "Cola (frente primero): " + " -> ".join(elementos)
