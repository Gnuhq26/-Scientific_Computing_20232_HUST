# Nội suy spline từng khúc
import numpy as np
from scipy.interpolate import interp1d

x = [float(i) for i in  input(u'Nhập x (các phần tử cách nhau bằng dấu cách): ').split()]
x = np.array(x, dtype=float)

y = [float(i) for i in input(u'Nhập y (các phần tử cách nhau bằng dấu cách): ').split()]
y = np.array(y, dtype=float)

f = interp1d(x, y, kind='linear')


print(f)