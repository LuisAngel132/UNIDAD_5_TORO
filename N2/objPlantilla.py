from asyncio.windows_events import NULL
import json


class ObjPlantilla:
   def __init__(self):
      self.navegator = NULL
      self.URL = NULL
      self.readTable = ObjReadTable()
      self.elements = []
      # self.elements.remove()
      pass
   
   def GetObjects(self,path_file):
      ObjectList = []
      # ObjectList.remove()
      with open(path_file, 'r', encoding='utf-8') as dataJson:
         dataObject = json.load(dataJson)
         for data in dataObject:
            obj = ObjPlantilla()
            obj.navegator = str(data['navegator'])
            obj.URL = str(data['URL'])
            obj.readTable.read = bool(data['readTable']["read"])
            obj.readTable.chart.x = str(data['readTable']["chart"]["x"])
            obj.readTable.chart.y = str(data['readTable']["chart"]["y"])
            obj.readTable.chart.quantity = int(data['readTable']["chart"]["quantity"])
            for element in data['elements']:
               if element['action'] == 'read_table':
                  objTable = ObjTable()
                  objTable.action = str(element['action'])
                  objTable.value = str(element['value'])
                  objTable.type_th = str(element['type_th'])
                  objTable.selector_th = str(element['selector_th'])
                  objTable.type_tb = str(element['type_tb'])
                  objTable.selector_tb = str(element['selector_tb'])
                  obj.elements.append(objTable)
                  continue
               objElement = ObjElement()
               objElement.action = str(element['action'])
               objElement.value = str(element['value'])
               objElement.type = str(element['type'])
               objElement.selector =str(element['selector'])
               obj.elements.append(objElement)
            ObjectList.append(obj)
         return ObjectList
   pass

class ObjReadTable:
   def __init__(self):
      self.read = NULL
      self.chart = ObjChart()
      pass
   pass
class ObjChart:
   def __init__(self):
      self.x = NULL
      self.y = NULL
      self.quantity = NULL
      pass
   pass
class ObjElement():
   def __init__(self):
      self.action = NULL
      self.value = NULL
      self.type = NULL
      self.selector = NULL
      pass
   pass
class ObjTable():
   def __init__(self):
      self.action = NULL
      self.value = NULL
      self.type_th = NULL
      self.selector_th = NULL
      self.type_tb = NULL
      self.selector_tb = NULL
      pass
   pass