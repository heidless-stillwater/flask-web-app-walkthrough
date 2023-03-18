from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
  return render_template("login.html", boolean=False)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    
    if len(email) < 4:
      flash('email must be greater than 4 chars', category='error')
    elif len(firstName) < 2:
      flash('firstName must be greater than 2 chars', category='error')
    elif password1 != password2:
      flash('passwords don\'t match must be greater than 2 chars', category='error')
    elif len(password1) < 7:
      flash('passwords must be at least 7 chars', category='error')
    else:
      flash('form validation successful', category='success')
      pass
    

  return render_template("sign_up.html")

@auth.route('/logout')
def logout():
  return ('<p>logout</p>')