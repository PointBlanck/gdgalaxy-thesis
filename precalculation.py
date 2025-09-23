""" Module responsible for the pre-calculation inspection of the model. """

# Import necessary modules
import numpy as np
import matplotlib.pyplot as plt
import potentials as pt

# Plot mass density from potentials
def plot_potentials(max_r, N_r, N_phi):
    """ Plots mass density for the disk, bulge and total axisymmetric potentials. """
    r = np.linspace(0.001, max_r, N_r)
    disk_potential = pt.disk_potential(r)
    bulge_potential = pt.bulge_potential(r)

    # Calculate derivatives
    disk_grad1 = np.gradient(disk_potential, r[1] - r[0])
    disk_grad2 = np.gradient(disk_grad1, r[1] - r[0])
    bulge_grad1 = np.gradient(bulge_potential, r[1] - r[0])
    bulge_grad2 = np.gradient(bulge_grad1, r[1] - r[0])
    density_disk = (disk_grad2 + ((1.0*disk_grad1)/r))/(4.0*np.pi*pt.G)
    density_bulge = (bulge_grad2 + ((2.0*bulge_grad1)/r))/(4.0*np.pi*pt.G)


    phi = np.linspace(0.001, 2*np.pi, N_phi)
    fig, ax = plt.subplots(2,2,layout="constrained")
    ax[0][0].plot(r[:-2], np.log10(density_disk[:-2]), label="Disk Density")
    ax[0][0].plot(r[:-2], np.log10(density_bulge[:-2]), label="Bulge Density")
    ax[0][0].plot(r[:-2], np.log10(density_disk[:-2] + density_bulge[:-2]), label="Total Density")
    ax[0][0].set_xlim(0, 5)
    ax[0][0].set_ylim(7.0,10.0)
    ax[0][0].set_box_aspect(1)
    ax[0][0].legend()
    plt.show()