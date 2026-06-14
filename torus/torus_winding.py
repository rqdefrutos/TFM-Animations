import numpy as np
import matplotlib.pyplot as plt

# Linear trajectories on a torus visualized as square with opposite sides identified
def linear_flow_torus(frequencies, initial_points, period=2*np.pi):
    # Plots linear trajectories on a torus visualized as a square with opposite sides identified
    # If q1, q2 are coprime integers, the period is 2pi
    
    t = np.linspace(0, period, 500)    
    phi = frequencies * t[:, None] + initial_points
    Q, R = np.divmod(phi, 2*np.pi)

    for q in np.unique(Q, axis=0):
        mask = np.all(Q == q, axis=1)
        line = R[mask].T
        plt.plot(*line, color="red")

    plt.xlim((0, 2*np.pi))
    plt.ylim((0, 2*np.pi))
    plt.xlabel(r"$\varphi^1$")
    plt.ylabel(r"$\varphi^2$")    
    plt.show()

def parametrize_torus(u, v, R, r):
    # R, r: big and small radii of the torus
    x = (R + r * np.cos(u)) * np.cos(v)
    y = (R + r * np.cos(u)) * np.sin(v)
    z = np.sin(u)
    return x, y, z

def plot_torus_surface(R, r):
    # Generates a figure of a torus with custom settings (opacity, color, orientation)
    # R, r: big and small radii of the torus

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    theta = np.linspace(0, 2*np.pi, 100)
    U, V = np.meshgrid(theta, theta)
    X, Y, Z = parametrize_torus(U, V, R, r)
    ax.plot_surface(X, Y, Z, color="blue", alpha=0.3)

    ax.set_aspect("equal")
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])
    ax.view_init(elev=35, azim=-10, roll=0)

    return fig, ax

def torus_winding(frequencies, initial_points, period=2*np.pi, R=2.0, r=1.0):
    # Figure of a trajectory winding around a torus of revolution

    fig, ax = plot_torus_surface(R, r)

    t = np.arange(0, period, 0.02)
    phi = frequencies * t[:, None] + initial_points
    x, y, z = parametrize_torus(phi[:, 0], phi[:, 1], R, r)

    ax.plot3D(x, y, z, color="red")

    plt.show()

def torus_winding_frames(frequencies, initial_points, num_frames, period=2*np.pi, R=2.0, r=1.0):
    # Saves frames of the animation in a folder
    # Use period = 100 for irrational q1/q2
    # Keep in mind that num_frames = duration * fps

    fig, ax = plot_torus_surface(R, r)

    t = np.arange(0, period, 0.05) # 20 nodes per unit of the parameter
    phi = frequencies * t[:, None] + initial_points
    x, y, z = parametrize_torus(phi[:, 0], phi[:, 1], R, r)

    point, = ax.plot3D([], [], [], "r.", markersize=15)
    trail, = ax.plot3D([], [], [], "r-")
    
    for i in range(num_frames):
        idx = round(i * len(t) / num_frames)
        point.set_data_3d([x[idx]], [y[idx]], [z[idx]])
        trail.set_data_3d(x[:idx], y[:idx], z[:idx])
        fig.savefig(f"frames/frame{i}.png")

""" Note: The frames for the final GIFs were generated with
these commands:
Periodic orbit: torus_winding_frames([1, 3], [0, 0], 150)
Dense orbit: torus_winding_frames([1, np.sqrt(2)], [0, 0], 450, period=100)
I wanted the GIFs to last approximately 5 and 15 seconds, respectively,
with a frame rate of around 30 fps, thus the choices for 150 and 450 frames.
The frames were then turned into a GIF using the website ezgif.com/maker """
