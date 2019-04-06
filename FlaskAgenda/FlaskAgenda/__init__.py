"""
The flask application package.
"""

from flask import Flask, request ,redirect 


app = Flask(__name__)

import FlaskAgenda.views
