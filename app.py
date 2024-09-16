from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from os import listdir, mkdir, path
from werkzeug.utils import secure_filename

from data import *
from utils import *

app = Flask(__name__)

UPLOAD_FOLDER = './storage/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.add_url_rule("/uploads/<name>", endpoint="download_file", build_only=True)

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
            return redirect(url_for('dashboard',user=flag[1:]))
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

@app.route('/<user>', methods=['GET','POST'])
def dashboard(user):
    user = eval(user)
    file_list=[]
    
    if request.method=='GET':
        print(user[-1])
        if user[-1] in listdir(f'./storage/'):
            file_list = listdir(f'./storage/{user[-1]}')
        else:
            mkdir(f'./storage/{user[-1]}')
            file_list=[]
        return render_template('dashboard.html',user=user[:], file_list=file_list, msg=0)
    
    if request.method=='POST':
        file_list = get_files(user[-1])
        file = request.files['file']
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('dashboard',user=user))
        elif file.filename == '':
            return render_template(
                        'dashboard.html',
                        user=user[:],
                        file_list=file_list,
                        msg=1)
        else:
            name = secure_filename(file.filename)
            file.save(path.join(app.config['UPLOAD_FOLDER'],user[-1],name))
            # if type(file_list)!=type([]):
            #     file_list=[name]
            # else:
            #     file_list.append(name)
            file_list.append(name)
            return render_template(
                        'dashboard.html',
                        user=user[:],
                        file_list=file_list,
                        msg=2)
        return redirect(url_for('dashboard',user=user))

@app.route('/uploads/<name>')
def download_file(name):
    username = request.args.get('username')
    return send_from_directory(path.join(app.config['UPLOAD_FOLDER'],username), name, as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)