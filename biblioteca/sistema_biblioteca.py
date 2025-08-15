#sistema_biblioteca.py
from materiales.libro_fisico import LibroFisico
from materiales.libro_digital import LibroDigital

class SistemaBiblioteca:
    """
    Clase que gestiona el sistema completo de la biblioteca.
    Implementa todas las funcionalidades requeridas.
    """
    
    def __init__(self):
        self.__materiales = []
    
    def registrar_libro_fisico(self):
        """Registra un nuevo libro físico en el sistema"""
        try:
            print("\n═══ REGISTRO DE LIBRO FÍSICO ═══")
            titulo = input("Ingrese el título del libro: ").strip()
            if not titulo:
                print("Error: El título no puede estar vacío")
                return False
            
            autor = input("Ingrese el autor del libro: ").strip()
            if not autor:
                print("Error: El autor no puede estar vacío")
                return False
            
            numero_ejemplar = input("Ingrese el número de ejemplar: ").strip()
            try:
                numero_ejemplar = int(numero_ejemplar)
                if numero_ejemplar <= 0:
                    print("Error: El número de ejemplar debe ser positivo")
                    return False
            except ValueError:
                print("Error: El número de ejemplar debe ser un número entero")
                return False
            
            libro = LibroFisico(titulo, autor, numero_ejemplar)
            self.__materiales.append(libro)
            
            print(f"Libro físico registrado exitosamente!")
            print(f"Código asignado: {libro.codigo}")
            return True
            
        except Exception as e:
            print(f"Error al registrar el libro: {str(e)}")
            return False
    
    def registrar_libro_digital(self):
        """Registra un nuevo libro digital en el sistema"""
        try:
            print("\n═══ REGISTRO DE LIBRO DIGITAL ═══")
            titulo = input("Ingrese el título del libro: ").strip()
            if not titulo:
                print("Error: El título no puede estar vacío")
                return False
            
            autor = input("Ingrese el autor del libro: ").strip()
            if not autor:
                print("Error: El autor no puede estar vacío")
                return False
            
            tamaño = input("Ingrese el tamaño del archivo (MB): ").strip()
            try:
                tamaño = float(tamaño)
                if tamaño <= 0:
                    print("Error: El tamaño del archivo debe ser positivo")
                    return False
            except ValueError:
                print("Error: El tamaño debe ser un número")
                return False
            
            libro = LibroDigital(titulo, autor, tamaño)
            self.__materiales.append(libro)
            
            print(f"Libro digital registrado exitosamente!")
            print(f"Código asignado: {libro.codigo}")
            return True
            
        except Exception as e:
            print(f"Error al registrar el libro: {str(e)}")
            return False
    
    def buscar_material(self, codigo):
        """Busca un material por su código único"""
        for material in self.__materiales:
            if material.codigo == codigo:
                return material
        return None
    
    def prestar_libro(self):
        """Gestiona el préstamo de un libro"""
        if not self.__materiales:
            print("No hay materiales registrados en la biblioteca")
            return False
        
        print("\n═══ PRÉSTAMO DE MATERIAL ═══")
        codigo = input("Ingrese el código del material a prestar: ").strip().upper()
        
        material = self.buscar_material(codigo)
        if not material:
            print("Material no encontrado")
            return False
        
        if material.prestado:
            print("Este material ya está prestado")
            return False
        
        if material.prestar():
            print("Material prestado exitosamente!")
            print(material.mostrar_informacion())
            return True
        else:
            print("Error al prestar el material")
            return False
    
    def devolver_libro(self):
        """Gestiona la devolución de un libro"""
        if not self.__materiales:
            print("No hay materiales registrados en la biblioteca")
            return False
        
        print("\n═══ DEVOLUCIÓN DE MATERIAL ═══")
        codigo = input("Ingrese el código del material a devolver: ").strip().upper()
        
        material = self.buscar_material(codigo)
        if not material:
            print("Material no encontrado")
            return False
        
        if not material.prestado:
            print("Este material no está prestado")
            return False
        
        if material.devolver():
            print("Material devuelto exitosamente!")
            print(material.mostrar_informacion())
            return True
        else:
            print("Error al devolver el material")
            return False
    
    def ver_informacion_material(self):
        """Muestra información de un material específico"""
        if not self.__materiales:
            print("No hay materiales registrados en la biblioteca")
            return False
        
        print("\n═══ CONSULTAR INFORMACIÓN ═══")
        codigo = input("Ingrese el código del material a consultar: ").strip().upper()
        
        material = self.buscar_material(codigo)
        if not material:
            print("Material no encontrado")
            return False
        
        print(material.mostrar_informacion())
        return True
    
    def listar_todos_los_materiales(self):
        """Lista todos los materiales registrados"""
        if not self.__materiales:
            print("No hay materiales registrados en la biblioteca")
            return
        
        print(f"\n═══ LISTA DE MATERIALES ({len(self.__materiales)}) ═══")
        for i, material in enumerate(self.__materiales, 1):
            tipo = "FÍSICO" if isinstance(material, LibroFisico) else "DIGITAL"
            estado = "PRESTADO" if material.prestado else "DISPONIBLE"
            print(f"{i:2d}. {tipo} | {material.codigo} | {material.titulo} | {estado}")

    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "="*60)
        print("     SISTEMA DE BIBLIOTECA UNIVERSITARIA")
        print("="*60)
        print("1. Registrar Libro Físico")
        print("2. Registrar Libro Digital")
        print("3. Prestar Material")
        print("4. Devolver Material")
        print("5. Ver Información de Material")
        print("6. Listar Todos los Materiales")
        print("7. Salir del Sistema")
        print("="*60)
    
    def ejecutar_sistema(self):
        """Método principal que ejecuta el sistema de biblioteca"""
        print("¡Bienvenido al Sistema de Biblioteca Universitaria!")
        print(" Gestiona tus materiales bibliográficos de forma sencilla")
        
        while True:
            try:
                self.mostrar_menu_principal()
                opcion = input("Seleccione una opción (1-7): ").strip()
                
                if opcion == "1":
                    self.registrar_libro_fisico()
                elif opcion == "2":
                    self.registrar_libro_digital()
                elif opcion == "3":
                    self.prestar_libro()
                elif opcion == "4":
                    self.devolver_libro()
                elif opcion == "5":
                    self.ver_informacion_material()
                elif opcion == "6":
                    self.listar_todos_los_materiales()
                elif opcion == "7":
                    print("\n¡Gracias por usar el Sistema de Biblioteca!")
                    print("¡Hasta la próxima!")
                    break
                else:
                    print("Opción inválida. Por favor seleccione una opción del 1 al 7")
                
                input("\n⏸  Presione Enter para continuar...")
                
            except KeyboardInterrupt:
                print("\n\n Sistema interrumpido por el usuario. ¡Hasta luego!")
                break
            except Exception as e:
                print(f"Error inesperado: {str(e)}")
                print(" Reiniciando menú...")