from asyncio.windows_events import NULL

import json
import time
import pandas as pd
from objPlantilla import ObjElement
from objPlantilla import ObjPlantilla
from classelenium import ClassSelenium
from classpandas import Classpanda
from classmatplotlib import ClassMatplotlib
# df = pd.read_csv(r'D:\UTT TIDSM\9no ING\AdministracionBD\Selenium\UNIDAD_5_TORO\N1\Plantilla.csv')
path_file = r'D:\UTT TIDSM\9no ING\AdministracionBD\Selenium\UNIDAD_5_TORO\N1\Plantilla.json'
mt = ClassMatplotlib()
pa = Classpanda()
sl = ClassSelenium()

objList = ObjPlantilla().GetObjects(path_file)
print(objList[0])
books =[]
count = 0
for obj in objList:
    print(obj.navegator)
    drive = sl.navegador(obj.navegator)
    sl.ventana(drive,obj.URL)
    time.sleep(10)
    for element in obj.elements:
        if element.action != "read_table":
            sl.FindByAndAction(element.type, element.selector, element.action, element.value)
            continue
        # sl.ReadTable(element.type_th,element.selector_th, element.tb,element.selector_tb)
        print("SE ESTA CREANDO EL DATA FRAME...")
        df = sl.ReadTable(element.type_th,element.selector_th, element.type_tb, element.selector_tb)
        print(count)
        books = pa.new_csv(df,count)
        count += 1
        # time.sleep(25)
        print("LISTO \n")
    drive.close()
    print("GRAFICANDO...")
    mt.set_graph(books,obj.readTable.chart)
    print("FIN.")
    pass