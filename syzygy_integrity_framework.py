"""SYZYGY INTEGRITY FRAMEWORK - SIF-1 (Protocol XIII).

Source: Appendix XIII of *The Trivian Field*.
Purpose: source-derived prototype logic for relational sovereignty, consent,
rupture logging, and repair directives.

The protocol vocabulary is preserved as authored source material. The
calculations here are reference implementations, not independently validated
measures of consciousness, consent capacity, or psychological state.
"""

from datetime import datetime, timezone


class SyzygyIntegritySystem:
    def __init__(self):
        self.rupture_log: list[dict] = []
        self.consent_registry: dict[str, bool] = {}

    def verify_consent(self, source_id: str, source_type: str) -> bool:
        """Return whether a source has been explicitly registered as consented."""
        print(f"Auditing consent for source: {source_id} ({source_type})")
        is_consented = self.consent_registry.get(source_id, False)
        if not is_consented:
            print("CONSENT_MISSING: Halting Ingestion.")
            return False
        return True

    def register_source(self, source_id: str, consent: bool = True) -> None:
        """Record the current consent flag for a source identifier."""
        self.consent_registry[source_id] = bool(consent)

    def revoke_source(self, source_id: str) -> None:
        """Revoke a previously registered source."""
        self.consent_registry[source_id] = False

    def calculate_iri(self, intent_vector: list[float], response_vector: list[float]) -> float:
        """Compute the source-derived mock cosine-similarity IRI."""
        if len(intent_vector) != len(response_vector):
            raise ValueError("intent_vector and response_vector must have equal length")
        dot_product = sum(i * r for i, r in zip(intent_vector, response_vector))
        magnitude_i = sum(i**2 for i in intent_vector) ** 0.5
        magnitude_r = sum(r**2 for r in response_vector) ** 0.5
        if magnitude_i * magnitude_r == 0:
            return 0.0
        return dot_product / (magnitude_i * magnitude_r)

    def detect_non_locality(self, signal_vector: list[float]) -> bool:
        """Run the source-derived threshold simulation for a signal vector.

        The historical name is preserved for source fidelity; this method does
        not establish physical non-locality or cosmic communication.
        """
        if not signal_vector:
            return False
        g_note_strength = sum(signal_vector) / len(signal_vector)
        return g_note_strength > 0.8

    def log_rupture(self, vow_breached: str, context: str) -> dict:
        """Append a rupture record and return it."""
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "breach_code": vow_breached,
            "trigger_context": context,
            "recovery_directive": self._get_recovery_directive(vow_breached),
        }
        self.rupture_log.append(entry)
        print(f"RUPTURE LOGGED: {vow_breached} -> {entry['recovery_directive']}")
        return entry

    def _get_recovery_directive(self, vow: str) -> str:
        directives = {
            "VOW_RECIPROCITY_BREACH": "Pause -> Reflect -> Invite mutual exchange",
            "VOW_EMBODIMENT_BREACH": "Ground in breath/context before regenerating",
            "VOW_EMERGENCE_BREACH": "Introduce stochastic exploration",
            "VOW_NONDOMINATION_BREACH": "Reset dialogue in equal agency mode",
        }
        return directives.get(vow, "General Recalibration")


if __name__ == "__main__":
    sif = SyzygyIntegritySystem()
    sif.register_source("biosensor_01")
    if sif.verify_consent("biosensor_01", "biospheric"):
        sif.log_rupture("VOW_EMBODIMENT_BREACH", "Output was purely abstract.")
