# Hồi quy tuyến tính 1 biến

import numpy as np
from scipy.stats import linregress

x = [float(i) for i in  input(u'Nhập x (các phần tử cách nhau bằng dấu cách): ').split()]
x = np.array(x, dtype=float)

y = [float(i) for i in input(u'Nhập y (các phần tử cách nhau bằng dấu cách): ').split()]
y = np.array(y, dtype=float)
assert len(x) == len(y), u'x và y phải cùng số phần tử'

a, b, r, p, std_err = linregress(x, y)

print('y = ax + b')
print(f'a: {a}')
print(f'b: {b}')