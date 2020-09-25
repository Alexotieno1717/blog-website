from flask import Flask, render_template
from . import main
from flask_login import login_required


@main.route('/')
def index():
    return render_template('index.html')
