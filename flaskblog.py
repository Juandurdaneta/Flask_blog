from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '7af438fb878f9927dfefa28b7805ec04'

posts = [{
    "title": "Post 1",
    "author": "Juan Urdaneta",
    "content": "My first post!",
    "datePosted" : "2021-10-07"
}, 
{    
    "title": "Post 2",
    "author": "Alba Gomez",
    "content": "Second post!",
    "datePosted" : "2021-10-07"
    }]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@admin.com" and form.password.data == "password":
            flash("Logged in succesfully!", "success")
            return redirect(url_for('home'))
        else:
            flash("Login unsuccesfull, please check your email and password and try again", "danger")
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)