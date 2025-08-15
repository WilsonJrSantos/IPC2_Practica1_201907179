from material_biblioteca import MaterialBiblioteca

class LibroFisico(MaterialBiblioteca):
    """
    Clase que representa un libro físico.
    Hereda de MaterialBiblioteca e implementa características específicas.
    """
    
    def __init__(self, titulo, autor, numero_ejemplar):
        super().__init__(titulo, autor)
        self.__numero_ejemplar = numero_ejemplar
    
    @property
    def numero_ejemplar(self):
        return self.__numero_ejemplar
    
    @numero_ejemplar.setter
    def numero_ejemplar(self, nuevo_numero):
        if isinstance(nuevo_numero, int) and nuevo_numero > 0:
            self.__numero_ejemplar = nuevo_numero
        else:
            raise ValueError("El número de ejemplar debe ser un entero positivo")
    
    def dias_prestamo(self):
        """Los libros físicos se prestan por 7 días máximo"""
        return 7
    
    def informacion_especifica(self):
        """Información específica del libro físico"""
        return f"Número de Ejemplar: {self.__numero_ejemplar}"
    
    def mostrar_informacion(self):
        """Muestra información completa del libro físico"""
        info_base = super().mostrar_informacion()
        info_especifica = info_base.replace("│         INFORMACIÓN GENERAL     │", 
                                             "│          LIBRO FÍSICO           │")
        
        lineas = info_especifica.split('\n')
        lineas.insert(-1, f"│ Ejemplar Nº: {self.__numero_ejemplar:<15} │")
        lineas.insert(-1, f"│ Días préstamo: {self.dias_prestamo():<13} │")
        
        return '\n'.join(lineas)