import math


def simpsons_rule(f, a, b, n):
    # Calculate step size
    h = (b - a) / n

    # Initialize sum variables
    sum1 = 0
    sum2 = 0

    # Iterate through each interval
    for i in range(1, n):
        x = a + i * h

        # Calculate f(x) for odd and even terms
        if i % 2 == 0:
            sum2 += f(x)
        else:
            sum1 += f(x)

    # Calculate integral using Simpson's rule formula
    integral = (h / 3) * (f(a) + 4 * sum1 + 2 * sum2 + f(b))
    return integral

# # Example usage
# def f(x):
#     return 1/(1+x)  # Define the function f(x)

# a = 0  # Lower limit of integration
# b = 1  # Upper limit of integration
# n = 5  # Number of intervals

special_dict = {'sin': 'math.sin', 'cos': 'math.cos',
                'e': 'math.e', 'tan': 'math.tan',
                'log': 'math.log10', 'ln': 'math.log'}

print('Valid operators: + - * / ^')
expr = input(u'f(x) = ')
expr = expr.replace('^', '**')
for org, tar in special_dict.items():
    expr = expr.replace(org, tar)

a = float(input('a (lower bound) = '))
b = float(input('b (upper bound) = '))
n = int(input('n (number of intervals) = '))

def f(x):
    return eval(expr)

result = simpsons_rule(f, a, b, n)
print("Approximated integral:", result)
