


class Usuario:

    def __init__(self, id_usuario: str, nombre: str, limite_prestamos: int = 3) -> None:
        self.id_usuario= id_usuario
        self.nombre = nombre
        self.limite_prestamos = limite_prestamos
        self.prestamos = []

        pass

    def puede_prestar(self) -> bool:
        prestamos_activos = [p for p in self.prestamos if p.fecha_devolucion is None]
        return len(prestamos_activos) < self.limite_prestamos

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
