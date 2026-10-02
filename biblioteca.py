class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = {}   # isbn -> Libro
        self._socios = {}   # dni -> Socio

    @property
    def nombre(self):
        return self._nombre

    def agregar_libro(self, libro):
        if libro.isbn in self._libros:
            raise ValueError(f"Ya existe un libro con ISBN {libro.isbn}")
        self._libros[libro.isbn] = libro

    def registrar_socio(self, socio):
        if socio.dni in self._socios:
            raise ValueError(f"Ya existe un socio con DNI {socio.dni}")
        self._socios[socio.dni] = socio

    def _buscar(self, isbn, dni):
        if isbn not in self._libros:
            raise ValueError(f"No existe el libro con ISBN {isbn}")
        if dni not in self._socios:
            raise ValueError(f"No existe el socio con DNI {dni}")
        return self._libros[isbn], self._socios[dni]

    def prestar(self, isbn, dni):
        libro, socio = self._buscar(isbn, dni)
        # Validar todo antes de modificar
        if not libro.disponible:
            raise ValueError(f"El libro '{libro.titulo}' no está disponible")
        if not socio.puede_pedir():
            raise ValueError(f"{socio.nombre} llegó al máximo de libros")
        socio.agregar_libro(libro)
        libro.prestar()

    def devolver(self, isbn, dni):
        libro, socio = self._buscar(isbn, dni)
        if libro not in socio.libros:
            raise ValueError(f"{socio.nombre} no tiene el libro '{libro.titulo}'")
        socio.quitar_libro(libro)
        libro.devolver()

    def libros_disponibles(self):
        return [l for l in self._libros.values() if l.disponible]