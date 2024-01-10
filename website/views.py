from flask import Blueprint,render_template, request, flash,redirect,url_for
from flask_login import current_user
from .models import Appointment
from . import db 
from datetime import datetime, timedelta

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/agendar', methods=['POST','GET'])
def appointment():
    date_format = "%Y-%m-%d %H"
    most_recent_appointment = Appointment.query.order_by(Appointment.end_date.desc()).first()

    most_recent_end_time = most_recent_appointment.end_date if most_recent_appointment else None

    if request.method=='POST':
        
        date_str = request.form.get("datetime-picker")

         # Adjust the format based on your input
        date = datetime.strptime(date_str, date_format)
        
        #some lambdas to compare attributes
        eq_year = lambda date1, date2: date1.year == date2.year
        eq_month = lambda date1, date2: date1.month == date2.month
        eq_day = lambda date1, date2: date1.day == date2.day
        greater_hour = lambda date1, date2: date1.hour > date2.hour

        if not(most_recent_end_time and eq_year(date, most_recent_appointment) 
            and eq_month(date, most_recent_appointment) and eq_day(date,most_recent_appointment)
            and greater_hour(date, most_recent_appointment)):
            formatted_most_recent_end_time = most_recent_end_time.strftime("%Y-%m-%d %H")
            flash(f'Error: La fecha seleccionada debe ser después de la última cita agendada. Última fecha: {formatted_most_recent_end_time}', category="error")
            return redirect(url_for('views.appointment'))
        
        # Calculate end time (two hours after the given date)
        end_time = date + timedelta(hours=2)
        if current_user.is_anonymous:
            name = request.form.get('name')
            apt = Appointment(guest_name=name,date=date, end_date=end_time)
            db.session.add(apt)
            db.session.commit()
            flash('Gracias por agendar su cita')
            return redirect(url_for('views.home'))
        else:
            user_id = current_user.id
            apt = Appointment(date=date, user_id=user_id, end_date=end_time)
            db.session.add(apt)
            db.session.commit()
            flash('Gracias por agendar su cita')
            return redirect(url_for('views.profile'))

    return render_template("appointment.html", default_date=most_recent_end_time)

@views.route('/perfil', methods=['GET','POST'])
def profile():
    return render_template("profile.html")

@views.route('/modelos', methods=['POST','GET'])
def shows():
    return render_template("videos.html")