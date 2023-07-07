"""
    Ejemplo de uso de hilos (threads)
"""

import requests
import time
import csv
import threading
import subprocess

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for lineaObtenida in lineas:
            print("Línea obtenida del archivo data:", lineaObtenida)
            valoresAux = lineaObtenida[0].split('|')
            lista.append((valoresAux[0], valoresAux[1]))
    return lista

def worker(numero, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url))
    resultado = requests.get(url)
    print("Se va a crear el archivo %s.txt" % numero)
    resultado.encoding = 'utf-8'
    with open("salida/%s.txt" % numero, "w", encoding='utf-8') as archivo:
        archivo.writelines(resultado.text)
    print("Archivo creado %s.txt" % numero)
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...', target=worker, args=(numero, url))
    hilo1.start()
