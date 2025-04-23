
from flask import Flask
from flask_cors import CORS
from routes.currency_route import currency_bp
from routes.person_route import person_bp
from routes.object_route import object_bp
from routes.profile_route import profile_bp
from routes.translation_route import translation_bp
from routes.speech import bp as speech_bp

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Register individual route blueprints
app.register_blueprint(currency_bp, url_prefix='/api')
app.register_blueprint(person_bp, url_prefix='/api')
app.register_blueprint(object_bp)  # Remove url_prefix to match the frontend request
app.register_blueprint(profile_bp, url_prefix='/api')
app.register_blueprint(translation_bp, url_prefix='/api')
app.register_blueprint(speech_bp, url_prefix='/api')  # Add speech blueprint with /api prefix

if __name__ == '__main__':
    app.run(debug=True, port=5000)
