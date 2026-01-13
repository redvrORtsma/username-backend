from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route("/check/<username>")
def check(username):
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Reddit": f"https://reddit.com/user/{username}"
    }

    results = []

    for site, url in sites.items():
        try:
            r = requests.get(url, timeout=5)
            found = r.status_code == 200
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
