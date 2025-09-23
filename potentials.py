""" Module responsible for the definition of important functions and potentials """

# TODO: Add comments that explain the units of each constant.
# TODO: Add a symbolic version of the potential to be able to illustrate its form
# in the command line in a pretty way!

# Import necessary modules
import numpy as np
import sympy as sp

# Define necessary quantities
# Global
G = 4.3009172706e-6

# Disk potential constants
M_d = 8.56e10
a_d = 5.3
b_d = 0.25

# Print constants
print("\nConstants of the model:")
print("G=",G)
print("M_d=", M_d)
print("a_d, b_d=",a_d,b_d)

# Bulge potential constants
M_b = 5.0e10
b_b = 1.5
print("M_b=",M_b)
print("\nb_b=",b_b)

# Spiral potential constants
h_z = 0.18
rho_0 = 5.0e7
b_cut = 0.474
c_cut = 0.335
C = 8.0/(3.0*np.pi)
R_s = 7.0
R_s0 = 6.0
r_0 = 8.0
a = -13
pitch_angle = (a*np.pi)/180.0
print("h_z=",h_z)
print("b_cut, c_cut",b_cut, c_cut)
print("C=", C)
print("R_s=",R_s)
print("a=", a)
print("Perturbation Amplitude:",rho_0)


# Define potentials
def disk_potential(r):
    """ Defines a Miyamoto-Nagai 2D Disk gravitational potential. """
    return -(G * M_d)/np.sqrt(r**2 + (a_d + b_d)**2)
# Print indicative value
print("\nDisk Potential Indicative Value")
print("V_d(0)=",disk_potential(0))

def bulge_potential(r):
    """ Defines a Plummer 2D Bulge gravitational potential. """
    return -(G * M_b)/np.sqrt(r**2 + b_b**2)
# Print indicative value
print("\nBulge Potential Indicative Value")
print("V_b(0)=", bulge_potential(0))

def spiral_potential(r, phi):
    """ Defines a spiral-shaped gravitational perturbation potential. """
    cutoff = b_cut - c_cut*np.atan((R_s0 - r))
    kappa = 2.0/(r*np.abs(np.sin(pitch_angle)))
    khz = kappa*h_z
    beta = (1.0 + khz + 0.3*(khz**2))/(1.0 + 0.3*khz)
    exp = np.exp(-((r - r_0)/R_s))
    return (4.0*np.pi*G*h_z*rho_0*C*exp*np.cos(2.0*(phi - (np.log(r/r_0)/np.tan(pitch_angle)))))/(kappa*beta)

# Print indicative value
print("\nSpiral Potential Indicative Value")
print("V_sp(1.0, 0.0)=", spiral_potential(1.0, 0.0))