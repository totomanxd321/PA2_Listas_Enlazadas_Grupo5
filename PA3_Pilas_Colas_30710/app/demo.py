"""Demostración reproducible de LIFO, FIFO y el caso de servicios académicos."""
from .estructuras import Cola, Pila
from .servicio_academico import ServicioAcademico

def main() -> None:
    print("=== DEMOSTRACIÓN DE LIFO Y FIFO ===")
    pila: Pila[str] = Pila()
    print("Pila vacía:", pila.esta_vacia())
    for accion in ("A1", "A2", "A3"):
        pila.apilar(accion)
    print("Pila de tope a base:", " -> ".join(pila))
    print("Tope:", pila.ver_tope())
    print("Desapilar:", pila.desapilar())

    cola: Cola[str] = Cola()
    print("Cola vacía:", cola.esta_vacia())
    for codigo in ("S101", "S102", "S103"):
        cola.encolar(codigo)
    print("Cola de frente a final:", " -> ".join(cola))
    print("Frente:", cola.ver_frente())
    print("Desencolar:", cola.desencolar())

    print("\n=== CASO APLICADO: SERVICIOS ACADÉMICOS ===")
    sistema = ServicioAcademico()
    sistema.modificar_ficha("correo", "alumna@instituto.edu")
    sistema.modificar_ficha("telefono", "988888888")
    sistema.modificar_ficha("estado", "En revisión")
    print("Ficha antes de deshacer:", sistema.ficha)
    accion = sistema.deshacer_ultima_modificacion()
    print("Se deshizo:", accion.campo)
    print("Ficha después de deshacer:", sistema.ficha)

    sistema.recibir_solicitud("S101", "Constancia de estudios")
    sistema.recibir_solicitud("S102", "Orientación de matrícula")
    sistema.recibir_solicitud("S103", "Reclamo académico")
    print("Pendientes:", [s.codigo for s in sistema.pendientes])
    print("Atendida:", sistema.atender_siguiente_solicitud().codigo)
    print("Restantes:", [s.codigo for s in sistema.pendientes])

if __name__ == "__main__":
    main()
