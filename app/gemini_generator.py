import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini API Key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Model
model = genai.GenerativeModel("models/gemini-flash-latest")


def generate_workout_gemini(user_input):

    prompt = f"""
You are a professional fitness trainer.

Create a clean and structured **7-day workout plan in HTML format**.

Rules:
- Use headings and lists for readability
- Each day should have warmup, workout, and cooldown
- Keep workouts beginner friendly unless intensity is high
- Keep it visually structured

Format EXACTLY like this:

<h3>Day 1 - Cardio</h3>
<ul>
<li><b>Warmup:</b> ...</li>
<li><b>Workout:</b> ...</li>
<li><b>Cooldown:</b> ...</li>
</ul>

<h3>Day 2 - Upper Body</h3>
<ul>
<li><b>Warmup:</b> ...</li>
<li><b>Workout:</b> ...</li>
<li><b>Cooldown:</b> ...</li>
</ul>

Continue until Day 7.

User Details:
Goal: {user_input['goal']}
Intensity: {user_input['intensity']}
"""

    try:
        response = model.generate_content(prompt)

        if response and response.text:
            return response.text

        else:
            raise Exception("Empty Gemini response")

    except Exception as e:

        print("Gemini error:", e)

        # Fallback HTML workout
        return """
<h3>Day 1 - Cardio</h3>
<ul>
<li><b>Warmup:</b> 5 min light stretching</li>
<li><b>Workout:</b> 20 min jogging</li>
<li><b>Cooldown:</b> Deep breathing and stretch</li>
</ul>

<h3>Day 2 - Upper Body</h3>
<ul>
<li><b>Warmup:</b> Arm circles and shoulder rolls</li>
<li><b>Workout:</b> Pushups – 3 sets, Dumbbell curls – 3 sets, Plank – 30 sec</li>
<li><b>Cooldown:</b> Shoulder stretch</li>
</ul>

<h3>Day 3 - Core</h3>
<ul>
<li><b>Warmup:</b> Torso twists</li>
<li><b>Workout:</b> Crunches – 3 sets, Leg raises – 3 sets, Russian twists</li>
<li><b>Cooldown:</b> Light stretching</li>
</ul>

<h3>Day 4 - Yoga / Recovery</h3>
<ul>
<li><b>Warmup:</b> Breathing exercises</li>
<li><b>Workout:</b> 20 min yoga and mobility</li>
<li><b>Cooldown:</b> Relaxation stretch</li>
</ul>

<h3>Day 5 - Lower Body</h3>
<ul>
<li><b>Warmup:</b> Light squats</li>
<li><b>Workout:</b> Squats – 3 sets, Lunges – 3 sets, Calf raises – 3 sets</li>
<li><b>Cooldown:</b> Hamstring stretch</li>
</ul>

<h3>Day 6 - Cardio</h3>
<ul>
<li><b>Warmup:</b> Jumping jacks</li>
<li><b>Workout:</b> 25 min cycling or brisk walk</li>
<li><b>Cooldown:</b> Stretch legs</li>
</ul>

<h3>Day 7 - Recovery</h3>
<ul>
<li><b>Warmup:</b> Light walk</li>
<li><b>Workout:</b> Full body stretching</li>
<li><b>Cooldown:</b> Deep breathing</li>
</ul>
"""