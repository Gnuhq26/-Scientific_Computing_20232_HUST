# Cực tiểu hoá không ràng buộc Newton
# Những chỗ comment <<<----------------- thì cần thay trực tiếp số liệu vào

import numpy as np

def newton_method(f, gf, hf, x0, tol=1e-6, max_iter=100):
    '''
    Thay f, gf (gradient của f), hf (hessian (hay đạo hàm bậc 2) của f ở phía dưới)
    tol: điều kiện dừng
    x0: giá trị điểm khởi tạo
    '''
    x = np.array(x0)
    converged = False

    for i in range(max_iter):
        grad = gf(x)
        hess = hf(x)

        if not np.all(np.linalg.eigvals(hess) > 0):
            print("Warning: Hessian phải xác định dương")

        d = np.linalg.solve(hess, -grad)
        x_new = x + d

        if np.linalg.norm(x_new - x) < tol:
            converged = True
            break

        x = x_new

    fval = f(x)

    return x, fval, converged


# Thay các hàm vào đây
# f(x)
def f(x):
    return x[0]**2 + x[1]**2 + 1 # <<<-----------------


# Đạo hàm cấp 1
def gf(x):
    return np.array([2*x[0], 2*x[1]]) # <<<-----------------


# Đạo hàm cấp 2
def hf(x):
    return np.array([[2, 0], [0, 2]]) # <<<-----------------

# Giá trị khởi tạo
x0 = [1, 1] # <<<-----------------

x, fval, converged = newton_method(f, gf, hf, x0)


print("Điểm cực tiểu:", x)
print("Giá trị cực tiểu:", fval)
print("Có hội tụ" if converged else "Không hội tụ")