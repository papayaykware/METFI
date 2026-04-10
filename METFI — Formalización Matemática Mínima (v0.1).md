# METFI — Formalización Matemática Mínima (v0.1)

## 1. Variables y parámetros clave

### 🔹 Geometría (toroide)

* ( R ): radio mayor (centro del toroide al centro del tubo)
* ( r ): radio menor (radio del tubo)
* ( \theta, \phi ): coordenadas angulares

Parametrización estándar:

[
x = (R + r\cos\theta)\cos\phi
]
[
y = (R + r\cos\theta)\sin\phi
]
[
z = r\sin\theta
]

---

### 🔹 Campos físicos

* ( \mathbf{E}(\mathbf{x}, t) ): campo eléctrico
* ( \mathbf{B}(\mathbf{x}, t) ): campo magnético
* ( \mathbf{J}(\mathbf{x}, t) ): densidad de corriente
* ( \rho(\mathbf{x}, t) ): densidad de carga

---

### 🔹 Parámetros del medio

* ( \epsilon ): permitividad efectiva (no homogénea)
* ( \mu ): permeabilidad efectiva
* ( \sigma ): conductividad

👉 En METFI: estos parámetros **no son constantes**, sino funciones espaciales y posiblemente dependientes de frecuencia:
[
\epsilon = \epsilon(\mathbf{x}, \omega)
]

---

### 🔹 Variables emergentes clave (METFI)

* ( A(t) ): amplitud global del modo toroidal dominante
* ( \phi(t) ): fase global del sistema
* ( \omega_0 ): frecuencia natural del toroide
* ( \gamma ): factor de disipación
* ( \kappa ): acoplamiento interno (núcleo-manto)

---

## 2. Ecuaciones núcleo (nivel mínimo viable)

### 🔹 Base electromagnética

Se parte de las ecuaciones de Ecuaciones de Maxwell:

[
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon}
]
[
\nabla \cdot \mathbf{B} = 0
]
[
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
]
[
\nabla \times \mathbf{B} = \mu \mathbf{J} + \mu\epsilon \frac{\partial \mathbf{E}}{\partial t}
]

---

### 🔹 Reducción a modo dominante (aproximación METFI)

Se proyecta el sistema a un **modo toroidal resonante dominante**:

[
A(t) = \int_{\text{toroide}} \mathbf{E} \cdot \psi(\mathbf{x}) , dV
]

donde ( \psi(\mathbf{x}) ) es la función propia del modo.

---

### 🔹 Dinámica efectiva (oscilador no lineal)

Aquí está el núcleo operativo del modelo:

\frac{d^2 A}{dt^2} + \gamma \frac{dA}{dt} + \omega_0^2 A + \alpha A^3 = \kappa F(t)

---

### Interpretación:

* ( \omega_0^2 A ): restauración (estructura toroidal)

* ( \gamma \dot{A} ): disipación interna

* ( \alpha A^3 ): no linealidad → clave para:

  * bifurcaciones
  * histéresis
  * colapso

* ( \kappa F(t) ): forzamiento externo/interno (solar, interno, etc.)

---

## 3. Definición operativa de “colapso resonante”

En este marco:

👉 **Colapso = transición no lineal abrupta del sistema**

Condición simplificada:

[
\frac{dA}{dt} \rightarrow \text{discontinuidad o divergencia local}
]

O más físicamente:

* Pérdida de estabilidad del atractor
* Cambio de régimen:

  * estable → caótico
  * oscilatorio → amortiguado crítico
  * coherente → desfasado

---

### 🔹 Indicador práctico (simulación)

Define:

[
C(t) = A(t)^2 + \left(\frac{dA}{dt}\right)^2
]

👉 Si ( C(t) ) presenta:

* picos abruptos
* cambio de régimen espectral

→ tienes candidato a ECDO

---

## 4. Supuestos explícitos (muy importante)

Este bloque es crítico para credibilidad:

### 🔸 Geofísicos

* Núcleo modelado como **medio electromagnético efectivo**
* Geometría aproximada: toroide (no esférica ideal)
* Desacoplamiento núcleo-manto posible

### 🔸 Electromagnéticos

* Existencia de modos resonantes globales
* Dominancia de un modo toroidal principal
* No linealidad relevante a escala planetaria

### 🔸 Simplificaciones

* Reducción a 1 grado de libertad (A(t))
* Homogeneización parcial del medio
* Ignorar turbulencia completa (fase 1)

---

## 5. Estructura de repositorio sugerida

```
models/
│
├── metfi_core_equations.md
├── metfi_assumptions.md
├── metfi_parameters.yaml
│
├── notebooks/
│   └── metfi_simplified_sim.ipynb
│
└── src/
    ├── geometry.py
    ├── field_modes.py
    ├── dynamics.py
    └── metrics.py
```

---

## 6. Notebook mínimo (concepto)

### 🔹 Modelo de juguete

Sistema:

[
\frac{d^2 A}{dt^2} + \gamma \frac{dA}{dt} + \omega_0^2 A + \alpha A^3 = F_0 \sin(\omega t)
]

---

### 🔹 Qué debes mostrar

1. Evolución de ( A(t) )
2. Espacio de fases:

   * ( A ) vs ( \dot{A} )
3. Barrido de frecuencia:

   * resonancia
   * salto no lineal
4. Identificación de colapso:

   * transición abrupta

---

## 7. Siguiente nivel (clave estratégica)

Una vez esto funcione:

### 🔸 Extensión natural

* Campo espacial:
  [
  A \rightarrow A(\mathbf{x}, t)
  ]

* Tipo ecuación:

[
\frac{\partial^2 A}{\partial t^2} = c^2 \nabla^2 A - \gamma \frac{\partial A}{\partial t} - \alpha A^3
]

---

### 🔸 Acoplamiento núcleo–manto

Sistema de dos osciladores:

[
A_c, A_m
]

con:

[
\dot{A}_c \sim \kappa (A_m - A_c)
]

---

## 8. Valor real de esta formalización

Esto ya permite:

✔ Simulación numérica inmediata
✔ Crítica científica concreta (ya no es abstracto)
✔ Comparación con sistemas conocidos:

* resonadores no lineales
* plasma confinado
* osciladores tipo Duffing
