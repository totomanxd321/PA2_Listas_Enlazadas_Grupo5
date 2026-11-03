# Representación gráfica

## Pila (LIFO), entra y sale por el tope
```
        apilar ↓   ↑ desapilar
      ┌────────────────────┐
tope→ │ Anular constancia  │
      ├────────────────────┤
      │ Cambiar nota       │
      ├────────────────────┤
      │ Editar matrícula   │
      └────────────────────┘
```

## Cola (FIFO), entra por el final y sale por el frente
```
 desencolar ←  ┌──────┬──────┬──────┬──────┐  ← encolar
   (frente)    │ S101 │ S102 │ S103 │ S104 │   (final)
               └──────┴──────┴──────┴──────┘
```

## Flujo del caso completo
```
Estudiante → [COLA de solicitudes] → atención → [PILA de acciones] → deshacer
              orden de llegada                    último en revertirse primero
```
