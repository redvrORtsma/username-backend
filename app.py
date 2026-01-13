from flask import Flask, jsonify
import requests

app = Flask(__name__)

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
    app.run()
