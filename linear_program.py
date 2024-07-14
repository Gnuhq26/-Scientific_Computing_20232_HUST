'''
Bài toán tối ưu được đưa về dạng chuẩn tắc: x = argmin_x f(x)
Các điều kiện ràng buộc được chuyển về dạng: Ax <= b
    VD: Điều kiện Gx = h thì đưa về -Gx <= -h và Gx <= h
c là bộ trọng số của f(x)
'''

from cvxopt import matrix, solvers


c = matrix([-5., -3.])

A = matrix([
    [1., 2., 1., -1., 0.],
    [1., 1., 4., 0., -1.]
])

b = matrix([10., 16., 32., 0., 0.])

solvers.options['show_progress'] = False
sol = solvers.lp(c, A, b)

print('Optimal solution:')
print(sol['x'])
