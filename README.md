# Text Word Frequency Analyzer

A standalone desktop application for analyzing word occurrences and statistics in text. It uses Python's built-in Tkinter and ttk for a clean white dashboard with soft blue accents.

## Features

- Large text input with a sample-text shortcut.
- Analyze Text and Clear Text buttons.
- Total word, unique word, and character counts.
- A complete word-frequency table sorted from most to least frequent, with the top five highlighted.
- A horizontal Canvas chart of up to ten most frequent words.
- A vertically scrollable dashboard for smaller screens.
- Helpful feedback for empty input and text without words.

Words are counted without regard to case. Punctuation is ignored, and simple contractions such as `don't` are kept as one word. Character count includes spaces, punctuation, and line breaks.

## Requirements

- Python 3 with Tkinter support.
- No third-party Python packages are required.

## Run the application

From this folder, run:

```bash
python app.py
```

On systems where the Python launcher is used, you can also run:

```bash
py app.py
```

The root `app.py` launches the maintained application in `Text word Frequency Analyzer\app.py`. You can also run that application directly from its folder with `python app.py`.

Paste or type text into the input area, then select **Analyze Text**. Use **Load Sample** to try the application or **Clear Text** to start over.

## Project files

```text
app.py                              # Root launcher for the desktop application
Text word Frequency Analyzer\
  app.py                            # Tkinter application implementation
requirements.txt                   # No external dependencies
README.md                          # Project documentation
```
