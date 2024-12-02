from flask import Flask, render_template

app = Flask(__name__)

#route homepage
@app.route("/")
def homepage():
    return render_template('homepage.html')

#route per la pagina di storia
@app.route('/storia')
def storia():
    return render_template('storia.html')

#route per la pagina dei Luoghi
@app.route('/luoghi')
def luoghi():
    return render_template('luoghi.html')

#route per la pagina delle curiosità
@app.route('/curiosita')
def curiosita():
    return render_template('curiosita.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 3245, debug=True)
