# TOTP

This is an implementation of the Time-based One-Time Password (TOTP) algorithm. The TOTP is an algorithm that generates a one-time password (OTP) using current time as a source of uniqueness.

It is considered as the time-based variant of the HMAC-based One-Time Password (HOTP) algorithm. In other word, TOTP replaces the counter with a value based on the current time:

TOTP is defined as `TOTP(K) = HOTP(K, T)`, where K is the key used to generate the OTP value and T is an integer and represents the number of time steps between the initial counter time T0 and the current Unix time. T is defined as follows

```
T = ⌊(Current Unix Time - T0) / X⌋
```

where
* T0 is the Unix time to start counting time steps. T0 = 0 in our implementation.
* X represents the time step in seconds. X = 30 is our implementation.


## Usage

```bash
python3 main.py [-h] [-g <filename>] [-k {otp.key}]
```

This program needs a hexadecimal key in order to generate the TOTP key. The program reads the hexadecimal key from the file give with the `-g` option and stores it in a file called `otp.key`. When using the program with the `-k otp.key` argument, the program generates a new temporary password based on the key given in the `otp.key` file.

For example, suppose `key.hex` file contains the hexadecimal key `6EAAcADeBBDe5cFCDa4fCeBdfCD2f7A3725B7eFfdFFD2de3Bd6c527b6a3F57Cf`, then the following usage will store the key in the `otp.key` file.

```bash
python3 main.py -g key.hex
```

Then, if you want a new temporary key based on the above hexadecimal key, use the following

```bash
python3 main.py -k otp.key
```

The key will be changed after every 30 seconds. So if you wait 30 seconds or more, a new temporary key will be generated.


## References

* [RFC 4226](https://datatracker.ietf.org/doc/html/rfc4226)
* [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238)
* [Time-based ont-time password](https://en.wikipedia.org/wiki/Time-based_one-time_password)
