from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.4'
DESCRIPTION = 'Creating Strong passwords and OTP'
LONG_DESCRIPTION = """
Password and OTP Generator
===========================

The Password and OTP Generator package provides a simple and versatile tool for generating secure passwords and one-time passwords (OTPs). With this package, you can easily generate passwords and OTPs of varying lengths and complexities to enhance the security of your applications.

Features
--------

**Password Generation:**

- Generate passwords with a customizable number of letters, symbols, and numbers.
- Choose from predefined functions to generate passwords of specific lengths:
  - ``four_digit_password()``: Generates a 4-digit password with 2 letters, 1 symbol, and 1 number.
  - ``six_digit_password()``: Generates a 6-digit password with 4 letters, 1 symbol, and 1 number.
  - ``eight_digit_password()``: Generates an 8-digit password with 4 letters, 2 symbols, and 2 numbers.
  - ``strong_password()``: Generates a strong password with a random length between 8 and 10 characters, including a mix of letters, symbols, and numbers.

**OTP Generation:**

- Generate one-time passwords (OTPs) with a customizable number of digits.
- Choose from predefined functions to generate OTPs of specific lengths:
  - ``four_digit_otp()``: Generates a 4-digit OTP.
  - ``six_digit_otp()``: Generates a 6-digit OTP.

Usage
-----

.. code-block:: python

    # Example usage for generating passwords
    import password_otp_generator

    # Generate a strong password
    password = password_otp_generator.strong_password()
    print("Generated Strong Password:", password)

    # Generate a 6-digit OTP
    otp = password_otp_generator.six_digit_otp()
    print("Generated OTP:", otp)

Installation
------------

.. code-block:: bash

    pip install password-otp-generator

"""

# Setting up
setup(
    name="quickkeys",
    version=VERSION,
    author="Mohammed shibil K (shibilmohd13)",
    author_email="shibilmhdjr13@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'password', 'otp'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)