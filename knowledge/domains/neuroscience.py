"""
Neuroscience Domain
===================
Neuroscience knowledge domain with META 50/50 equilibrium.
Fundamental duality: Excitation/Inhibition (neural signaling balance).
"""

from typing import Any

from core.equilibrium import MetaEquilibrium
from knowledge.domains.base import (
    ConceptType,
    KnowledgeDomain,
    RelationType,
)
from models.domain import DomainType


class NeuroscienceDomain(KnowledgeDomain):
    """
    Neuroscience knowledge domain.

    Fundamental Duality: Excitation / Inhibition
    - Excitation: Activating signals, depolarization, action potentials
    - Inhibition: Suppressing signals, hyperpolarization, signal dampening

    Secondary Dualities:
    - Sensory / Motor
    - Central / Peripheral
    - Conscious / Unconscious
    """

    def __init__(self, meta_equilibrium: MetaEquilibrium | None = None):
        super().__init__(
            name="Neuroscience",
            domain_type=DomainType.FUNDAMENTAL,
            description="The study of the nervous system, brain, and neural function",
            meta_equilibrium=meta_equilibrium,
        )

    def _initialize_duality(self) -> None:
        """Initialize Excitation/Inhibition duality."""
        self._domain.set_duality(
            positive_name="excitation",
            positive_value=50,
            negative_name="inhibition",
            negative_value=50,
            duality_name="neuroscience_duality",
        )
        self._domain.activate()

    def _initialize_axioms(self) -> None:
        """Initialize fundamental neuroscience principles."""
        principles = [
            (
                "Neuron Doctrine",
                "The nervous system is composed of individual cells called neurons",
            ),
            (
                "All-or-None Principle",
                "Action potentials fire fully or not at all",
            ),
            (
                "Dale's Principle",
                "A neuron releases the same neurotransmitter(s) at all its synapses",
            ),
            (
                "Synaptic Plasticity",
                "Synaptic strength can be modified by experience",
            ),
            (
                "Hebbian Learning",
                "Neurons that fire together wire together",
            ),
            (
                "Localization of Function",
                "Different brain regions serve different functions",
            ),
            (
                "Neural Integration",
                "Neurons integrate multiple inputs to produce output",
            ),
            (
                "Homeostatic Balance",
                "Neural systems maintain stable activity levels",
            ),
        ]

        for name, description in principles:
            self.create_concept(
                name=name,
                concept_type=ConceptType.PRINCIPLE,
                description=description,
                certainty=90,
            )

    def get_fundamental_concepts(self) -> list[str]:
        """Get fundamental neuroscience concepts."""
        return [
            "Neuron",
            "Synapse",
            "Action Potential",
            "Neurotransmitter",
            "Brain",
            "Cortex",
            "Memory",
            "Consciousness",
            "Perception",
            "Cognition",
            "Plasticity",
            "Receptor",
            "Axon",
            "Dendrite",
            "Glia",
        ]

    def initialize_branches(self) -> None:
        """Initialize major neuroscience branches."""
        branches = [
            (
                "Cellular Neuroscience",
                "Study of neurons at the cellular level",
                ConceptType.THEORY,
            ),
            (
                "Molecular Neuroscience",
                "Molecular mechanisms of neural function",
                ConceptType.THEORY,
            ),
            (
                "Systems Neuroscience",
                "Study of neural circuits and systems",
                ConceptType.THEORY,
            ),
            (
                "Cognitive Neuroscience",
                "Neural basis of cognition",
                ConceptType.THEORY,
            ),
            (
                "Behavioral Neuroscience",
                "Neural basis of behavior",
                ConceptType.THEORY,
            ),
            (
                "Computational Neuroscience",
                "Mathematical models of neural function",
                ConceptType.THEORY,
            ),
            (
                "Clinical Neuroscience",
                "Neural disorders and treatments",
                ConceptType.THEORY,
            ),
            (
                "Developmental Neuroscience",
                "Development of the nervous system",
                ConceptType.THEORY,
            ),
            (
                "Sensory Neuroscience",
                "Neural processing of sensory information",
                ConceptType.THEORY,
            ),
            (
                "Affective Neuroscience",
                "Neural basis of emotion",
                ConceptType.THEORY,
            ),
        ]

        for name, description, concept_type in branches:
            self.create_concept(name, concept_type, description)

    def initialize_brain_regions(self) -> None:
        """Initialize major brain regions."""
        regions = [
            ("Cerebral Cortex", "Outer layer for higher functions", ["Thought", "Perception"]),
            ("Frontal Lobe", "Planning and decision making", ["Executive function"]),
            ("Parietal Lobe", "Spatial processing and integration", ["Sensory integration"]),
            ("Temporal Lobe", "Auditory processing and memory", ["Language", "Memory"]),
            ("Occipital Lobe", "Visual processing", ["Vision"]),
            ("Hippocampus", "Memory formation", ["Learning", "Spatial memory"]),
            ("Amygdala", "Emotional processing", ["Fear", "Emotion"]),
            ("Thalamus", "Sensory relay station", ["Relay", "Consciousness"]),
            ("Hypothalamus", "Homeostatic regulation", ["Hunger", "Temperature"]),
            ("Cerebellum", "Motor coordination", ["Balance", "Learning"]),
            ("Brainstem", "Vital functions", ["Breathing", "Heart rate"]),
            ("Basal Ganglia", "Movement control", ["Motor planning"]),
        ]

        for name, description, functions in regions:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["functions"] = functions

    def initialize_neuron_types(self) -> None:
        """Initialize neuron classifications."""
        neurons = [
            ("Sensory Neuron", "Afferent, carries sensory information", "Touch receptors"),
            ("Motor Neuron", "Efferent, controls muscle movement", "Alpha motor neurons"),
            ("Interneuron", "Connects neurons within CNS", "Cortical interneurons"),
            ("Pyramidal Cell", "Excitatory cortical neuron", "Cortex, hippocampus"),
            ("Purkinje Cell", "Inhibitory cerebellar neuron", "Cerebellum"),
            ("Dopaminergic Neuron", "Releases dopamine", "Substantia nigra"),
            ("GABAergic Neuron", "Releases GABA, inhibitory", "Throughout brain"),
            ("Glutamatergic Neuron", "Releases glutamate, excitatory", "Throughout brain"),
        ]

        for name, description, location in neurons:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["location"] = location

    def initialize_neurotransmitters(self) -> None:
        """Initialize major neurotransmitters."""
        neurotransmitters = [
            ("Glutamate", "Main excitatory neurotransmitter", "Excitatory", "Learning"),
            ("GABA", "Main inhibitory neurotransmitter", "Inhibitory", "Anxiety reduction"),
            ("Dopamine", "Reward and movement", "Modulatory", "Motivation"),
            ("Serotonin", "Mood regulation", "Modulatory", "Mood"),
            ("Norepinephrine", "Arousal and attention", "Modulatory", "Alertness"),
            ("Acetylcholine", "Muscle control and memory", "Both", "Memory"),
            ("Endorphin", "Pain and pleasure", "Modulatory", "Analgesia"),
            ("Oxytocin", "Social bonding", "Modulatory", "Trust"),
        ]

        for name, description, effect_type, function in neurotransmitters:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata.update({
                "effect_type": effect_type,
                "primary_function": function,
            })

    def initialize_neural_processes(self) -> None:
        """Initialize neural processes."""
        processes = [
            ("Action Potential", "Electrical impulse along axon", "~100 m/s"),
            ("Synaptic Transmission", "Chemical signal across synapse", "~1 ms"),
            ("Long-Term Potentiation", "Strengthening of synaptic connection", "Hours to years"),
            ("Long-Term Depression", "Weakening of synaptic connection", "Hours to years"),
            ("Neurogenesis", "Birth of new neurons", "Limited in adults"),
            ("Myelination", "Insulation of axons", "During development"),
            ("Apoptosis", "Programmed cell death", "During development"),
            ("Neuroplasticity", "Brain's ability to reorganize", "Lifelong"),
        ]

        for name, description, timescale in processes:
            concept = self.create_concept(
                name=name,
                concept_type=ConceptType.DEFINITION,
                description=description,
            )
            concept.metadata["timescale"] = timescale

    def initialize_neuroscience_pairs(self) -> None:
        """Initialize fundamental neuroscience pairs with META 50/50 balance."""
        pairs = [
            ("Excitation", "Inhibition", "Activating vs suppressing"),
            ("Sensory", "Motor", "Input vs output"),
            ("Central", "Peripheral", "Brain/spine vs body nerves"),
            ("Conscious", "Unconscious", "Aware vs unaware"),
            ("Sympathetic", "Parasympathetic", "Fight vs rest"),
            ("Afferent", "Efferent", "Toward vs away from brain"),
            ("Neuron", "Glia", "Signaling vs supporting"),
            ("Axon", "Dendrite", "Sending vs receiving"),
            ("Synapse", "Gap", "Connection vs separation"),
            ("Depolarization", "Repolarization", "Firing vs resetting"),
            ("Long-term", "Short-term", "Permanent vs temporary"),
            ("Memory", "Forgetting", "Retention vs loss"),
            ("Learning", "Unlearning", "Acquiring vs removing"),
            ("Plasticity", "Stability", "Changing vs fixed"),
            ("Gray Matter", "White Matter", "Cell bodies vs fibers"),
            ("Cortex", "Subcortex", "Outer vs inner brain"),
            ("Left Brain", "Right Brain", "Logic vs creativity"),
            ("Waking", "Sleeping", "Active vs resting state"),
            ("Pain", "Pleasure", "Aversion vs reward"),
            ("Voluntary", "Involuntary", "Chosen vs automatic"),
        ]

        for positive, negative, description in pairs:
            pos_concept = self.create_concept(
                name=f"{positive} (Neuroscience)",
                concept_type=ConceptType.DEFINITION,
                description=f"Positive pole: {description.split(' vs ')[0]}",
            )
            neg_concept = self.create_concept(
                name=f"{negative} (Neuroscience)",
                concept_type=ConceptType.DEFINITION,
                description=f"Negative pole: {description.split(' vs ')[1]}",
            )

            self.create_relation(
                pos_concept,
                neg_concept,
                RelationType.CONTRADICTS,
                strength=50,
            )

    def get_brain_facts(self) -> dict[str, Any]:
        """Get brain statistics and facts."""
        return {
            "neurons": 86_000_000_000,
            "synapses": 100_000_000_000_000,
            "weight_grams": 1400,
            "percent_body_weight": 2,
            "percent_energy_use": 20,
            "neuron_types": 10000,
            "glial_cells": 85_000_000_000,
        }

    def demonstrate_neural_balance(self) -> dict[str, Any]:
        """Demonstrate neural balance principles."""
        return {
            "concept": "Neural Equilibrium",
            "dualities": {
                "excitation_inhibition": {
                    "excitatory_input": 50.0,
                    "inhibitory_input": 50.0,
                    "meaning": "E/I balance is critical for brain function",
                },
                "autonomic_balance": {
                    "sympathetic": 50.0,
                    "parasympathetic": 50.0,
                    "meaning": "Fight-or-flight balanced with rest-and-digest",
                },
                "hemispheric_balance": {
                    "left_hemisphere": 50.0,
                    "right_hemisphere": 50.0,
                    "meaning": "Both hemispheres contribute to cognition",
                },
            },
            "homeostatic_plasticity": {
                "potentiation": 50.0,
                "depression": 50.0,
                "description": "Synaptic strength adjusts to maintain stability",
            },
            "meta_meaning": "Neuroscience demonstrates META 50/50 in excitation-inhibition balance",
        }


def create_neuroscience_domain(
    meta_equilibrium: MetaEquilibrium | None = None, initialize_all: bool = True
) -> NeuroscienceDomain:
    """
    Factory function to create a fully initialized neuroscience domain.

    Args:
        meta_equilibrium: Shared MetaEquilibrium instance
        initialize_all: Whether to initialize all content

    Returns:
        Initialized NeuroscienceDomain
    """
    domain = NeuroscienceDomain(meta_equilibrium)

    if initialize_all:
        domain.initialize_branches()
        domain.initialize_brain_regions()
        domain.initialize_neuron_types()
        domain.initialize_neurotransmitters()
        domain.initialize_neural_processes()
        domain.initialize_neuroscience_pairs()

    return domain
