# TOTP

This is an implementation of the Time-based One-Time Password (TOTP) algorithm. The TOTP is an algorithm that generates a one-time password (OTP) using current time as a source of uniqueness.

It is considered as the time-based variant of the HMAC-based One-Time Password (HOTP) algorithm. In other words, TOTP replaces the counter with a value based on the current time:

TOTP is defined as `TOTP(K) = HOTP(K, T)`, where K is the secret key used to generate the OTP value and T is an integer and represents the number of time steps between the initial counter time T0 and the current Unix time. T is defined as follows

```
T = ⌊(Current Unix Time - T0) / X⌋
```

where
* T0 is the Unix time to start counting time steps. T0 = 0 in our implementation.
* X represents the time step in seconds. 30 is the default value in our implementation and it can be modified.


The base32 encoding/decoding is used for generating the key. This is because base32 is used to deliver the secret key in a human readable form.


The implementation follows the TOTP algorithm requirements as mentioned in (RFC 6238)[https://datatracker.ietf.org/doc/html/rfc6238]


## Usage

Create a virtual environment using

```bash
python3.{your version} -m venv env
```

Then, activate the virtual environment

```bash
source env/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Now, you can go and generate some keys.


```bash
python3 generate.py [-h] [-g <filename>] [-k {otp.key}]
```

This program needs a hexadecimal key in order to generate the TOTP key. The program reads the hexadecimal key from the file give with the `-g` option and stores it in a file called `otp.key`. When using the program with the `-k otp.key` argument, the program generates a new temporary password based on the key given in the `otp.key` file.

For example, suppose `key.hex` file contains the hexadecimal key `6EAACADEBBDE5CFCDA4FCEBDFCD2F7A3725B7EFFDFFD2DE3BD6C527B6A3F57CF`, then the following usage will store the key in the `otp.key` file.

```bash
python3 generate.py -g key.hex
```

Then, if you want a new temporary key based on the above hexadecimal key, use the following

```bash
python3 generate.py -k otp.key
```

This will pop up a windown containing the qr code of the OTP value. After that qr code (e.g., using Google Authenticator app) enter the 6 digits in the prompt given in the program. The program will verify if the value you typed is valid or not.

The key will be changed after every 30 seconds. So if you wait 30 seconds or more, a new temporary key will be generated.


### URI string format

`otpauth://TYPE/LABEL?PARAMETERS`


#### Scheme

Each URI begins with a scheme name that refers to a specification for assigning identifiers within that scheme. For example, `otpauth` is used by Authenticator apps to generate one-time passcodes using OATH.

The otpauth:// URI scheme was originally formalised by Google.


#### TYPE

The TYPE is either __hotp__ or __totp__ and is needed to distinguish whether the credential will be used for counter-based HOTP or for time-based TOTP


#### LABEL

The label is used to identify which account a credential is associated with. It also serves as the unique identifier for the credential itsel.

The label is created from:

* Issuer: An optional string value indicating the provider or service this account is associated with.
* Account name: A URI-encoded string that usually is the user's email address.

It is formed as "Issuer:Account" when both parameters are present. More details [here](https://docs.yubico.com/yesdk/users-manual/application-oath/uri-string-format.html).


#### Secret

The secret is provided to the user in the QR code, this secret key is needef for one-time password generation.


#### Digits

The number of digits in a one-time password (OTP).


#### Period

Period it is only used if the type is TOTP.

The period parameter defines a validity period in seconds for the TOTP code.


## References

* [RFC 4226](https://datatracker.ietf.org/doc/html/rfc4226)
* [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238)
* [Keyed-hash Message Authentication Code](https://en.wikipedia.org/wiki/HMAC)
* [Time-based ont-time password](https://en.wikipedia.org/wiki/Time-based_one-time_password)
* [URI string format](https://docs.yubico.com/yesdk/users-manual/application-oath/uri-string-format.html)
