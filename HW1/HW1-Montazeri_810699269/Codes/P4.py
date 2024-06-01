import sympy as sp
from numpy import *

u, v = [], []
for i in range(3):
    u.append([sp.Symbol(f'u{i}')])
    v.append([sp.Symbol(f'v{i}')])
print('Vector U:', u)
print('Vector V:', v)

u = array(u)
v = array(v)

lhs = eye(3) + u*v.T
lhs = sp.Matrix(lhs)
LHS = lhs.det()
RHS = 1 + dot(u.T, v)
print('Left Hand Side of the equation:\t', LHS)
print('Right Hand Side of the equation:\t', RHS)
print('The difference of LHS and RHS of the equation:\t', LHS - RHS)
