from flask import Flask, render_template

app=Flask(__name__)

from admin import routes