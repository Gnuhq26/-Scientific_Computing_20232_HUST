# Tính sai số

from scipy.optimize import minimize_scalar

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

def abs_df(x, h=1e-5):
    return abs((f(x + h) - f(x - h)) / (2 * h))

a = float(input('a = '))
c = float(input('c = '))
x_chosen = float(input('x* = '))

x_min = minimize_scalar(abs_df, bounds=(a, c), method='bounded').x
abs_df_min = abs_df(x_min)
error = abs(f(x_chosen)) / abs_df_min
print(f'Error: {error}')