# PA3 | Pilas (LIFO) y colas (FIFO) en una unidad de servicios académicos

**Curso:** Algoritmo y Estructura de Datos Basados en Inteligencia Artificial · **Código:** 30710 · **NRC:** 4134
**Docente:** Wildr Julio Espinoza Bravo · **Evaluación:** PA3, sesiones 8 a 10

## Objetivo
Modelar con una **pila** el historial de acciones que se deshacen en orden inverso y con una **cola** la atención de solicitudes en orden de llegada, justificando la elección de cada estructura.

## Integrantes
1. Leonardo Cuadros
2. Jhonatan Lino
3. Anthony Fernando
4. Victor Sinche

## Estructura de archivos
```
PA3_Pilas_Colas_Grupo5/
├── README.md
├── app/
│   ├── estructuras.py   # Pila y Cola
│   └── demo.py          # Flujo completo del caso
├── tests/
│   └── test_estructuras.py
├── docs/
│   ├── PSEUDOCODIGO.md
│   ├── DIAGRAMAS.md
│   ├── SELECCION_ESTRUCTURA.md
│   └── COMPARACION.md
├── diagramas/
└── entrega/             # informe PDF
```

## Instrucciones de uso
Requiere Python 3.10 o superior, sin dependencias externas. Desde la raíz del repositorio:

```
python -m app.demo
python -m unittest discover -s tests -v
```

## Decisiones de diseño
- **Pila:** historial de acciones; el último cambio es el primero en deshacerse.
- **Cola:** solicitudes de atención; se atiende primero a quien llegó primero.
- Ambas son de capacidad fija, con control de desbordamiento y de estructura vacía. Todas las operaciones son O(1).

## Informe y video
- Informe PDF: `entrega/` (pendiente de agregar)
- **Video de YouTube (no listado):** PENDIENTE, agregar el enlace aquí
