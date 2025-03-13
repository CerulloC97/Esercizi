import os
import sys
from collections import defaultdict

def get_shebang(file_path):
    try:
        with open(file_path, 'rb') as f:
            first_line = f.readline().decode(errors='ignore').strip()
            if first_line.startswith("#!"):
                return first_line
    except Exception:
        pass
    return None

def count_executables(directory):
    interpreter_count = defaultdict(int)
    
    if not os.path.isdir(directory):
        print(f"Errore: '{directory}' non è una directory valida.")
        sys.exit(1)
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.access(file_path, os.X_OK) and os.path.isfile(file_path):
                shebang = get_shebang(file_path)
                if shebang:
                    interpreter_count[shebang] += 1
    
    for shebang, count in sorted(interpreter_count.items(), key=lambda x: -x[1]):
        print(f"{count} {shebang}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <directory>")
        sys.exit(1)
    
    count_executables(sys.argv[1])