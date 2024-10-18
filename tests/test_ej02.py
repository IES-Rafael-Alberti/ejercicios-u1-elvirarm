
from src.construye_funciones.ej02_def import total_precio_horas

def test_comprobar_total():
    assert total_precio_horas (6,10,60) == 60
    assert total_precio_horas (0,10,0) == 0