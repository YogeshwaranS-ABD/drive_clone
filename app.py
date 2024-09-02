from flask import Flask, render_template, request, url_for, redirect
from data import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',why=why)


@app.route('/signin', methods=['GET','POST'])
def signin():
    if request.method=='GET':
        return render_template('signin.html')
    if request.method=='POST':
        data = request.form
        return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')


if __name__=='__main__':
    app.run(debug=True)