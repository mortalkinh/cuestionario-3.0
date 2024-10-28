# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'byronmortal4@gmail.com'  # Tu correo
app.config['MAIL_PASSWORD'] = 'zzek hgvr dymf vium'  # Tu contraseña específica
app.config['MAIL_DEFAULT_SENDER'] = 'byronmortal4@gmail.com'  # Tu correo

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        results = {f'q{i}': request.form.get(f'q{i}') for i in range(1, 11)}
        si_count = sum(1 for key in results if results[key] == 'si')
        no_count = sum(1 for key in results if results[key] == 'no')

        # Preparar el contenido del correo
        email_content = f"""
        Resultados del cuestionario de {nombre}:
        Sí: {si_count}
        No: {no_count}
        
        Detalles:
        1. {results['q1']}
        2. {results['q2']}
        3. {results['q3']}
        4. {results['q4']}
        5. {results['q5']}
        6. {results['q6']}
        7. {results['q7']}
        8. {results['q8']}
        9. {results['q9']}
        10. {results['q10']}
        """

        # Enviar correo
        msg = Message("Resultados del Cuestionario", recipients=["byronmortal4@gmail.com"])
        msg.body = email_content
        mail.send(msg)

        return redirect(url_for('thank_you'))

    return render_template('quiz.html')

@app.route('/thank_you')
def thank_you():
    return "Gracias por enviar tus respuestas. ¡Los resultados han sido enviados por correo!"

if __name__ == '__main__':
    app.run(debug=True)
