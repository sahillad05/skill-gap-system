import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

URL = "https://api.adzuna.com/v1/api/jobs/in/search/1"

def fetch_jobs():
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 20,
        "what": "data analyst",
        "where": "India"
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()

        # Save raw data
        with open("data/jobs_raw.json", "w") as f:
            json.dump(data, f, indent=4)

        print("✅ Job data fetched and saved!")
    else:
        print("❌ Failed:", response.status_code)


if __name__ == "__main__":
    fetch_jobs()