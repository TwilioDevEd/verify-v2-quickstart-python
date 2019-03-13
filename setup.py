import io

from setuptools import find_packages, setup

setup(
    name='verify-quickstart',
    version='1.0.0',
    url='https://www.twilio.com/docs/verify',
    maintainer='Twilio',
    description='Tutorial for phone verification with Twilio.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
