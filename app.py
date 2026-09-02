# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:23:47 2026

@author: HP
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/certificate")
def certificate():
    return render_template("certificate.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=False)