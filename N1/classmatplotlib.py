import matplotlib.pyplot as plt
import pandas as pd
class Matplotlib:
    def graph(self,graph_x_name,graph_y_name,graph,element_x,element_y):
        plt.bar(element_x, element_y)
        plt.ylabel(graph_y_name)
        plt.xlabel(graph_x_name)
        plt.title(graph)
        plt.show()
    def set_graph(self,books,df):
        cont = 0
        elementx = ""
        elementy = ""
        for i in books:
            data = pd.read_csv(i)
            number = df["Elementos_Grafica"][cont]
            dataframe=data[:number].copy()
            for d in dataframe.keys():
                if d == df["Elemento_X"][cont]:
                    elementx = d
                if d == df["Elemento_Y"][cont]:
                    elementy = d
            data1 = dataframe.sort_values(by=[elementy])
            data2 = data1[elementy]
            data4 = dataframe[elementx]
            self.graph(elementx, elementy, i, data4, data2)
            cont += 1