from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, DateTimeField, BooleanField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from models import User,Appointment


class RegisterForm(FlaskForm):
    def validate_username(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError('El correo ya esta en uso! Por favor trate con uno diferente')

    name = StringField(label='Nombre:', validators=[Length(min=2), DataRequired()])
    email = StringField(label='Correo electronico:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Contraseña:', validators=[Length(min=8), DataRequired()])
    password2 = PasswordField(label='Confirme contraseña:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Crear Cuenta')


class LoginForm(FlaskForm):
    email = StringField(label='Correo Electronico:', validators=[DataRequired()])
    password = PasswordField(label='Contraseña:', validators=[DataRequired()])
    submit = SubmitField(label='Inicie Sesion')

class AppointmentForm(FlaskForm):
    date = DateTimeField(label="Seleccione una fecha y hora:", validators=[DataRequired()])
    submit = SubmitField(label='Reservar cita')

class AppointmentIncognitoForm(FlaskForm):
    name = StringField(label='Nombre:', validators=[Length(min=2), DataRequired()])
    email = StringField(label='Correo electronico:', validators=[Email(), DataRequired()])
    date = DateTimeField(label="Seleccione una fecha y hora:", validators=[DataRequired()])
    submit = SubmitField(label='Reservar cita')

class CancelAppointment(FlaskForm):
    delete = BooleanField(label='Quiere cancelar su reservacion?',validators=[DataRequired()])

class MoveAppointment(FlaskForm):
    newDate = DateTimeField(label="Seleccione una nueva fecha y hora:", 
                            validators=[DataRequired()])

