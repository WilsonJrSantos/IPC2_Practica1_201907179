from sistema_biblioteca import SistemaBiblioteca

def main():
    """Función principal que inicia el sistema"""
    try:
        sistema = SistemaBiblioteca()
        sistema.ejecutar_sistema()
    except Exception as e:
        print(f"Error crítico del sistema: {str(e)}")
        print("Por favor, contacte al administrador del sistema")

if __name__ == "__main__":
    main()