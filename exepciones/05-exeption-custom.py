
class Mierror(Exception):
    "Esta clase para representar un eror"
    
    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo =  codigo
    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"
    
def divsion(n=0):

    if n == 0:
        raise Mierror("No se puede divir por cero",  805)
    return 5/0


try:
    divsion()
except Mierror as e:
    print(e)
   
    

