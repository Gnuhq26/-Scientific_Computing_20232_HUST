# Cực tiểu một biến

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

k = 0
while abs(b - a) >= 2 * eps:
    k += 1
    x1 = a + (b - a) / 2 - eps / 2
    x2 = a + (b - a) / 2 + eps / 2
    f1 = f(x1)
    f2 = f(x2)

    if f1 < f2:
        b = x2
    elif f1 > f2:
        a = x1
    else:
        a = x1
        b = x2

print(f'Số bước lặp: {k}')
print(f'Độ dài đoạn (b - a): {b - a}')
print(f'x = {x1}')
print(f'fmin = {f(x1)}')
