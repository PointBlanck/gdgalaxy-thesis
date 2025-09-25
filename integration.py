""" Module containing code pertaining to computation and integration of the physical system. """

# TODO: Check the details with those on Mathematica for integrate function


import numpy as np
import scipy.integrate as sc
import matplotlib.pyplot as plt
import potentials as pt



def system(t, y):
    """ Define the system that needs to be integrated. """
    r, z, phi, pr, pphi= y
    drdt = pt.hamiltonian_dpr(r, z, phi, pr, pphi)
    dphidt = pt.hamiltonian_dpphi(r, z, phi, pr, pphi)
    dprdt = -pt.hamiltonian_dr(r, z, phi, pr, pphi)
    dpphidt = -pt.hamiltonian_dphi(r, z, phi, pr, pphi)
    return np.array([drdt, dphidt, dprdt, dpphidt])

def event(t, y):
    """ Define an event to track during integration. """
    return np.cos(y[1])

def integrate():
    """ Integrates the system for the specified period of time. """
    z = 0.0
    fig, ax = plt.subplots(layout="constrained")
    event.direction = -1
    lines = []
    r_c = float(input("Integration: Input r_c: "))
    pphi_c = (r_c**2)*pt.angular_velocity(r_c, z)
    energy = pt.axisymmetric_hamiltonian(r_c, z, 0.0, pphi_c)
    t0, N = input("Integration: Input t0, N: ").split(",")
    t0 = float(t0)
    N = int(N)
    ksi0, pksi0 = input("Integration: Input ksi0, pksi0: ").split(",")
    ksi0 = float(ksi0)
    pksi0 = float(pksi0)
    method = input("Integration: Input preffered integration method.")
    r0 = r_c - ksi0
    phi0 = np.pi/2.0
    pr0 = -pksi0
    pphi0 = (r0**2)*pt.Omega_sp + r0*np.sqrt((r0**2)*(pt.Omega_sp**2) - (pr0**2) - 2*pt.axisymmetric_potential(r0, z) + 2*energy)
    y0 = [r0, z, phi0, pr0, pphi0]
    sol = sc.solve_ivp(system,(t0,N*pt.angular_velocity(r_c, z)), y0, rtol = 1e-6, atol=1e-6, dense_output=True, method="RK45")
    lines.append(ax.scatter(r_c - sol.y_events[1], -sol.y_events[2], c="b", s=20))
    plt.show()

