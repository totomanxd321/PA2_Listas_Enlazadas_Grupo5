""" Estructuras enlazadas """
from dataclasses import dataclass
from typing import Optional, Iterator


@dataclass
class Solicitud:
    """Representa la unidad de información (nodo de datos) almacenada en cada estructura."""
    codigo: str
    asunto: str
    estado: str = "Pendiente"

    def __post_init__(self):
        """Valida que el código del registro no esté vacío antes de instanciar el objeto."""
        if not self.codigo or not self.codigo.strip():
            raise ValueError("El código de la solicitud no puede estar vacío ni contener solo espacios.")


class NodoSimple:
    """Nodo individual para la lista enlazada simple que conecta un dato con el siguiente nodo."""
    def __init__(self, dato: Solicitud):
        self.dato: Solicitud = dato
        self.siguiente: Optional["NodoSimple"] = None


class ListaSimple:
    """Lista simple con punteros optimizados."""

    def __init__(self):
        self.cabeza: Optional[NodoSimple] = None
        self.cola: Optional[NodoSimple] = None
        self.tamano: int = 0

    def __iter__(self) -> Iterator[Solicitud]:
        """Permite recorrer secuencialmente la estructura."""
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def codigos(self) -> list[str]:
        """Retorna una lista simple con los códigos en orden de enlace."""
        return [solicitud.codigo for solicitud in self]

    def buscar(self, codigo: str) -> Optional[NodoSimple]:
        """Busca y retorna la referencia completa al nodo que coincide con el código (O(n))."""
        if not codigo:
            return None
        actual = self.cabeza
        while actual is not None:
            if actual.dato.codigo == codigo:
                return actual
            actual = actual.siguiente
        return None

    def _comprobar_unico(self, codigo: str) -> None:
        """Verifica que el código no exista previamente para evitar duplicados en el registro."""
        if self.buscar(codigo) is not None:
            raise ValueError(f"Error de integridad: El código de solicitud '{codigo}' ya se encuentra registrado.")

    def insertar_inicio(self, dato: Solicitud) -> None:
        """Inserta una nueva solicitud al principio de la lista simple (O(1) de enlaces)."""
        self._comprobar_unico(dato.codigo)
        nuevo = NodoSimple(dato)
        
        # El nuevo nodo apunta a la antigua cabeza
        nuevo.siguiente = self.cabeza
        # La cabeza ahora pasa a ser el nuevo nodo
        self.cabeza = nuevo
        
        # Si la lista estaba vacía, la cola también debe apuntar al nuevo nodo
        if self.cola is None:
            self.cola = nuevo
            
        self.tamano += 1

    def insertar_final(self, dato: Solicitud) -> None:
        """Inserta una solicitud al final utilizando el puntero cola de forma directa (O(1))."""
        self._comprobar_unico(dato.codigo)
        nuevo = NodoSimple(dato)
        
        if self.cola is None:
            # Si la lista está vacía, cabeza y cola coinciden
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            # La antigua cola enlaza con el nuevo nodo y actualizamos el puntero cola
            self.cola.siguiente = nuevo
            self.cola = nuevo
            
        self.tamano += 1

    def insertar_despues(self, codigo_previo: str, dato: Solicitud) -> bool:
        """Inserta un nodo inmediatamente después de otro ubicado mediante su código."""
        self._comprobar_unico(dato.codigo)
        previo = self.buscar(codigo_previo)
        
        if previo is None:
            return False  # No se encontró el punto de anclaje previo
            
        nuevo = NodoSimple(dato)
        # 1. El nuevo nodo apunta al sucesor que tenía el nodo previo
        nuevo.siguiente = previo.siguiente
        # 2. El nodo previo ahora apunta al nuevo nodo
        previo.siguiente = nuevo
        
        # Si insertamos justo después de la cola, actualizamos el puntero cola
        if self.cola is previo:
            self.cola = nuevo
            
        self.tamano += 1
        return True

    def modificar(self, codigo: str, *, asunto: Optional[str] = None,
                  estado: Optional[str] = None) -> bool:
        """Modifica los atributos internos de una solicitud sin alterar su posición ni sus enlaces."""
        nodo = self.buscar(codigo)
        if nodo is None:
            return False
        if asunto is not None:
            if not asunto.strip():
                raise ValueError("El asunto no puede estar vacío.")
            nodo.dato.asunto = asunto
        if estado is not None:
            if not estado.strip():
                raise ValueError("El estado no puede estar vacío.")
            nodo.dato.estado = estado
        return True

    def eliminar(self, codigo: str) -> bool:
        """Elimina un nodo de la lista simple reajustando los punteros anterior y siguiente."""
        anterior = None
        actual = self.cabeza
        
        # Buscamos el nodo y guardamos una referencia a su predecesor
        while actual is not None and actual.dato.codigo != codigo:
            anterior, actual = actual, actual.siguiente
            
        if actual is None:
            return False  # El elemento no existe
            
        if anterior is None:
            # El elemento a eliminar es la cabeza
            self.cabeza = actual.siguiente
        else:
            # El elemento está en el interior o es la cola
            anterior.siguiente = actual.siguiente
            
        # Si eliminamos el último elemento, actualizamos el puntero cola
        if self.cola is actual:
            self.cola = anterior
            
        # Limpieza de referencias del nodo extraído
        actual.siguiente = None
        self.tamano -= 1
        return True

    def reubicar_despues(self, codigo: str, codigo_destino: str) -> bool:
        """Reubica un nodo existente hacia una nueva posición detrás de un nodo destino."""
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
            return True  # Ya se encuentra en la posición correcta
            
        # 1. Desconectar el nodo de su posición original
        if anterior is None:
            self.cabeza = nodo.siguiente
        else:
            anterior.siguiente = nodo.siguiente
            
        if self.cola is nodo:
            self.cola = anterior
            
        # 2. Conectar el nodo detrás del nodo destino
        nodo.siguiente = destino.siguiente
        destino.siguiente = nodo
        
        if self.cola is destino:
            self.cola = nodo
            
        return True


class NodoDoble:
    """Nodo con doble enlace (anterior y siguiente) para navegación bidireccional."""
    def __init__(self, dato: Solicitud):
        self.dato: Solicitud = dato
        self.anterior: Optional["NodoDoble"] = None
        self.siguiente: Optional["NodoDoble"] = None


class ListaDoble:
    """Estructura de lista doble para consulta retrospectiva de expedientes."""

    def __init__(self):
        self.cabeza: Optional[NodoDoble] = None
        self.cola: Optional[NodoDoble] = None
        self.tamano: int = 0

    def insertar_final(self, dato: Solicitud) -> None:
        """Inserta un nodo manteniendo sincronizados los punteros doble (anterior/siguiente)."""
        nuevo = NodoDoble(dato)
        nuevo.anterior = self.cola
        nuevo.siguiente = None
        
        if self.cola is None:
            self.cabeza = nuevo
        else:
            self.cola.siguiente = nuevo
            
        self.cola = nuevo
        self.tamano += 1

    def recorrer_adelante(self) -> list[str]:
        """Recorre la lista doble desde la cabeza hacia la cola."""
        salida = []
        actual = self.cabeza
        while actual is not None:
            salida.append(actual.dato.codigo)
            actual = actual.siguiente
        return salida

    def recorrer_atras(self) -> list[str]:
        """Recorre la lista doble en sentido inverso, desde la cola hacia la cabeza."""
        salida = []
        actual = self.cola
        while actual is not None:
            salida.append(actual.dato.codigo)
            actual = actual.anterior
        return salida


class NodoCircular:
    """Nodo con enlace simple que apunta al siguiente elemento de una ronda."""
    def __init__(self, dato: Solicitud):
        self.dato: Solicitud = dato
        self.siguiente: Optional["NodoCircular"] = None


class ListaCircular:
    """Lista circular simple donde el último nodo (cola) conecta de vuelta con la cabeza."""

    def __init__(self):
        self.cola: Optional[NodoCircular] = None
        self.tamano: int = 0
        self.turno: Optional[NodoCircular] = None

    def insertar_final(self, dato: Solicitud) -> None:
        """Inserta un nodo preservando la propiedad circular del ciclo."""
        nuevo = NodoCircular(dato)
        
        if self.cola is None:
            # Lista vacía: el nodo se apunta a sí mismo
            nuevo.siguiente = nuevo
            self.cola = nuevo
            self.turno = nuevo
        else:
            # El nuevo nodo apunta a la cabeza actual (cola.siguiente)
            nuevo.siguiente = self.cola.siguiente
            # La cola actual apunta al nuevo nodo
            self.cola.siguiente = nuevo
            # El nuevo nodo pasa a ser la nueva cola
            self.cola = nuevo
            
        self.tamano += 1

    def una_vuelta(self) -> list[str]:
        """Realiza un recorrido completo controlado por el tamaño para evitar bucles infinitos."""
        if self.cola is None:
            return []
            
        actual = self.cola.siguiente  # Inicia en la cabeza
        resultado = []
        for _ in range(self.tamano):
            resultado.append(actual.dato.codigo)
            actual = actual.siguiente
            
        return resultado

    def siguiente_revision(self) -> Optional[str]:
        """Obtiene el turno actual y desplaza el cursor circular hacia el siguiente miembro."""
        if self.turno is None:
            return None
            
        codigo = self.turno.dato.codigo
        self.turno = self.turno.siguiente
        return codigo