from flask import Blueprint, render_template, request, flash

auth_routes = Blueprint('auth_route', __name__)


@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean="True")

@auth_routes.route("/logout")
def logout():
    return "<p>Logout</p>"

@auth_routes.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif len(firstName) < 2:
            flash("First Name must be greater than 1 characters.", category='error')
        elif password1 != password2:
            flash("Your passwords don't match!", category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category='error')
        else:
            flash("Account created!", category='success')
            
    return render_template("sign_up.html")

