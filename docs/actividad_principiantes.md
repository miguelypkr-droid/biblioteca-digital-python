# Actividad Guiada (Principiantes)

**Duración sugerida:** 45–60 min

## Objetivos
- Definir clases básicas (`Libro`, `Usuario`, `Biblioteca`).
- Usar listas y diccionarios para colecciones e historiales.
- Implementar flujo básico de préstamo y devolución.

## Pasos
1. **Clase `Libro`**
   - Atributos: `id_libro`, `titulo`, `autor`, `anio`, `genero`, `prestado=False`.
   - Método `__str__`.
   - *Checkpoint:* crear y `print()` de 2 libros.

2. **Clase `Usuario`**
   - Atributos: `id_usuario`, `nombre`, `limite_prestamos=2`, `prestamos=[]`.
   - Método `puede_prestar()`.
   - *Checkpoint:* validar `puede_prestar()` en vacío.

3. **Clase `Biblioteca` – altas**
   - Estructuras: `catalogo (dict)`, `usuarios (dict)`, `historial_prestamos (dict)`.
   - Métodos: `registrar_libro()`, `registrar_usuario()`.
   - *Checkpoint:* registrar 3 libros y 2 usuarios.

4. **Préstamo/Devolución**
   - `prestar(id_usuario, id_libro)`: valida disponibilidad y cupo.
   - `devolver(id_prestamo)`: marca devolución y actualiza estados.
   - Actualiza `historial_prestamos` con strings descriptivos.
   - *Checkpoint:* 2 préstamos, 1 devolución, imprimir historial.

## Pistas útiles
- `historial.setdefault(id, []).append(evt)`
- Comprensiones de listas para filtrar estados.

## Criterios de Éxito Mínimo
- Préstamo y devolución funcionan.
- Historial registra eventos.
