import logging
from flask import Flask, jsonify, request
from threading import Thread
import time

# Initialize Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(
    filename='healthcheck.log',  # Logs will be written to this file
    level=logging.INFO,          # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Function to perform continuous health checks
def continuous_healthcheck():
    while True:
        health_status = {
            "status": "healthy",
            "uptime": "Application is running smoothly",
            "version": "1.0.0"
        }
        logger.info(
            "Automated Healthcheck. Status: %s, Uptime: %s, Version: %s",
            health_status["status"],
            health_status["uptime"],
            health_status["version"]
        )
        time.sleep(60)  # Log healthcheck every 60 seconds

@app.route("/")
def homepage():
    return "Welcome to the homepage! Healthchecks are being logged automatically."

@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    health_status = {
        "status": "healthy",
        "uptime": "Application is running smoothly",
        "version": "1.0.0"
    }
    return jsonify(health_status), 200

if __name__ == "__main__":
    # Start the continuous healthcheck in a separate thread
    healthcheck_thread = Thread(target=continuous_healthcheck, daemon=True)
    healthcheck_thread.start()

    # Run the Flask app
    app.run(debug=True)
