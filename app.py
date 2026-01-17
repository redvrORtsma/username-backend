from flask import Flask, jsonify 
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

SITES = {
    "GitHub": {
        "url": "https://github.com/{}",
        "not_found": "Not Found"
    },
    "Twitter": {
        "url": "https://twitter.com/{}",
        "not_found": "This account doesn't exist"
    },
    "Reddit": {
        "url": "https://www.reddit.com/user/{}",
        "not_found": "nobody on Reddit goes by that name"
    },
    "Instagram": {
        "url": "https://www.instagram.com/{}/",
        "not_found": "Sorry, this page isn't available"
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "not_found": "Couldn't find this account"
    },
    "YouTube": {
        "url": "https://www.youtube.com/@{}",
        "not_found": "This channel does not exist"
    },
    "Steam": {
        "url": "https://steamcommunity.com/id/{}",
        "not_found": "The specified profile could not be found"
    },
    "Twitch": {
        "url": "https://www.twitch.tv/{}",
        "not_found": "Sorry. Unless you've got a time machine"
    },
    "Pinterest": {
        "url": "https://www.pinterest.com/{}/",
        "not_found": "This account doesn't exist"
    },
    "SoundCloud": {
        "url": "https://soundcloud.com/{}",
        "not_found": "We can't find that page"
    },
    "DeviantArt": {
        "url": "https://www.deviantart.com/{}",
        "not_found": "Llama Not Found"
    },
    "XboxGamertag": {
        "url": "https://xboxgamertag.com/search/{}",
        "not_found": "Gamertag doesn't exist"
    },
    "Spotify": {
        "url": "https://open.spotify.com/user/{}",
        "not_found": "Couldn't find that page"
    },
    "Vimeo": {
        "url": "https://vimeo.com/{}",
        "not_found": "Sorry, we couldn't find that page"
    },
    "Snapchat": {
        "url": "https://www.snapchat.com/add/{}",
        "not_found": "Sorry"
    }
}

@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Username checker API is running"})

@app.route("/check/<username>")
def check(username):
    results = []
    headers = {"User-Agent": "Mozilla/5.0"}

    for site, data in SITES.items():
        url = data["url"].format(username)
        found = False

        try:
            r = requests.get(url, headers=headers, timeout=7)
            if r.status_code == 200 and data["not_found"].lower() not in r.text.lower():
                found = True
        except:
            found = False

        results.append({
            "site": site,
            "found": found,
            "url": url
        })

    return jsonify(results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




