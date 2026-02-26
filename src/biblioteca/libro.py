"""
Módulo que define la clase Libro.

TODO (Principiantes - Paso 1):
- Definir la clase Libro con los atributos indicados.
- Implementar el método __str__ para mostrar la información del libro.
"""


class Libro:

    def __init__(self, id_libro: str, titulo: str, autor: str, anio: int, genero: str) -> None:
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.prestado = False

    def __str__(self):


        """
        pass  # TODO: Implementar

    def __str__(self) -> str:
        """
        Devuelve una representación en texto del libro.

        TODO: Retornar un string con el formato:
        "{id_libro}: {titulo} - {autor} ({anio}) [{genero}] · {estado}"

        Donde estado es "Prestado" si prestado=True, o "Disponible" si prestado=False.

        Ejemplo de salida:
        "L001: Cien años de soledad - García Márquez (1967) [Realismo Mágico] · Disponible"
        """
        pass  # TODO: Implementar
