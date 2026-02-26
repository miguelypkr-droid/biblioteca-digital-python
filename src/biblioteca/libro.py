class Libro:

    def __init__(self, id_libro: str, titulo: str, autor: str, anio: int, genero: str) -> None:
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.prestado = False

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"{self.id_libro}: {self.titulo} - {self.autor} ({self.anio}) [{self.genero}] · {estado}"

    pass