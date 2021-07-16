from logging import debug
from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)
app.secret_key = 'dausers'

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
    
    User.create_user(request.form)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)


