# Phương pháp lát cắt vàng

special_dict = {'sin': 'math.sin', 'cos': 'math.cos',
                'e': 'math.e', 'tan': 'math.tan',
                'log': 'math.log10', 'ln': 'math.log'}

print('Valid operators: + - * / ^')
expression = input(u'f(x) = ')
expression = expression.replace('^', '**')
for org, tar in special_dict.items():
    expression = expression.replace(org, tar)

a = float(input('a = '))
b = float(input('b = '))
eps = float(input('epsilon = '))

def f(x):
    return eval(expression)

x1 = a + (b - a) * 0.382
x2 = a + (b - a) * 0.618
f1 = f(x1)
f2 = f(x2)
while abs(b - a) > 2 * eps:
    if f1 > f2:
        a = x1
        x1 = x2
        f1 = f2
        x2 = a + (b - a) * 0.618
        f2 = f(x2)
    else:
        b = x2
        x2 = x1
        f2 = f1
        x1 = a + (b - a) * 0.382
        f1 = f(x1)

print(f'Khoảng có nghiệm: [{a}, {b}]')