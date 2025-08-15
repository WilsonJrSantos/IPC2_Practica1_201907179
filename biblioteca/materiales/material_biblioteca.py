import random
import string
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class MaterialBiblioteca(ABC):
    """
    Clase abstracta que representa un material genérico de biblioteca.
    Implementa el concepto de Abstracción definiendo la estructura común
    para todos los materiales bibliográficos.
    """
    
    def __init__(self, titulo, autor):
        # Atributos privados - Implementa Encapsulamiento
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = self.__generar_codigo()
        self.__prestado = False
        self.__fecha_prestamo = None
        self.__fecha_devolucion = None
    
    def __generar_codigo(self):
        """Genera un código único de 8 caracteres alfanuméricos"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    # Getters
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def prestado(self):
        return self.__prestado
    
    @property
    def fecha_prestamo(self):
        return self.__fecha_prestamo
    
    @property
    def fecha_devolucion(self):
        return self.__fecha_devolucion
    
    # Setters
    @titulo.setter
    def titulo(self, nuevo_titulo):
        if nuevo_titulo and nuevo_titulo.strip():
            self.__titulo = nuevo_titulo.strip()
        else:
            raise ValueError("El título no puede estar vacío")
    
    @autor.setter
    def autor(self, nuevo_autor):
        if nuevo_autor and nuevo_autor.strip():
            self.__autor = nuevo_autor.strip()
        else:
            raise ValueError("El autor no puede estar vacío")
    
    def prestar(self):
        """Presta el material si está disponible"""
        if not self.__prestado:
            self.__prestado = True
            self.__fecha_prestamo = datetime.now()
            self.__fecha_devolucion = self.__fecha_prestamo + timedelta(days=self.dias_prestamo())
            return True
        return False
    
    def devolver(self):
        """Devuelve el material si está prestado"""
        if self.__prestado:
            self.__prestado = False
            self.__fecha_prestamo = None
            self.__fecha_devolucion = None
            return True
        return False
    
    def mostrar_informacion(self):
        """Muestra información básica del material"""
        estado = "Prestado" if self.__prestado else "Disponible"
        info = f"""
╭─────────────────────────────────╮
│         INFORMACIÓN GENERAL     │
├─────────────────────────────────┤
│ Título: {self.__titulo:<20} │
│ Autor:  {self.__autor:<20} │
│ Código: {self.__codigo:<20} │
│ Estado: {estado:<20} │"""
        
        if self.__prestado and self.__fecha_devolucion:
            fecha_dev = self.__fecha_devolucion.strftime("%d/%m/%Y")
            info += f"\n│ Devolver antes: {fecha_dev:<12} │"
        
        info += "\n╰─────────────────────────────────╯"
        return info
    
    @abstractmethod
    def dias_prestamo(self):
        """Define los días máximos de préstamo según el tipo de material"""
        pass
    
    @abstractmethod
    def informacion_especifica(self):
        """Información específica según el tipo de material"""
        pass