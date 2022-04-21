<a  href="https://www.twilio.com">
<img  src="https://static0.twilio.com/marketing/bundles/marketing/img/logos/wordmark-red.svg"  alt="Twilio"  width="250"  />
</a>

# Verify Quickstart

![](https://github.com/TwilioDevEd/verify-v2-quickstart-python/workflows/Flask/badge.svg)

> This template is part of Twilio CodeExchange. If you encounter any issues with this code, please open an issue at [github.com/twilio-labs/code-exchange/issues](https://github.com/twilio-labs/code-exchange/issues).

## About

Simple phone verification with Python, Flask, and Twilio Verify.

[Read the full quickstart here](https://www.twilio.com/docs/verify/quickstarts/python-flask)!

Implementations in other languages: [.NET](https://github.com/TwilioDevEd/verify-v2-quickstart-csharp) | [Java](https://github.com/TwilioDevEd/verify-v2-quickstart-java)  | [Ruby](https://github.com/TwilioDevEd/verify-v2-quickstart-rails)    | [PHP](https://github.com/TwilioDevEd/verify-v2-quickstart-php) | [Node](https://github.com/TwilioDevEd/verify-v2-quickstart-node)

<!--
### How it works

**TODO: Describe how it works**
-->

## Set up

### Requirements

- [Python](https://www.python.org/downloads) version >= **3.6.x**
- Twilio account - [sign up](https://www.twilio.com/try-twilio)
- Verify service - [create](https://www.twilio.com/console/verify/services)

### Twilio Account Settings

This application gives a ready-made starting point for writing your own registration flow using phone authentication. Before we begin, we need to collect
all the config values we need to run the application:

| Config&nbsp;Value     | Description                                                                                                                    |
|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| Account&nbsp;SID      | Your primary Twilio account identifier, find this [in the Console](https://www.twilio.com/console)                             |
| Auth&nbsp;Token       | Used to authenticate, you'll also find this [in the Console](https://www.twilio.com/console)                                   |
| Verification&nbsp;SID | Your verification service identifier, find this or create a new service [here](https://www.twilio.com/console/verify/services) |

### Local development

After the above requirements have been met:

1. Clone this repository and `cd` into it

   ```bash
   git clone git@github.com:TwilioDevEd/verify-v2-quickstart-python.git
   cd verify-v2-quickstart-python
   ```

2. Prepare the environment and install dependencies

   ```bash
   make install
   ```

3. Set your environment variables

   ```bash
   cp .env.example .env
   ```

   See [Twilio Account Settings](#twilio-account-settings) to locate the necessary environment variables.


4. Set the database

   ```bash
   make serve-setup
   ```

5. Run the application

   ```bash
   make serve
   ```

   This will start a development server. It will reload whenever you change any files.

6. Navigate to [http://localhost:5000](http://localhost:5000)

That's it!

### Docker

If you have [Docker](https://www.docker.com/) already installed on your machine, you can use our `docker-compose.yml` to setup your project.

1. Make sure you have the project cloned.
2. Setup the `.env` file as outlined in the [Local Development](#local-development) steps.
3. Run `docker-compose up`.

### Tests

You can run the tests locally by typing:

```bash
python manage.py test
```

### Cloud deployment

Additionally to trying out this application locally, you can deploy it to a variety of host services. Here is a small selection of them.

Please be aware that some of these might charge you for the usage or might make the source code for this application visible to the public. When in doubt research the respective hosting service first.

| Service                           |                                                                                                                                                                |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Heroku](https://www.heroku.com/) | [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/TwilioDevEd/verify-v2-quickstart-python/tree/master) |

**Some notes:**

- For Heroku, please [check this](https://devcenter.heroku.com/articles/django-app-configuration) to properly configure the project for deployment.
- [Glitch](https://glitch.com/) is not included because it only supports NodeJS officially. Instead, you can try [PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/) which is a similar alternative por Python projects.
- [Zeit Now](https://zeit.co) is also not included because it uses a serverless architecture which doesn't work with frameworks such as Django.

## Resources

- The CodeExchange repository can be found [here](https://github.com/twilio-labs/code-exchange/).

## Contributing

This template is open source and welcomes contributions. All contributions are subject to our [Code of Conduct](https://github.com/twilio-labs/.github/blob/master/CODE_OF_CONDUCT.md).

[Visit the project on GitHub](https://github.com/twilio-labs/sample-template-django)

## License

[MIT](http://www.opensource.org/licenses/mit-license.html)

## Disclaimer

No warranty expressed or implied. Software is as is.

[twilio]: https://www.twilio.com
