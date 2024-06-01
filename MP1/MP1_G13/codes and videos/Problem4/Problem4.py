import cv2
import mediapipe as mp
import math
import sys
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Open the video files by cv2
video_path_1 = 'E:/w1.mp4'  # front view video file location
video_1 = cv2.VideoCapture(video_path_1)
video_path_2 = 'E:/w2.mp4'  # Sideview video file location
video_2 = cv2.VideoCapture(video_path_2)

# Check if the videos opened successfully
if not video_1.isOpened():
    print("Error! Could not open the video1!")
    sys.exit(0)
if not video_2.isOpened():
    print("Error! Could not open the video2!")
    sys.exit(0)

RightAnkleY_1 = []
RightAnkleZ_1 = []
RightKneeY_1 = []
RightKneeZ_1 = []
my_theta_x = []

RightAnkleX_2 = []
RightAnkleZ_2 = []
RightKneeX_2 = []
RightKneeZ_2 = []
my_theta_y = []

Q, phi, e, r, r0 = [], [], [], [], []


def rotation_matrix(alpha, beta):
    R = np.array([[np.cos(beta), np.sin(beta)*np.sin(alpha), np.sin(beta)*np.cos(alpha)],
                  [0, np.cos(alpha), -np.sin(alpha)],
                  [-np.sin(beta), np.cos(beta)*np.sin(alpha), np.cos(beta)*np.cos(alpha)]])
    return R


def vect(R):
    return (1/2 * np.array([[R[2, 1]-R[1, 2]], [R[0, 2]-R[2, 0]], [R[1, 0]-R[0, 1]]]))


while True:
    # Read frames
    ret_1, frame_1 = video_1.read()
    ret_2, frame_2 = video_2.read()

    # if the videos end, break
    if not ret_1 and not ret_2:
        break

    # Convert frame to RGB
    frame_1 = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    frame_2 = cv2.cvtColor(frame_2, cv2.COLOR_BGR2RGB)

    height1, width1 = frame_1.shape[0], frame_1.shape[1]
    height2, width2 = frame_2.shape[0], frame_2.shape[1]

    # Process with MediaPipe Pose
    result_1 = pose.process(frame_1)
    result_2 = pose.process(frame_2)

    if result_1.pose_landmarks:
        y_right_knee_1 = (
            result_1.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x
            * frame_1.shape[1]
        )
        z_right_knee_1 = (
            frame_1.shape[0]
            - result_1.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y
            * frame_1.shape[0]
        )
        y_right_ankle_1 = (
            result_1.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x
            * frame_1.shape[1]
        )
        z_right_ankle_1 = (
            frame_1.shape[0]
            - result_1.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y
            * frame_1.shape[0]
        )

        RightAnkleY_1.append(y_right_ankle_1)
        RightAnkleZ_1.append(z_right_ankle_1)
        RightKneeY_1.append(y_right_knee_1)
        RightKneeZ_1.append(z_right_knee_1)

        z = z_right_knee_1 - z_right_ankle_1
        y = y_right_knee_1 - y_right_ankle_1
        L = math.sqrt(y**2 + z**2)
        th_x_rad = math.atan2(z / L, y / L)
        th_x_deg = math.degrees(th_x_rad)
        my_theta_x.append(th_x_deg)  # theta_x

    if result_2.pose_landmarks:
        x_right_knee_2 = (
            result_2.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x
            * frame_2.shape[1]
        )
        z_right_knee_2 = (
            frame_2.shape[0]
            - result_2.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y
            * frame_2.shape[0]
        )
        x_right_ankle_2 = (
            result_2.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x
            * frame_2.shape[1]
        )
        z_right_ankle_2 = (
            frame_2.shape[0]
            - result_2.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y
            * frame_2.shape[0]
        )

        RightAnkleX_2.append(x_right_ankle_2)
        RightAnkleZ_2.append(z_right_ankle_2)
        RightKneeX_2.append(x_right_knee_2)
        RightKneeZ_2.append(z_right_knee_2)

        z = z_right_knee_2 - z_right_ankle_2
        x = x_right_knee_2 - x_right_ankle_2
        L = math.sqrt(x**2 + z**2)
        th_y_rad = math.atan2(z / L, x / L)
        th_y_deg = math.degrees(th_y_rad)
        my_theta_y.append(th_y_deg)  # theta_y

    Q.append(rotation_matrix(th_x_rad, th_y_rad))
    phi.append(np.arccos((np.trace(Q[-1])-1)/2))
    e.append(vect(Q[-1])/np.sin(phi[-1]))   # vector e
    r.append(e[-1]*np.sin(phi[-1]/2))
    r0.append(np.cos(phi[-1]/2))    # quaternion value
    print(f"frame {len(Q)}:\te={e[-1].reshape(1, 3)},\t r0={r0[-1]}")


# Release videos
video_1.release()
video_2.release()

numFrames = len(Q)
seconds = numFrames / 30
print('\nfront view frames:\t width =', width1, 'height =', height1)
print('side view frames:\t width =', width2, 'height =', height2)
print('\nnumber of frames processed:', numFrames)
print('length of videos in seconds:', round(seconds, 4))


# Defining some functions to simplify the plotting processes

def posPlot(X, Y, w, h, name):
    # Define the colormap from green to red
    colors = [(0, 'green'), (0.5, 'yellow'), (1, 'red')]
    cmap = LinearSegmentedColormap.from_list('CustomCmap', colors)

    # Compute the color gradient based on the position of points
    gradient = [(j / numFrames) for j in range(numFrames)]

    # Plotting the points with color gradient
    plt.title(name)
    plt.scatter(X, Y, c=gradient, cmap=cmap, s=10)
    plt.xlim(0, w)
    plt.ylim(0, h)

    # Customizing colorbar
    cbar = plt.colorbar()
    cbar.set_ticks([0, 0.5, 1])
    cbar.set_ticklabels(['Start', '', 'Stop'])

    plt.grid()
    plt.show()


def angPlot(angle, name):
    X = np.arange(0, seconds, 1/30)
    plt.title(rf"{name}")
    plt.plot(X, angle)
    if not 'r_0' in name:
        plt.ylim(0, 200)
        plt.ylabel('degrees')
    plt.xlabel('seconds')
    plt.grid()
    plt.show()


def smoothPlot(angle, name):
    X = np.arange(0, seconds, 1/30)

    # Applying moving average smoothing
    window_size = 6
    y_smooth = np.convolve(angle, np.ones(
        window_size)/window_size, mode='valid')

    plt.plot(X[window_size//2:-window_size//2+1],
             y_smooth, label='Filtered', color='r')
    plt.plot(X, angle, label='Raw', color='b', alpha=0.6)

    plt.title(rf"{name}")
    plt.xlabel('seconds')
    plt.ylabel('degrees')
    plt.grid()
    plt.legend()
    plt.show()


# Drawing the plots
posPlot(RightKneeX_2, RightKneeZ_2, width2, height2, 'Right Knee Side view')
posPlot(RightAnkleX_2, RightAnkleZ_2, width2, height2, 'Right Ankle Side view')
posPlot(RightKneeY_1, RightKneeZ_1, width1, height1, 'Right Knee Front view')
posPlot(RightAnkleY_1, RightAnkleZ_1, width2,
        height2, 'Right Ankle Front view')

angPlot(my_theta_x, "Roll angle (front view): $\\theta_x$")
angPlot(my_theta_y, "Pitch angle (side view): $\\theta_y$")
angPlot(r0, 'Quternion Value $r_0$:')
smoothPlot(my_theta_x, "Filtered Roll angle: $\\theta_x$")
smoothPlot(my_theta_y, "Filtered Pitch angle: $\\theta_y$")
