
from app.estructuras import Accion, Cola, Pila, PilaVaciaError, Solicitud


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def main():
    titulo("1. COLA (FIFO): llegada de solicitudes")
    cola = Cola(capacidad=5)
    for codigo, asunto in [("S101", "Constancia de estudios"),
                           ("S102", "Reclamo de nota"),
                           ("S103", "Cambio de turno"),
                           ("S104", "Retiro de curso")]:
        cola.encolar(Solicitud(codigo, asunto))
        print(f"Encolar {codigo}")
    print(cola)
    print("Frente:", cola.ver_frente())

    titulo("2. Atención en orden de llegada + registro en PILA (LIFO)")
    historial = Pila(capacidad=10)
    while not cola.esta_vacia():
        sol = cola.desencolar()
        sol.estado = "atendida"
        historial.apilar(Accion(f"Atender {sol.codigo} ({sol.asunto})"))
        print(f"Desencolar y atender {sol.codigo}")
    print(cola)
    print(historial)
    print("Tope:", historial.ver_tope())

    titulo("3. Deshacer acciones (orden inverso al registro)")
    while not historial.esta_vacia():
        accion = historial.desapilar()
        print("Deshacer ->", accion.descripcion)
    print(historial)

    titulo("4. Manejo de error: desapilar con pila vacía")
    try:
        historial.desapilar()
    except PilaVaciaError as error:
        print("Error controlado:", error)

    titulo("5. Selección de estructura")
    tabla = [
        ("Registro de acciones recientes para revertir", "PILA"),
        ("Atención de solicitudes en orden de llegada", "COLA"),
        ("Último ingresado se atiende primero", "PILA"),
        ("Flujo de espera de trámites pendientes", "COLA"),
    ]
    for situacion, estructura in tabla:
        print(f"{situacion:<48} -> {estructura}")


if __name__ == "__main__":
    main()
