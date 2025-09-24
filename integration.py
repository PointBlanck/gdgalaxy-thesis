""" Module containing code pertaining to computation and integration of the physical system. """

import numpy as np
import sympy as sp
import scipy as sc
import potentials as pt

r, phi, pr, pphi = sp.symbols('r phi pr pphi', real=True)
V_d = -(pt.G * pt.M_d)/sp.sqrt(r**2 + (pt.a_d + pt.b_d)**2)
V_b = -(pt.G * pt.M_b)/sp.sqrt(r**2 + pt.b_b**2)
cutoff = pt.b_cut - pt.c_cut*sp.atan((pt.R_s0 - r))
kappa = 2.0/(r*sp.Abs(sp.sin(pt.pitch_angle)))
khz = kappa*pt.h_z
beta = (1.0 + khz + 0.3*(khz**2))/(1.0 + 0.3*khz)
e = sp.exp(-((r - pt.r_0)/pt.R_s))
V_sp = (4.0*np.pi*pt.G*pt.h_z*pt.rho_0*pt.C*e*sp.cos(2.0*(phi - (sp.log(r/pt.r_0)/np.tan(pt.pitch_angle)))))/(kappa*beta)
V_ax = V_d + V_b
V_tot = V_ax + V_sp
H = (pr**2)/2.0 + (pphi**2)/(2.0*(r**2)) - pt.Omega_sp*pphi + V_ax + V_sp
DH_r = sp.diff(H, r)
DH_phi = sp.diff(H, phi)
DH_pr = sp.diff(H, pr)
DH_pphi = sp.diff(H, pphi)
hamiltonian_dr = sp.lambdify((r, phi, pr, pphi), DH_r, 'scipy')
hamiltonian_dphi = sp.lambdify((r, phi, pr, pphi), DH_phi, 'scipy')
hamiltonian_dpr = sp.lambdify((r, phi, pr, pphi), DH_pr, 'scipy')
hamiltonian_dpphi = sp.lambdify((r, phi, pr, pphi), DH_pphi, 'scipy')

def system(t, y):
    """ Define the system that needs to be integrated. """
    r, phi, pr, pphi= y
    drdt = hamiltonian_dpr(r, phi, pr, pphi)
    dphidt = hamiltonian_dpphi(r, phi, pr, pphi)
    dprdt = -hamiltonian_dr(r, phi, pr, pphi)
    dpphidt = -hamiltonian_dphi(r, phi, pr, pphi)
    return np.array([drdt, dphidt, dprdt, dpphidt])

def integrate():
    pass
