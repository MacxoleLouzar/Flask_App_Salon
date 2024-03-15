from flask import Flask, render_template, session
from login import login_blueprint
from register import register_blueprint
from Salon import salon_blueprint
from DB import init_db

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'secret'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SalonDB'
app.config['UPLOAD_FOLDER'] = 'static/images'

# Initialize database
init_db(app)

app.register_blueprint(login_blueprint)
app.register_blueprint(register_blueprint)
app.register_blueprint(salon_blueprint)

@app.route('/')
def landing():
    user_email = session.get('email')
    return render_template('landing.html', user_email=user_email)

if __name__ == '__main__':
    app.run(debug=True)
