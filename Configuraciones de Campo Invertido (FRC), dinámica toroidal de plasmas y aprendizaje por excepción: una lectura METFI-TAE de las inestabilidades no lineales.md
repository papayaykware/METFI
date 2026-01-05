# Configuraciones de Campo Invertido (FRC), dinámica toroidal de plasmas y aprendizaje por excepción: una lectura METFI-TAE de las inestabilidades no lineales

![status](https://img.shields.io/badge/status-stable-darkgreen)
![theory](https://img.shields.io/badge/framework-METFI%20%7C%20TAE-blue)
![license](https://img.shields.io/badge/license-CC%20BY--NC--SA-lightgrey)
![discipline](https://img.shields.io/badge/domain-plasma%20physics%20%7C%20complex%20systems-purple)

---

> **Repositorio conceptual**: análisis transversal de configuraciones de campo invertido (FRC) desde los marcos METFI (Modelo Electromagnético Toroidal de Forzamiento Interno) y TAE (Teoría de Aprendizaje por Excepción).

---

## 📑 Table of Contents

* [Abstract](#abstract)
* [1. Introducción](#1-introducción)
* [2. Formación de FRC por theta-pinch](#2-formación-de-frc-por-theta-pinch)
* [3. Sobrecompresión e inestabilidad](#3-sobrecompresión-e-inestabilidad)
* [4. Lectura METFI de las FRC](#4-lectura-metfi-de-las-frc)
* [5. Aprendizaje por excepción en plasma (TAE)](#5-aprendizaje-por-excepción-en-plasma-tae)
* [6. Paralelismos bioelectromagnéticos](#6-paralelismos-bioelectromagnéticos)
* [7. Programas de seguimiento](#7-programas-de-seguimiento)
* [8. Implicaciones epistemológicas](#8-implicaciones-epistemológicas)
* [Conclusiones](#conclusiones)
* [Resumen ejecutivo](#resumen-ejecutivo)
* [Referencias comentadas](#referencias-comentadas)
* [Notebooks reproducibles](#notebooks-reproducibles)

---

## Abstract

Las configuraciones de campo invertido (Field-Reversed Configurations, FRC) constituyen estados autoorganizados del plasma magnetizado caracterizados por topologías toroidales cerradas y ausencia de bobinas internas. Simulaciones cinéticas de alta resolución muestran que, bajo compresión theta-pinch, estas estructuras alcanzan regímenes de coherencia electromagnética crítica, seguidos de transiciones abruptas hacia inestabilidad cuando el forzamiento interno supera la capacidad topológica del sistema. Este documento propone una interpretación rigurosa de dichos fenómenos desde los marcos METFI y TAE, entendiendo la inestabilidad no como fallo, sino como evento de aprendizaje físico inducido por excepción.

---

## 1. Introducción

Las FRC representan un caso límite de coherencia toroidal sostenida dinámicamente. A diferencia de tokamaks o stellarators, el campo no es impuesto sino emergente, lo que las convierte en laboratorios privilegiados para estudiar pérdida de simetría, colapso no lineal y reorganización topológica.

---

## 2. Formación de FRC por theta-pinch

La compresión theta-pinch induce corrientes azimutales que generan inversión del campo axial. El resultado es una geometría cerrada donde plasma y campo se co-sostienen.

> **Insight METFI**: estabilidad basada en circulación interna, no en restricción externa.

---

## 3. Sobrecompresión e inestabilidad

Cuando el sistema es forzado más allá de su umbral geométrico:

* emergen modos no axisimétricos,
* se pierde coherencia de fase,
* ocurre reconexión rápida,
* se libera energía de forma explosiva.

---

## 4. Lectura METFI de las FRC

METFI describe sistemas toroidales sometidos a forzamiento interno donde la pérdida de simetría induce efectos no lineales globales. Las FRC reproducen este patrón a escala de laboratorio:

* topología toroidal cerrada,
* auto-sostenimiento electromagnético,
* colapso abrupto al cruzar umbrales geométricos.

---

## 5. Aprendizaje por excepción en plasma (TAE)

TAE formaliza la inestabilidad como transición de régimen. El plasma "aprende" cuando las reglas locales dejan de ser válidas.

---

## 6. Paralelismos bioelectromagnéticos

Campos toroidales acoplados en sistemas biológicos (cerebro–corazón–neuroentérico) muestran dinámicas análogas:

* coherencia funcional,
* forzamiento creciente,
* pérdida de simetría,
* reorganización abrupta.

METFI no iguala escalas, identifica **principios geométricos compartidos**.

---

## 7. Programas de seguimiento

### 7.1 Métricas geométricas

* Conectividad de líneas de campo.
* Desviación angular acumulada.
* Evolución de superficies de flujo.

### 7.2 Indicadores de fase

* Coherencia espectral.
* Retardos temporales internos.
* Correlaciones campo–corriente.

### 7.3 Estudios multi-escala

* Barridos de resolución.
* Comparación MHD ideal vs cinético.
* Histéresis tras colapso controlado.

---

## 8. Implicaciones epistemológicas

Las simulaciones FRC muestran que la estabilidad es una fase transitoria. Los sistemas complejos revelan su estructura profunda solo bajo excepción.

> **Principio clave**: sin colapso no hay conocimiento estructural.

---

## Conclusiones

Las FRC constituyen un modelo físico excepcional para estudiar coherencia toroidal, pérdida de simetría y aprendizaje inducido por excepción. METFI y TAE proporcionan un marco coherente para interpretar estos fenómenos más allá del paradigma incrementalista.

---

## Resumen ejecutivo

* Las FRC son estructuras electromagnéticas autoorganizadas.
* La estabilidad depende de la geometría, no solo de la energía.
* La sobrecompresión induce colapso topológico.
* METFI explica la pérdida de simetría toroidal.
* TAE interpreta la inestabilidad como aprendizaje.
* La excepción es informativa, no patológica.

---

## Referencias comentadas

<details>
<summary><strong>Taylor, J.B. (1974)</strong> – Relaxation of toroidal plasma</summary>
DOI: 10.1103/PhysRevLett.33.1139  
Introduce el concepto de relajación topológica y campos invertidos.
</details>

<details>
<summary><strong>Freidberg, J.P.</strong> – Ideal MHD</summary>
Libro fundamental sobre límites del enfoque ideal frente a no linealidades.
</details>

<details>
<summary><strong>Loureiro, N.F. et al.</strong> – Magnetic reconnection</summary>
DOI: 10.1088/0034-4885/77/12/125901  
Análisis riguroso de reconexión sin sesgo industrial.
</details>

<details>
<summary><strong>Rostoker & Binderbauer</strong> – FRC compact concepts</summary>
Exploración física de FRC más allá de marketing tecnológico.
</details>

---

## Notebooks reproducibles

* [`/notebooks/FRC_topology_analysis.ipynb`](./notebooks/FRC_topology_analysis.ipynb)
* [`/notebooks/Phase_coherence_metrics.ipynb`](./notebooks/Phase_coherence_metrics.ipynb)
* [`/notebooks/METFI_toroidal_symmetry.ipynb`](./notebooks/METFI_toroidal_symmetry.ipynb)

---

> **Autor conceptual**: framework METFI–TAE
> Documento diseñado para lectura técnica, revisión crítica y extensión reproducible.
