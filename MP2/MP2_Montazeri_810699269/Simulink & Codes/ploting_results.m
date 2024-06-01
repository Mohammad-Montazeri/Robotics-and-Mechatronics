clc
close all
TAUT = TAU';
figure()
%%
% Plot torques and forces with title 'joints torque and force using simscape and dynamic model'

for i=1:4
    subplot(2,2,i);
    plot(out.TorqueForce.time , out.TorqueForce.Data(:,i),'LineStyle',markers{4},'LineWidth',2)
    hold on
    plot(0:Ts_M:tf , TAUT(:,i),'LineWidth',1)

    if ((i==2) || (i==3))
        leg1 = "$\tau"+ num2str(i) + "_{sim}$";
        leg2 = "$\tau_"+ num2str(i) + "$";
        legend(leg1 ,leg2, 'Interpreter', 'latex')
        titles = "torque "+ num2str(i);
        title(titles)
        xlabel('t')
        ylabel('\tau (N.m)')
    else
        leg1 = "$f"+ num2str(i) + "_{sim}$";
        leg2 = "$f_"+ num2str(i) + "$";
        legend(leg1 ,leg2, 'Interpreter', 'latex')
        titles = "force "+ num2str(i);
        title(titles)
        xlabel('t')
        ylabel('F (N)')
    end
end
sgtitle('Joint-space torques and forces obtained using Simscape and from Dynamic model')