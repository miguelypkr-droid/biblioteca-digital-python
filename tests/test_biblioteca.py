"""
Pruebas unitarias para el sistema de Biblioteca Digital.

NOTA IMPORTANTE PARA ESTUDIANTES:
---------------------------------
Estas pruebas están diseñadas para verificar tu implementación.
Al principio, TODAS las pruebas fallarán porque el código no está implementado.

A medida que completes cada parte de la actividad, más pruebas pasarán.
Ejecuta las pruebas frecuentemente para verificar tu progreso:

    python -m unittest discover -s tests -p "test_*.py" -v

Cuando TODAS las pruebas pasen, habrás completado la actividad exitosamente.
"""
import unittest

from src.biblioteca.biblioteca import Biblioteca
from src.biblioteca.libro import Libro
from src.biblioteca.usuario import Usuario


class BibliotecaTests(unittest.TestCase):
    def setUp(self):
        self.b = Biblioteca()
        # Datos base
        self.libros = [
            Libro("L001", "Cien años de soledad", "García Márquez", 1967, "Realismo Mágico"),
            Libro("L002", "El coronel no tiene quien le escriba", "García Márquez", 1961, "Realismo Mágico"),
            Libro("L003", "1984", "George Orwell", 1949, "Distopía"),
        ]
        for l in self.libros:
            self.b.registrar_libro(l)
        self.b.registrar_usuario(Usuario("U001", "Ana", limite_prestamos=2))
        self.b.registrar_usuario(Usuario("U002", "Carlos", limite_prestamos=1))

    def test_registro_unico_de_ids(self):
        with self.assertRaises(ValueError):
            self.b.registrar_libro(self.libros[0])  # id repetido
        with self.assertRaises(ValueError):
            self.b.registrar_usuario(Usuario("U001", "Otro"))  # id repetido

    def test_prestar_y_devolver_flujo_feliz(self):
        msg = self.b.prestar("U001", "L001")
        self.assertIn("Préstamo concedido", msg)
        # devolver
        self.assertEqual("Devolución registrada.", self.b.devolver("P001"))

    def test_libro_ya_prestado(self):
        self.b.prestar("U001", "L001")
        self.assertEqual("El libro ya está prestado.", self.b.prestar("U002", "L001"))

    def test_limite_de_prestamos_de_usuario(self):
        # U002 tiene límite 1
        self.b.prestar("U002", "L002")
        self.assertEqual("El usuario no tiene cupo disponible.", self.b.prestar("U002", "L003"))

    def test_busquedas(self):
        res_autor = self.b.buscar_por_autor("García Márquez")
        self.assertGreaterEqual(len(res_autor), 2)
        res_titulo = self.b.buscar_por_titulo("cien")
        self.assertTrue(any(l.titulo == "Cien años de soledad" for l in res_titulo))
        res_genero = self.b.buscar_por_genero("Distopía")
        self.assertEqual(len(res_genero), 1)

    def test_reportes(self):
        self.b.prestar("U001", "L001")
        self.b.prestar("U001", "L003")
        self.b.devolver("P001")
        top = self.b.top_autores_mas_prestados(k=2)
        self.assertTrue(len(top) <= 2)
        disp = self.b.disponibles_por_genero()
        self.assertIsInstance(disp, dict)
        activos = self.b.prestamos_activos_por_usuario()
        self.assertGreaterEqual(sum(activos.values()), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
