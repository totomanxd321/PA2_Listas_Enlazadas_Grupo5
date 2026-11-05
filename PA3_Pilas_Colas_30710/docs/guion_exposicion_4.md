# PA3 — Guion de exposición (cuatro integrantes)

**Curso:** 30710 · **Docente:** Wildr Julio Espinoza Bravo · **NRC:** 4134  
**Formato:** todos los integrantes con cámaras encendidas. Duración referencial: 10 a 12 minutos.

## Leonardo Cuadros — Presentación y pila LIFO (3 minutos)
> Buenos días, profesor. Presentamos la PA3 sobre pilas y colas. La unidad de servicios académicos tiene dos necesidades diferentes: deshacer cambios y atender solicitudes según su llegada. Para deshacer elegimos una pila LIFO: el último cambio es el primero que se revierte. En el gráfico tenemos A1, A2 y A3. A3 se encuentra en el tope y sale primero. Nuestra clase Pila implementa apilar, desapilar, ver_tope y esta_vacia. En una ficha, registramos el campo y su valor anterior; por eso deshacer A3 restaura el valor original, no solo elimina una etiqueta.

**En pantalla:** portada, pila y pseudocódigo de las cuatro operaciones.

## Jhonatan Lino — Cola FIFO (2 minutos)
> La segunda necesidad es respetar turnos. Una cola FIFO atiende primero a quien llegó primero. Entran S101, S102 y S103; el frente es S101. Encolar inserta al final y desencolar quita por el frente. Ver_frente solo consulta y esta_vacia comprueba si quedan solicitudes. Usamos una cola enlazada con punteros frente y final para que las dos operaciones principales sean O(1). Si usáramos una pila, S103 sería atendida antes que S101 y no cumpliríamos el enunciado.

**En pantalla:** gráfico de cola, tabla de cambios y pseudocódigo.

## Anthony Fernando — Selección y comparación (2:30 minutos)
> En la tercera actividad elegimos pila para revertir acciones recientes, cola para atención por llegada, pila cuando el último debe salir primero y cola para trámites pendientes. La razón es el orden de extracción. En la cuarta actividad comparamos LIFO con FIFO, tope con frente/final y las operaciones de cada estructura. No elegimos una sola estructura para ambos procesos, porque cambiaríamos su lógica. Una pila sirve para deshacer; una cola garantiza turnos.

**En pantalla:** tabla de selección y cuadro comparativo del informe.

## Victor Sinche — Programa, pruebas y conclusión (3 minutos)
> Implementamos ambos mecanismos en Python. Ejecutamos `python -m app.demo`: primero veremos A3 desapilada y luego S101 atendida. El sistema restaura el valor anterior de la ficha, evita solicitudes duplicadas y maneja estructuras vacías con errores controlados. Después ejecutamos `python -m unittest discover -s tests -v`: son 22 pruebas que verificamos localmente. En conclusión, la estructura correcta depende de cuál elemento debe salir primero. Nuestra pila mantiene una reversión coherente y nuestra cola ordena los trámites académicos.

**En pantalla:** terminal, salida de la demo, pruebas y README de GitHub.

## Lista final para el grupo
- Grabar a **los cuatro** con cámaras encendidas.
- Mostrar gráficos, pseudocódigo, demo y resultado de tests.
- Publicar video en YouTube preferentemente como no listado.
- Pegar enlace real de YouTube en el README.
- La asistencia la verifica el profesor.
