# METFI Field Simulation 2D (v0.2)
# Spatially extended nonlinear field model (wave-like + toroidal-inspired dynamics)

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Grid parameters
# -----------------------------

Nx, Ny = 100, 100
Lx, Ly = 10.0, 10.0

dx = Lx / Nx
dy = Ly / Ny

x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# -----------------------------
# Time parameters
# -----------------------------

dt = 0.01
T = 10.0
steps = int(T / dt)

# -----------------------------
# Physical parameters
# -----------------------------

c = 1.0          # propagation speed
gamma = 0.05     # damping
alpha = 1.0      # nonlinearity

# -----------------------------
# Initial condition (localized perturbation)
# -----------------------------

A = np.exp(-((X - Lx/2)**2 + (Y - Ly/2)**2))
A_prev = np.copy(A)

# -----------------------------
# Helper: Laplacian (finite differences)
# -----------------------------

def laplacian(Z):
    return (
        np.roll(Z, 1, axis=0) + np.roll(Z, -1, axis=0) +
        np.roll(Z, 1, axis=1) + np.roll(Z, -1, axis=1) -
        4 * Z
    ) / (dx * dy)

# -----------------------------
# Simulation loop
# -----------------------------

snapshots = []

for step in range(steps):
    lap = laplacian(A)
    
    # Wave-like update with damping and nonlinearity
    A_next = (
        2*A - A_prev
        + dt**2 * (c**2 * lap - gamma * (A - A_prev)/dt - alpha * A**3)
    )
    
    # Optional: noise (structured perturbation)
    noise = 0.01 * np.random.randn(Nx, Ny)
    A_next += noise
    
    # Update fields
    A_prev = A
    A = A_next
    
    # Store snapshots occasionally
    if step % 50 == 0:
        snapshots.append(A.copy())

# -----------------------------
# Visualization
# -----------------------------

plt.figure()
plt.imshow(A, extent=[0, Lx, 0, Ly], origin='lower')
plt.title("Final Field State A(x,y)")
plt.colorbar()
plt.show()

# -----------------------------
# Energy-like metric
# -----------------------------

energy = np.sum(A**2)
print("Final field energy:", energy)

# -----------------------------
# Collapse detection (spatial)
# -----------------------------

threshold = np.mean(A) + 3*np.std(A)
collapse_points = np.where(A > threshold)

print("Number of high-intensity points:", len(collapse_points[0]))
