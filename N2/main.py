import pandas as pd
from classelenium import Selenium
df = pd.read_csv('Plantilla.csv')
sl = Selenium()
drive = sl.navegador(df['Navegador'][0])
cont = 0
all=df['Path_Formulario_Input'].count()
sl.ventana(drive, df['Url'][0])
while(all>cont):
    sl.write_Input(drive,df['Path_Formulario_Input'][cont],df['Valor_Input'][cont])
    cont +=1
all=df['Path_Formulario_Select'].count()
cont = 0
while(all>cont):
    sl.write_Select(drive,df['Path_Formulario_Select'][cont],df['Valor_Select'][cont])
    cont +=1
all=df['Path_Formulario_Checkbox'].count()
cont = 0
while(all>cont):
    sl.write_Checkbox(drive,df['Path_Formulario_Checkbox'][cont])
    cont +=1
sl.save(drive,df["Guardar_Botton"][0])
drive.close()