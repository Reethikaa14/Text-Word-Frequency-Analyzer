"""Launch the Text Word Frequency Analyzer desktop application."""

import runpy
from pathlib import Path


APPLICATION_PATH = (
    Path(__file__).resolve().parent
    / "Text word Frequency Analyzer"
    / "app.py"
)


def main():
    """Run the maintained Tkinter application."""
    runpy.run_path(str(APPLICATION_PATH), run_name="__main__")


if __name__ == "__main__":
    main()
