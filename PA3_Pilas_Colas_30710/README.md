# PA3 — Pilas LIFO y colas FIFO

**Curso:** Algoritmo y Estructura de Datos Basados en Inteligencia Artificial (30710). **Institución:** ISIL.  
**NRC:** 4134. **Docente:** Wildr Julio Espinoza Bravo. **Grupo:** Leonardo Cuadros, Jhonatan Lino, Anthony Fernando y Victor Sinche.

## Objetivo y solución
Modelar dos procesos de una unidad de servicios académicos: **deshacer cambios en orden inverso** (pila LIFO) y **atender solicitudes por llegada** (cola FIFO). La solución consta de conceptos, selección técnica, diagramas, pseudocódigo, código y pruebas.

## Materiales del proyecto
- **[Informe completo en PDF](entrega/Informe_PA3_Pilas_Colas.pdf)** (6 páginas con desarrollo, diagramas y conclusiones).
- [Informe completo en Markdown](docs/informe.md).
- [Algoritmos en pseudocódigo](pseudocodigo/algoritmos.md).
- [Diagrama de pila](diagramas/01_pila_lifo.svg), [diagrama de cola](diagramas/02_cola_fifo.svg) y [flujo integral](diagramas/03_flujo_general.svg).
- Implementación: `app/estructuras.py`, `app/servicio_academico.py`, `app/demo.py`.
- Pruebas: `tests/test_pilas_colas.py`.

## Estructura
```text
PA3_Pilas_Colas_30710/
├── README.md
├── entrega/Informe_PA3_Pilas_Colas.pdf
├── docs/informe.md
├── pseudocodigo/algoritmos.md
├── diagramas/01_pila_lifo.svg
├── diagramas/02_cola_fifo.svg
├── diagramas/03_flujo_general.svg
├── app/__init__.py
├── app/estructuras.py
├── app/servicio_academico.py
├── app/demo.py
└── tests/test_pilas_colas.py
```

## Implementación y verificación
Python 3.10 o superior, sin dependencias externas. Comandos empleados en la comprobación del programa:

```bash
python -m app.demo
python -m unittest discover -s tests -v
```

**Verificación local:** 22 pruebas correctas (6 de pila, 7 de cola y 9 del caso).


**Fuente:** enunciado y rúbrica de la PA3 (sesiones 8-10, curso 30710), suministrados por el docente.
