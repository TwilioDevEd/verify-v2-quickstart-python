import os

from flask import Flask, render_template

from dotenv import load_dotenv, find_dotenv


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'verify.sqlite'),
    )

    load_dotenv(find_dotenv())

    try:
        # Secret key
        app.secret_key = os.environ['SECRET_KEY']

        # Twilio Verify Service
        app.config['VERIFICATION_SID'] = os.environ['VERIFICATION_SID']
    except KeyError:
        raise Exception(
            'Missing environment variables. See .env.example for details')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    from verify import db
    db.init_app(app)

    @app.route('/users')
    def list_users():
        database = db.get_db()
        users = database.execute('SELECT * FROM user').fetchall()
        return render_template('users.html', users=users)

    # apply the blueprints to the app
    from verify import auth, secret
    app.register_blueprint(auth.bp)
    app.register_blueprint(secret.bp)

    # make url_for('index') == secret content
    app.add_url_rule('/', endpoint='secret')

    return app
