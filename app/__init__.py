from flask import Flask
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')

# Register blueprints
from app.routes import main
app.register_blueprint(main) 