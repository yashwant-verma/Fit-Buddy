import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model
model = genai.GenerativeModel("models/gemini-flash-latest")


def update_workout_plan(original_plan, feedback):

    prompt = f"""
You are a professional fitness trainer.

A user already has a workout plan and wants improvements.

Original Workout Plan:
{original_plan}

User Feedback:
{feedback}

Update the workout plan based on the feedback.

Rules:
- Keep it a 7-day workout plan
- Improve the plan according to feedback
- Keep exercises simple and practical
- Return ONLY HTML
- DO NOT use markdown
- DO NOT add explanations outside the plan

Use this format:

<h3>Day 1 - Title</h3>
<ul>
<li>Warmup: ...</li>
<li>Workout: ...</li>
<li>Cooldown: ...</li>
</ul>

Repeat for all 7 days.
"""

    try:

        response = model.generate_content(prompt)

        if response and response.text:

            plan = response.text.strip()

            # Remove markdown if Gemini adds it
            plan = plan.replace("```html", "").replace("```", "")

            return plan

        else:
            raise Exception("Empty response")

    except Exception:

        # Clean fallback workout
        return f"""
<h3>Updated Workout Plan</h3>

<p><b>User Feedback:</b> {feedback}</p>

<h3>Day 1 - Light Cardio</h3>
<ul>
<li>Warmup: 5 min stretching</li>
<li>Workout: 20 min brisk walking</li>
<li>Cooldown: light stretching</li>
</ul>

<h3>Day 2 - Upper Body</h3>
<ul>
<li>Pushups – 3 sets</li>
<li>Dumbbell curls – 3 sets</li>
<li>Plank – 30 seconds</li>
</ul>

<h3>Day 3 - Core</h3>
<ul>
<li>Crunches – 3 sets</li>
<li>Leg raises – 3 sets</li>
<li>Russian twists – 3 sets</li>
</ul>

<h3>Day 4 - Yoga / Recovery</h3>
<ul>
<li>20 minutes light yoga</li>
</ul>

<h3>Day 5 - Lower Body</h3>
<ul>
<li>Squats – 3 sets</li>
<li>Lunges – 3 sets</li>
<li>Calf raises – 3 sets</li>
</ul>

<h3>Day 6 - Cardio</h3>
<ul>
<li>Cycling – 25 minutes</li>
</ul>

<h3>Day 7 - Recovery</h3>
<ul>
<li>Stretching and walking</li>
</ul>
"""