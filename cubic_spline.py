import numpy as np
from scipy.interpolate import CubicSpline

x = [float(i) for i in  input(u'Nhập x (các phần tử cách nhau bằng dấu cách): ').split()]
x = np.array(x, dtype=float)

y = [float(i) for i in input(u'Nhập y (các phần tử cách nhau bằng dấu cách): ').split()]
y = np.array(y, dtype=float)

print('Ma trận hệ số (mỗi hàng tương ứng với hệ số ax^3 + bx^2 + cx + d của mỗi khoảng):')
f = CubicSpline(x, y)

print(f.c.T)