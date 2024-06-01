from numpy import *

# points on the line
P = array([[1], [2], [3]])
Q = array([[4], [5], [6]])

# two points from which the Plucker line is seen
a = array([[0], [0], [0]])
b = array([[0], [0], [1]])

# unit vector of the line passing P & Q
e = (Q - P) / linalg.norm((Q - P))

# the moments of Plucker line using point P on the
# line and two origins a & b
na = cross((P - a).flatten(), e.flatten())
nb = cross((P - b).flatten(), e.flatten())

n_a = na.reshape((3, 1))
n_b = nb.reshape((3, 1))

# Plucker line representations consisting of e & ka or kb
ka = vstack((e, n_a))
kb = vstack((e, n_b))

a = a.flatten()
b = b.flatten()

# the Cross Product Matrix (CPM) or cross product
# skew-symmetric matrix of points a & b
A = array([[0, -a[2], a[1]],
           [a[2], 0, -a[0]],
           [-a[1], a[0], 0]])

B = array([[0, -b[2], b[1]],
           [b[2], 0, -b[0]],
           [-b[1], b[0], 0]])

I = eye(3, 3)
O = zeros((3, 3))

# the transformation matrix to convert ka to kb
U = block([[I, O],
           [A - B, I]])

print(f'1st Plucker line: ka = \n{ka}\n')
print(f'2nd Plucker line: kb = \n{kb}\n')
print(f'Transformation matrix between ka & kb: U = \n{U}\n')
print('Difference of the two sides of the transformation eq:')
print(f'kb = U ka -> kb - U ka = \n{kb - U@ka} = 0')
