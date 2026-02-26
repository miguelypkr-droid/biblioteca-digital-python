"""
Script de demostración del sistema de Biblioteca Digital.

Este archivo muestra cómo usar las clases una vez implementadas.
Ejecútalo después de completar la actividad para verificar tu implementación:

    python -m src.biblioteca.main_demo

Salida esperada (aproximada):
    Préstamo concedido (id=P001).
    Préstamo concedido (id=P002).
    El libro ya está prestado.
    Devolución registrada.
    Préstamo concedido (id=P003).
    Top autores: [('García Márquez', 2), ('George Orwell', 1)]
    Disponibles por género: {'Realismo Mágico': 1, 'Distopía': 0, ...}
    Activos por usuario: {'U001': 1, 'U002': 1}
"""
from src.biblioteca.biblioteca import Biblioteca
from src.biblioteca.libro import Libro
from src.biblioteca.usuario import Usuario


def demo() -> None:
    """Ejecuta una demostración del sistema de biblioteca."""

    # Crear instancia de la biblioteca
    b = Biblioteca()

    # -------------------------------------------------------------------------
    # Paso 1: Registrar libros en el catálogo
    # -------------------------------------------------------------------------
    libros = [
        Libro("L001", "Cien años de soledad", "García Márquez", 1967, "Realismo Mágico"),
        Libro("L002", "El coronel no tiene quien le escriba", "García Márquez", 1961, "Realismo Mágico"),
        Libro("L003", "1984", "George Orwell", 1949, "Distopía"),
        Libro("L004", "Fahrenheit 451", "Ray Bradbury", 1953, "Ciencia Ficción"),
        Libro("L005", "El Principito", "Antoine de Saint-Exupéry", 1943, "Fábula"),
    ]
    for libro in libros:
        b.registrar_libro(libro)

    print(f"Libros registrados: {len(b.catalogo)}")

    # -------------------------------------------------------------------------
    # Paso 2: Registrar usuarios
    # -------------------------------------------------------------------------
    b.registrar_usuario(Usuario("U001", "Ana"))
    b.registrar_usuario(Usuario("U002", "Carlos", limite_prestamos=2))

    print(f"Usuarios registrados: {len(b.usuarios)}")

    # -------------------------------------------------------------------------
    # Paso 3: Realizar préstamos y devoluciones
    # -------------------------------------------------------------------------
    print("\n--- Operaciones de préstamo ---")
    print(b.prestar("U001", "L001"))  # Debería funcionar
    print(b.prestar("U001", "L003"))  # Debería funcionar
    print(b.prestar("U002", "L001"))  # Debería fallar: libro ya prestado

    print("\n--- Devolución ---")
    print(b.devolver("P001"))  # Devolver el primer préstamo

    print("\n--- Nuevo préstamo después de devolución ---")
    print(b.prestar("U002", "L001"))  # Ahora debería funcionar

    # -------------------------------------------------------------------------
    # Paso 4: Consultar reportes (Avanzados)
    # -------------------------------------------------------------------------
    print("\n--- Reportes ---")
    print("Top autores más prestados:", b.top_autores_mas_prestados())
    print("Disponibles por género:", b.disponibles_por_genero())
    print("Préstamos activos por usuario:", b.prestamos_activos_por_usuario())


if __name__ == "__main__":
    demo()
