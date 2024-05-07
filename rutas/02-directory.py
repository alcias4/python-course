from pathlib import Path


path = Path("rutas")


# path.exists()
# path.mkdir()
# path.rmdir() # vavcio
# path.rename("canchito feliz")

archivos = [p for p in path.iterdir() if not p.is_dir()]

archivos = [p for p in path.glob("01-*.py")] # buscar 
archivos = [p for p in path.glob("**/*.py")] # buscar en todo carpetas de rutas

archivos = [p for p in path.rglob("*.py")] # buscar 
print(archivos)
# for p in path.iterdir():
#     print(p)