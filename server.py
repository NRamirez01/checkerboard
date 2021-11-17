from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def basis():
    return render_template('checkerboard.html', column = 4, row = 4)

@app.route('/<number>')
def eightbyfour(number):
    return render_template('checkerboard.html', column = int(number), row = 2)

@app.route('/<number>/<row>')
def userdefinedsize(number,row):
    return render_template('checkerboard.html', column = int(int(number)/2), row = int(int(row)/2))

if __name__ == "__main__":
    app.run(debug=True)