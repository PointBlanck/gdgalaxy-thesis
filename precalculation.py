""" Module responsible for the pre-calculation inspection of the model. """

# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import potentials as pt

# Plot mass density from potentials
def plots():
    """ Plots mass density for the disk, bulge and total axisymmetric potentials. """
    
    fig, ax = plt.subplots(2,2,layout = "constrained")
    p1, p2, p3, p4 = input("Q2: How many plots would you like? (Input 1 or 0)(mass density, rotation velocity, Omega vs r, Isodensities of spiral density)").split(",")
    p1 = int(p1.strip())
    p2 = int(p2.strip())
    p3 = int(p3.strip())
    p4 = int(p4.strip())
    if p1 == 1:
        plot_density(fig, ax)
    if p2 == 1:
        plot_rotation_velocity(fig, ax)
    if p3 == 1:
        plot_omega(fig, ax)
    if p4 == 1:
        plot_spiral_potential(fig, ax)
    plt.show()
    

def plot_density(fig, ax):
    """ Plots mass density for the disk, bulge and total axisymmetric potentials. """
    max_r = int(input("Mass Density: Input max_r"))
    dim_r = int(input("Mass Density: Input dim_r"))
    r = np.linspace(0, max_r, dim_r)
    disk_potential = pt.disk_potential(r)
    bulge_potential = pt.bulge_potential(r)

    # Calculate derivatives
    dr = r[1] - r[0]
    disk_grad1 = np.gradient(disk_potential, dr)
    disk_grad2 = np.gradient(disk_grad1, dr)
    bulge_grad1 = np.gradient(bulge_potential, dr)
    bulge_grad2 = np.gradient(bulge_grad1, dr)
    # =======================================================================
    # Needs to be updated to account for z dependence
    density_disk = (disk_grad2 + ((1.0*disk_grad1)/r))/(4.0*np.pi*pt.G)
    # =======================================================================
    density_bulge = (bulge_grad2 + ((2.0*bulge_grad1)/r))/(4.0*np.pi*pt.G)

    # Make the plots
    ax[0][0].plot(r, np.log10(density_disk), label="Disk Density")
    ax[0][0].plot(r, np.log10(density_bulge), label="Bulge Density")
    ax[0][0].plot(r, np.log10(density_disk + density_bulge), label="Total Density")
    ax[0][0].set_xlim(0, max_r)
    ax[0][0].set_ylim(7.0,10.0)
    ax[0][0].set_box_aspect(1)
    ax[0][0].legend()

def plot_rotation_velocity(fig, ax):
    """ Plot rotation velocity vs r. """
    # =======================================================================
    # Doesn't produce same output because I didn't include halo potential
    # =======================================================================
    max_r = int(input("Rotation velocity: Input max_r"))
    dim_r = int(input("Rotation velocity: Input dim_r"))
    r = np.linspace(0, max_r, dim_r)
    disk_potential = pt.disk_potential(r)
    bulge_potential = pt.bulge_potential(r)
    axisymmetric_potential = disk_potential + bulge_potential

    dr = r[1] - r[0]
    total_potential_grad1 = np.gradient(axisymmetric_potential, dr)
    rotation_velocity = np.sqrt(r*total_potential_grad1)

    ax[0][1].plot(r, rotation_velocity, label = "Rotation velocity")
    ax[0][1].set_xlim(0, max_r)
    ax[0][1].set_ylim(0, 300)
    ax[0][1].set_box_aspect(1)
    ax[0][1].legend()

def plot_omega(fig, ax):
    """ Plot omega. """
    max_r = int(input("Plot omega: Input max_r"))
    dim_r = int(input("Plot omega: Input dim_r"))
    r = np.linspace(0, max_r, dim_r)
    disk_potential = pt.disk_potential(r)
    bulge_potential = pt.bulge_potential(r)
    axisymmetric_potential = disk_potential + bulge_potential

    dr = r[1] - r[0]
    total_potential_grad1 = np.gradient(axisymmetric_potential, dr)
    total_potential_grad2 = np.gradient(total_potential_grad1, dr)
    omega = np.sqrt((r**(-1))*total_potential_grad1)
    epic = np.sqrt(total_potential_grad2 + (3.0*(r**(-1)))*total_potential_grad1)

    ax[1][0].plot(r, omega, label = "Ω")
    ax[1][0].plot(r, omega - epic/4.0, label = "Ω - κ/4")
    ax[1][0].plot(r, omega - epic/2.0, label = "Ω - κ/2")
    ax[1][0].plot(r, omega + epic/2.0, label = "Ω + κ/2")
    ax[1][0].plot(r, np.ones((np.size(r),1))*pt.Omega_sp, label = "$Ω_{sp}$")
    ax[1][0].set_xlim(0, max_r)
    ax[1][0].set_ylim(0, 80)
    ax[1][0].set_box_aspect(1)
    ax[1][0].legend()

def plot_spiral_potential(fig, ax):
    """ Plot spiral potential perturbation. """
    max_x, max_y, dim_x, dim_y = input("Plot spiral density: Input max_x, max_y, dim_x, dim_y").split(",")
    max_x = int(max_x.strip())
    max_y = int(max_y.strip())
    dim_x = int(dim_x.strip())
    dim_y = int(dim_y.strip())
    x, y = np.meshgrid(np.linspace(-max_x, max_x, dim_x), np.linspace(-max_y, max_y, dim_y))
    r = np.sqrt(x**2 + y**2)
    phi = np.atan2(y,x)
    spiral_potential = pt.spiral_potential(r, phi)
    ax[1][1].pcolormesh(x, y, spiral_potential, cmap="inferno")
    ax[1][1].set_xlim(-max_x, max_x)
    ax[1][1].set_ylim(-max_y, max_y)
    ax[1][1].set_box_aspect(1)