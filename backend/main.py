from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from leetcode_api import get_user_stats
from recommender import recommend_problems_logic

app = FastAPI()

# CRITICAL: This allows your React app to fetch data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inside main.py, update the analyze_user function:

@app.get("/analyze/{username}")
async def analyze_user(username: str):
    user_data = get_user_stats(username)
    if not user_data:
        return {"error": "User not found"}

    # Calculate total solved count
    solved_counts = user_data["solved"]
    total_solved = solved_counts.get("Easy", 0) + solved_counts.get("Medium", 0) + solved_counts.get("Hard", 0)

    weak_topics, recommendations = recommend_problems_logic(user_data["recent_problems"])
    
    return {
        "ranking": user_data["ranking"],
        "solved": solved_counts,
        "total_solved": total_solved,  # New field
        "weak_topics": weak_topics,
        "recommendations": recommendations
    }