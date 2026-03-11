import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-flash-latest")


def generate_workout_gemini(user_input):

    prompt = f"""
Create a structured 7-day workout plan.

Goal: {user_input['goal']}
Intensity: {user_input['intensity']}
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:

        # Dummy fallback workout
        return """
<h3>7-Day Workout Plan</h3>

<b>Day 1 - Cardio</b>
Warmup: 5 min stretching  
Workout: 20 min jogging  
Cooldown: light stretching  

<b>Day 2 - Upper Body</b>
Pushups – 3 sets  
Dumbbell curls – 3 sets  
Plank – 30 sec  

<b>Day 3 - Core</b>
Crunches – 3 sets  
Leg raises – 3 sets  
Russian twists – 3 sets  

<b>Day 4 - Rest / Yoga</b>
20 min light yoga  

<b>Day 5 - Lower Body</b>
Squats – 3 sets  
Lunges – 3 sets  
Calf raises – 3 sets  

<b>Day 6 - Cardio</b>
Cycling – 25 min  

<b>Day 7 - Recovery</b>
Stretching and walking
"""