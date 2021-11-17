import pandas
import numpy
from pandas import ExcelWriter


class GenerateExcel:
    def __init__(self, columns=None, rows=None, path="subnetting.xlsx"):
        self._columns = columns
        self._rows = rows    
        self._path = path

        self.writer = ExcelWriter(self._path)

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        self._columns = value

    @property
    def rows(self):
        return self._rows
    
    @rows.setter
    def rows(self, value):
        self._rows=value

    def generate(self, name):
        data = pandas.DataFrame(numpy.array(self._rows), columns=self._columns)
        data.to_excel(self.writer, name, index=False)

    def save_book(self):
        self.writer.save()

