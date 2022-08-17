import time
import pandas as pd
from classelenium import Selenium
from objPlantilla import ObjElement
from objPlantilla import ObjPlantilla

sl = Selenium()
path_file = r'Plantilla.json'

objList = ObjPlantilla().GetObjects(path_file)
for obj in objList:
    print(obj.navegator)
    drive = sl.navegador(obj.navegator)
    sl.ventana(drive,obj.URL)
    time.sleep(5)
    for element in obj.elements:
        print("\nelemento: "+element.selector+"\naccion: "+element.action+"\n")
        sl.FindByAndAction(element.type, element.selector, element.action, element.value)
    drive.close()
    print("FIN.")
    pass