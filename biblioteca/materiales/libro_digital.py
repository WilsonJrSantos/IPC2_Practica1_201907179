from .material_biblioteca import MaterialBiblioteca

class LibroDigital(MaterialBiblioteca):
    """
    Clase que representa un libro digital.
    Hereda de MaterialBiblioteca e implementa características específicas.
    """
    
    def __init__(self, titulo, autor, tamaño_archivo):
        super().__init__(titulo, autor)
        self.__tamaño_archivo = tamaño_archivo
    
    @property
    def tamaño_archivo(self):
        return self.__tamaño_archivo
    
    @tamaño_archivo.setter
    def tamaño_archivo(self, nuevo_tamaño):
        if isinstance(nuevo_tamaño, (int, float)) and nuevo_tamaño > 0:
            self.__tamaño_archivo = nuevo_tamaño
        else:
            raise ValueError("El tamaño del archivo debe ser un número positivo")
    
    def dias_prestamo(self):
        """Los libros digitales se prestan por 3 días máximo"""
        return 3
    
    def informacion_especifica(self):
        """Información específica del libro digital"""
        return f"Tamaño de Archivo: {self.__tamaño_archivo} MB"
    
    def mostrar_informacion(self):
        """Muestra información completa del libro digital"""
        info_base = super().mostrar_informacion()
        info_especifica = info_base.replace("│         INFORMACIÓN GENERAL     │", 
                                             "│          LIBRO DIGITAL          │")
        
        lineas = info_especifica.split('\n')
        lineas.insert(-1, f"│ Archivo: {self.__tamaño_archivo:<18} MB │")
        lineas.insert(-1, f"│ Días préstamo: {self.dias_prestamo():<13} │")
        
        return '\n'.join(lineas)