import pandas
import numpy
from pandas import ExcelWriter
class GenerateExcel:
    def __init__(self,colums,rows,path):
        self.columns=columns
        self.rows=rows
        self.path=path
        
    def generate(self):
        data=pandas.DataFrame(numpy.array(self.rows),columns=self.columns)
        writer=ExcelWriter(self.path)
        data.to_excel(writer,"hoja de datos", index=False)
        writer.save()


if __name__ == '__main__':
    columns=['nombre','edad']
    rows=[['juan','28'],['andres','21']]
    path='/home/david/Desktop/prueba.xlsx'
    excel=GenerateExcel(columns,rows,path)
    excel.generate()
