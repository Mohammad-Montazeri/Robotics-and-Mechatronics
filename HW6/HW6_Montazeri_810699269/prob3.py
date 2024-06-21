import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from collections import Counter
import matplotlib.lines as mlines

# Given points and their labels
points = np.array([-9, -8, -7, -5, -3, -1, 0, 1, 3, 5, 7, 8, 9])
labels = np.array([1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1])

# Transform the points using the given phi function
def phi(x): return np.array([np.cos(np.pi / 4 * x), np.sin(np.pi / 4 * x)])
transformed_points = np.array([phi(x) for x in points])

x = np.round(transformed_points[:, 0], decimals=5)
y = np.round(transformed_points[:, 1], decimals=5)

# Count occurrences of each point
xy = list(zip(x, y))
counts = Counter(xy)

# Fit SVM to the transformed points
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(transformed_points, labels)

# Get the separator line
w = clf.coef_[0]
b = clf.intercept_[0]
slope = -w[1] / w[0]
intercept = -b / w[0]

# Print the equation of the separator line
print(
    f"The equation of the separator line is: y = {slope:.2f}x + {intercept:.2f}")


# Plot the transformed points and the decision boundary
plt.figure(figsize=(10, 6))
plt.scatter(x, y, c=labels, cmap='bwr', s=350, alpha=1)

# Annotate with counts
for (xi, yi), count in counts.items():
    plt.text(xi, yi, str(count), fontsize=17,
             ha='center', va='center', color='w')


plt.xlabel(r'$x_1 = \cos\left(\frac{\pi}{4} x\right)$')
plt.ylabel(r'$x_2 = \sin\left(\frac{\pi}{4} x\right)$')
plt.title('Transformed Points and SVM Separator Line')
plt.grid(alpha=0.3)
# plt.axis('equal')


# plot the decision function
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = clf.decision_function(xy).reshape(XX.shape)

# plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k',
           levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])

# plot support vectors
ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[
           :, 1], s=100, linewidth=1, facecolors='none')

# Define custom legend handles
red_handle = mlines.Line2D([], [], color='red', marker='o', linestyle='None', markersize=10, label='Positive')
blue_handle = mlines.Line2D([], [], color='blue', marker='o', linestyle='None', markersize=10, label='Negative')

# Add custom legend to the plot
plt.legend(handles=[red_handle, blue_handle], loc='upper right')

plt.show()
