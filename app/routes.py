from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .database import get_original_plan
from .gemini_generator import generate_workout_gemini
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .updated_plan import update_workout_plan
from .database import save_user, save_plan, update_plan, get_all_users

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


# Home page
@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Generate workout
@router.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):

    user_input = {
        "name": name,
        "age": age,
        "weight": weight,
        "goal": goal,
        "intensity": intensity
    }

    workout = generate_workout_gemini(user_input)

    tip = generate_nutrition_tip_with_flash(goal)

    user_id = save_user(name, age, weight, goal, intensity)

    save_plan(user_id, workout)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "workout": workout,
            "tip": tip,
            "user_id": user_id
        }
    )


# Update plan with feedback
@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    user_id: int = Form(...),
    feedback: str = Form(...)
):

    original_plan = get_original_plan(user_id)

    updated_plan = update_workout_plan(original_plan, feedback)

    update_plan(user_id, updated_plan)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "workout": updated_plan,
            "tip": "Updated workout plan based on your feedback!",
            "user_id": user_id
        }
    )

# Admin dashboard
@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request):

    users = get_all_users()

    return templates.TemplateResponse(
        "all_users.html",
        {
            "request": request,
            "users": users
        }
    )