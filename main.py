import os
from src.services.prueba_equipo import ejecutar_prueba

def limpiar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    limpiar_terminal()
    ejecutar_prueba()
