# Phương pháp dây cung

import math

special_dict = {'sin': 'math.sin', 'cos': 'math.cos',
                'e': 'math.e', 'tan': 'math.tan',
                'log': 'math.log10', 'ln': 'math.log'}

print('Valid operators: + - * / ^')
expression = input(u'f(x) = ')
expression = expression.replace('^', '**')
for org, tar in special_dict.items():
    expression = expression.replace(org, tar)

a = float(input('a = '))
c = float(input('c = '))
eps = float(input('epsilon = '))

def f(x):
    return eval(expression)

i = 1
bsign = False
while True:
    b = a - (c - a) / (f(c) - f(a)) * f(a)
    fb = f(b)
    print(f'iter {i}: a = {a}; b (root) = {b}; c = {c}')
    i += 1
    print(f'\tf(b) = {fb};\t\terror = {c - a}\n')
    if fb == 0:
        break
    if f(a) * fb < 0:
        c = b
    else:
        a = b
    if bsign: break
    if c - a <= eps:
        bsign = True
    