from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "AI DevOps Project Running"

@app.route("/cpu")
def cpu_spike():
    x = 0
    for i in range(10000000):
        x += i
    return "CPU Spike simulated"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)