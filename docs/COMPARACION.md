# Actividad 4: comparación pila vs cola

| Aspecto | Pila | Cola |
|---|---|---|
| Principio de funcionamiento | LIFO: último en entrar, primero en salir | FIFO: primero en entrar, primero en salir |
| Operaciones principales | apilar, desapilar, ver tope, vacía | encolar, desencolar, ver frente, vacía |
| Forma de acceso | Un solo extremo (tope) | Dos extremos (final para entrar, frente para salir) |
| Ventajas en aplicación | Deshacer/rehacer, recursión, evaluación de expresiones | Turnos, atención justa, planificación de procesos |
| Costo de operaciones | O(1) | O(1) |

## Conclusión grupal
Elegir bien la estructura hace que el diseño refleje el flujo real del problema.
Si el historial de acciones fuera una cola, se revertiría la acción más antigua
y no la última. Si las solicitudes se guardaran en una pila, quien llegó primero
esperaría indefinidamente. En el caso de la unidad de servicios académicos, la
cola garantiza equidad en la atención y la pila garantiza reversión correcta.
