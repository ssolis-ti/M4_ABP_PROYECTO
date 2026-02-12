import sys
import os

# Aseguramos que el directorio raíz esté en el path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from src.main import main
    if __name__ == "__main__":
        main()
except ImportError as e:
    print(f"Error starting application: {e}")
    input("Press Enter to exit...")
