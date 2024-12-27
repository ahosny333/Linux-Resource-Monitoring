from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

@app.route("/")
def index():
    # Serve the HTML webpage
    return render_template("index.html")

@app.route("/resources", methods=["GET"])
def get_resources():
    # Return system resource data as JSON
    data = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage('/')._asdict()
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
