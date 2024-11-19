from main import registrar_entradas, contar_dinero, autos_por_dia
import random

def test_contar_dinero():
    sumas = []
    for i in range(5):
        suma = random.randint(1000, 10000)
        sumas.append(suma)
    print(sumas)
    assert contar_dinero(sumas) == sum(sumas)
