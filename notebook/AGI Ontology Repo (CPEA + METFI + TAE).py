# =========================
# AGI Ontology Repo (CPEA + METFI + TAE)
# Predictive + Error-Driven Ontology (TAE Enabled)
# =========================

# NEW MODULE: ontology/predictive_engine.py

import random

class PredictiveEngine:
    def __init__(self):
        self.memory = {}

    def predict_icp(self, context):
        # simple baseline prediction (can be replaced by ML later)
        if "last_icp" in self.memory:
            return self.memory["last_icp"] + random.uniform(-0.05, 0.05)
        return 0.5

    def update_memory(self, icp):
        self.memory["last_icp"] = icp

# =========================
# UPDATED ontology/adaptive_layer.py
# =========================
class AdaptiveOntology:
    def __init__(self, graph):
        self.graph = graph

    def reinforce(self, path, error):
        for src, dst in path:
            if self.graph.graph.has_edge(src, dst):
                if error < 0.1:
                    self.graph.graph[src][dst]['weight'] += 0.02
                else:
                    self.graph.graph[src][dst]['weight'] -= 0.02

    def prune(self, threshold=0.1):
        to_remove = []
        for u, v, data in self.graph.graph.edges(data=True):
            if data['weight'] < threshold:
                to_remove.append((u, v))
        for edge in to_remove:
            self.graph.graph.remove_edge(*edge)

    def decay(self):
        for u, v, data in self.graph.graph.edges(data=True):
            data['weight'] *= 0.995

# =========================
# UPDATED src/system_loop.py
# =========================
from ontology.graph_builder import OntologyGraph
from ontology.reasoning_engine import OntologyReasoner
from ontology.dynamics_engine import DynamicsEngine
from ontology.adaptive_layer import AdaptiveOntology
from ontology.predictive_engine import PredictiveEngine
from src.icp import compute_icp
from src.eeg_simulator import get_eeg
from src.metfi_simulator import METFISimulator

class SystemLoop:
    def __init__(self):
        self.ontology = OntologyGraph(
            "ontology/concepts.yaml",
            "ontology/relations.yaml"
        )
        self.reasoner = OntologyReasoner(self.ontology)
        self.dynamics = DynamicsEngine()
        self.adaptive = AdaptiveOntology(self.ontology)
        self.predictor = PredictiveEngine()
        self.metfi = METFISimulator()
        self.threshold = 0.5

    def run(self, steps=30):
        for step in range(steps):
            print(f"\n--- Step {step} ---")

            # EEG input
            eeg = get_eeg()
            icp_real = compute_icp(eeg)

            # Prediction
            icp_pred = self.predictor.predict_icp(context=None)

            # Error computation (TAE core)
            error = abs(icp_pred - icp_real)

            print(f"ICP real: {icp_real:.3f}")
            print(f"ICP pred: {icp_pred:.3f}")
            print(f"Prediction error: {error:.3f}")

            # Update predictor memory
            self.predictor.update_memory(icp_real)

            # METFI simulation
            field = self.metfi.step()
            print("Toroidal Field:", field)

            # ECDO event
            ecdo = self.dynamics.check_ecdo()
            print("ECDO Triggered:", ecdo)

            # Ontological reasoning
            impacts = self.reasoner.propagate_signal("icp", depth=2)
            print("Impacts:", impacts)

            # Adaptive learning (TAE)
            self.adaptive.reinforce(impacts, error)

            # Structural pruning
            self.adaptive.prune()

            # Natural decay
            self.adaptive.decay()

# =========================
# run.py remains unchanged
# =========================
