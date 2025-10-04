import os
import google.generativeai as genai

# Read API key securely from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("Set your Gemini API key in the GEMINI_API_KEY environment variable.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-robotics-er-1.5-preview")

filename = "test_image.jpg"
prompt = ("Detect all objects in this image. For each, provide its name ")

with open(filename, "rb") as f:
    img_bytes = f.read()

response = model.generate_content([
    prompt,
    {"mime_type": "image/jpeg", "data": img_bytes}
])

print("\n--- Gemini Robotics-ER 1.5 Output ---\n")
print(response.text)
print("\n-------------------------------------\n")
