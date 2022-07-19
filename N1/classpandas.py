import pandas as pd
class Classpanda:
    books =[]
    def new_csv(self,data,cont):
            df = pd.DataFrame(data)
            name = "dataframe" + str(cont) + ".csv"
            self.books.append(name)
            df.to_csv(r"" + name + "", index=False, header=True)
            return self.books
