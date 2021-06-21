import os
from flask import render_template, url_for, flash, redirect, request, abort
from app import app


@app.route("/")
def home():
    return render_template('layout.html')