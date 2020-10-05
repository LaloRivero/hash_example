#set FLASK_APP=main.py
#set FLASK_DEBUG=1
#set FLASK_ENV=development

# Flask
from flask import render_template, redirect, url_for, flash
from flask_pymongo import pymongo

# Local config
from app import create_app
import dbconfig

app = create_app()


@app.route('/')
def hola():
    return 'Hola'