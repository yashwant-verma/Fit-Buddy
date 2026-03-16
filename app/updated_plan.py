import google.generativeai as genai

model = genai.GenerativeModel("models/gemini-flash-latest")


def update_workout_plan(original_plan, feedback):

    prompt = f"""
Original Plan:

{original_plan}

User Feedback:
{feedback}

Update the workout plan accordingly.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:

        # Dummy updated workout if API fails
        return f"""
<h3>Updated Workout Plan</h3>

<p><b>User Feedback:</b> {feedback}</p>

<b>Day 1</b> – Light Cardio + Stretching  
<b>Day 2</b> – Upper Body Strength (Pushups, Dumbbells)  
<b>Day 3</b> – Core Workout (Crunches, Planks)  
<b>Day 4</b> – Yoga / Mobility  
<b>Day 5</b> – Lower Body (Squats, Lunges)  
<b>Day 6</b> – Cardio (Cycling or Running)  
<b>Day 7</b> – Recovery & Stretching

"""