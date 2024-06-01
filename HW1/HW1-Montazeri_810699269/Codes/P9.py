from numpy import *

R = array([
    [1/sqrt(2), 0, 1/sqrt(2)],
    [-1/2, 1/sqrt(2), 1/2],
    [-1/2, -1/sqrt(2), 1/2]
])

# part 1)
print('part 1)')
print(f'|R| = {linalg.det(R)} ≈ 1')
print(f'R^T R = \n{R.T@R} ≈ I')

# part 2)
print('\npart 2)')
vect_R = 1/2 * array([
    [R[2][1]-R[1][2]],
    [R[0][2]-R[2][0]],
    [R[1][0]-R[0][1]]
])

phi = arccos((trace(R) - 1)/2)
e = vect_R / sin(phi)

print(f'Rotation angle = phi = {rad2deg(phi)} degrees')
print(f'Rotation axis vector = e = \n{e}')
print(f'Magnitude of e = {linalg.norm(e)} ≈ 1')

# part 3)
print('\npart 3)')
r0 = cos(phi/2)
r = sin(phi/2)*e
print('Euler-Rodrigues parameters of rotation:')
print(f'r0 = {r0}')
print(f'r = \n{r}')