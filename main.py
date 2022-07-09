from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
from pandas import json_normalize
import numpy as np
import matplotlib.pyplot as plt

#TODO() DICCIONARIO DATA
data ={}
#TODO()CONEXION A CHROME
driver = webdriver.Chrome(executable_path="C:\DRIVER\chromedriver_win32\chromedriver.exe")
#TODO()CONEXION A FIREXOX NO FUNCIONA
#driver = webdriver.Firefox(executable_path="C:\DRIVER\geckodriver-v0.31.0-win64\geckodriver.exe")
#TODO()CONEXION A EDGE NO FUNCIONA
#driver = webdriver.Edge(executable_path="C:\DRIVER\edgedriver_arm64\msedgedriver.exe")
# TODO() PAGINA USADAS
driver.get("https://mx.investing.com/equities/mexico")
#driver.get("https://mx.investing.com/equities/united-states")
#driver.get("https://mx.investing.com/equities/united-kingdom")
#driver.get("https://mx.investing.com/equities/germany")
#TODO() ESPERA DEL PROGRAMA
time.sleep(30)
#TODO EXTRACCION DE CABECERAS A LA TABLA
title = driver.find_elements(By.XPATH, "//*[@id='cross_rate_markets_stocks_1']/thead/tr/th")
#TODO()EXTRACCION DE LA ETIQUETA TR DE LA TABLA
rowscolumns = driver.find_elements(By.XPATH, "//*[@id='cross_rate_markets_stocks_1']/tbody/tr")
#TODO() ESPERA DEL PROGRAMA
time.sleep(20)
#TODO() POR CABECERA (10)
for t in range(len(title)):
    # TODO() INSERTANDO LOS TITULOS DE CABECERA
    data[title[t].text] = []
 #TODO() LOS TR QUE SON 34 IGUAL 34 FILAS
for col in range(1,len(rowscolumns)):
    # TODO() LOS TITULOS ASIGNANDO ELEMENTO POR CAMPO EN SI 34 FILAS POR 10 CAMPOS
    for d in range(1,len(title)):
         data[title[d-1].text].append(driver.find_element(By.XPATH, "//*[@id='cross_rate_markets_stocks_1']/tbody/tr["+str(col)+"]/td["+str(d)+"]").text)
    # TODO()ERROR DESCONOCIDO SE PASA DICIONARIO PARA ASIGANR UN DATAFRAME
    #df = pd.DataFrame(data)
#TODO() NO ES POSIBLE HASTA ARREGLAR EL ERROR CONVERSION A CSV
#df.to_csv (r'C:\Users\export_dataframe.csv', index = False, header=True)#
#TODO() CSV ABRIRLO PARA LA GRAFICA
#df = pd.read_csv("../data/medals.csv", index_col="Country")
#TODO 1O PRIMEROS ELEMENTOS CON MAYOR ACCIONES
#datatop =df[:10].copy()
#TODO() CREACION DE LA GRAFICA ERROR EN ACOMODACION DE VALORES DE MAYOR A MENOR
#for d in data:
 #   print(d.title())
plt.bar(data['Nombre'], data['Máximo'])
plt.ylabel('Máximo')
plt.xlabel('Nombre')
plt.title('Máximo en valores de acciones')
plt.show()
#TODO CERRAR NAVEGADOR
driver.close()
#TODO COMENTACIONES POR SI SON REQUERIDAS COMO EJEMPLOS
#columnas = driver.find_element(By.XPATH,"//*[@id='cross_rate_markets_stocks_1']/tbody/tr[]").text
#print(columnas,end='')
#//*[@id="cross_rate_markets_stocks_1"]


