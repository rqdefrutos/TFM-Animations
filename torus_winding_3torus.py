import numpy as np
import matplotlib.pyplot as plt

def linear_flow_3_torus(frequencies, initial_points, period=2*np.pi):
    # Plots linear trajectories on a 3-torus visualized as a cube with opposite sides identified
    # If the frequencies are integers the period is 2pi
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    t = np.linspace(0, period, 500)
    phi = frequencies * t[:, None] + initial_points
    Q, R = np.divmod(phi, 2*np.pi)

    for q in np.unique(Q, axis=0):
        mask = np.all(Q == q, axis=1)
        line = R[mask].T
        ax.plot3D(*line, color="red")
    
    plt.show()

frequencies = [7, 5, -9]
intial_point = [0, 0, 0]
linear_flow_3_torus(frequencies, intial_point)

# figure 'orbits_on_3_torus': frequencies = [7, 5, -9] and [7, 5, -10] (with initial_points=[0,0,0])
