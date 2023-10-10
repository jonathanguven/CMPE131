from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def hello_name():
    XX = 'XX'
    YY = 'YY'
    ZZ = ['ZZ1', 'ZZ2']
    return render_template('template.html', XX = XX, YY = YY, ZZ = ZZ)

if __name__ == "__main__":
    app.run() 

