#respondendo ao exercício 2

import random

def coletar_temperatura_sensor():
    temperatura = random.uniform(5, 35) # entre 5 e 35
    return temperatura
 
def pritar_temperatura(temp):
    txt = f'A temperatura é {round(temp,2)} ela está '
    if temp < 18:
        print(txt+'baixa')
    elif  18 >= temp <= 26:
        print(txt+'normal')
    else:
        print(txt+'alta')

def pipeline_sensor_iot():
    i = 0
    while i < 10:
        temp = coletar_temperatura_sensor()
        pritar_temperatura(temp)
        i += 1

pipeline_sensor_iot()