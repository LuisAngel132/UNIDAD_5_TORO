from selenium import webdriver
from selenium.webdriver.common.by import By
class Selenium:
    driver = ""
    drive = ""
    data = {}
    def navegador(self,drive):
        self.drive = drive
        if self.drive =="chrome":
            self.driver = webdriver.Chrome(executable_path="C:\DRIVER\chromedriver_win32\chromedriver.exe")
        if self.drive =="edge":
            self.driver = webdriver.Firefox(executable_path="C:\DRIVER\geckodriver-v0.31.0-win64\geckodriver.exe")
        if self.drive =="firefox":
            self.driver = webdriver.Edge(executable_path="C:\DRIVER\edgedriver_arm64\msedgedriver.exe")
        return self.driver
    def ventana(self,drive,url):
        drive.get(""+str(url)+"")
    def dimension_tabla(self,tr,th,drive):
        title = th.replace('"', "'")
        rowscolumns = tr.replace('"', "'")
        title2 = drive.find_elements(By.XPATH, ""+str(title)+"")
        rowscolumns2 = drive.find_elements(By.XPATH, ""+str(rowscolumns)+"")
        for t in range(len(title2)):
            # TODO() INSERTANDO LOS TITULOS DE CABECERA
            if len(title2[t].text) > 1:
                self.data[title2[t].text] = []
        for col in range(1, len(rowscolumns2) + 1):
            # TODO() LOS TITULOS ASIGNANDO ELEMENTO POR CAMPO EN SI 34 FILAS POR 10 CAMPOS
            for d in range(1, len(title2)):
                text = drive.find_element(By.XPATH,str(rowscolumns)+"[" + str(col) + "]/td[" + str(d) + "]").text
                if len(text) > 1:
                    self.data[title2[d - 1].text].append(text)
        return self.data
