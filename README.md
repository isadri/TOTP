# totp

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
