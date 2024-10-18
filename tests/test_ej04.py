from src.ej04_def2 import grados_celsius

def test_grado_celsius():
    assert round(grados_celsius(20),2) == -6.67
    assert round(grados_celsius(2.45),2) == -16.42
    assert round(grados_celsius(-15),2) == -26.11