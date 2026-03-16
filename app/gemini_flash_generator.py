import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model
model = genai.GenerativeModel("models/gemini-flash-latest")


def generate_nutrition_tip_with_flash(goal):

    prompt = f"""
You are a professional nutrition coach.

Give ONE short nutrition tip for someone whose goal is: {goal}.

Rules:
- Maximum 40 words
- Practical advice
- Return ONLY HTML
- DO NOT use markdown
- DO NOT add explanations

Format EXACTLY like this:

Your tip text here.
"""

    try:
        response = model.generate_content(prompt)

        if response and response.text:

            tip = response.text.strip()

            # Remove markdown formatting if Gemini adds it
            tip = tip.replace("```html", "").replace("```", "")

            return tip

        else:
            raise Exception("Empty response")

    except Exception:

        return """
Stay hydrated and eat balanced meals with protein,
healthy fats, whole grains, and vegetables to support energy
levels and recovery.
"""