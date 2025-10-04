# Gemini Robotics-ER 1.5 Object Recognition Demo

A simple Python demo for object recognition and reasoning using Google's advanced Vision-Language Model, **Gemini Robotics-ER 1.5**.

***

## Features

- Detect objects in images with Gemini Robotics-ER 1.5
- Returns highly-accurate scene descriptions and object names
- Outputs rich reasoning about the image (e.g. relationships, affordances)
- Safe: does **not** expose your API key, reads it from an environment variable
- Ready for extension with bounding boxes and more advanced reasoning prompts

***

## Getting Started

### 1. Clone this repo


### 2. Install dependencies

```bash
pip install google-generativeai
```

### 3. Get your Gemini API key

- Sign up at [Google AI Studio](https://aistudio.google.com/)
- Copy your API key

### 4. Set your Gemini API key as an environment variable

#### **Windows:**
```cmd
set GEMINI_API_KEY=your_real_api_key
```

#### **Mac/Linux:**
```bash
export GEMINI_API_KEY=your_real_api_key
```

### 5. Add an image to test

Place your image in the repo folder and name it `test_image.jpg`  
(Or update `filename` in the script for your own image)

### 6. Run the demo

```bash
python test_gemini.py
```

***

## Output

- The script prints Gemini's object recognition and reasoning output directly in your terminal.
- You can easily customize the `prompt` in `test_gemini.py` to try advanced use cases (task decomposition, safety, step-by-step reasoning).

***

## Example Prompt

```python
prompt = ("Detect all objects in this image. For each, provide its name "
          "and, if possible, bounding box coordinates.")
```

***

## Customization

- Try different prompt strings to explore Gemini’s capabilities:
  - Object recognition
  - Affordance detection
  - Task decomposition
  - Scene reasoning
- You can add support for bounding box visualization with Pillow (see issues for ideas).

***

## Security

- **Never share your API key in the code**—only use environment variables.
- This approach is safe for public repos and collaborative projects.

***

## License

MIT (or your preferred license)

***

## Credits

Created by [YourName]  
Inspired by Google Gemini Robotics-ER 1.5 and modern VLM research.

***

