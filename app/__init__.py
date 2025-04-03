from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

from app import routes 