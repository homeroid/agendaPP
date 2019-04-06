"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from FlaskAgenda import app

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'agenda_phone'

mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/insert',methods = ['POST'])
def insert():

        if request.method == "POST":
            name = request.form['name']
            lastname = request.form['lastname']
            email = request.form['email']
            number= request.form['number']
            type = request.form['type']

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO agenda (name, lastname, email, number, type) VALUES (%s, %s, %s) ", (name, lastname, email, number, type)
            return redirect(url_for('Index'))
