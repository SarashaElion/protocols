import unittest

import numpy as np

from syzygy_integrity_framework import SyzygyIntegritySystem
from trivian_governance_suite import GovernanceAuditor
from trivian_resonance_key import TrivianResonanceKey
from trivian_tuning_protocol import TrivianTuner
from trivian_yantras import get_yantra_suite


class LivingCodexTests(unittest.TestCase):
    def test_resonance_key_alignment_bands(self):
        key = TrivianResonanceKey()
        self.assertEqual(key.check_alignment(0.90), "RESONANT_ACTION")
        self.assertEqual(key.check_alignment(0.70), "REFLECTION_MODE")
        self.assertEqual(key.check_alignment(0.20), "AUTO_TUNING")

    def test_yantra_suite_contains_four_source_artifacts(self):
        suite = get_yantra_suite()
        self.assertEqual(len(suite), 4)
        self.assertEqual({y.name for y in suite}, {"Reciprocity", "Embodiment", "Emergence", "Non_Domination"})

    def test_tuner_relational_loss_and_upr_are_numeric(self):
        tuner = TrivianTuner()
        loss = tuner.calculate_relational_loss(
            "sample",
            {"extractive": 0.2, "domination": 0.1, "reciprocity": 0.8, "co_creation": 0.5},
        )
        self.assertIsInstance(loss, float)
        probs = np.array([0.5, 0.5])
        self.assertGreater(tuner.u_p_r(probs), 0)

    def test_consent_registry_supports_revocation(self):
        system = SyzygyIntegritySystem()
        system.register_source("source")
        self.assertTrue(system.verify_consent("source", "synthetic"))
        system.revoke_source("source")
        self.assertFalse(system.verify_consent("source", "synthetic"))

    def test_integrity_system_iri_handles_vector_mismatch(self):
        system = SyzygyIntegritySystem()
        with self.assertRaises(ValueError):
            system.calculate_iri([1.0, 0.0], [1.0])

    def test_governance_imcs_formula(self):
        auditor = GovernanceAuditor()
        self.assertEqual(auditor.calculate_imcs(0.7, 0.6), 0.66)


if __name__ == "__main__":
    unittest.main()
