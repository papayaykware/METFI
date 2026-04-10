{
  "nodes": [
    {"id": "GeomagneticVariation", "type": "ObservationalEntity", "level": 1},
    {"id": "SeismicSignal", "type": "ObservationalEntity", "level": 1},
    {"id": "GeodynamoModel", "type": "PhysicalInterpretation", "level": 2},
    {"id": "Magnetohydrodynamics", "type": "PhysicalInterpretation", "level": 2},
    {"id": "ToroidalFieldStructure", "type": "METFIHypothesis", "level": 3},
    {"id": "InternalForcingMechanism", "type": "METFIHypothesis", "level": 3},
    {"id": "SymmetryBreaking", "type": "METFIHypothesis", "level": 3},
    {"id": "GeoBioCoupling", "type": "METFIHypothesis", "level": 3},
    {"id": "EarthFieldMatrix", "type": "NarrativeFramework", "level": 4}
  ],
  "edges": [
    {"source": "GeomagneticVariation", "target": "GeodynamoModel", "relation": "EXPLAINED_BY"},
    {"source": "GeodynamoModel", "target": "ToroidalFieldStructure", "relation": "EXTENDED_BY"},
    {"source": "SymmetryBreaking", "target": "SeismicSignal", "relation": "INDUCES"},
    {"source": "ToroidalFieldStructure", "target": "EarthFieldMatrix", "relation": "EMERGES_AS"},
    {"source": "GeoBioCoupling", "target": "GeomagneticVariation", "relation": "COUPLES_WITH"}
  ]
}
