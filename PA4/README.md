# Orientación inteligente dentro del campus · PA4

**Curso 30710 — Algoritmo y Estructura de Datos Basados en Inteligencia Artificial.**

El módulo ordena el directorio de un campus, busca un servicio por nombre y compara rutas entre ubicaciones. El campus es didáctico. Para ir de Entrada a Laboratorio, BFS elige dos tramos (14 minutos) y A* elige tres (4 minutos). DFS permite inspeccionar las seis ubicaciones alcanzables.

## Integrantes y organización

| Equipo del curso | Responsabilidad propuesta | Producto para sustentar |
|---|---|---|
| Leonardo Cuadros | Directorio y recursividad | Traza de búsqueda, casos base y consulta ausente |
| Jhonatan Lino | Ordenamiento | Divisiones, mezclas y prueba de orden |
| Anthony Fernando | Grafo, DFS y BFS | Conexiones, orden de visita y ruta de menos tramos |
| Victor Sinche | A* e integración | Heurística, comparación de costos y verificación final |

La [matriz de participación](docs/Matriz_participacion.xlsx) vincula los aportes reales con fecha, evidencia y revisión de otro integrante. La nota calculada es una coevaluación interna sobre 20. La asistencia la verifica el docente.

## Archivos

- [Informe completo](docs/Informe_PA4.pdf) — cuatro actividades, pseudocódigo, trazas, decisiones, conclusiones y anexo.
- [Grafo del campus](docs/Grafo.png) — conexiones bidireccionales y minutos por tramo.
- [Programa](campus.py) — directorio y búsquedas.
- [Pruebas](test_campus.py) — siete comprobaciones automatizadas.
- [Salida del programa](evidencias/demostracion.txt) y [registro de pruebas](evidencias/pruebas.txt).

## Ejecución

Con Python 3.8 o superior, abrir una terminal en la carpeta que contiene este README. El programa usa únicamente la biblioteca estándar.

```sh
python campus.py
python -m unittest -v
```

Si el comando de Python 3 en el equipo es `python3` o `py -3`, sustituir `python` por ese comando en ambas líneas. La primera muestra el directorio, dos consultas, el orden DFS y las rutas. La segunda termina en `OK` si se cumplen todas las comprobaciones.

## Exposición

Video de YouTube omitido por decisión del grupo.
