# METFI Ontology v0.1

## Clases principales

### C1: ObservationalEntity
Definición: Fenómeno empírico medible y reproducible.

Subclases:
- GeomagneticVariation
- SeismicSignal
- ElectromagneticInduction
- BioelectricalSignal

---

### C2: PhysicalInterpretation
Definición: Modelo explicativo compatible con física estándar.

Subclases:
- GeodynamoModel
- Magnetohydrodynamics
- ResonantCavityModel
- NonlinearDynamics

---

### C3: METFIHypothesis
Definición: Extensión teórica no validada dentro del modelo METFI.

Subclases:
- ToroidalFieldStructure
- InternalForcingMechanism
- SymmetryBreaking
- GeoBioCoupling

---

### C4: NarrativeFramework
Definición: Constructo conceptual derivado.

Subclases:
- EarthFieldMatrix
- BioResonantSystem
- CoherenceCollapseModel

---

## Relaciones (Relational Properties)

### R1: OBSERVED_AS
Dominio: ObservationalEntity  
Rango: PhysicalInterpretation  

---

### R2: EXPLAINED_BY
Dominio: ObservationalEntity  
Rango: PhysicalInterpretation  

---

### R3: EXTENDED_BY
Dominio: PhysicalInterpretation  
Rango: METFIHypothesis  

---

### R4: EMERGES_AS
Dominio: METFIHypothesis  
Rango: NarrativeFramework  

---

### R5: COUPLES_WITH
Dominio: METFIHypothesis  
Rango: ObservationalEntity  

---

### R6: INDUCES
Dominio: METFIHypothesis  
Rango: ObservationalEntity  

---

## Atributos clave

- certainty_level: {1,2,3,4}
- temporal_scale: {instant, short, long}
- spatial_scale: {local, regional, global}
- coupling_strength: float [0,1]
