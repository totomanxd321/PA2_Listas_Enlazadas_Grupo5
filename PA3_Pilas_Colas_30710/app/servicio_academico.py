"""Caso aplicado de pila para deshacer y cola para atender solicitudes."""
from dataclasses import dataclass
from typing import Any
from .estructuras import Cola, Pila

@dataclass(frozen=True)
class Cambio:
    campo: str
    valor_anterior: Any
    valor_nuevo: Any

@dataclass(frozen=True)
class Solicitud:
    codigo: str
    asunto: str

class ServicioAcademico:
    def __init__(self) -> None:
        self.ficha = {
            "correo": "alumno@instituto.edu",
            "telefono": "900000000",
            "estado": "Pendiente",
        }
        self.historial: Pila[Cambio] = Pila()
        self.pendientes: Cola[Solicitud] = Cola()
        self.atendidas: list[Solicitud] = []
        self._codigos_registrados: set[str] = set()

    def modificar_ficha(self, campo: str, nuevo_valor: str) -> bool:
        """Registra solamente modificaciones efectivas, conservando el valor anterior."""
        if campo not in self.ficha:
            raise KeyError(f"Campo inexistente: {campo}")
        anterior = self.ficha[campo]
        if anterior == nuevo_valor:
            return False
        self.ficha[campo] = nuevo_valor
        self.historial.apilar(Cambio(campo, anterior, nuevo_valor))
        return True

    def deshacer_ultima_modificacion(self) -> Cambio:
        cambio = self.historial.desapilar()
        self.ficha[cambio.campo] = cambio.valor_anterior
        return cambio

    def recibir_solicitud(self, codigo: str, asunto: str) -> None:
        if not codigo.strip() or not asunto.strip():
            raise ValueError("El código y el asunto no pueden estar vacíos")
        if codigo in self._codigos_registrados:
            raise ValueError(f"La solicitud {codigo} ya fue registrada")
        self.pendientes.encolar(Solicitud(codigo, asunto))
        self._codigos_registrados.add(codigo)

    def atender_siguiente_solicitud(self) -> Solicitud:
        solicitud = self.pendientes.desencolar()
        self.atendidas.append(solicitud)
        return solicitud
