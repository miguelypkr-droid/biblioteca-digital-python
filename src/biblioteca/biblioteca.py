class Biblioteca:
    def __init__(self) -> None:
        self.catalogo: dict[str, Libro] = {}
        self.usuarios: dict[str, Usuario] = {}
        self.prestamos_activos: list[Prestamo] = []
        self.indice_por_autor: dict[str, list[str]] = {}
        self.indice_por_genero: dict[str, list[str]] = {}
        self.historial_prestamos: dict[str, list[str]] = {}

    def registrar_libro(self, libro: Libro) -> None:
        if libro.id_libro in self.catalogo:
            raise ValueError("El id_libro ya existe.")
        self.catalogo[libro.id_libro] = libro
        """
        Registra un libro en el catálogo.

        TODO:
        1. Verificar que el id_libro no exista ya en self.catalogo.
           Si existe, lanzar ValueError("El id_libro ya existe.")
        2. Agregar el libro al diccionario self.catalogo usando id_libro como clave.

        TODO (Avanzados - Paso 1):
        3. Agregar el id_libro a self.indice_por_autor[libro.autor]
        4. Agregar el id_libro a self.indice_por_genero[libro.genero]

        Pista: Usa dict.setdefault(clave, []).append(valor) para los índices.

        Args:
            libro: Instancia de Libro a registrar

        Raises:
            ValueError: Si el id_libro ya está registrado
        """
        pass  # TODO: Implementar

    def registrar_usuario(self, usuario: Usuario) -> None:
        """
        Registra un usuario en el sistema.

        TODO:
        1. Verificar que el id_usuario no exista ya en self.usuarios.
           Si existe, lanzar ValueError("El id_usuario ya existe.")
        2. Agregar el usuario al diccionario self.usuarios usando id_usuario como clave.

        Args:
            usuario: Instancia de Usuario a registrar

        Raises:
            ValueError: Si el id_usuario ya está registrado
        """
        pass  # TODO: Implementar

    # =========================================================================
    # OPERACIONES DE NEGOCIO (Principiantes - Paso 4)
    # =========================================================================

    def prestar(self, id_usuario: str, id_libro: str) -> str:
        """
        Realiza el préstamo de un libro a un usuario.

        TODO:
        1. Validar que id_usuario exista en self.usuarios.
           Si no existe, lanzar ValueError("Usuario no existe.")
        2. Validar que id_libro exista en self.catalogo.
           Si no existe, lanzar ValueError("Libro no existe.")
        3. Si el libro ya está prestado (libro.prestado == True),
           retornar "El libro ya está prestado."
        4. Si el usuario no puede prestar más (usuario.puede_prestar() == False),
           retornar "El usuario no tiene cupo disponible."
        5. Marcar el libro como prestado (libro.prestado = True).
        6. Crear un nuevo Prestamo con un ID único (ej: "P001", "P002", ...).
           Pista: f"P{len(self.prestamos_activos)+1:03d}" genera "P001", "P002", etc.
        7. Agregar el préstamo a usuario.prestamos y a self.prestamos_activos.
        8. Registrar el evento en el historial (opcional pero recomendado).
        9. Retornar f"Préstamo concedido (id={id_prestamo})."

        Args:
            id_usuario: ID del usuario que solicita el préstamo
            id_libro: ID del libro a prestar

        Returns:
            Mensaje indicando el resultado de la operación

        Raises:
            ValueError: Si el usuario o libro no existen
        """
        pass  # TODO: Implementar

    def devolver(self, id_prestamo: str) -> str:
        """
        Registra la devolución de un préstamo.

        TODO:
        1. Buscar el préstamo en self.prestamos_activos por id_prestamo.
        2. Si no se encuentra, retornar "No se encontró el préstamo activo."
        3. Si se encuentra:
           a. Llamar a prestamo.marcar_devuelto()
           b. Marcar el libro como no prestado (libro.prestado = False)
           c. Remover el préstamo de self.prestamos_activos
           d. Registrar el evento en el historial (opcional)
           e. Retornar "Devolución registrada."

        Args:
            id_prestamo: ID del préstamo a devolver

        Returns:
            Mensaje indicando el resultado de la operación
        """
        pass  # TODO: Implementar

    # =========================================================================
    # BÚSQUEDAS (Avanzados - Paso 2)
    # =========================================================================

    def buscar_por_autor(self, autor: str) -> list[Libro]:
        """
        Busca libros por nombre de autor.

        TODO:
        1. Obtener la lista de IDs desde self.indice_por_autor.get(autor, [])
        2. Convertir los IDs a objetos Libro y retornarlos.

        Args:
            autor: Nombre del autor a buscar

        Returns:
            Lista de libros del autor (puede estar vacía)
        """
        pass  # TODO: Implementar

    def buscar_por_genero(self, genero: str) -> list[Libro]:
        """
        Busca libros por género.

        TODO:
        1. Obtener la lista de IDs desde self.indice_por_genero.get(genero, [])
        2. Convertir los IDs a objetos Libro y retornarlos.

        Args:
            genero: Género a buscar

        Returns:
            Lista de libros del género (puede estar vacía)
        """
        pass  # TODO: Implementar

    def buscar_por_titulo(self, texto: str) -> list[Libro]:
        """
        Busca libros cuyo título contenga el texto dado (case-insensitive).

        TODO:
        1. Convertir el texto de búsqueda a minúsculas.
        2. Filtrar self.catalogo.values() buscando libros cuyo título
           (en minúsculas) contenga el texto.

        Pista: Usa una list comprehension con 'in' para verificar substring.

        Args:
            texto: Texto a buscar en los títulos

        Returns:
            Lista de libros que coinciden (puede estar vacía)
        """
        pass  # TODO: Implementar

    # =========================================================================
    # REPORTES (Avanzados - Paso 4)
    # =========================================================================

    def top_autores_mas_prestados(self, k: int = 3) -> list[tuple]:
        """
        Retorna los k autores con más préstamos en el historial.

        TODO:
        1. Recorrer self.historial_prestamos para contar préstamos por autor.
        2. Los eventos de préstamo contienen "Prestado: {titulo}".
        3. Usar el título para encontrar el autor en self.catalogo.
        4. Retornar los k autores más frecuentes como lista de tuplas (autor, cantidad).

        Pista: Usa collections.Counter para contar y su método most_common(k).

        Args:
            k: Cantidad de autores a retornar (default: 3)

        Returns:
            Lista de tuplas (autor, cantidad) ordenada de mayor a menor
        """
        pass  # TODO: Implementar

    def disponibles_por_genero(self) -> dict[str, int]:
        """
        Cuenta libros disponibles (no prestados) por género.

        TODO:
        1. Para cada género en self.indice_por_genero:
        2. Contar cuántos de sus libros tienen prestado=False.
        3. Retornar diccionario {género: cantidad_disponibles}.

        Returns:
            Diccionario con cantidad de libros disponibles por género
        """
        pass  # TODO: Implementar

    def prestamos_activos_por_usuario(self) -> dict[str, int]:
        """
        Cuenta préstamos activos por usuario.

        TODO:
        1. Crear un diccionario con todos los id_usuario inicializados en 0.
        2. Recorrer self.prestamos_activos y sumar 1 por cada préstamo.
        3. Retornar el diccionario {id_usuario: cantidad_activos}.

        Returns:
            Diccionario con cantidad de préstamos activos por usuario
        """
        pass  # TODO: Implementar

    # =========================================================================
    # UTILIDADES INTERNAS (Opcional - pueden ser útiles)
    # =========================================================================

    def _registrar_evento(self, id_usuario: str, evento: str) -> None:
        """
        Registra un evento en el historial de un usuario.

        Uso sugerido:
        self._registrar_evento(id_usuario, f"{datetime.now().date()} - Prestado: {titulo}")
        self._registrar_evento(id_usuario, f"{datetime.now().date()} - Devuelto: {titulo}")

        Args:
            id_usuario: ID del usuario
            evento: Descripción del evento
        """
        self.historial_prestamos.setdefault(id_usuario, []).append(evento)

    def _ids_a_libros(self, ids: list[str]) -> list[Libro]:
        """
        Convierte una lista de IDs a una lista de objetos Libro.

        Args:
            ids: Lista de id_libro

        Returns:
            Lista de objetos Libro correspondientes
        """
        return [self.catalogo[i] for i in ids if i in self.catalogo]
