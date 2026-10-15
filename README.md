# PA2 | Gestión dinámica de solicitudes con listas enlazadas

**Curso:** Algoritmo y Estructura de Datos Basados en Inteligencia Artificial · **Código:** 30710  
**Evaluación:** PA2, sesiones 5 a 7 · **Modalidad:** grupal (hasta 5 estudiantes)

## Objetivo

Modelar el registro cambiante de solicitudes de atención usando listas enlazadas y explicar cómo se conectan los nodos durante recorridos, inserciones, búsquedas, modificaciones, eliminaciones y reubicaciones. Se contrastan una **lista simple**, una **doble** y una **circular**, justificando el uso de cada una en la misma organización.

## Integrantes

1. [Nombre y apellido del integrante 1]
2. [Nombre y apellido del integrante 2]
3. [Nombre y apellido del integrante 3]
4. [Nombre y apellido del integrante 4]
5. [Nombre y apellido del integrante 5]

## Caso y decisiones de diseño

- **Lista enlazada simple:** mantiene el orden de las solicitudes y permite gestionar su alta, búsqueda, cambio de estado, baja y reubicación.
- **Lista doble:** conserva la secuencia de revisión de expedientes, permitiendo retroceder sin reiniciar desde el principio.
- **Lista circular simple:** asigna turnos de supervisión repetidos; después de la última solicitud retorna a la primera.
- Cada nodo almacena una `Solicitud` (`codigo`, `asunto`, `estado`) y uno o dos enlaces a otros nodos, según la estructura. El ejemplo usa códigos únicos dentro de la lista simple.

## Organización del repositorio

```text
PA2_Listas_Enlazadas_Grupo5/
├── README.md
├── app/
│   ├── __init__.py
│   ├── estructuras.py          # Nodos y tres tipos de lista
│   └── demo.py                 # Ejecución de las operaciones explicadas
├── tests/
│   └── test_estructuras.py     # Pruebas automáticas
├── docs/
│   ├── PSEUDOCODIGO.md
│   ├── DIAGRAMAS.md
│   ├── GUIA_EXPOSICION_5.md
│   ├── CHECKLIST_ENTREGA.md
│   └── PROMPT_CODEX.md
├── diagramas/                  # Diagramas PNG y SVG
└── entrega/
    ├── Informe_PA2_Listas_Enlazadas.pdf
    ├── Informe_PA2_Listas_Enlazadas.docx
    ├── Guion_PA2_5_Integrantes.pdf
    ├── Guion_PA2_5_Integrantes.docx
    └── Laminas_PA2_Para_Exposicion.pdf
```

## Requisitos y ejecución

- Python **3.10 o superior**. El proyecto usa **solo la biblioteca estándar**, sin instalar dependencias.
- Abrir una terminal en la **raíz del repositorio** y ejecutar:

```bash
python -m app.demo
```

El programa muestra el orden original con cinco nodos y después cada operación realizada, además del recorrido doble y de los turnos circulares.

## Comprobar funcionamiento

Desde la raíz, ejecutar:

```bash
python -m unittest discover -s tests -v
```

Las pruebas cubren: recorridos, inserciones, búsqueda, modificación, eliminación de cabeza/interior/cola, reubicación, códigos repetidos, lista vacía, navegación bidireccional y circularidad.

## Ejemplo comprobable de la lista simple

```text
Inicial:          S101 → S102 → S103 → S104 → S105 → ∅
Insertar inicio:  S100 → S101 → S102 → S103 → S104 → S105 → ∅
Insertar al fin:  S100 → S101 → S102 → S103 → S104 → S105 → S106 → ∅
Después de S102:  S100 → S101 → S102 → S102A → S103 → S104 → S105 → S106 → ∅
Eliminar S104:    S100 → S101 → S102 → S102A → S103 → S105 → S106 → ∅
```

`∅` indica la referencia nula del último nodo de la lista simple.

## Comparación de costos

| Operación | Lista simple: costo estructural |
| --- | --- |
| Recorrer / buscar por código | O(n) |
| Insertar al inicio con nodo preparado | O(1) |
| Insertar al final con puntero `cola` | O(1) |
| Insertar después del nodo conocido | O(1) |
| Insertar después de un **código** que primero debe localizarse | O(n) |
| Eliminar la cabeza | O(1) |
| Eliminar interior o cola buscando por código | O(n) |
| Modificar datos de un nodo ya localizado | O(1) |

**Aclaración importante:** en la implementación, cada inserción de la lista simple comprueba antes si el código ya existe, lo que añade **O(n)** al tiempo completo de esa llamada. La tabla distingue el costo de cambiar enlaces del costo adicional de la búsqueda/validación. No se presenta erróneamente el método completo como O(1).

## Informe y video

- Informe final: [`entrega/Informe_PA2_Listas_Enlazadas.pdf`](entrega/Informe_PA2_Listas_Enlazadas.pdf)
- Archivo editable: [`entrega/Informe_PA2_Listas_Enlazadas.docx`](entrega/Informe_PA2_Listas_Enlazadas.docx)
- Guion de exposición: [`docs/GUIA_EXPOSICION_5.md`](docs/GUIA_EXPOSICION_5.md) y [`entrega/Guion_PA2_5_Integrantes.pdf`](entrega/Guion_PA2_5_Integrantes.pdf)
- Láminas para mostrar en la grabación: [`entrega/Laminas_PA2_Para_Exposicion.pdf`](entrega/Laminas_PA2_Para_Exposicion.pdf)
- **Video de YouTube (no listado):** `[PEGAR AQUÍ EL ENLACE REAL DEL VIDEO]`
- **Repositorio de GitHub:** `[PEGAR AQUÍ EL ENLACE REAL DEL REPOSITORIO]`

> **Antes de entregar:** reemplazar los cinco nombres y enlaces. Publicar el video con cámaras encendidas y participación de los cinco miembros, confirmar que el enlace funciona sin iniciar sesión y dejar evidencia verídica de asistencia y avances en clases. No se incluye evidencia inventada.

## Material de apoyo

Los documentos `docs/PSEUDOCODIGO.md` y `docs/DIAGRAMAS.md` amplían el procedimiento. `docs/PROMPT_CODEX.md` está listo para llevar esta versión al repositorio con Codex sin cambiar el comportamiento ni las respuestas del informe.
