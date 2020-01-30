from itertools import chain
import fruit_sale_functions as fsf
from plotly import offline

sum_list = fsf.find_sum_list('Clementines')
total_sum = sum(sum_list)
print(total_sum)
