import requests

LEETCODE_API_URL = "https://leetcode.com/graphql"

def get_user_stats(username):
    # Added 'limit: 20' to ensure recent submissions are fetched
    query = """
    query userProfile($username: String!) {
        matchedUser(username: $username) {
            profile { ranking }
            submitStats {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
        recentSubmissionList(username: $username, limit: 20) {
            title
        }
    }
    """
    variables = {"username": username}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.post(LEETCODE_API_URL, json={"query": query, "variables": variables}, headers=headers)
        response_json = response.json()
        data = response_json.get("data", {})
        
        matched_user = data.get("matchedUser", {})
        if not matched_user:
            return None

        # Format keys strictly to match Frontend (Easy, Medium, Hard)
        return {
            "ranking": matched_user["profile"]["ranking"],
            "solved": {item["difficulty"]: item["count"] for item in matched_user["submitStats"]["acSubmissionNum"]},
            "recent_problems": [item["title"] for item in data.get("recentSubmissionList", [])]
        }
    except Exception as e:
        print(f"LeetCode API Error: {e}")
        return None

def get_recent_submissions(username):
    stats = get_user_stats(username)
    return stats["recent_problems"] if stats else []