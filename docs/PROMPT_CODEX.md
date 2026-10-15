# Instrucción lista para Codex: publicación e implementación en GitHub

Copia el texto siguiente en Codex cuando tengas abierta la carpeta de proyecto y un repositorio autorizado.

---

Actúa como desarrollador colaborador del trabajo PA2 del curso 30710, «Algoritmo y Estructura de Datos Basados en Inteligencia Artificial». Tengo ya preparados los archivos de este proyecto: `app/estructuras.py`, `app/demo.py`, `tests/test_estructuras.py`, `README.md`, `docs/`, `diagramas/` y `entrega/`. Mi objetivo es publicar **este mismo proyecto** en el repositorio GitHub que autorice, sin inventar funcionalidades ni modificar respuestas académicas.

Tareas:
1. Comprueba la estructura de carpetas. No borres el informe ni los diagramas.
2. Ejecuta desde la raíz `python -m app.demo` y `python -m unittest discover -s tests -v`. Reporta el resultado.
3. Comprueba que la implementación usa **nodos propios enlazados**, no listas nativas como estructura de almacenamiento de la lista simple, doble y circular. Las listas de Python usadas para recoger/mostrar resultados sí están permitidas.
4. Verifica integridad de los enlaces `cabeza`, `cola`, `siguiente` y `anterior` en las operaciones implementadas. Conserva códigos únicos en lista simple y la seguridad del recorrido circular con un límite explícito.
5. Verifica que el README contenga el objetivo, los cinco integrantes (si te los proporciono), instrucciones para ejecutar y probar, estructura del repositorio y el enlace **real** del video si te lo proporciono. De lo contrario, mantén marcadores de pendiente.
6. Comprueba y, si hace falta, configura un `.gitignore` para `__pycache__`, `.pytest_cache`, `.venv`, archivos temporales y datos personales no intencionales.
7. Muestra los cambios propuestos y solicita mi aprobación antes de hacer un `git push` o publicar en remoto. No inventes URL de GitHub ni de YouTube, ni afirmes que un video o una asistencia ya existen.
8. Si un cambio funcional es necesario, explica cómo afecta pseudocódigo, diagramas y PDF; evita que código e informe se contradigan.

Criterio: solución comprensible por un alumno de primeros ciclos, variables y comentarios en español, sin bibliotecas adicionales y completamente demostrable ante cámara.

---
