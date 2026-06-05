import numpy as np
import matplotlib.pyplot as plt

def init_2d_figure(m, g):
    # Generates figure with a quiver plot of the Hamiltonian vector field of the pendulum

    fig, ax = plt.subplots()
    hamilton_field = lambda y: [y[1]/m, -m*g*np.sin(y[0])]
    xmin, xmax = -5, 5
    ymin, ymax = -8, 8

    x = np.linspace(xmin, xmax, 20)
    y = np.linspace(ymin, ymax, 20)
    X, Y = np.meshgrid(x, y)
    U, V = hamilton_field([X, Y])
    ax.quiver(X, Y, U, V)

    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel(r"$p_{\theta}$")
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_xlim(xmin, xmax)

    return fig, ax

def init_3d_figure():
    # Generates a 3D figure with the cylindrical phase space of the pendulum

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    theta = np.linspace(0, 2*np.pi, 200)
    z = np.linspace(-10, 10, 200)
    Theta, Z = np.meshgrid(theta, z)
    X = np.cos(Theta)
    Y = np.sin(Theta)
    ax.plot_surface(X, Y, Z, color="gray", alpha=0.3)

    return fig, ax

def find_trajectories(lam_values, m, g, R):
    const = m * g * R

    trajectories = []
    for lam in lam_values:
        theta = np.acos(-lam/const) * np.linspace(-1, 1, 200) if lam < const else np.pi * np.linspace(-1, 1, 200)

        p_theta = R * np.sqrt(2 * m * np.clip(lam + const*np.cos(theta), 0, None))

        trajectories.append((theta, p_theta))
    
    return trajectories

def plot_trajectory_2d(ax, theta, p_theta, color="blue"):
    for shift in [-2*np.pi, 0, 2*np.pi]:
        ax.plot(theta + shift, p_theta, color=color)
        ax.plot(theta + shift, -p_theta, color=color)
    
def plot_trajectory_3d(ax, theta, p_theta, color="blue", label=""):
    x = np.cos(theta)
    y = np.sin(theta)
    ax.plot3D(x, y, p_theta, color=color, label=label)
    ax.plot3D(x, y, -p_theta, color=color)



# The figures of the project were generated with code similar to the functions below
def figure_phase_plane():
    m = 1.0
    g = 9.81
    R = 1.0
    fig, ax = init_2d_figure(m, g)
    lam_values = m * g * R * np.linspace(-1, 2, 9)
    for theta, p_theta in find_trajectories(lam_values, m, g, R):
        plot_trajectory_2d(ax, theta, p_theta)    
    plt.show()

def figure_repr_level_sets():
    m = 1.0
    g = 9.81
    R = 1.0
    fig2D, ax2D = init_2d_figure(m, g)
    fig3D, ax3D = init_3d_figure()
    lam_values = m * g * R * np.arange(3)
    labels = [r"-mgR < $\lambda$ < mgR", r"$\lambda$ = mgR", r"$\lambda$ > mgR"]
    for i, (theta, p_theta) in enumerate(find_trajectories(lam_values, m, g, R)):
        plot_trajectory_2d(ax2D, theta, p_theta, color=plt.cm.viridis(i/2))
        plot_trajectory_3d(ax3D, theta, p_theta, color=plt.cm.viridis(i/2), label=labels[i])
    
    ax3D.legend()
    plt.show()
