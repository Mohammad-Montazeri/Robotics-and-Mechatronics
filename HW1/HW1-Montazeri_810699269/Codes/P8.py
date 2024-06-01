from sympy import *
from fractions import Fraction
from numpy import array, eye

# defining a text style class to highlight the results
class TextStyle:
    BOLD = '\033[1;34m'
    END = '\033[0m'


# defining variables and constants to abbreviate rotation matrix terms
t, alpha = symbols('t, a')
c = cos(alpha * t/2)
s = sin(alpha * t/2)
r = (2*sqrt(3)/3) * s * c
a = Fraction(1, 3)
b = Fraction(2, 3)

# given rotation matrix
Q = Matrix([
    [c**2-a*s**2, b*s**2-r, b*s**2+r],
    [b*s**2+r, c**2-a*s**2, b*s**2-r],
    [b*s**2-r, b*s**2+r, c**2-a*s**2]
])

# part 1)
print('part 1)')
vect_Q = 1/2 * Matrix([
    [Q[2, 1]-Q[1, 2]],
    [Q[0, 2]-Q[2, 0]],
    [Q[1, 0]-Q[0, 1]]
])

phi = acos((trace(Q) - 1)/2)
e = vect_Q / sin(phi)
print(f'Rotation angle = phi = {phi.evalf(2)} radians')
print('Rotation axis vector = e = ')
print(matrix2numpy(e.evalf(2)))
# pprint(e.evalf(2))

r0 = cos(phi/2)
r = sin(phi/2)*e
print('\nEuler-Rodrigues parameters of rotation:')
print(f'r0 = {r0.evalf(2)}')
print(f'r = \n{matrix2numpy(r.evalf(2))}')
# pprint(r.evalf(2))


# part 3)
print('\npart 3)')
times = [pi/2/alpha, 2*pi/alpha, pi/alpha]


def singularity_handler(Q, theta):
    # defining parametric axis of rotation (e)
    R_axis = []
    for i in range(3):
        R_axis.append([Symbol(f'e{i}')])

    E = array(R_axis)
    lhs = E@E.T  # left-hand-side of the equation
    rhs = 1/2 * (eye(3, 3) + Q)  # right-hand-side of the equation
    eq = []  # defining the system of 3 equations and 3 unknowns
    for col in range(3):
        eq.append(lhs[0][col] - rhs[0][col])

    # convert R_axis from numpy-array type to list
    R_list = array(R_axis).flatten().tolist()
    print(f'The unknowns of the parametric axis of rotation (e): {R_list}')
    print(
        f'The system of equations derived to solve for the mentioned unknowns: \n{eq}')
    ans = solve(eq, R_list)
    R_1 = sin(theta/2) * array(ans[0])
    R_2 = sin(theta/2) * array(ans[1])
    print('There are 2 answers for axis of rotation:')
    print(TextStyle.BOLD, end='')
    print(f'  R_1:  {R_1}')
    print(f'  R_2:  {R_2}')
    print(TextStyle.END, end='')


for T in times:
    # qp, rp = substituter(T)
    # vect_q = vect_Q.subs(t, T)
    # Phi = acos((trace(q) - 1)/2)
    # E = vect_q / sin(Phi)
    # R0 = cos(Phi/2)
    # R = sin(Phi/2)*E
    q = matrix2numpy(Q.subs(t, T))
    Phi = phi.subs(t, T)
    E = e.subs(t, T)
    R0 = cos(Phi/2)
    R = matrix2numpy((sin(Phi/2)*E).evalf(4))
    print(TextStyle.BOLD, end='')
    print(f'E-R parameters at t = {T}:')
    print(f'R0 = {R0}')
    print(f'R = \n{R}')
    print(TextStyle.END, end='')
    print(f'Q: \n{q}')
    print(f'phi = {Phi}')
    print(f'e = {E.evalf(4)}\n')
    if [nan] in R:
        print('This instance is subject to singularity and thus zero division problem. \nBy handling the singularity, the new E-R parameters are derived.')
        singularity_handler(q, Phi)
