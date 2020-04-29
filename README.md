<a href="https://www.twilio.com">
  <img src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg" alt="Twilio" width="250" />
</a>

# Verify Quickstart

![](https://github.com/TwilioDevEd/verify-v2-quickstart-python/workflows/Flask/badge.svg)

> We are currently in the process of updating this sample template. If you are encountering any issues with the sample, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues) and we'll try to help you.

Simple phone verification with Python, Flask, and Twilio Verify.

[Read the full quickstart here](https://www.twilio.com/docs/verify/api-beta/quickstarts/python-flask)!

## Install

    ```
    python3 -m venv venv
    . venv/bin/activate
    ```

Or on Windows cmd:

    ```
    py -3 -m venv venv
    venv\Scripts\activate.bat
    ```

Install the dependencies:

    ```
    pip install -r requirements.txt
    ```

Copy `.env.example` to `.env` to setup you environment.

    ```
    cp .env.example .env
    ```

Edit `.env` to add your Twilio access keys. You'll need to set your `TWILIO_ACCOUNT_SID` and
`TWILIO_AUTH_TOKEN` from the [Twilio Console](https://www.twilio.com/console).
For the `VERIFICATION_SID` variable you'll need to provision a
[Verification Service](https://www.twilio.com/console/verify/services).

## Run

    ```
    flask init-db
    flask run
    ```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.

## Meta

* No warranty expressed or implied. Software is as is. Diggity.
* The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by Twilio Developer Education.
