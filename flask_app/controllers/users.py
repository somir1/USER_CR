from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.users import User

@app.route('/')
def index ():

    #getting users from database
    userslist = User.get_all()
    return render_template('index.html', userlist = userslist)

@app.route('/create.html')
def adNew():
    return render_template('create.html')

@app.route('/users', methods = ['POST'])
def create_user():
    print('post user')
    user_id = User.create_user(request.form)
    print(user_id)
    return redirect('/showuser/'+ str(user_id) + '/show')

@app.route('/users/<int:user_id>/delete')
def delete_theuser(user_id):
    data = {
        'id' : user_id
    }

    User.delete_DAuser(data)
    return redirect('/')

@app.route('/showuser/<int:user_id>/show')
def show_new(user_id):
    data = {
        'id' : user_id
    }
    user = User.show_user(data)
    print(user)
    return render_template('showuser.html', user = user)

@app.route('/edituser/<int:user_id>/edit')
def edit_user(user_id):
    
    data = {
        'id' : user_id
    }

    user = User.show_user(data)
    return render_template('edit.html', user = user)

@app.route('/updateuser', methods = ['POST'])
def update_user():
    print(request.form['id'])
    data = {
        'id' : request.form['id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.edit_theuser(data)
    return redirect('/')
