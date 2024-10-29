from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Inscripción a cursos
@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    datos = {}
    if request.method == 'POST':
        datos = request.form
    return render_template('inscripcion.html', datos=datos)

# Registro de usuarios
@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    datos = {}
    if request.method == 'POST':
        datos = request.form
    return render_template('registro_usuario.html', datos=datos)

# Registro de productos
@app.route('/registro_producto', methods=['GET', 'POST'])
def registro_producto():
    datos = {}
    if request.method == 'POST':
        datos = request.form
    return render_template('registro_producto.html', datos=datos)

# Registro de libros
@app.route('/registro_libro', methods=['GET', 'POST'])
def registro_libro():
    datos = {}
    if request.method == 'POST':
        datos = request.form
    return render_template('registro_libro.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
