from flask import Flask
import os

app = Flask(app)

@app.route("/")
def home():
    return f"Environment: {os.getenv('APP_ENV')} | App Running Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
