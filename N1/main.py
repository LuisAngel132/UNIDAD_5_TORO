import time
import pandas as pd
from classelenium import Selenium
from classpandas import Classpanda
from classmatplotlib import Matplotlib
df = pd.read_csv('Plantilla.csv')
mt = Matplotlib()
pa = Classpanda()
sl = Selenium()
drive = sl.navegador(df['Navegador'][0])
all = df['Urls'].count()
cont = 0
books =[]
while(all > cont ):
    sl.ventana(drive,df['Urls'][cont])
    data = sl.dimension_tabla(df['Path_Tr'][cont],df['Path_Th'][cont],drive)
    books = pa.new_csv(data,cont)
    time.sleep(25)
    cont += 1
drive.close()
mt.set_graph(books,df)

