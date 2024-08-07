function ForceandTorques = OpenMan_torquesandforce(b1,b1_dot,b1_ddot,b4_ddot,theta2,theta3,theta2_dot,theta3_dot,theta2_ddot,theta3_ddot)
%OPENMAN_TORQUESANDFORCE
%    FORCEANDTORQUES = OPENMAN_TORQUESANDFORCE(B1,B1_DOT,B1_DDOT,B4_DDOT,THETA2,THETA3,THETA2_DOT,THETA3_DOT,THETA2_DDOT,THETA3_DDOT)

%    This function was generated by the Symbolic Math Toolbox version 8.2.
%    26-May-2024 18:14:38

t2 = abs(theta2_dot);
t3 = abs(theta3_dot);
t4 = atan(1.7e1./1.6e2);
t5 = atan(3.756512201809707e-2);
t6 = conj(theta2);
t7 = theta2.*2.0;
t8 = t3.^2;
t9 = conj(theta3);
t10 = t2.^2;
t11 = t6+t9-theta2;
t12 = real(theta2);
t13 = t12.*2.0;
t14 = t13+theta3;
t15 = theta2+theta3;
t16 = cos(t13);
t17 = cos(theta2);
t18 = sin(t13);
t19 = sin(theta2);
t20 = t9+t13;
t21 = t7+theta3;
t22 = real(theta3);
t23 = t22.*2.0;
t24 = t13+t23;
t25 = -t6+theta2+theta3;
t26 = cos(t7);
t27 = sin(t7);
t28 = theta3.*2.0;
t29 = t7+t28;
t30 = cos(t14);
t31 = sin(t14);
t32 = conj(theta2_dot);
t33 = t6+t9;
t34 = conj(theta3_dot);
t35 = cos(t15);
t36 = sin(t15);
t37 = conj(b1_dot);
t38 = cos(t20);
t39 = sin(t20);
t40 = cos(t6);
t41 = sin(t6);
t42 = sin(t29);
t43 = cos(t11);
t44 = sin(t11);
t45 = cos(t33);
t46 = cos(t29);
t47 = t8.*t35.*2.72e-2;
t48 = sin(t33);
t49 = b1.^2;
t50 = cos(t21);
t51 = cos(t24);
t52 = cos(theta3);
t53 = sin(t21);
t54 = sin(t24);
t55 = cos(t25);
t56 = sin(theta3);
t57 = sin(t25);
t58 = b1_dot.*t34.*t45.*4.25e-3;
t59 = (b1_dot.*t34.*t48)./2.5e1;
t60 = t35.*t37.*theta3_dot.*4.25e-3;
t61 = (t36.*t37.*theta3_dot)./2.5e1;
t62 = b1.*t8.*t35.*3.4e-1;
ForceandTorques = [b1_ddot.*3.0-(t8.*(b1.*(1.7e1./1.0e1)-sin(theta2+theta3+atan(9.0./4.0e1)).*6.97e-1+3.970617080505246e2.*cos(theta2-atan(3.97e2./7.0)).*1.7e-3+1.36e-1))./2.0-(t10.*(b1.*(1.2e1./5.0)-t17.*1.992e-1-t19.*1.752e-1+1.92e-1))./2.0+1.609005904277545e2.*theta3_ddot.*(cos(t4+t6+t9)./4.0e3+cos(t4+theta2+theta3)./4.0e3)+3.649572303709025e3.*theta2_ddot.*(cos(t5+t6)./1.0e4+cos(t5+theta2)./1.0e4);t47+t58+t59+t60+t61+t62+theta2_ddot.*5.23416e-2+b1_ddot.*t17.*3.647e-1-b1_ddot.*t19.*1.37e-2+b1_ddot.*t40.*3.647e-1-b1_ddot.*t41.*1.37e-2+b1.*theta2_ddot.*1.92e-1-t8.*t17.*2.6996e-2-t10.*t16.*6.321337507941464e-35+t8.*t19.*4.76e-4+t10.*t17.*7.008e-3-t10.*t18.*9.346802917505229e-34-t10.*t19.*7.968e-3-t8.*t26.*1.771328785307354e-35-t8.*t27.*5.021420716319299e-34-t10.*t26.*5.452226713888917e-35+t10.*t27.*7.018875782857494e-36-t8.*t36.*6.12e-3-t8.*t42.*4.841037108459644e-34-t8.*t46.*2.294632467472642e-34+t8.*t50.*2.455894138103358e-34-t8.*t51.*3.186989538156448e-36+t8.*t53.*1.008172270500411e-33-t8.*t54.*4.279939479771276e-35-t16.*theta2_ddot.*9.346802917505229e-34-t17.*theta2_ddot.*1.5936e-2+t18.*theta2_ddot.*6.321337507941464e-35-t19.*theta2_ddot.*1.4016e-2+t26.*theta2_ddot.*7.018875782857494e-36+t27.*theta2_ddot.*5.452226713888917e-35-t30.*theta3_ddot.*5.942891873784027e-35+t31.*theta3_ddot.*7.376006081103849e-36-t38.*theta3_ddot.*5.942891873784027e-35+t39.*theta3_ddot.*7.376006081103849e-36+t43.*theta3_ddot.*1.590975e-2-t44.*theta3_ddot.*1.40725e-3+t49.*theta2_ddot.*(6.0./5.0)+t55.*theta3_ddot.*1.590975e-2-t57.*theta3_ddot.*1.40725e-3+theta2_ddot.*cos(-t6+theta2).*2.500796e-1-b1.*t8.*t17.*3.3745e-1+b1.*t8.*t19.*5.95e-3+b1.*t10.*t17.*8.76e-2-b1.*t10.*t19.*9.96e-2-b1.*t8.*t36.*7.65e-2+b1_dot.*t32.*t40.*1.37e-2+b1_dot.*t32.*t41.*3.647e-1-b1.*t17.*theta2_ddot.*1.992e-1-b1.*t19.*theta2_ddot.*1.752e-1+t17.*t37.*theta2_dot.*1.37e-2+t19.*t37.*theta2_dot.*3.647e-1-t30.*t32.*theta3_dot.*1.47520121622077e-35-t31.*t32.*theta3_dot.*1.188578374756805e-34-t34.*t38.*theta2_dot.*1.47520121622077e-35-t34.*t39.*theta2_dot.*1.188578374756805e-34;t47+t58+t59+t60+t61+t62+theta3_ddot.*2.943343e-1+theta3_ddot.*cos(-t6-t9+theta2+theta3).*1.1585e-2+(b1_ddot.*t35)./2.5e1-b1_ddot.*t36.*4.25e-3+(b1_ddot.*t45)./2.5e1-b1_ddot.*t48.*4.25e-3+b1.*theta3_ddot.*1.36e-1-t8.*t36.*6.12e-3-t8.*t42.*4.841037108459644e-34-t8.*t46.*2.294632467472642e-34+t8.*t50.*1.227947069051679e-34-t8.*t51.*3.186989538156448e-36-t8.*t52.*2.79905e-2+t8.*t53.*5.040861352502053e-34-t8.*t54.*4.279939479771276e-35-t8.*t56.*1.355155e-1+t17.*theta3_ddot.*9.52e-4+t19.*theta3_ddot.*5.3992e-2-t26.*theta3_ddot.*5.021420716319299e-34+t27.*theta3_ddot.*1.771328785307354e-35-t30.*theta2_ddot.*5.942891873784027e-35+t31.*theta2_ddot.*7.376006081103849e-36-t35.*theta3_ddot.*1.224e-2-t36.*theta3_ddot.*5.44e-2-t38.*theta2_ddot.*5.942891873784027e-35+t39.*theta2_ddot.*7.376006081103849e-36+t42.*theta3_ddot.*2.294632467472642e-34+t43.*theta2_ddot.*1.590975e-2-t44.*theta2_ddot.*1.40725e-3-t46.*theta3_ddot.*4.841037108459644e-34+t49.*theta3_ddot.*(1.7e1./2.0e1)+t50.*theta3_ddot.*1.008172270500411e-33-t51.*theta3_ddot.*4.279939479771276e-35-t52.*theta3_ddot.*2.71031e-1-t53.*theta3_ddot.*2.455894138103358e-34+t54.*theta3_ddot.*3.186989538156448e-36+t55.*theta2_ddot.*1.590975e-2+t56.*theta3_ddot.*5.5981e-2-t57.*theta2_ddot.*1.40725e-3-b1.*t8.*t36.*7.65e-2+b1.*t17.*theta3_ddot.*1.19e-2+b1.*t19.*theta3_ddot.*6.749e-1-b1.*t35.*theta3_ddot.*1.53e-1-b1.*t36.*theta3_ddot.*6.8e-1-t30.*t32.*theta3_dot.*7.376006081103849e-36-t31.*t32.*theta3_dot.*5.942891873784027e-35-t34.*t38.*theta2_dot.*7.376006081103849e-36-t34.*t39.*theta2_dot.*5.942891873784027e-35+t34.*t43.*theta2_dot.*1.40725e-3+t34.*t44.*theta2_dot.*1.590975e-2+t32.*t55.*theta3_dot.*1.40725e-3+t32.*t57.*theta3_dot.*1.590975e-2;b4_ddot.*(3.0./2.0e1)+1.4715];
