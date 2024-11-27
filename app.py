from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route('/storia')
def storia():
    return render_template('storia.html')

@app.route('/luoghi')
def luoghi():
    return render_template('luoghi.html')

@app.route('/curiosita')
def curiosita():
    return render_template('curiosita.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 3245, debug=True)
