import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app
from werkzeug.security import check_password_hash, generate_password_hash

from verify.db import get_db

from twilio.rest import Client

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Initialize Twilio client
client = Client()


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


def start_verification(to, channel='sms'):
    if channel not in ('sms', 'voice'):
        channel = 'sms'

    service = app.config.get("VERIFICATION_SID")

    verification = client.verify \
        .services(service) \
        .verifications \
        .create(to=to, channel=channel)
    
    return verification.sid


def check_verification(phone, code):
    service = app.config.get("VERIFICATION_SID")
    
    try:
        verification_check = client.verify \
            .services(service) \
            .verification_checks \
            .create(to=phone, code=code)

        if verification_check.valid:
            db = get_db()
            db.execute(
                'UPDATE user SET verified = 1 WHERE phone_number = ?', 
                (phone,)
            )
            db.commit()
            flash('Your phone number has been verified! Please login to continue.')
    except Exception as e:
        flash("Error validating code: {}".format(e))


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        phone = request.form['full_phone']
        channel = request.form['channel']
        
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not phone:
            error = 'Phone number is required'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {0} is already registered.'.format(username)

        if error is None:
            session['phone'] = phone
            vsid = start_verification(phone, channel)

            if vsid is not None:
                # the verification was sent to the user and the username is valid
                # redirect to verification check
                db.execute(
                    'INSERT INTO user (username, password, phone_number) VALUES (?, ?, ?)',
                    (username, generate_password_hash(password), phone)
                )
                db.commit()
                return redirect(url_for('auth.verify'))

        flash(error)
    return render_template('auth/register.html')


@bp.route('/verify', methods=('GET', 'POST'))
def verify():
    """Verify a user on registration with their phone number"""
    if request.method == 'POST':
        phone = session.get('phone')
        code = request.form['code']
        check_verification(phone, code)
        return redirect(url_for('auth.login'))

    return render_template('auth/verify.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            # store the user id in a new session and return to secret content
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('secret'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('auth.login'))
