# Gemini Robotics-ER 1.5 Object Recognition Demo

A simple Python demo for object recognition and scene reasoning using Google's **Gemini Robotics-ER 1.5** vision language model.

## Features

- Detect and describe objects in images with Gemini Robotics-ER 1.5
- Returns scene descriptions, object names, and spatial reasoning
- API key loaded from an environment variable (never hard coded)
- Easy to extend with custom prompts for affordances, task decomposition, and bounding boxes

## Requirements

- Python 3.8+
- A [Google AI Studio](https://aistudio.google.com/) API key

## Installation

```bash
git clone https://github.com/chiranjivaraoatluri13/gemini-robotics-er-demo.git
cd gemini-robotics-er-demo
pip install google-generativeai
```

## Setup

Set your Gemini API key as an environment variable.

**Windows (cmd):**

```cmd
set GEMINI_API_KEY=your_api_key_here
```

**Windows (PowerShell):**

```powershell
$env:GEMINI_API_KEY = "your_api_key_here"
```

**macOS / Linux:**

```bash
export GEMINI_API_KEY=your_api_key_here
```

Place a test image named `test_image.jpg` in the project folder (or change `filename` in `test_gemini.py`).

## Usage

```bash
python test_gemini.py
```

Example output:

```
Gemini Robotics-ER 1.5 Output

[Object list and scene reasoning printed here]
```

## Customizing prompts

Edit the `prompt` variable in `test_gemini.py`:

```python
prompt = (
    "Detect all objects in this image. For each, provide its name "
    "and, if possible, bounding box coordinates."
)
```

Try prompts for affordance detection, safety analysis, or step by step task decomposition.

## Security

Never commit your API key. Always use environment variables for credentials.

## Project structure

```
gemini-robotics-er-demo/
├── test_gemini.py    # Main demo script
└── README.md
```

## License

MIT

## Author

[CHIRANJIVA RAO ATLURI](https://github.com/chiranjivaraoatluri13)
