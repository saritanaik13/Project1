import numpy as np
from new import Univariate

salary = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]

bs = Univariate()
b = bs.center_spread(salary)
print(b)