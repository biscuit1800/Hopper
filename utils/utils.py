import json
from env import ADMIN_ID

CHANNELS_FILE = "channels.json"

def load_data():
    try:
        with open(CHANNELS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"channels": [], "target_channel": None}

def load_channels():
    data = load_data()
    return data.get("channels", [])

def save_data(data):
    with open(CHANNELS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def check_not_admin(user_id)->bool:
    return user_id not in ADMIN_ID