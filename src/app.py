import logging
from flask import Flask

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Get a logger for your app

app.logger.setLevel(logging.INFO)

@app.route('/')
def hellow_world():
    return "Hellow World !!"

if __name__ == '__main__':
    try:
        logger.info("flask app execution begins")
        app.run(debug=False, host='localhost', port=5000)
    except Exception as e:
        logger.error("an error occurred: {e}")

