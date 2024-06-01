from numpy import *

def vect(R):
    vect_R = 1/2 * array([
        [R[2][1]-R[1][2]],
        [R[0][2]-R[2][0]],
        [R[1][0]-R[0][1]]
    ])
    return vect_R

def NaturalInvariant(Q):
    phi = arccos((trace(Q) - 1)/2)
    e = vect(Q) / sin(phi)
    return phi, e

def LinearInvariant(Q):
    phi, e = NaturalInvariant(Q)
    q0 = cos(phi)
    q = sin(phi)*e
    print(f'q0 = {q0}')
    print(f'q = \n{q}\n')

def EulerRodriguesPara(Q):
    phi, e = NaturalInvariant(Q)
    r0 = cos(phi/2)
    r = sin(phi/2)*e
    print(f'r0 = {r0}')
    print(f'r = \n{r}\n')

R = array([
    [1/sqrt(2), 0, 1/sqrt(2)],
    [-1/2, 1/sqrt(2), 1/2],
    [-1/2, -1/sqrt(2), 1/2]
])

print('part 1: Natural invariants of rotation')
Phi, E = NaturalInvariant(R)
print(f'phi = {rad2deg(Phi)} degrees')
print(f'e = \n{E}\n')

print('part 2: Linear invariants of rotation')
LinearInvariant(R)

print('part 3: Euler-Rodrigues parameters of rotation')
EulerRodriguesPara(R)

print('part 4 (Bonus):')

def euler_rodrigues_to_rotation_matrix(theta, axis):
    """
    Convert Euler-Rodrigues parameters to a rotation matrix.

    Parameters:
    - theta: Rotation angle in radians.
    - axis: 3D axis of rotation as a numpy array [x, y, z].

    Returns:
    - Rotation matrix as a 3x3 numpy array.
    """
    axis = asarray(axis)
    # Normalize the rotation axis to handle singularities
    axis = axis / linalg.norm(axis)

    # Extract components of the normalized rotation axis
    x, y, z = axis

    c = cos(theta)
    s = sin(theta)
    t = 1 - c

    # Build the rotation matrix
    rotation_matrix = array([
        [t*x*x + c, t*x*y - s*z, t*x*z + s*y],
        [t*x*y + s*z, t*y*y + c, t*y*z - s*x],
        [t*x*z - s*y, t*y*z + s*x, t*z*z + c]
    ])

    return rotation_matrix

# Test the function with two inputs:

# (a) Case where singularity happens
theta_a = pi  # 180 degrees
axis_a = array([1, 0, 0])
rotation_matrix_a = euler_rodrigues_to_rotation_matrix(theta_a, axis_a)

# (b) Case where singularity does not happen
theta_b = pi / 4  # 45 degrees
axis_b = array([0, 1, 0])
rotation_matrix_b = euler_rodrigues_to_rotation_matrix(theta_b, axis_b)

# (c) Case where singularity happens
theta_c = pi  # 180 degrees
axis_c = sqrt(3)/3 * array([1, 1, 1])
rotation_matrix_c = euler_rodrigues_to_rotation_matrix(theta_c, axis_c)

print("Rotation Matrix for Case (a):")
print(rotation_matrix_a)

print("\nRotation Matrix for Case (b):")
print(rotation_matrix_b)

print("\nRotation Matrix for Case (c):")
print(3*rotation_matrix_c)
