""" Module responsible for the definition of important functions and potentials """

# TODO: Add comments that explain the units of each constant.
# TODO: Add a symbolic version of the potential to be able to illustrate its form
# in the command line in a pretty way!
# TODO: Check on halo definition... It might have a mistake. Get reference from mathematica notebook.

# Import necessary modules
import numpy as np
import sympy as sp

# Define necessary quantities
# Global
G = 4.3009172706e-6
Omega_sp = 15.0

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

# Halo potential constants
r_h = 12.0
M_h0 = 10.7e10
gamma = 1.02
r_hmax = 100.0

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

# ============================================================================
# Symbolic definitions
# ============================================================================

r, z, phi, pr, pphi = sp.symbols('r z phi pr pphi', real=True)
# Disk potential
V_d = -(G * M_d)/sp.sqrt(r**2 + (a_d + sp.sqrt(z**2 + b_d**2))**2)
# Bulge potential
V_b = -(G * M_b)/sp.sqrt(r**2 + b_b**2)
# Halo potential
r_ratio = r/r_h
M_h = (M_h0 * (r_ratio**(gamma + 1.0)))/(1 + r_ratio**gamma)
V_h = (-G*M_h)/r + ((G*M_h0)/(gamma*r_h))*(-((gamma)/(1+ r_ratio**gamma)) + sp.log(1 + r_ratio)**gamma)
# Spiral Potential
cutoff = b_cut - c_cut*sp.atan((R_s0 - r))
kappa = 2.0/(r*sp.Abs(sp.sin(pitch_angle)))
khz = kappa*h_z
beta = (1.0 + khz + 0.3*(khz**2))/(1.0 + 0.3*khz)
e = sp.exp(-((r - r_0)/R_s))
V_sp = (4.0*np.pi*G*h_z*rho_0*C*e*sp.cos(2.0*(phi - (sp.log(r/r_0)/np.tan(pitch_angle)))))/(kappa*beta)
# Axisymmetric potential
V_ax = V_d + V_b
# Total potential
V_tot = V_ax + V_sp
# Hamiltonian definition
H_ax = (pr**2)/2.0 + (pphi**2)/(2*(r**2)) + V_ax
H = (pr**2)/2.0 + (pphi**2)/(2.0*(r**2)) - Omega_sp*pphi + V_ax + V_sp
DH_r = sp.diff(H, r)
DH_phi = sp.diff(H, phi)
DH_pr = sp.diff(H, pr)
DH_pphi = sp.diff(H, pphi)
DV_ax =sp.diff(V_ax, r)
omega = sp.sqrt((1/r)*DV_ax)
# Lambdification
axisymmetric_potential = sp.lambdify((r, z), V_ax, 'scipy')
axisymmetric_hamiltonian = sp.lambdify((r, z, pr, pphi), H_ax, 'scipy')
hamiltonian_dr = sp.lambdify((r, z, phi, pr, pphi), DH_r, 'scipy')
hamiltonian_dphi = sp.lambdify((r, z, phi, pr, pphi), DH_phi, 'scipy')
hamiltonian_dpr = sp.lambdify((r, z, phi, pr, pphi), DH_pr, 'scipy')
hamiltonian_dpphi = sp.lambdify((r, z, phi, pr, pphi), DH_pphi, 'scipy')
angular_velocity = sp.lambdify((r, z), omega, 'scipy')

"""# Define potentials
def disk_potential(r):
    Defines a Miyamoto-Nagai 2D Disk gravitational potential.
    return -(G * M_d)/np.sqrt(r**2 + (a_d + b_d)**2)
# Print indicative value
print("\nDisk Potential Indicative Value")
print("V_d(0)=",disk_potential(0))

def bulge_potential(r):
    Defines a Plummer 2D Bulge gravitational potential.
    return -(G * M_b)/np.sqrt(r**2 + b_b**2)
# Print indicative value
print("\nBulge Potential Indicative Value")
print("V_b(0)=", bulge_potential(0))

def spiral_potential(r, phi):
    Defines a spiral-shaped gravitational perturbation potential.
    cutoff = b_cut - c_cut*np.atan((R_s0 - r))
    kappa = 2.0/(r*np.abs(np.sin(pitch_angle)))
    khz = kappa*h_z
    beta = (1.0 + khz + 0.3*(khz**2))/(1.0 + 0.3*khz)
    exp = np.exp(-((r - r_0)/R_s))
    return (4.0*np.pi*G*h_z*rho_0*C*exp*np.cos(2.0*(phi - (np.log(r/r_0)/np.tan(pitch_angle)))))/(kappa*beta)

def hamiltonian(r, phi, pr, pphi):
    Definition of the hamiltonian
    return (pr**2)/2.0 + (pphi**2)/(2.0*(r**2)) - Omega_sp*pphi + disk_potential(r) + bulge_potential(r) + spiral_potential(r, phi)


# Print indicative value
print("\nSpiral Potential Indicative Value")
print("V_sp(1.0, 0.0)=", spiral_potential(1.0, 0.0))"""