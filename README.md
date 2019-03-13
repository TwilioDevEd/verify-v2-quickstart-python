# Verify Quickstart

Simple phone verification with Python, Flask, and Twilio Verify.

## Install

    python3 -m venv venv
    . venv/bin/activate

Or on Windows cmd:

    py -3 -m venv venv
    venv\Scripts\activate.bat

Install Verify:

    pip install -r requirements.txt

## Run

    export FLASK_APP=verify
    export FLASK_ENV=development
    flask init-db
    flask run

Or on Windows cmd:

    set FLASK_APP=verify
    set FLASK_ENV=development
    flask init-db
    flask run

Open http://127.0.0.1:5000 in a browser.
