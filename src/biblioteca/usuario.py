"""
Módulo que define la clase Usuario.

TODO (Principiantes - Paso 2):
- Definir la clase Usuario con los atributos indicados.
- Implementar el método puede_prestar() para validar límite de préstamos.
- Implementar el método __str__ para mostrar la información del usuario.
"""


class Usuario:
    """Representa a una persona que puede solicitar préstamos en la biblioteca."""

    def __init__(self, id_usuario: str, nombre: str, limite_prestamos: int = 3) -> None:
        """
        Inicializa un nuevo usuario.

        TODO: Asignar los parámetros a atributos de instancia.
        Además, crear un atributo 'prestamos' como una lista vacía que
        almacenará referencias a los préstamos del usuario.

        Args:
            id_usuario: Identificador único del usuario (ej: "U001")
            nombre: Nombre del usuario
            limite_prestamos: Máximo de préstamos activos permitidos (default: 3)
        """
        pass  # TODO: Implementar

    def puede_prestar(self) -> bool:
        """
        Verifica si el usuario puede solicitar un nuevo préstamo.

        TODO: Contar cuántos préstamos activos tiene el usuario.
        Un préstamo está activo si su fecha_devolucion es None.
        Retornar True si la cantidad de activos es menor al limite_prestamos.

        Pista: Usa una list comprehension para filtrar préstamos activos.

        Returns:
            True si el usuario puede pedir más libros, False si ya alcanzó el límite.
        """
        pass  # TODO: Implementar

    def __str__(self) -> str:
        """
        Devuelve una representación en texto del usuario.

        TODO: Retornar un string con el formato:
        "{id_usuario} - {nombre} · préstamos activos: {cantidad}"

        Donde cantidad es el número de préstamos con fecha_devolucion = None.

        Ejemplo de salida:
        "U001 - Ana · préstamos activos: 2"
        """
        pass  # TODO: Implementar
