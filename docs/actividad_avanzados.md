# Actividad Guiada (Avanzados)

**Duración sugerida:** 45–75 min

## Objetivos
- Índices por autor/género, búsquedas y reportes.
- Validaciones, excepciones y límites por usuario.
- Diseño POO claro y reutilizable.

## Pasos
1. **Índices por autor y género**
   - Mantener `indice_por_autor` y `indice_por_genero` en `registrar_libro()`.
   - *Checkpoint:* búsquedas por autor devuelven cantidad esperada.

2. **Búsquedas**
   - `buscar_por_titulo(texto)` con substring case-insensitive.
   - Devuelve lista de `Libro`.

3. **Reglas y errores**
   - Evitar préstamo duplicado; respetar límite por usuario.
   - Usar `ValueError` para IDs inexistentes.

4. **Reportes**
   - `top_autores_mas_prestados(k)` usando el historial.
   - `disponibles_por_genero()` y `prestamos_activos_por_usuario()`.
