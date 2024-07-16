import numpy as np
from sympy import symbols, simplify

x = [float(i) for i in  input(u'Nhập x (các phần tử cách nhau bằng dấu cách): ').split()]
x = np.array(x, dtype=float)

y = [float(i) for i in input(u'Nhập y (các phần tử cách nhau bằng dấu cách): ').split()]
y = np.array(y, dtype=float)
assert len(x) == len(y), u'x và y phải cùng số phần tử'

def lagrange_interp(x, y, z):
    n = len(x)
    s = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if j != i:
                p *= (z - x[j])/(x[i] - x[j])
        s += y[i]*p
    return s

z = np.arange(1, 5, 0.1)

y_interp = [lagrange_interp(x, y, i) for i in z]

x_sym = symbols('x')
polynomial = 0
n = len(x)
for i in range(n):
    p = 1
    for j in range(n):
        if j != i:
            p *= (x_sym - x[j])/(x[i] - x[j])
    polynomial += y[i]*p
    
polynomial = simplify(polynomial)
print('f(x) =', str(polynomial).replace('**', '^'))
x = float(input(u'Nội suy tại x = '))
print(f'f({x}) =', eval(str(polynomial)))