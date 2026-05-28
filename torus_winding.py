import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    theta = np.linspace(0, 2*np.pi, 100)
    U, V = np.meshgrid(theta, theta)
    X, Y, Z = parametrize_torus(U, V, R, r)
    ax.plot_surface(X, Y, Z, color="blue", alpha=0.3)

    return fig, ax

def torus_winding(frequencies, initial_points, period=2*np.pi, R=2.0, r=1.0):
    # Figure of a trajectory winding around a torus of revolution

    fig, ax = plot_torus_surface(R, r)

    t = np.linspace(0, period, 500)
    phi = frequencies * t[:, None] + initial_points
    x, y, z = parametrize_torus(phi[:, 0], phi[:, 1], R, r)

    ax.plot3D(x, y, z, color="red")

    ax.set_aspect("equal")
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    plt.show()

def winding_animation(frequencies, initial_points, period=2*np.pi, R=2.0, r=1.0):
    # Displays animation of a winding of the torus
    # Use period=100 for irrational q1/q2

    fig, ax = plot_torus_surface(R, r)

    t = np.linspace(0, period, 2000)
    phi = frequencies * t[:, None] + initial_points
    x, y, z = parametrize_torus(phi[:, 0], phi[:, 1], R, r)

    point, = ax.plot3D([], [], [], "r.", markersize=15)
    trail, = ax.plot3D([], [], [], "r-")

    def update(i):
        idx = i * 5
        point.set_data_3d([x[idx]], [y[idx]], [z[idx]])
        trail.set_data_3d(x[:idx], y[:idx], z[:idx])
        return point, trail

    ax.set_aspect("equal")
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    anim = FuncAnimation(fig, update, frames=300, interval=50, blit=True)
    plt.show()

    return anim

# torus_anim: winding_animation([1.0, np.sqrt(2)], [0, 0], period=100)
winding_animation([1, 3], [0, 0])