from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker, scoped_session

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/career', methods=['GET'])
def career():
    return render_template('career.html')



@app.route('/study', methods=['GET'])
def study():
    return render_template('study.html')



@app.route('/MyProjects', methods=['GET'])
def MyProjects():
    return render_template('MyProjects.html')



@app.route('/Goals', methods=['GET'])
def Goals():
    return render_template('Goals.html')



@app.route('/woodworking', methods=['GET'])
def woodworking():
    return render_template('woodworking.html')



@app.route('/sports', methods=['GET'])
def sports():
    return render_template('sports.html')



@app.route('/Poetry', methods=['GET'])
def poetry():
    return render_template('Poetry.html')




app.secret_key = os.urandom(12)
app.run(debug=True,host='0.0.0.0', port=4000)
