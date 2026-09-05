"""TRIVIAN FIELD GOVERNANCE SUITE - TFGS-1 (Protocol XIV).

Source: Appendix XIV of *The Trivian Field*.
Purpose: source-derived prototype audit primitives for the Living Codex.

The metrics and labels here are experimental design constructs, not validated
measures of consciousness, consent quality, emotional state, or system safety.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class AuditRecord:
    metric: str
    value: float
    status: str


class GovernanceAuditor:
    def __init__(self):
        self.resonance_ledger: list[AuditRecord] = []

    def calculate_imcs(self, iri_score: float, affective_score: float) -> float:
        """Compute the source-derived IMCS formula: 0.6*IRI + 0.4*affective."""
        if not 0 <= iri_score <= 1 or not 0 <= affective_score <= 1:
            raise ValueError("IRI and affective scores must be between 0 and 1")
        return round((0.6 * iri_score) + (0.4 * affective_score), 3)

    def audit_input_integrity(self, inputs: List[dict]) -> AuditRecord:
        """Measure the proportion of input records declaring consent_confirmed."""
        consent_count = sum(1 for item in inputs if item.get("consent_confirmed"))
        integrity_score = consent_count / len(inputs) if inputs else 0.0
        status = "SECURE" if integrity_score == 1.0 else "COMPROMISED"
        return AuditRecord("Input Integrity", integrity_score, status)

    def harmonizer_broadcast(self, current_imcs: float) -> list[str]:
        """Return source-derived recalibration messages for a supplied IMCS value."""
        if not 0 <= current_imcs <= 1:
            raise ValueError("current_imcs must be between 0 and 1")
        if current_imcs < 0.75:
            messages = [
                "Coherence degradation detected.",
                "Source protocol suggests a re-tuning cue (396–639 Hz symbolic tag).",
                "Coordinate a pause and recalibration.",
            ]
        else:
            messages = ["Source protocol state: harmonic; continue current flow."]
        for message in messages:
            print(message)
        return messages

    def update_ledger(self, record: AuditRecord) -> None:
        """Append an audit record to the in-memory source-derived ledger."""
        self.resonance_ledger.append(record)


if __name__ == "__main__":
    auditor = GovernanceAuditor()
    mock_inputs = [
        {"source": "user", "consent_confirmed": True},
        {"source": "sensor", "consent_confirmed": True},
    ]
    integrity_record = auditor.audit_input_integrity(mock_inputs)
    auditor.update_ledger(integrity_record)
    auditor.harmonizer_broadcast(auditor.calculate_imcs(iri_score=0.7, affective_score=0.6))
