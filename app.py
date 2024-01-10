'''from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
db = SQLAlchemy(app)

# User model representing the 'users' table in the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the database tables
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Query the database to find the user
    user = User.query.filter_by(username=username, password=password).first()
    
    # Check if the user exists in the database
    if user:
        # Redirect to the dashboard after successful login
        return redirect(url_for('dashboard'))
    else:
        # Redirect back to the login page with an error message
        return render_template('login.html', error='Invalid credentials. Please try again.')

@app.route('/dashboard')
def dashboard():
    # Display dashboard content after successful login
    return "Welcome to the Dashboard!"

if __name__ == '__main__':
    app.run(debug=True)


Pagina fondo color: rosado 
Navbar : si - color blanco letras color dorado
paginas: inicio - fotos - agendar cita - registrarse - perfil
registrarse: nombre, correo, contrasena
sitio web sensitivo para cada usuario: invitado, registrado, manager
agendar cita: se refleja para el manager - manda al correo de nayeli
registrarse tiene un beneficio - cada 10 citas una promocion
manager: revisar citas, aprobarlas, agregar fotos y subir videos
        agregar texto - cada pagina - cambiar color ????
invitado: registrarse - acceso a fotos - agendar cita con nombre
registrado: agendar cita - acceso a la promocion - accesso a fotos
'''