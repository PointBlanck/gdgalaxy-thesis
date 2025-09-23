import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import potentials as pt


# r = sp.symbols('r', real=True)
# V_d = -(pt.G * pt.M_d)/(sp.sqrt(r**2 + (pt.a_d + pt.b_d)**2))
# print(V_d)
# grad1_Vd = sp.diff(V_d, r)
# print(grad1_Vd)
# grad2_Vd = sp.diff(V_d, r, 2)
# print(grad2_Vd)
# den = (grad2_Vd + (1/r)*grad1_Vd)/(4.0*np.pi*pt.G)
# denlamb = sp.lambdify(r, den, "numpy")

r, z = np.meshgrid(np.linspace(0, 10, 1000), np.linspace(-10, 10, 10000))
rr = np.linspace(0, 10, 1000)
disk_potential = pt.disk_potential(r, z)
bulge_potential = pt.bulge_potential(rr)
total_potential = disk_potential + bulge_potential
# Calculate derivatives
print(np.shape(disk_potential[5000]))
disk_grad_r1 = np.gradient(disk_potential[5000], r[1] - r[0], axis=0)
disk_grad_r2 = np.gradient(disk_grad_r1, r[1] - r[0], axis=0)
disk_grad_z2 = np.gradient(np.gradient(disk_potential[:][500], z[1] - z[0], axis=0), z[1] - z[0], axis=0)
bulge_grad1 = np.gradient(bulge_potential, rr[1] - rr[0])
bulge_grad2 = np.gradient(bulge_grad1, rr[1] - rr[0])
density_disk = (disk_grad_r2 + (2.0*r**(-1))*disk_grad_r1 + disk_grad_z2.T)/(4.0*np.pi*pt.G)
density_bulge = (bulge_grad2 + (2.0*rr**(-1))*bulge_grad1)/(4.0*np.pi*pt.G)

# Plot the potentials
fig, ax = plt.subplots(layout="constrained")
ax.plot(r[:-1], density_disk[:-1])
ax.plot(rr[:-1], density_bulge[:-1])
ax.plot(rr[:-1], density_disk[:-1] + density_bulge[:-1])
ax.set_xlim(0, 10)
ax.set_ylim(-5.0e7, 10.0e7)
ax.set_box_aspect(1)
plt.show()