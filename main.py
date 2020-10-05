#set FLASK_APP=main.py
#set FLASK_DEBUG=1
#set FLASK_ENV=development

# Flask
from flask import render_template, redirect, url_for, flash
from flask_pymongo import pymongo

# Local config
from app import create_app
from app.form import SignInForm, SignUpForm
import dbconfig

app = create_app()


@app.route('/')
def signin():
    data_form = SignInForm()
    context = {
        'data_form': data_form
    }
    return render_template('signin.html', **context)