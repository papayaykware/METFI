# METFI — Solar–Toroidal Coupling Model  
## Periodic External Forcing of a Nonlinear Terrestrial Electromagnetic Toroid

---

[![Status](https://img.shields.io/badge/status-theoretical_framework-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Field](https://img.shields.io/badge/field-Magnetohydrodynamics-orange)]()
[![Model](https://img.shields.io/badge/model-Nonlinear_Dynamics-red)]()
[![Reproducibility](https://img.shields.io/badge/reproducibility-notebooks_available-brightgreen)]()

---

# 📚 Table of Contents

- [1. Conceptual Overview](#1-conceptual-overview)
- [2. Domain Definition](#2-domain-definition)
- [3. Governing Equations](#3-governing-equations)
- [4. Toroidal Decomposition](#4-toroidal-decomposition)
- [5. Energetic Functional](#5-energetic-functional)
- [6. Internal Symmetry Breaking (ECDO)](#6-internal-symmetry-breaking-ecdo)
- [7. Solar Periodic Forcing](#7-solar-periodic-forcing)
- [8. Reduced Nonlinear Amplitude Model](#8-reduced-nonlinear-amplitude-model)
- [9. Parametric Resonance & Stability](#9-parametric-resonance--stability)
- [10. Phase Synchronization Dynamics](#10-phase-synchronization-dynamics)
- [11. Energy Transfer Formalism](#11-energy-transfer-formalism)
- [12. Bifurcation Structure](#12-bifurcation-structure)
- [13. Reproducible Notebooks](#13-reproducible-notebooks)
- [14. References](#14-references)

---

# 1. Conceptual Overview

> [!NOTE]
> The METFI framework models Earth as a self-organized electromagnetic toroidal system subject to internal forcing and external periodic modulation.

The terrestrial magnetic structure is treated as a nonlinear toroidal attractor governed by magnetohydrodynamic (MHD) induction. Solar variability acts as an external periodic driver capable of modulating stability, phase coherence, and energy transfer.

---

# 2. Domain Definition

We define a toroidal domain  
\[
\Omega \subset \mathbb{R}^3
\]

Using toroidal coordinates:

- \( \rho \) — minor radius  
- \( \theta \) — poloidal angle  
- \( \phi \) — toroidal angle  

Primary fields:

- Magnetic field \( \mathbf{B}(\mathbf{x},t) \)  
- Velocity field \( \mathbf{v}(\mathbf{x},t) \)  
- Current density \( \mathbf{J}(\mathbf{x},t) \)

---

# 3. Governing Equations

## Maxwell (Quasi-static approximation)

\[
\nabla \cdot \mathbf{B} = 0
\]

\[
\nabla \times \mathbf{B} = \mu_0 \mathbf{J}
\]

\[
\mathbf{J} = \sigma(\mathbf{E} + \mathbf{v} \times \mathbf{B})
\]

---

## MHD Induction Equation

\[
\frac{\partial \mathbf{B}}{\partial t}
=
\nabla \times (\mathbf{v} \times \mathbf{B})
+
\eta \nabla^2 \mathbf{B}
\]

where:

\[
\eta = \frac{1}{\mu_0 \sigma}
\]

---

# 4. Toroidal Decomposition

\[
\mathbf{B} = \mathbf{B}_T + \mathbf{B}_P
\]

Toroidal component:

\[
\mathbf{B}_T = B_\phi(\rho,\theta,t)\,\hat{\phi}
\]

Poloidal component:

\[
\mathbf{B}_P = \nabla \times (A_\phi \hat{\phi})
\]

---

# 5. Energetic Functional

Magnetic energy:

\[
\mathcal{E}
=
\int_\Omega
\frac{|\mathbf{B}|^2}{2\mu_0}
\, dV
\]

Stability condition:

\[
\delta \mathcal{E} = 0
\]

---

# 6. Internal Symmetry Breaking (ECDO)

We introduce anisotropic perturbation:

\[
\mathbf{v}
=
\mathbf{v}_0
+
\epsilon \mathbf{v}_1(\theta,\phi)
\]

If:

\[
\epsilon R_m \gtrsim 1
\]

then axial symmetry breaks and nonlinear mode transfer occurs.

Magnetic Reynolds number:

\[
R_m = \frac{V L}{\eta}
\]

---

# 7. Solar Periodic Forcing

External solar magnetic field:

\[
\mathbf{B}_{ext}(t)
=
B_s \cos(\omega_s t)\hat{e}_z
\]

Total field:

\[
\mathbf{B}_{tot} = \mathbf{B}_{int} + \mathbf{B}_{ext}
\]

Modified induction equation:

\[
\frac{\partial \mathbf{B}_{int}}{\partial t}
=
\nabla \times (\mathbf{v} \times \mathbf{B}_{int})
+
\nabla \times (\mathbf{v} \times \mathbf{B}_{ext})
+
\eta \nabla^2 \mathbf{B}_{int}
\]

---

# 8. Reduced Nonlinear Amplitude Model

Projecting onto dominant toroidal mode:

\[
\mathbf{B}_{int} \approx A(t)\mathbf{B}_0
\]

Reduced equation:

\[
\frac{dA}{dt}
=
\alpha A
-
\beta A^3
+
\gamma B_s \cos(\omega_s t)
\]

This is a nonlinear forced oscillator.

---

# 9. Parametric Resonance & Stability

Parametric form:

\[
\frac{dA}{dt}
=
(\alpha + \epsilon \cos \omega_s t)A
-
\beta A^3
\]

Resonance condition:

\[
\omega_s \approx \omega_0
\]

Instability threshold:

\[
\epsilon > \epsilon_c
\]

---

# 10. Phase Synchronization Dynamics

Phase difference:

\[
\Delta\phi = \phi_{int} - \phi_s
\]

Evolution equation:

\[
\frac{d\Delta \phi}{dt}
=
\omega_0 - \omega_s
-
K \sin(\Delta \phi)
\]

Synchronization occurs if:

\[
|\omega_0 - \omega_s| < K
\]

---

# 11. Energy Transfer Formalism

Magnetic energy variation:

\[
\frac{dE}{dt}
=
\int
\mathbf{B}_{int}\cdot
\nabla \times (\mathbf{v} \times \mathbf{B}_{ext})
\, dV
-
\eta \int |\nabla \times \mathbf{B}|^2 dV
\]

Positive average implies net solar pumping.

---

# 12. Bifurcation Structure

The reduced system exhibits:

- Supercritical pitchfork bifurcation
- Limit cycles
- Phase locking regimes
- Chaotic windows (for strong forcing)

> [!WARNING]
> Nonlinear amplification depends critically on internal conductivity and solar spectral distribution.

---

# 13. Reproducible Notebooks

📂 `notebooks/`

- `01_linear_stability.ipynb`
- `02_forced_nonlinear_oscillator.ipynb`
- `03_parametric_resonance_scan.ipynb`
- `04_phase_synchronization_model.ipynb`

Each notebook includes:

- Numerical integration (Runge–Kutta 4)
- Bifurcation diagrams
- Phase portraits
- Energy evolution plots

---

# 14. References

<details>
<summary><strong>Maxwell & MHD Foundations</strong></summary>

- Alfvén, H. (1942). *Existence of Electromagnetic-Hydrodynamic Waves*. Nature.  
  DOI: https://doi.org/10.1038/150405d0  

- Moffatt, H.K. (1978). *Magnetic Field Generation in Electrically Conducting Fluids*.  
  Cambridge University Press.

</details>

<details>
<summary><strong>Solar–Terrestrial Coupling</strong></summary>

- Dungey, J. (1961). *Interplanetary Magnetic Field and the Auroral Zones*.  
  Phys. Rev. Lett.  
  DOI: https://doi.org/10.1103/PhysRevLett.6.47  

- Parker, E.N. (1958). *Dynamics of the Interplanetary Gas and Magnetic Fields*.  
  Astrophysical Journal.  
  DOI: https://doi.org/10.1086/146579  

</details>

<details>
<summary><strong>Nonlinear Dynamics</strong></summary>

- Landau, L. (1944). *On the Problem of Turbulence*.  
- Strogatz, S. (2015). *Nonlinear Dynamics and Chaos*.  

</details>

---

# Summary

- Earth modeled as nonlinear electromagnetic toroid  
- Solar forcing introduced as periodic external driver  
- Stability governed by MHD induction  
- Resonance and synchronization possible  
- Bifurcation structure defines transition regimes  
- Framework consistent with classical electromagnetism  

---

© Conceptual Framework — METFI
