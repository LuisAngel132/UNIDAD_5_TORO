import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class Selenium:
    driver = ""
    drive = ""
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
    def write_Input(self,drive,i,keys):
            input = i.replace('"', "'")
            element = drive.find_element(By.XPATH, "" + str(input) + "")
            element.click()
            time.sleep(.2)
            element.send_keys(keys)
    def write_Select(self,drive,i,keys):
        input = i.replace('"', "'")
        print(input,keys)
        select = Select(drive.find_element(By.XPATH, "" + str(input) + ""))
        select.select_by_visible_text(keys)
    def write_Checkbox(self,drive,i):
        input = i.replace('"', "'")
        element = drive.find_element(By.XPATH, "" + str(input) + "")
        element.click()
    def save(self,drive,i):
        input = i.replace('"', "'")
        element = drive.find_element(By.XPATH, "" + str(input) + "")
        element.submit()
