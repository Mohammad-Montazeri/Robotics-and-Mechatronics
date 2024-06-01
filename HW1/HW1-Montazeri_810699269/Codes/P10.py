from numpy import *
from numpy import round

print('Part 1:')

a = array([
    [0],
    [10],
    [0]
])

b = array([
    [7],
    [0],
    [0]
])

c = array([
    [-7],
    [0],
    [0]
])

d = array([
    [0],
    [8],
    [2]
])

ap = 1/4 * array(
    [[390],
     [4030 - 5*sqrt(3)],
     [1615 + 10*sqrt(3)]]
)

bp = 1/8 * array(
    [[800 + 14*sqrt(3)],
     [8021 + 14*sqrt(3)],
     [3214-21*sqrt(3)]]
)

cp = 1/8 * array(
    [[800 - 14*sqrt(3)],
     [7979 - 14*sqrt(3)],
     [3186 + 21*sqrt(3)]]
)

e1 = (b - c)/linalg.norm(b - c)
e2 = (a - (b+c)/2) / linalg.norm(a - (b+c)/2)
e3 = cross(e1.flatten(), e2.flatten()).reshape((3, 1))
print(f'e1 = {e1.flatten()}, e2 = {e2.flatten()}, e3 = {e3.flatten()}')

e1p = (bp - cp)/linalg.norm(bp - cp)
e2p = (ap - (bp+cp)/2) / linalg.norm(ap - (bp+cp)/2)
e3p = cross(e1p.flatten(), e2p.flatten()).reshape((3, 1))
print(
    f' e1\' = {e1p.flatten()}, \n e2\' = {e2p.flatten()}, \n e3\' = {e3p.flatten()}')


def D(x, y):
    # abirritate dot product of 2 vectors
    return dot(x.T, y)[0, 0]


Q = array([
    [D(e1, e1p), D(e1, e2p), D(e1, e3p)],
    [D(e2, e1p), D(e2, e2p), D(e2, e3p)],
    [D(e3, e1p), D(e3, e2p), D(e3, e3p)]
])


print(f'\nRoation Matrix: \n{Q}')
print(f'\n|Q| = {linalg.det(Q)} = 1')
print(f'Q^T * Q = \n{round(Q.T @ Q, decimals=5)} = I\n')

print(f'e1\' - Q*e1 = {(e1p - Q@e1).flatten()}')
print(f'e2\' - Q*e2 = {(e2p - Q@e2).flatten()}')
print(f'e3\' - Q*e3 = {(e3p - Q@e3).flatten()}')

print('\nPart 4 (Bonus):')
e4 = (d - (b+c)/2) / linalg.norm(d - (b+c)/2)
e4p = Q@e4
print(f'e4 = {e4.flatten()}')
print(f'e4\' = Q * e4 = \n{e4p}')

dp = e4p * linalg.norm(d - (b+c)/2) + ((bp+cp)/2)

e4pp = (dp - (bp+cp)/2) / linalg.norm(dp - (bp+cp)/2)

print(f'\nd\' = \n{dp}')
print(
    f'\nThe e4\' vector obtained using new d\' = \n{e4pp} = previously achieved e4\' vector.')
