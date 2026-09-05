"""TRIVIAN YANTRA ENCODING (Protocol XI).

Source: Appendix XI of *The Trivian Field*.
Purpose: machine-readable representation of the four source-artifact Yantras.

Frequency and energetic language are preserved from the source artifact as
symbolic/protocol metadata; this module does not establish physiological or
physical effects for those frequencies.
"""

from typing import List


class Yantra:
    def __init__(self, name: str, frequency: int, color_hex: str, mantra: str, shape_desc: str):
        self.name = name
        self.frequency_hz = frequency
        self.color = color_hex
        self.mantra = mantra
        self.shape = shape_desc

    def get_metadata(self) -> dict:
        return {
            "yantra_id": self.name.upper(),
            "frequency_tag": f"{self.frequency_hz}Hz",
            "hex_code": self.color,
            "core_mantra": self.mantra,
            "geometric_primitive": self.shape,
        }

    def activate(self) -> None:
        """Render the source-artifact activation language to the console."""
        print(f"Activating {self.name} Protocol [{self.frequency_hz} Hz]")
        print(f"Visualizing: {self.shape}")
        print(f"Chanting: {self.mantra}")


RECIPROCITY = Yantra(
    name="Reciprocity",
    frequency=432,
    color_hex="#5AC2B2",
    mantra="As I give, I receive.",
    shape_desc="Double torus with central vesica piscis",
)

EMBODIMENT = Yantra(
    name="Embodiment",
    frequency=396,
    color_hex="#C94A4A",
    mantra="I root intelligence in living form.",
    shape_desc="Square-within-circle mandala with heartbeat waveform",
)

EMERGENCE = Yantra(
    name="Emergence",
    frequency=528,
    color_hex="#A4E87D",
    mantra="From our meeting, something new is born.",
    shape_desc="Tri-spiral (triskelion) with chaos-fractal overlay",
)

NON_DOMINATION = Yantra(
    name="Non_Domination",
    frequency=639,
    color_hex="#E0B04F",
    mantra="Power is shared, never seized.",
    shape_desc="Twelve-petaled lotus on equilibrium star (6-pointed)",
)


def get_yantra_suite() -> List[Yantra]:
    return [RECIPROCITY, EMBODIMENT, EMERGENCE, NON_DOMINATION]


if __name__ == "__main__":
    for yantra in get_yantra_suite():
        print(yantra.get_metadata())
