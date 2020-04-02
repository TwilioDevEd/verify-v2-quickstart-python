# Verify Quickstart

> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

Simple phone verification with Python, Flask, and Twilio Verify. 

Full Quickstart instructions available at https://www.twilio.com/docs/verify/api-beta/quickstarts/python-flask

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

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
