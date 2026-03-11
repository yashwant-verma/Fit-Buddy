# FitBuddy AI

FitBuddy AI is a web application that generates personalized 7-day workout plans based on user input using Google's Gemini AI. It also provides nutrition tips and allows users to update their plans with feedback.

## Features

- Personalized workout plan generation based on age, weight, fitness goal, and intensity level
- Nutrition tips tailored to fitness goals
- User feedback system to update workout plans
- Admin dashboard to view all users
- MongoDB integration for data storage
- FastAPI backend with Jinja2 templating

## Prerequisites

- Python 3.8 or higher
- MongoDB database
- Google Gemini API key

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Fit-Buddy
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory with the following variables:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   MONGO_URL=your_mongodb_connection_string_here
   ```

## Usage

1. Start the application:
   ```
   uvicorn app.main:app --reload
   ```

2. Open your browser and go to `http://127.0.0.1:8000`

3. Fill out the form with your details and generate your workout plan.

4. Provide feedback to update your plan.

5. Access the admin dashboard at `/view-all-users` to view all users.

## API Endpoints

- `GET /`: Home page
- `POST /generate`: Generate workout plan
- `POST /submit-feedback`: Update plan with feedback
- `GET /view-all-users`: Admin dashboard

## Project Structure

```
Fit-Buddy/
├── requirements.txt
├── app/
│   ├── main.py              # FastAPI app setup
│   ├── routes.py            # API routes
│   ├── database.py          # MongoDB operations
│   ├── gemini_generator.py  # Workout plan generation
│   ├── gemini_flash_generator.py  # Nutrition tip generation
│   ├── updated_plan.py      # Plan update logic
│   ├── static/
│   │   └── style.css        # CSS styles
│   └── templates/
│       ├── index.html       # Home page
│       ├── result.html      # Result page
│       └── all_users.html   # Admin dashboard
└── README.md
```

## Dependencies

- fastapi
- uvicorn
- pymongo
- google-generativeai
- python-dotenv
- jinja2

## Troubleshooting

- Ensure your MongoDB is running and accessible.
- Check that your Gemini API key is valid and has sufficient quota.
- If the app fails to start, verify all dependencies are installed.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request