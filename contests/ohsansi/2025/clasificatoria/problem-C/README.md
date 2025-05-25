# Problema C

Dado:
* $N$ $(1 \leq N \leq 10^5)$
* Arreglo $A$ de tamaño $N$. $(1 \leq A_i \leq 10^6)$

Imprimir:
* El arreglo puede que tenga algunos elementos iguales **consecutivos**. Tu tarea es eliminar algunos elementos del arreglo, **manteniendo el orden original del arreglo** de manera que:
  * No existen elementos iguales consecutivos en el arreglo.
  * El tamaño del arreglo es lo más grande posible *(es decir, tienes que eliminar solo lo necesario)*.
* Tu tarea es imprimir este arreglo resultante luego de eliminar los elementos necesarios.

## Subtareas

### Subtarea 1
* El arreglo no tiene repetidos consecutivos: $A_i \neq A_{i+1}$ para todo $1 \leq i < N$

### Subtarea 2
* Si $A_i = A_{i+1}$ se garantiza que $A_{i+1} \neq A_{i+2}$.

### Subtarea 3
* $1 \leq N \leq 1000$

### Subtarea 4
* Sin restricciones adicionales.