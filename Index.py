from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def nosotros():
    return render_template('nosotros.html')

@app.route('/nosotros')
def noticias():
    return render_template('noticias.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__name__':
    app.run(debug=True)