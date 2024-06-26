from pathlib import Path


path = Path("hola-mundo/mi-archivo.py")

path.is_file() 
path.is_dir()
path.exists()


print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)


p = path.with_name("chanchito.py") # cambiar el nombre del archivo

print(p)


p = path.with_suffix(".js")

print(p)