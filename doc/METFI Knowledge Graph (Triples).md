# METFI Knowledge Graph (Triples)

## Nivel 1 → Nivel 2

GeomagneticVariation → EXPLAINED_BY → GeodynamoModel  
SeismicSignal → EXPLAINED_BY → NonlinearDynamics  
ElectromagneticInduction → EXPLAINED_BY → Magnetohydrodynamics  

---

## Nivel 2 → Nivel 3

GeodynamoModel → EXTENDED_BY → ToroidalFieldStructure  
Magnetohydrodynamics → EXTENDED_BY → InternalForcingMechanism  
NonlinearDynamics → EXTENDED_BY → SymmetryBreaking  

---

## Nivel 3 → Nivel 1 (retroacción)

SymmetryBreaking → INDUCES → SeismicSignal  
InternalForcingMechanism → INDUCES → GeomagneticVariation  
ToroidalFieldStructure → COUPLES_WITH → ElectromagneticInduction  

---

## Nivel 3 → Nivel 4

ToroidalFieldStructure → EMERGES_AS → EarthFieldMatrix  
GeoBioCoupling → EMERGES_AS → BioResonantSystem  
SymmetryBreaking → EMERGES_AS → CoherenceCollapseModel  

---

## Acoplamiento geo-bio

GeoBioCoupling → COUPLES_WITH → BioelectricalSignal  
BioelectricalSignal → EXPLAINED_BY → ResonantCavityModel  
