from src.ej05_def2 import calcula_precio

def test_calcula_precio():
    
    assert calcula_precio (5,50) == "El precio final del artículo con IVA 50.00 es 7.50."
    assert calcula_precio(5,201) == "El precio final del artículo con IVA 21.00 es 6.05."