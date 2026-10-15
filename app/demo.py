"""Demostración explicable durante el video de evaluación PA2."""
from app.estructuras import ListaSimple, ListaDoble, ListaCircular, Solicitud


def ejecutar_demostracion():
    lista = ListaSimple()
    iniciales = [
        ("S101", "Constancia"), ("S102", "Orientación"),
        ("S103", "Reclamo"), ("S104", "Actualización"), ("S105", "Consulta"),
    ]
    for codigo, asunto in iniciales:
        lista.insertar_final(Solicitud(codigo, asunto))
    print("1. Lista inicial con cinco nodos:", " -> ".join(lista.codigos()))
    lista.insertar_inicio(Solicitud("S100", "Atención preferente"))
    print("2. Insertar al inicio:", " -> ".join(lista.codigos()))
    lista.insertar_final(Solicitud("S106", "Nueva solicitud"))
    print("3. Insertar al final:", " -> ".join(lista.codigos()))
    lista.insertar_despues("S102", Solicitud("S102A", "Caso complementario"))
    print("4. Insertar después de S102:", " -> ".join(lista.codigos()))
    encontrado = lista.buscar("S103")
    print("5. Buscar S103:", encontrado.dato.asunto if encontrado else "No encontrado")
    lista.modificar("S103", estado="En proceso")
    print("6. Modificar S103:", lista.buscar("S103").dato.estado)
    lista.eliminar("S104")
    print("7. Eliminar S104:", " -> ".join(lista.codigos()))
    lista.reubicar_despues("S105", "S101")
    print("8. Reubicar S105 después de S101:", " -> ".join(lista.codigos()))

    doble = ListaDoble()
    for codigo in ("S201", "S202", "S203"):
        doble.insertar_final(Solicitud(codigo, "Seguimiento"))
    print("9. Lista doble ->:", " <-> ".join(doble.recorrer_adelante()))
    print("10. Lista doble <-:", " <-> ".join(doble.recorrer_atras()))

    circular = ListaCircular()
    for codigo in ("S301", "S302", "S303"):
        circular.insertar_final(Solicitud(codigo, "Revisión periódica"))
    print("11. Una vuelta circular:", " -> ".join(circular.una_vuelta()), "-> vuelve al inicio")
    print("12. Cinco turnos:", " -> ".join(circular.siguiente_revision() for _ in range(5)))


if __name__ == "__main__":
    ejecutar_demostracion()
