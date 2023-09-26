from app import app, render_template

@app.route("/")
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
