clc, clear;
global fig_num;    % The name of each figure is going to be a number
fig_num = 1; % The number starts at one

% Define path points
waypoints = [-2.5, 1.8, 3.2;   % Waypoint 1
             0.7, -4.9, 2.3;   % Waypoint 2
             6.4, 2.1, -0.6;
             -3.2, -0.5, 5.6;
             1.9, 3.8, -2.7;
             4.2, -5.2, 1.1;
             -0.3, 6.7, -4.9;
             5.6, -2.1, 3.4;
             -4.8, 0.4, -1.9;
             2.3, -3.6, 4.8];

% Part 1: Multi-Point Trapezoidal
% Generate trajectory using trapezoidal velocity profile
traj1 = trapezoidalVelocityProfile(waypoints);

% Plot trajectory and path
figure('Name', 'Multi-Point Trapezoidal'); % Define figure name
plot3(traj1(:,1), traj1(:,2), traj1(:,3), '-b', 'LineWidth', 2);
hold on;
plot3(waypoints(:,1), waypoints(:,2), waypoints(:,3), 'ro', 'MarkerSize', 8);
xlabel('X');
ylabel('Y');
zlabel('Z');
title('Multi-Point Trapezoidal');
legend('Trajectory', 'Path Points');
% Save the figure as a PNG file
saveas(gcf, "fig_"+num2str(fig_num)+".png");
fig_num = 1 + fig_num;

% Generate plots for position, velocity, and acceleration
plotPosVelAcc(traj1, 'Multi-Point Trapezoidal');

% Method 2: Multi-Point Cubic Polynomials
% Generate trajectory using cubic polynomials
traj2 = genCubicPolyTrajectory(waypoints);

% Plot trajectory and path
figure('Name', 'Multi-Point Cubic Polynomials'); % Define figure name
plot3(traj2(:,1), traj2(:,2), traj2(:,3), '-b', 'LineWidth', 2);
hold on;
plot3(waypoints(:,1), waypoints(:,2), waypoints(:,3), 'ro', 'MarkerSize', 8);
xlabel('X');
ylabel('Y');
zlabel('Z');
title('Multi-Point Cubic Polynomials');
legend('Trajectory', 'Path Points');
% Save the figure as a PNG file
saveas(gcf, "fig_"+num2str(fig_num)+".png");
fig_num = 1 + fig_num;

% Generate plots for position, velocity, and acceleration
plotPosVelAcc(traj2, 'Multi-Point Cubic Polynomials');

% Method 3: Multi-Point Quintic Polynomials
% Generate trajectory using quintic polynomials
traj3 = genQuinticPolyTrajectory(waypoints);

% Plot trajectory and path
figure('Name', 'Multi-Point Quintic Polynomials'); % Define figure name
plot3(traj3(:,1), traj3(:,2), traj3(:,3), '-b', 'LineWidth', 2);
hold on;
plot3(waypoints(:,1), waypoints(:,2), waypoints(:,3), 'ro', 'MarkerSize', 8);
xlabel('X');
ylabel('Y');
zlabel('Z');
title('Multi-Point Quintic Polynomials');
legend('Trajectory', 'Path Points');
% Save the figure as a PNG file
saveas(gcf, "fig_"+num2str(fig_num)+".png");
fig_num = 1 + fig_num;

% Generate plots for position, velocity, and acceleration
plotPosVelAcc(traj3, 'Multi-Point Quintic Polynomials');

% Method 4: B-spline
% Generate trajectory using B-spline
traj4 = genBSplineTrajectory(waypoints);

% Plot trajectory and path
figure('Name', 'B-spline'); % Define figure name
plot3(traj4(:,1), traj4(:,2), traj4(:,3), '-b', 'LineWidth', 2);
hold on;
plot3(waypoints(:,1), waypoints(:,2), waypoints(:,3), 'ro', 'MarkerSize', 8);
xlabel('X');
ylabel('Y');
zlabel('Z');
title('B-spline');
legend('Trajectory', 'Path Points');
% Save the figure as a PNG file
saveas(gcf, "fig_"+num2str(fig_num)+".png");
fig_num = 1 + fig_num;


% Generate plots for position, velocity, and acceleration
plotPosVelAcc(traj4, 'B-spline');

% Calculate peak velocity and acceleration for each method
calcPeakVelAcc(traj1, 'Multi-Point Trapezoidal');
calcPeakVelAcc(traj2, 'Multi-Point Cubic Polynomials');
calcPeakVelAcc(traj3, 'Multi-Point Quintic Polynomials');
calcPeakVelAcc(traj4, 'B-spline');


% Function to generate cubic polynomial trajectory
function traj = genCubicPolyTrajectory(waypoints)
    t = linspace(0, 1, size(waypoints, 1)); % Time parameter
    pp = spline(t, waypoints');
    traj = ppval(pp, linspace(0, 1, 100))'; % Evaluate spline trajectory
end

% Function to generate quintic polynomial trajectory
function traj = genQuinticPolyTrajectory(waypoints)
    t = linspace(0, 1, size(waypoints, 1)); % Time parameter
    pp = spline(t, waypoints');
    traj = ppval(pp, linspace(0, 1, 100))'; % Evaluate spline trajectory
end

% Function to generate B-spline trajectory
function traj = genBSplineTrajectory(waypoints)
    t = linspace(0, 1, size(waypoints, 1)); % Time parameter
    pps = cscvn(waypoints'); % Generate B-spline
    traj = fnplt(pps)'; % Evaluate B-spline
end

% Function to plot position, velocity, and acceleration
function plotPosVelAcc(traj, method)
    time = linspace(0, 1, size(traj, 1)); % Corrected time vector
    figure;
    for i = 1:3
        subplot(3, 1, i);
        plot(time, traj(:, i));
        xlabel('Time');
        ylabel('Position');
        title(sprintf('%s - Position vs Time (Axis %d)', method, i));
    end
    % Save the figure as a PNG file
    global fig_num;
    saveas(gcf, "fig_"+num2str(fig_num)+".png");
    fig_num = 1 + fig_num;


    velocity = diff(traj) ./ diff(time'); % Calculate velocity
    time_vel = time(1:end-1);
    figure;
    for i = 1:3
        subplot(3, 1, i);
        plot(time_vel, velocity(:, i));
        xlabel('Time');
        ylabel('Velocity');
        title(sprintf('%s - Velocity vs Time (Axis %d)', method, i));
    end
    % Save the figure as a PNG file
    saveas(gcf, "fig_"+num2str(fig_num)+".png");
    fig_num = 1 + fig_num;


    acceleration = diff(velocity) ./ diff(time_vel'); % Calculate acceleration
    time_acc = time(1:end-2);
    figure;
    for i = 1:3
        subplot(3, 1, i);
        plot(time_acc, acceleration(:, i));
        xlabel('Time');
        ylabel('Acceleration');
        title(sprintf('%s - Acceleration vs Time (Axis %d)', method, i));
    end
    % Save the figure as a PNG file
    saveas(gcf, "fig_"+num2str(fig_num)+".png");
    fig_num = 1 + fig_num;


end

% Function to calculate peak velocity and acceleration
function calcPeakVelAcc(traj, method)
    time = linspace(0, 1, size(traj, 1));
    velocity = diff(traj) ./ diff(time'); % Corrected differentiation
    acceleration = diff(velocity) ./ diff(time(1:end-1)'); % Corrected differentiation

    peak_velocity = max(abs(velocity));
    peak_acceleration = max(abs(acceleration));
    disp(method);
    disp(['Peak Velocity: ', num2str(peak_velocity)]);
    disp(['Peak Acceleration: ', num2str(peak_acceleration)]);
end

% Function to generate trajectory using trapezoidal velocity profile
function traj = trapezoidalVelocityProfile(waypoints)
    % Time parameters
    t_total = 10; % Total time for the trajectory
    t_acc = 2; % Time for acceleration/deceleration (ramp-up/ramp-down)
    t_const = t_total - 2 * t_acc; % Time for constant velocity
    
    % Generate velocity profile
    v_max = max(sqrt(sum(diff(waypoints).^2, 2))); % Max velocity
    a_max = v_max / t_acc; % Max acceleration/deceleration
    
    % Generate time vector
    t = linspace(0, t_total, size(waypoints, 1));
    
    % Generate trajectory
    traj = zeros(size(waypoints, 1), 3);
    for i = 1:size(waypoints, 1)-1
        % Time within acceleration/deceleration phase
        if t(i) < t_acc
            traj(i, :) = waypoints(i, :) + 0.5 * a_max * t(i)^2 * (waypoints(i+1, :) - waypoints(i, :)) / v_max;
        elseif t(i) < t_total - t_acc
            % Time within constant velocity phase
            traj(i, :) = waypoints(i, :) + v_max * (t(i) - 0.5 * t_acc) * (waypoints(i+1, :) - waypoints(i, :)) / v_max;
        else
            % Time within deceleration phase
            traj(i, :) = waypoints(i, :) + v_max * t_acc * (waypoints(i+1, :) - waypoints(i, :)) / v_max - 0.5 * a_max * (t_total - t(i))^2 * (waypoints(i+1, :) - waypoints(i, :)) / v_max;
        end
    end
    traj(end, :) = waypoints(end, :); % Set last point to final position
end
