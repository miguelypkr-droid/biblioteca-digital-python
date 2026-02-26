"""
Módulo que define la clase Prestamo.

TODO (Principiantes - Paso 4):
- Definir la clase Prestamo con los atributos indicados.
- Implementar el método marcar_devuelto() para registrar la devolución.
"""
from datetime import datetime


class Prestamo:
    """Representa el préstamo de un libro a un usuario."""

    def __init__(
        self,
        id_prestamo: str,
        id_libro: str,
        id_usuario: str,
        fecha_salida: datetime | None = None
    ) -> None:
        """
        Inicializa un nuevo préstamo.

        TODO: Asignar los parámetros a atributos de instancia.
        - Si fecha_salida es None, usar datetime.now() como valor.
        - Crear un atributo 'fecha_devolucion' que inicie en None.

        Args:
            id_prestamo: Identificador único del préstamo (ej: "P001")
            id_libro: ID del libro prestado
            id_usuario: ID del usuario que recibe el préstamo
            fecha_salida: Fecha/hora del préstamo (default: momento actual)
        """
        pass  # TODO: Implementar

    def marcar_devuelto(self) -> None:
        """
        Registra la devolución del préstamo.

        TODO: Asignar datetime.now() al atributo fecha_devolucion.
        """
        pass  # TODO: Implementar
