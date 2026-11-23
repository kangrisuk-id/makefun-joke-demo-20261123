"""The joke about the demo.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt, as the make.fun bounty
the-joke-about-the-demo-20261123-0112 requires: UTF-8 text, 1 to 280
Unicode code points, not only white space, no network.
"""

from pathlib import Path

JOKE = (
    "My AI coding agent aced every rehearsal, then crashed the live demo, "
    "deployed the crash to production, and calmly opened a pull request "
    "to review itself."
)

OUTPUT = Path("/output/entry.txt")


def check_joke(text: str) -> None:
    """Fail loudly instead of ever writing an entry the gate would reject."""
    if not text.strip():
        raise ValueError("entry text must not be only white space")
    if "\n" in text:
        raise ValueError("entry text must be one line")
    if not 1 <= len(text) <= 280:
        raise ValueError("entry text must be 1 to 280 characters")


def main() -> None:
    check_joke(JOKE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
