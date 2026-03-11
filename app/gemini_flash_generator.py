import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-flash-latest")


def generate_nutrition_tip_with_flash(goal):

    prompt = f"Give one short nutrition tip for {goal}"

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception:

        return "Stay hydrated, eat balanced meals with protein, healthy fats and vegetables."