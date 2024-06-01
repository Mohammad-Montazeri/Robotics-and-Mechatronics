clear all
clc
%% FKP
% D-H parametes: 
% load('parameters.mat'); %Import from parameters.mlx workspace
syms b1 b4 theta2 theta3
a = [0, 400, 250, 0];
b = [b1, 257.7, 0, -b4];
alpha = [pi/2, 0, 0, pi];
th = [0, theta2, theta3, 0];

% Write your code here 
Q1=Qfunc(1,th,alpha);
Q2=Qfunc(2,th,alpha);
Q3=Qfunc(3,th,alpha);
Q4=Qfunc(4,th,alpha);
a1=afunc(1,a,b,th);
a2=afunc(2,a,b,th);
a3=afunc(3,a,b,th);
a4=afunc(4,a,b,th);

% Rotation matrix
Q=vpa(simplify(Q1*Q2*Q3*Q4),4)
phi = vpa(acos((trace(Q) - 1)/2), 4)

% Displacement matrix
P=vpa(simplify(a1+Q1*a2+Q1*Q2*a3+Q1*Q2*Q3*a4),4)

% Final Transition matrix
T=[Q, P; 0,0,0,1];
T=vpa(simplify(T),4)

% With the initial condition: b=[800, 0, 0, 100] th=[0, 0, pi/2, 0]
T_init=round(subs(T, [b1, b4, theta2, theta3], [800, 100, 0, pi/2]))

P0 = subs(P, [b1, b4, theta2, theta3], [800, 100, 0, pi/2]);
x0 = vpa(P0(1))
y0 = vpa(P0(2))
z0 = vpa(P0(3))
phi0 = rad2deg(0 + pi/2)

%% *Jacobian*
e = [0;0;1];

e11 = e;
e21 = Q1*e;
e31 = Q1*Q2*e;
e41 = Q1*Q2*Q3*e;

a11 = a1;
a21 = Q1*a2;
a31 = Q1*Q2*a3;
a41 = Q1*Q2*Q3*a4;

r11 = a11+a21+a31+a41;
r21 = a21+a31+a41;
r31 = a31+a41;
r41 = a41;

J = [0, 1, 1, 0; e11, cross(e21, r21), cross(e31, r31), e41]; 
J = vpa(simplify(J),4)

%% IKP
% Known parametes
syms x y z phi

% equations
eq1 = x == 400*cos(theta2) + 250*cos(theta2+theta3);
eq2 = y == b4 - 257.7;
eq3 = z == b1 + 400*sin(theta2) + 250*sin(theta2+theta3);
eq4 = phi == theta2 + theta3;

% solve equations
IKP = solve([eq1, eq2, eq3, eq4], [theta2, theta3, b1, b4]);
theta_2 = IKP.theta2
theta_4 = IKP.theta3
b_1 = IKP.b1
b_4 = IKP.b4
