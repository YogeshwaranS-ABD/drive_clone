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
        name = data['username']
        passwd = data['password']
        flag=user_check(name, passwd)
        if flag[0]==1:
            return redirect(url_for('dashboard',user=flag[1]))
        return render_template('failed.html', content=flag)

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    if request.method=='POST':
        data = request.form
        if is_unique_user(data['username'],data['email']):
            if data['password']==data['rpassword']:
                update_db([ data['fullname'], data['username'], data['email'], encrypt(data['password'])])
                return render_template('failed.html', content='Registerd Successfully. Please Login again')
            else:
                return render_template('failed.html', content='Password and Re-Type password didn\'t match. Please try again')
        else:
            return render_template('failed.html', content='The User is already registerd. Contact Admin to channge or get a new password!')

@app.route('/change-password', methods=['GET','POST'])
def change_password():
    if request.method=='GET':
        return render_template('passwd.html')
    if request.method=='POST':
        data  = request.form
        return f"the data given is {data}"

@app.route('/<user>/dashboard')
def dashboard(user):
    return f'<h1> Welcome {user} </h1>'

if __name__=='__main__':
    app.run(debug=True)