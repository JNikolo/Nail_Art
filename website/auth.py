from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/iniciar_sesion', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Bienvenido! Recuerde que por 10 citas puede aplicar a una promocion', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Clave incorrecta. Trate de nuevo.', category='error')
        else:
            flash('El correo no existe.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/cerrar_sesion')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/registrarse', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('El correo electronico ya existe.', category='error')
        elif len(email) < 4:
            flash('El correo debe ser mayor a 4 caracteres.', category='error')
        elif len(name) < 2:
            flash('El nombre debe contener almenos 2 caracteres.', category='error')
        elif password1 != password2:
            flash('Las contraseñas no coinciden.', category='error')
        elif len(password1) < 7:
            flash('La contraseña debe contener almenos 8 caracteres.', category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Cuenta creada! Gracias por formar parte!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)