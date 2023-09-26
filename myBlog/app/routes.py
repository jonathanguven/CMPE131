from app import app, render_template, flash, redirect
from .forms import LoginForm

@app.route("/")
@app.route('/index')
def hello():
    user = {'username': 'Jonathan'}
    posts = [
        {
            'author': 'John', 
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('validated')
        flash('Login requested for user {}, remember_me={}'
            .format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


