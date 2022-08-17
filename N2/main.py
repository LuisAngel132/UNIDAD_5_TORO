import time
import pandas as pd
from classelenium import Selenium
from objPlantilla import ObjElement
from objPlantilla import ObjPlantilla

df = pd.read_csv(r'D:\UTT TIDSM\9no ING\AdministracionBD\Selenium\UNIDAD_5_TORO\N2\Plantilla.csv')
sl = Selenium()
path_file = r'D:\UTT TIDSM\9no ING\AdministracionBD\Selenium\UNIDAD_5_TORO\N2\Plantilla.json'

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





# drive = sl.navegador(df['Navegador'][0])
# cont = 0
# all=df['Path_Formulario_Input'].count()
# sl.ventana(drive, df['Url'][0])
# while(all>cont):
#     sl.write_Input(drive,df['Path_Formulario_Input'][cont],df['Valor_Input'][cont])
#     cont +=1
# all=df['Path_Formulario_Select'].count()
# cont = 0
# while(all>cont):
#     sl.write_Select(drive,df['Path_Formulario_Select'][cont],df['Valor_Select'][cont])
#     cont +=1
# all=df['Path_Formulario_Checkbox'].count()
# cont = 0
# while(all>cont):
#     sl.write_Checkbox(drive,df['Path_Formulario_Checkbox'][cont])
#     cont +=1

# time.sleep(3)
# sl.save(drive,df["Guardar_Botton"][0])
# drive.close()