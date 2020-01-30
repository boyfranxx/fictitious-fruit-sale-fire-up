from itertools import chain
import fruit_sale_functions as fsf
import pyodbc
from plotly import offline

sum_list = fsf.find_sum_list('Clementines')
total_sum = sum(filter(None, chain.from_iterable(sum_list)))
print(sum_list)
