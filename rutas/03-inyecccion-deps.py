
from pathlib  import Path

path = Path()

dependencia = {
    "db": "base de datos",
    "api": "Esto es la api",
    "graphql": "Esto es un graphql"
}


paths = [p for p in path.iterdir() if p.is_dir()]

def load(p):
    paquetes = __import__(str(p).replace("/", "."))
    try:
        paquetes.init(**dependencia)
    except:
        print("El paquete no tiene funcion init()")

list(map(load, paths))
