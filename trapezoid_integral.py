# Tích tích phân theo công thức hình thang

import numpy as np
import math

special_dict = {'sin': 'math.sin', 'cos': 'math.cos',
                'e': 'math.e', 'tan': 'math.tan',
                'log': 'math.log10', 'ln': 'math.log'}

print('Valid operators: + - * / ^')
expression = input(u'f(x) = ')
expression = expression.replace('^', '**')
for org, tar in special_dict.items():
    expression = expression.replace(org, tar)
    
def f(x):
    return eval(expression)

class Integral:
    def __init__(self, f):
        self.f = f
        
    def solve(self, start, end, n_steps):
        step = (end - start) / n_steps
        space = np.arange(start, end, step, dtype=float)
        return np.sum((self.f(space + step) + self.f(space)) * step / 2)
            
integral = Integral(f)

start = float(input('start: '))
end = float(input('end: '))
n_steps = float(input('NUMBER of steps (not step size): '))

print(integral.solve(start, end, n_steps))