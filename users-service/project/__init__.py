import os
from flask import Flask, jsonify

# Instantiate the app
app = Flask(__name__)

# Set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# Routes
@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


