import time
import pandas as pd
from classelenium import ClassSelenium
from classpandas import Classpanda
from classmatplotlib import ClassMatplotlib
df = pd.read_csv(r'D:\UTT TIDSM\9no ING\AdministracionBD\Selenium\UNIDAD_5_TORO\N1\Plantilla.csv')
mt = ClassMatplotlib()
pa = Classpanda()
sl = ClassSelenium()
drive = sl.navegador(df['Navegador'][0])
all = df['Path_Tr'].count()
# all = df['Urls'].count()
cont = 0
books =[]
btn= ""
sl.ventana(drive,df['Urls'][0])
while(all > cont ):
    btn = str(df['Path_Btn'][cont])

    if btn != "": 
        print("btn: "+btn)
        sl.Click(btn,drive)
    # print("SE ESTA CREANDO EL DATA FRAME...")
    # data = sl.dimension_tabla(df['Path_Tr'][cont],df['Path_Th'][cont],drive)
    # print(cont)
    # books = pa.new_csv(data,cont)
    # time.sleep(25)
    # print("LISTO \n")
    cont += 1
drive.close()
print("GRAFICANDO...")
mt.set_graph(books,df)
print("FIN.")

