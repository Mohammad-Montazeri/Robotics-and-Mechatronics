from sympy import *

t1, t2, t3, t4, t5, t6 = symbols('t1, t2, t3, t4, t5, t6')

a = [None for i in range(6)]
Q = [None for i in range(7)]

Q[0] = Matrix([
    [cos(t1), 0, sin(t1)],
    [sin(t1), 0, -cos(t1)],
    [0, 1, 0]
])

Q[1] = Matrix([
    [cos(t2), sin(t2), 0],
    [sin(t2), -cos(t2), 0],
    [0, 0, -1]
])

Q[2] = Matrix([
    [cos(t3), 0, sin(t3)],
    [sin(t3), 0, -cos(t3)],
    [0, 1, 0]
])

Q[3] = Matrix([
    [cos(t4), 0, sin(t4)],
    [sin(t4), 0, -cos(t4)],
    [0, 1, 0]
])

Q[4] = Matrix([
    [cos(t5), 0, sin(t5)],
    [sin(t5), 0, -cos(t5)],
    [0, 1, 0]
])

Q[5] = Matrix([
    [cos(t6), -sin(t6), 0],
    [sin(t6), cos(t6), 0],
    [0, 0, 1]
])

Q[6] = eye(3, 3)

a[0] = 150*Matrix([
    [cos(t1)],
    [sin(t1)],
    [3]
])

a[1] = 570*Matrix([
    [cos(t2)],
    [sin(t2)],
    [0]
])

a[2] = 200*Matrix([
    [cos(t3)],
    [sin(t3)],
    [0]
])

a[3] = 640*Matrix([
    [0],
    [0],
    [1]
])

a[4] = 30*Matrix([
    [cos(t5)],
    [sin(t5)],
    [0]
])

a[5] = 200*Matrix([
    [0],
    [0],
    [1]
])

P = zeros(3, 1)
ans = eye(3, 3)
for i in range(6):
    ans = ans@Q[i-1]
    P += ans@a[i]
    P = simplify(P)

pprint(P)
print()
print(matrix2numpy(P))
print()
