from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

# This will use the bootstrap and python package to put at disclosure the bootstrap css (used on the base html)
bootstrap = Bootstrap5(app)

# We have to create a random secret key for using the csrf security
app.secret_key = "randooooom"
correct_email = "admin@email.com"
correct_password = "12345678"


def check_credentials(email, password):
    if email == correct_email and password == correct_password:
        return True
    else:
        return False


# We create our own class that inheritances the FROM class, and define some inputs for it
class Login(FlaskForm):
    email = StringField(label='Email', validators=[
        DataRequired(message="Cómo lo vas a dejar vacío, maestro?"),
        Email(message="You need to put an email")
    ])
    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message="Mínimo 8 caracteres papá")
    ])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template('index.html')


# In the login, we create an object with the past class, and pass it as a variable
@app.route('/login', methods=['GET', 'POST'])
def get_login():
    login = Login()
    # This checks if the validations are met. (The .validate_on_submit takes into account if it's a post method because
    # if its already submitted, it should be a Post method)
    if login.validate_on_submit():
        if check_credentials(email=login.email.data, password=login.password.data):
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', login=login)


if __name__ == '__main__':
    app.run(debug=True)
