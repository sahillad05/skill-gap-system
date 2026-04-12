import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

# You can expand this later
SKILLS = ["python", "sql", "machine learning", "power bi"]

def fetch_youtube_data():
    all_results = []

    for skill in SKILLS:
        params = {
            "part": "snippet",
            "q": f"{skill} tutorial",
            "type": "video",
            "maxResults": 10,
            "key": API_KEY
        }

        response = requests.get(SEARCH_URL, params=params)

        if response.status_code == 200:
            data = response.json()

            for item in data["items"]:
                video = {
                    "skill": skill,
                    "title": item["snippet"]["title"],
                    "description": item["snippet"]["description"]
                }
                all_results.append(video)

        else:
            print(f"❌ Error for {skill}: {response.status_code}")

    # Save data
    with open("data/youtube_raw.json", "w") as f:
        json.dump(all_results, f, indent=4)

    print("✅ YouTube data fetched and saved!")


if __name__ == "__main__":
    fetch_youtube_data()