import numpy as np


def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton's method for finding roots of a non-linear equation f(x) = 0
    
    Parameters:
        f (function): The non-linear function to solve
        df (function): The derivative of the non-linear function f(x)
        x0 (float): The initial guess for the root
        tol (float): The tolerance for the root
        max_iter (int): The maximum number of iterations
    
    Returns:
        x (float): The root of the non-linear equation
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            break
        x -= fx / dfx
        print(f'step: {i} - x: {x}')
    return x

# Example usage
f = lambda x: x**2 - 4 # <<<------------------------- Thay hàm f vào đây
df = lambda x: 2 * x # <<<------------------------- Thay đạo hàm của f vào đây
x0 = 1.5


root = newton_method(f, df, x0)
print("Root of x^2 - 2 = 0: ", root)